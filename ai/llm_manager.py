import openai
import requests
from core.interfaces import ILLMProvider

class OpenAIProvider(ILLMProvider):
    def __init__(self, api_key: str):
        openai.api_key = api_key

    async def generate_response(self, prompt: str, context: list) -> str:
        messages = [{"role": "system", "content": "Eres Miranda, una asistente virtual avanzada."}]
        messages.extend(context)
        messages.append({"role": "user", "content": prompt})
        
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages
        )
        return response.choices[0].message['content']

class OllamaProvider(ILLMProvider):
    def __init__(self, model_name: str = "llama3"):
        self.model_name = model_name
        self.url = "http://localhost:11434/api/generate"

    async def generate_response(self, prompt: str, context: list) -> str:
        # Aquí se formatearía el contexto para modelos locales
        payload = {"model": self.model_name, "prompt": prompt, "stream": False}
        response = requests.post(self.url, json=payload)
        return response.json().get("response", "")