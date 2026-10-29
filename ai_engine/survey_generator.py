import logging
import json
from .gemini_client import GeminiClient

logger = logging.getLogger(__name__)

class SurveyGenerator:
    def __init__(self, gemini_client: GeminiClient):
        self.client = gemini_client

    def generate_survey(self, themes: list[dict], target_department: str = None) -> list[dict]:
        if not self.client.has_api_key:
            logger.info("Using mock response for SurveyGenerator")
            return self._get_mock_survey(target_department, themes)

        dept_str = target_department if target_department else "all departments across the organization"
        prompt = f"""
        Generate a set of 5-6 employee micro-survey questions addressing these themes: {json.dumps(themes)}.
        Target department: {dept_str}. Tailor the terminology and operational scenarios specifically to {dept_str} (e.g. for Engineering ask about sprints, code reviews, technical debt; for Sales ask about quotas, commissions, pipeline; for Operations ask about shifts, process bottlenecks).
        
        MUST follow these strict question framing rules:
        - NEVER ask yes/no questions.
        - NEVER ask vague sentiment questions (e.g., "Are you satisfied?").
        - ALWAYS anchor questions to a specific timeframe (e.g., "In the past 30 days...", "Over the past 2 weeks...").
        - ALWAYS ask about observable behaviors, not internal feelings (e.g., "How often does your manager provide actionable feedback?").
        - Ensure responses use a 5-point Likert scale measuring frequency or agreement, mapped to the behavioral question (or open_text if appropriate).
        - Use positive framing ("what would make your experience better?" not "what's wrong?").
        
        Return the result ONLY as a JSON list of objects matching this schema:
        [
            {{"question": "string", "theme": "string", "response_type": "likert_5" or "open_text", "options": ["string"] or null}}
        ]
        """
        
        response = self.client.generate(prompt, response_format="json")
        if response and isinstance(response, list) and len(response) > 0:
            return response
        else:
            return self._get_mock_survey(target_department, themes)
            
    def _get_mock_survey(self, target_department: str = None, themes: list[dict] = None):
        dept = str(target_department).lower() if target_department else "all"
        
        if "eng" in dept:
            return [
                {
                    "question": "In the past 30 days, how frequently have sprint planning and technical debt discussions aligned with your engineering career pathways?",
                    "theme": "Career Growth",
                    "response_type": "likert_5",
                    "options": ["Never", "Rarely", "Sometimes", "Often", "Consistently"]
                },
                {
                    "question": "In the past 2 weeks, how often has your engineering manager or tech lead provided actionable architectural feedback on your pull requests?",
                    "theme": "Management Alignment",
                    "response_type": "likert_5",
                    "options": ["Never", "Once", "Twice", "3-4 times", "5+ times"]
                },
                {
                    "question": "Over the last quarter, how frequently have you been able to completely disconnect from on-call or off-hours production incident alerts?",
                    "theme": "Work-Life Balance",
                    "response_type": "likert_5",
                    "options": ["Never", "Rarely", "Sometimes", "Often", "Always"]
                },
                {
                    "question": "In the past 6 months, how clearly have engineering band promotions and seniority benchmarks been communicated?",
                    "theme": "Compensation",
                    "response_type": "likert_5",
                    "options": ["Never", "Rarely", "Sometimes", "Often", "Always"]
                },
                {
                    "question": "Reflecting on the past month, what specific developer tools, CI/CD pipeline improvements, or codebase changes would most improve your daily sprint velocity?",
                    "theme": "Work Environment",
                    "response_type": "open_text",
                    "options": None
                }
            ]
        elif "sale" in dept:
            return [
                {
                    "question": "In the past 30 days, how clearly have your quarterly quota expectations and commission accelerator tiers been communicated?",
                    "theme": "Compensation",
                    "response_type": "likert_5",
                    "options": ["Never", "Rarely", "Sometimes", "Often", "Consistently"]
                },
                {
                    "question": "In the past 2 weeks, how frequently has sales leadership actively assisted you with enterprise deal strategy or pipeline bottlenecks?",
                    "theme": "Management Alignment",
                    "response_type": "likert_5",
                    "options": ["Never", "Once", "Twice", "3-4 times", "5+ times"]
                },
                {
                    "question": "Over the last quarter, how realistic and attainable have your assigned sales territory quotas felt?",
                    "theme": "Work Environment",
                    "response_type": "likert_5",
                    "options": ["Never", "Rarely", "Sometimes", "Often", "Always"]
                },
                {
                    "question": "In the past 6 months, how often have you had transparent conversations regarding promotion pathways to Senior Account Executive or Lead roles?",
                    "theme": "Career Growth",
                    "response_type": "likert_5",
                    "options": ["Never", "Rarely", "Sometimes", "Often", "Always"]
                },
                {
                    "question": "Reflecting on recent cycles, what specific sales enablement collateral, CRM tooling, or SDR support would most elevate your deal win rates?",
                    "theme": "Work Environment",
                    "response_type": "open_text",
                    "options": None
                }
            ]
        elif "op" in dept:
            return [
                {
                    "question": "In the past 30 days, how manageable has your daily operational ticket and workload volume been without requiring unscheduled overtime?",
                    "theme": "Work-Life Balance",
                    "response_type": "likert_5",
                    "options": ["Never", "Rarely", "Sometimes", "Often", "Consistently"]
                },
                {
                    "question": "In the past 2 weeks, how quickly has operations leadership resolved workflow blockers or resource shortages flagged by the team?",
                    "theme": "Management Alignment",
                    "response_type": "likert_5",
                    "options": ["Never", "Within days", "Within a week", "After multiple escalations", "Unresolved"]
                },
                {
                    "question": "Over the last quarter, how consistently has your contribution to operational SLAs and system uptime been recognized?",
                    "theme": "Recognition",
                    "response_type": "likert_5",
                    "options": ["Never", "Rarely", "Sometimes", "Often", "Always"]
                },
                {
                    "question": "In the past 6 months, how clearly have cross-skilling or process lead advancement pathways been outlined for your role?",
                    "theme": "Career Growth",
                    "response_type": "likert_5",
                    "options": ["Never", "Rarely", "Sometimes", "Often", "Always"]
                },
                {
                    "question": "What process automation, SOP revisions, or workflow tools would eliminate the most friction in your daily operations?",
                    "theme": "Work Environment",
                    "response_type": "open_text",
                    "options": None
                }
            ]
        elif "market" in dept:
            return [
                {
                    "question": "In the past 30 days, how realistic have cross-departmental campaign deadlines and creative launch expectations been?",
                    "theme": "Work-Life Balance",
                    "response_type": "likert_5",
                    "options": ["Never", "Rarely", "Sometimes", "Often", "Consistently"]
                },
                {
                    "question": "In the past 2 weeks, how much strategic autonomy have you had in shaping campaign concepts and messaging?",
                    "theme": "Management Alignment",
                    "response_type": "likert_5",
                    "options": ["None", "Minimal", "Moderate", "Substantial", "Complete Autonomy"]
                },
                {
                    "question": "Over the last quarter, how well-aligned were marketing campaign deliverables with product launch and sales priorities?",
                    "theme": "Organizational Alignment",
                    "response_type": "likert_5",
                    "options": ["Never", "Rarely", "Sometimes", "Often", "Always"]
                },
                {
                    "question": "In the past 6 months, how clearly have growth pathways into Senior Brand or Marketing Management roles been discussed?",
                    "theme": "Career Growth",
                    "response_type": "likert_5",
                    "options": ["Never", "Rarely", "Sometimes", "Often", "Always"]
                },
                {
                    "question": "What creative design tools, analytics software, or agency support would most elevate your campaign performance?",
                    "theme": "Work Environment",
                    "response_type": "open_text",
                    "options": None
                }
            ]
        else:
            return [
                {
                    "question": "In the past 30 days, how often have you had discussions with leadership regarding your career advancement pathways?",
                    "theme": "Career Growth",
                    "response_type": "likert_5",
                    "options": ["Never", "Rarely", "Sometimes", "Often", "Consistently"]
                },
                {
                    "question": "In the past 2 weeks, how frequently has your manager provided you with actionable feedback on your work?",
                    "theme": "Management Alignment",
                    "response_type": "likert_5",
                    "options": ["Never", "Once", "Twice", "3-4 times", "5+ times"]
                },
                {
                    "question": "Over the last quarter, how consistently have you observed team members being recognized for their contributions?",
                    "theme": "Recognition",
                    "response_type": "likert_5",
                    "options": ["Never", "Rarely", "Sometimes", "Often", "Always"]
                },
                {
                    "question": "In the past 30 days, how frequently have you been able to completely detach from work communications during off-hours?",
                    "theme": "Work-Life Balance",
                    "response_type": "likert_5",
                    "options": ["Never", "Rarely", "Sometimes", "Often", "Always"]
                },
                {
                    "question": "Looking back over the past 6 months, how often have you observed salary and compensation decisions being communicated transparently?",
                    "theme": "Compensation",
                    "response_type": "likert_5",
                    "options": ["Never", "Rarely", "Sometimes", "Often", "Always"]
                },
                {
                    "question": "Reflecting on the past month, what specific resources or support changes would make your day-to-day experience more productive?",
                    "theme": "Work Environment",
                    "response_type": "open_text",
                    "options": None
                }
            ]
