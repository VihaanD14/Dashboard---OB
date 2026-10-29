import logging
import json
from .gemini_client import GeminiClient

logger = logging.getLogger(__name__)

class ThemeExtractor:
    def __init__(self, gemini_client: GeminiClient):
        self.client = gemini_client

    def extract_themes(self, exit_feedback_texts: list[str]) -> dict:
        if not self.client.has_api_key:
            logger.info("Using mock response for ThemeExtractor")
            return self._get_mock_themes()

        prompt = f"""
        Analyze these exit interview responses. Extract: 
        1) Top themes with frequency %, 
        2) Sentiment intensity per theme (-1 to 1), 
        3) Stated vs implied reasons (detect when free-text suggests different issues than stated reason), 
        4) Demographic patterns
        
        Feedback: {json.dumps(exit_feedback_texts)}
        
        Return the result ONLY as a JSON object matching this schema:
        {{
            "themes": [
                {{"name": "string", "frequency_pct": "float", "sentiment": "float", "keywords": ["string"]}}
            ],
            "stated_vs_implied": [
                {{"issue": "string", "stated_reason": "string", "actual_implied_reason": "string"}}
            ],
            "emerging_concerns": ["string"]
        }}
        """
        
        response = self.client.generate(prompt, response_format="json")
        if response:
            return response
        else:
            return self._get_mock_themes()
            
    def _get_mock_themes(self):
        return {
            "themes": [
                {"name": "Career Growth", "frequency_pct": 32.0, "sentiment": -0.6, "keywords": ["promotion", "stuck", "path", "development"]},
                {"name": "Compensation", "frequency_pct": 24.0, "sentiment": -0.8, "keywords": ["pay", "commission", "base", "market"]},
                {"name": "Work-Life Balance", "frequency_pct": 18.0, "sentiment": -0.9, "keywords": ["burnout", "stress", "workload", "hours"]},
                {"name": "Management", "frequency_pct": 15.0, "sentiment": -0.7, "keywords": ["expectations", "communication", "1-on-1s"]},
                {"name": "Recognition", "frequency_pct": 11.0, "sentiment": -0.4, "keywords": ["valued", "appreciated", "credit"]}
            ],
            "stated_vs_implied": [
                {"issue": "Better opportunity vs Burnout", "stated_reason": "Better opportunity", "actual_implied_reason": "Unsustainable workload causing burnout"},
                {"issue": "Career growth vs Compensation", "stated_reason": "Career growth", "actual_implied_reason": "Lack of clear compensation progression"}
            ],
            "emerging_concerns": [
                "Lack of structured mentorship for junior roles",
                "Unrealistic targets post-reorganization"
            ]
        }
