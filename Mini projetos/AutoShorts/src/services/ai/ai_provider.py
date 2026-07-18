from config import AI_PROVIDER

from services.ai.openai_provider import OpenAIProvider
from services.ai.gemini_provider import GeminiProvider


class AIProvider:

    @staticmethod
    def create():

        if AI_PROVIDER.lower() == "openai":
            return OpenAIProvider()

        elif AI_PROVIDER.lower() == "gemini":
            return GeminiProvider()

        raise ValueError(f"Provider '{AI_PROVIDER}' não suportado.")