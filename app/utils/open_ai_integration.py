import openai
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configura a chave da API da OpenAI
openai.api_key = OPENAI_API_KEY

def chat_completion(messages, model="gpt-4-turbo-preview", **kwargs):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            **kwargs
        )
        # Retorna o conteúdo da mensagem gerada pelo modelo
        return response.choices[0].message["content"]
    except Exception as e:
        print(f"Erro ao chamar a API da OpenAI: {e}")
        return "Houve um erro ao processar a sua mensagem. Por favor, tente novamente."
