import logging
import json
from .gemini_client import GeminiClient

logger = logging.getLogger(__name__)

class RecommendationEngine:
    def __init__(self, gemini_client: GeminiClient):
        self.client = gemini_client

    def generate_recommendations(self, risk_segments: list[dict], company_policies: dict) -> list[dict]:
        if not self.client.has_api_key:
            logger.info("Using mock response for RecommendationEngine")
            return self._get_mock_recommendations()

        prompt = f"""
        Generate actionable retention recommendations based on these high-risk segments and existing policies.
        Risk Segments: {json.dumps(risk_segments)}
        Company Policies: {json.dumps(company_policies)}
        
        Categorize each recommendation into the Retention Action Matrix:
        - quick_win: low cost, high impact
        - strategic: high cost, high impact
        - nice_to_have: low cost, low impact
        - avoid: high cost, low impact
        
        Consider existing company policies to avoid duplicates.
        Include estimated timeline and ROI rationale.
        
        Return the result ONLY as a JSON list of objects matching this schema:
        [
            {{
                "title": "string",
                "description": "string",
                "target_segment": "string",
                "category": "quick_win" | "strategic" | "nice_to_have" | "avoid",
                "estimated_cost": "low" | "medium" | "high",
                "expected_impact": "low" | "medium" | "high",
                "timeline": "string",
                "evidence": "string"
            }}
        ]
        """
        
        response = self.client.generate(prompt, response_format="json")
        if response:
            return response
        else:
            return self._get_mock_recommendations()
            
    def _get_mock_recommendations(self):
        return [
            {
                "title": "Mandatory Bi-Weekly 1-on-1s",
                "description": "Enforce a strict schedule for managers to conduct 1-on-1 career discussions, especially targeting Engineering Juniors.",
                "target_segment": "Engineering - Junior",
                "category": "quick_win",
                "estimated_cost": "low",
                "expected_impact": "high",
                "timeline": "Immediately",
                "evidence": "Exit interviews strongly cited 'manager doesn't have time for 1-on-1s'."
            },
            {
                "title": "Skill-Based Rotation Program",
                "description": "Allow junior engineers stuck in maintenance to dedicate 20% time to new tech projects.",
                "target_segment": "Engineering - Junior",
                "category": "strategic",
                "estimated_cost": "medium",
                "expected_impact": "high",
                "timeline": "Next Quarter",
                "evidence": "Addresses the stated reason of lack of growth and being stuck on old tech."
            },
            {
                "title": "Sales Compensation Review Task Force",
                "description": "Form a committee to review the recent commission structure changes against market benchmarks.",
                "target_segment": "Sales - Mid",
                "category": "strategic",
                "estimated_cost": "high",
                "expected_impact": "high",
                "timeline": "Within 3 Months",
                "evidence": "Sales attrition heavily linked to dissatisfaction with new commission caps."
            },
            {
                "title": "Additional Peer Recognition Badges",
                "description": "Expand the existing monthly peer-to-peer awards with specialized digital badges.",
                "target_segment": "All Staff",
                "category": "nice_to_have",
                "estimated_cost": "low",
                "expected_impact": "low",
                "timeline": "Next Month",
                "evidence": "Builds slightly on existing recognition without significant cost."
            },
            {
                "title": "Across-the-board Base Pay Increase",
                "description": "Raise all salaries unconditionally to counteract inflation complaints.",
                "target_segment": "All Staff",
                "category": "avoid",
                "estimated_cost": "high",
                "expected_impact": "low",
                "timeline": "Annual Cycle",
                "evidence": "Too expensive and doesn't target the specific risk segments showing flight indicators."
            },
            {
                "title": "Workload Balancing & Temporary Contractors",
                "description": "Hire temporary staff to offset the burden on senior operations staff experiencing burnout post-reorg.",
                "target_segment": "Operations - Senior",
                "category": "strategic",
                "estimated_cost": "high",
                "expected_impact": "high",
                "timeline": "Within 1 Month",
                "evidence": "Senior Ops personnel explicitly cite 'doing the job of two people'."
            },
            {
                "title": "Revamp 'BetterHelp' Wellness Communication",
                "description": "Send targeted reminders to stressed departments about the existing free mental health support.",
                "target_segment": "Operations - Senior",
                "category": "quick_win",
                "estimated_cost": "low",
                "expected_impact": "medium",
                "timeline": "Next Week",
                "evidence": "Policy exists but underutilized by those explicitly citing burnout."
            },
            {
                "title": "Extended Friday Team Lunches",
                "description": "Provide free lunch every Friday to improve general morale.",
                "target_segment": "All Staff",
                "category": "nice_to_have",
                "estimated_cost": "medium",
                "expected_impact": "low",
                "timeline": "Ongoing",
                "evidence": "Improves environment but doesn't directly solve structural attrition drivers."
            }
        ]
