from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from config.setting import get_llm_config

load_dotenv()


_settings = get_llm_config()

Groq_client = ChatGroq(
    api_key = _settings.groq_api_key,
    model = _settings.llm_model_name,
    temperature = _settings.temperature,
)