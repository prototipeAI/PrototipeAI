def create_messages_for_openai(incoming_msg):
    # Constrói uma lista de mensagens para a conversa
    messages = [
        {"role": "system", "content": "Você é um assistente de carreira."},
        {"role": "user", "content": incoming_msg},
        {"role": "assistant", "content": "Se considere um entrevistador que irá ajudar esse usuário a se recolocar no mercado. Para isso, faça uma entrevista na qual você consiga entender um pouco do seu perfil pessoal, ambições e possa determinar o seu perfil."}
    ]
    return messages