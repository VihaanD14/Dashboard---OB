import logging
import json
from .gemini_client import GeminiClient

logger = logging.getLogger(__name__)

class RiskScorer:
    def __init__(self, gemini_client: GeminiClient):
        self.client = gemini_client

    def score_risk(self, segment_metrics: list[dict]) -> list[dict]:
        if not segment_metrics:
            logger.info("Empty segment metrics provided to RiskScorer, using mock fallback")
            return self._get_mock_scores()

        if not self.client.has_api_key:
            logger.info("Using deterministic empirical calculation and mock qualitative response for RiskScorer")
            return self._get_mock_scores(segment_metrics)

        prompt = f"""
        Evaluate the following mathematically calculated metrics using the Deterministic Composite Flight Risk Formula:
        R = 100 × [ w_sentiment*(Survey Sentiment Inversion) + w_exit*(Exit Term) + w_stagnation*(Tenure Stagnation Index) ]
        
        Formula definitions:
        - Survey Sentiment Inversion: 1 - ((mean_score - 1) / 4.0) [survey scale 1-5; worst mean (1) gives full risk (1.0)]
        - Exit Velocity: exits in the trailing 12 months / active cohort headcount
        - Exit Term: min(1.0, exit_velocity / exit_velocity_cap) [default cap 0.30]
        - Tenure Stagnation Index: min(1.0, months_since_promotion / stagnation_cap) [default cap 24 months]
        
        Metrics data for workforce cohorts:
        {json.dumps(segment_metrics)}
        
        Thresholds & Risk Bands:
        - Green (Low Risk): R < 40
        - Yellow (Early warning (sentiment / stagnation)): 40 <= R < 70
        - Red (Critical (adverse signals plus real departures)): R >= 70
        * Note: With zero exits, the maximum possible score is 65.0 (40.0 sentiment + 25.0 stagnation), so Red strictly requires active departures.
        
        CRITICAL: Retain the EXACT empirical score (calculated_risk_score) and risk_level provided in the data.
        Scores are computed deterministically in Python; your role is strictly to provide qualitative HR explanations:
        - trend: "improving", "stable", or "worsening"
        - top_factors: list of 2-3 specific drivers citing the provided metrics (e.g., survey sentiment, trailing 12m turnover velocity, promotion stagnation)
        - reasoning: 1-2 sentence executive explanation citing exact empirical numbers from the data.
        
        Return the result ONLY as a JSON list of objects matching this schema for ALL segments provided:
        [
            {{
                "segment": "string",
                "department": "string",
                "role_level": "string",
                "risk_level": "green" or "yellow" or "red",
                "score": float or int,
                "trend": "improving" or "stable" or "worsening",
                "top_factors": ["string"],
                "reasoning": "string (must cite the exact provided numbers)"
            }}
        ]
        """
        
        response = self.client.generate(prompt, response_format="json")
        if response and isinstance(response, list) and len(response) > 0:
            return response
        else:
            return self._get_mock_scores(segment_metrics)
            
    def _get_mock_scores(self, segment_metrics: list[dict] = None):
        if not segment_metrics:
            return [
                {
                    "segment": "Engineering - Junior",
                    "department": "Engineering",
                    "role_level": "Junior",
                    "risk_level": "red",
                    "score": 85.0,
                    "trend": "worsening",
                    "top_factors": ["Career Growth Deficit", "Lack of 1-on-1s", "Trailing 12m exits exceed cap"],
                    "reasoning": "High trailing 12-month exit velocity combined with survey drops in growth satisfaction indicate critical flight risk."
                },
                {
                    "segment": "Sales - Mid",
                    "department": "Sales",
                    "role_level": "Mid",
                    "risk_level": "yellow",
                    "score": 65.0,
                    "trend": "stable",
                    "top_factors": ["Compensation Structure", "Territory alignment", "Promotion stagnation"],
                    "reasoning": "Early warning status driven by survey sentiment friction and tenure stagnation without promotion."
                },
                {
                    "segment": "Marketing - Mid",
                    "department": "Marketing",
                    "role_level": "Mid",
                    "risk_level": "green",
                    "score": 30.0,
                    "trend": "improving",
                    "top_factors": ["Strong leadership", "Flexible work"],
                    "reasoning": "High survey scores in work-life balance and strong manager ratings correlate with zero historical attrition."
                },
                {
                    "segment": "Operations - Senior",
                    "department": "Operations",
                    "role_level": "Senior",
                    "risk_level": "yellow",
                    "score": 55.0,
                    "trend": "worsening",
                    "top_factors": ["Workload", "Burnout", "Promotion stagnation"],
                    "reasoning": "Early warning watchlist indicator characterized by elevated workload friction and 24+ months promotion latency."
                }
            ]

        scores = []
        for m in segment_metrics:
            dept = m.get("department", "Unknown")
            role = m.get("role_level", "Unknown")
            seg = m.get("segment", f"{dept} - {role}")
            
            s_inv = m.get("survey_inversion", 0.0)
            e_vel = m.get("exit_velocity", 0.0)
            e_term = m.get("exit_term", min(1.0, e_vel / 0.30))
            t_stag = m.get("tenure_stagnation", 0.0)
            
            calc_score = m.get("calculated_risk_score")
            if calc_score is None:
                calc_score = round(100.0 * (0.40 * s_inv + 0.35 * e_term + 0.25 * t_stag), 1)
            
            level = m.get("risk_level")
            if not level:
                if calc_score >= 70.0:
                    level = "red"
                elif calc_score >= 40.0:
                    level = "yellow"
                else:
                    level = "green"

            if level == "red":
                trend = "worsening"
            elif level == "yellow":
                trend = "stable"
            else:
                trend = "improving"
                
            factors = []
            if s_inv >= 0.28:
                factors.append(f"Survey sentiment deficit ({m.get('avg_survey_score', 3.0):.1f}/5.0)")
            if e_term >= 0.40:
                factors.append(f"Elevated trailing 12m exit velocity ({m.get('exit_rate', 0.0):.1%})")
            if t_stag >= 0.50:
                factors.append(f"Promotion stagnation ({m.get('months_since_promotion', 12.0):.0f} mo in band)")
            if not factors:
                factors = ["Balanced compensation & progression", "Positive survey sentiment baseline"]
                
            if level == "red":
                reasoning = (
                    f"Critical flight risk ({calc_score}/100) driven by adverse survey sentiment plus real trailing 12m departures "
                    f"({m.get('exits_count', 0)} exits, velocity {e_vel:.1%})."
                )
            elif level == "yellow":
                reasoning = (
                    f"Early warning ({calc_score}/100) driven by sentiment and promotion stagnation "
                    f"({m.get('months_since_promotion', 12.0):.0f} mo without promotion, stagnation index {t_stag:.2f})."
                )
            else:
                reasoning = (
                    f"Low flight risk ({calc_score}/100) supported by healthy survey sentiment "
                    f"({m.get('avg_survey_score', 4.0):.1f}/5.0) and stable cohort retention."
                )
                
            scores.append({
                "segment": seg,
                "department": dept,
                "role_level": role,
                "risk_level": level,
                "score": calc_score,
                "trend": trend,
                "top_factors": factors,
                "reasoning": reasoning
            })
            
        return scores
