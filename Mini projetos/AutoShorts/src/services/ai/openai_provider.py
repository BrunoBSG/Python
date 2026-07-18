import os

from openai import OpenAI

from config import OPENAI_MODEL


class OpenAIProvider:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def find_best_clips(self, transcript: str):

        prompt = f"""
Você é um especialista em vídeos virais.

Analise a transcrição abaixo.

Encontre os 5 melhores momentos para Shorts.

Cada trecho deve ter entre 30 e 60 segundos.

Retorne APENAS JSON.

Transcrição:

{transcript}
"""

        response = self.client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "Você cria Shorts virais."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5
        )

        
    def test_connection(self):

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": "Responda apenas: conexão funcionando."
                    }
                ]
            )    
            
            return response.choices[0].message.content