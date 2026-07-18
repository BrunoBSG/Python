from google import genai

from config import GEMINI_API_KEY
from config import GEMINI_MODEL


class GeminiProvider:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def find_best_clips(self, transcript: str):

        prompt = f"""
Você é um especialista em criar vídeos virais para YouTube Shorts.

Analise a transcrição abaixo.

Encontre os 5 melhores momentos.

Cada trecho deve ter entre 30 e 60 segundos.

Considere:
- momentos engraçados;
- momentos emocionantes;
- curiosidades;
- revelações;
- frases de impacto.

Retorne APENAS um JSON válido.

Formato:

[
    {{
        "start": 35.2,
        "end": 68.4,
        "reason": "Momento muito engraçado."
    }},
    {{
        "start": 145.7,
        "end": 191.3,
        "reason": "Grande reviravolta."
    }}
]

Transcrição:

{transcript}
"""

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        return response.text

    def test_connection(self):

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents="Responda apenas: conexão funcionando."
        )

        return response.text
    def list_models(self):

        for model in self.client.models.list():
            print(model.name)