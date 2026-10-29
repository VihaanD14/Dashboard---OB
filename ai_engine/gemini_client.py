import os
import json
import logging
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GeminiClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        # Only enable API calling if a valid Google AI Studio key is provided (starts with 'AIzaSy')
        self.has_api_key = bool(self.api_key and self.api_key.strip().startswith("AIzaSy"))
        
        if self.has_api_key:
            try:
                genai.configure(api_key=self.api_key.strip())
                self.model = genai.GenerativeModel("gemini-1.5-flash")
                logger.info("GeminiClient initialized with valid Gemini API key.")
            except Exception as e:
                logger.warning(f"Failed to configure GeminiClient: {e}. Falling back to instant offline responses.")
                self.has_api_key = False
        else:
            logger.info("GeminiClient: No valid Gemini API key detected (must start with 'AIzaSy'). Using high-performance mock intelligence telemetry.")

    def generate(self, prompt, response_format="json"):
        if not self.has_api_key:
            return None
            
        try:
            config = genai.types.GenerationConfig(
                response_mime_type="application/json" if response_format == "json" else "text/plain"
            )
            # 4-second timeout to prevent stalling the Streamlit event loop
            response = self.model.generate_content(prompt, generation_config=config, request_options={"timeout": 4.0})
            
            if response_format == "json":
                try:
                    return json.loads(response.text)
                except json.JSONDecodeError:
                    logger.error("Failed to decode JSON from Gemini response.")
                    return None
            return response.text
        except Exception as e:
            logger.warning(f"Gemini API call timed out or failed ({e}). Using instant telemetry fallback.")
            return None
