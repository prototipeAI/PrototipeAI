from openai import OpenAI
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()
client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Configura a chave da API da OpenAI

def chat_completion(messages, model="gpt-4o", **kwargs):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            **kwargs,
            temperature=0.7,
            top_p=1#,
            #frequency_penalty=0,
            #presence_penalty=0
        )
        # Retorna o conteúdo da mensagem gerada pelo modelo
        return response.choices[0].message.content
    except Exception as e:
        print(f"Erro ao chamar a API da OpenAI: {e}")
        return "Houve um erro ao processar a sua mensagem. Por favor, tente novamente."