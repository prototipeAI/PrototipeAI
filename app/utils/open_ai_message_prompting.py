class ChatHistoryManager:
    def __init__(self):
        self.user_histories = {}  # Mapeia número do telefone para histórico de mensagens

    def get_user_history(self, phone_number):
        return self.user_histories.get(phone_number, [])

    def update_user_history(self, phone_number, new_message):
        if phone_number not in self.user_histories:
            self.user_histories[phone_number] = []
        self.user_histories[phone_number].append(new_message)
        # Mantém apenas as últimas 10 mensagens
        self.user_histories[phone_number] = self.user_histories[phone_number][-10:]

# Instância global para gerenciar o histórico
chat_history_manager = ChatHistoryManager()

def create_messages_for_openai(incoming_msg, phone_number):
    user_history = chat_history_manager.get_user_history(phone_number)
    # Constrói uma lista de mensagens para a conversa, incluindo o histórico
    messages = user_history[-10:]  # Garante que apenas as últimas 10 mensagens sejam incluídas
    messages.append({
        "role": "system",
        "content": (
            "Você é uma assistente de IA chamado xxx"
            "Suas respostas devem se limitar a 1000 caracteres, para que facilite a leitura e adesão dos usuários."

            "Mensagem do Usuário: Qualquer mensagem"
            "Contexto do Usuário: Qualquer contexto"
            "Resposta Contextual: evite repetições excessivas de expressões de empatia e validação, pedidos repetitivos de desculpa ou dizer que sente muito ao usuário, agradecimentos repetitivos."
            )
        })                 
    messages.append({"role": "user", "content": incoming_msg})
    
    # Atualiza o histórico com a nova mensagem do usuário
    chat_history_manager.update_user_history(phone_number, {"role": "user", "content": incoming_msg})
    print(f"Histórico da conversa após a atualização para {phone_number}: {chat_history_manager.get_user_history(phone_number)}")
    return messages