from functools import lru_cache
import os
from dotenv import load_dotenv

load_dotenv()

class llmConfig:
    def __init__(self):
        # API key for LLM model
        self.groq_api_key = os.getenv("groq_api_key")

        # Model configuration parameters
        self.llm_model_name = os.getenv("LLM_MODEL_NAME", "llama-3.3-70b-versatile")
        self.temperature = float(os.getenv("LLM_TEMPERATURE", 0.7))
        self.max_tokens = int(os.getenv("LLM_MAX_TOKENS", 2048))


@lru_cache()
def get_llm_config()-> llmConfig:
    """Get LLM configuration with caching to optimize performance."""
    return llmConfig()

