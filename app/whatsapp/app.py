import os, logging
from flask import Flask, request, jsonify
from clients.twilio import TwilioWhatsAppClient, TwilioWhatsAppMessage
from twilio.twiml.messaging_response import MessagingResponse  # Certifique-se de ter essa importação
from app.utils.open_ai_integration import chat_completion
from app.utils.open_ai_message_prompting import chat_history_manager, create_messages_for_openai
from dotenv import load_dotenv
from app.whatsapp.chat import Sender
import requests
import time

load_dotenv()
logging.basicConfig()
logger = logging.getLogger("WP-APP")
logger.setLevel(logging.DEBUG)
# Correção na inicialização do TwilioWhatsAppClient com os.getenv para buscar variáveis de ambiente
chat_client = TwilioWhatsAppClient(
    account_sid=os.getenv("TWILIO_ACCOUNT_SID"),
    auth_token=os.getenv("TWILIO_AUTH_TOKEN"),
    from_number=os.getenv("TWILLIO_WHATSAPP_NUMBER"),
)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health_check():
    return "App is running!"

@app.route("/whatsapp/reply", methods=["POST"])
def reply_to_whatsapp_message():
    try:
        incoming_msg = request.form.get("Body")
        sender_phone = request.values.get("From")
        sender_name = request.values.get("ProfileName", sender_phone)
        sender = Sender(phone_number=sender_phone, name=sender_name)
        logger.debug(f"Sender: {sender}")
        logger.debug(f"Recebendo mensagem: {incoming_msg}")

        # Construindo mensagens para a conversa com histórico
        messages = create_messages_for_openai(incoming_msg, sender.phone_number)
        
        # Obtendo a resposta da OpenAI
        openai_response = chat_completion(messages)

        # Atualiza o histórico com a resposta da OpenAI
        # Após receber a resposta da OpenAI
        chat_history_manager.update_user_history(sender.phone_number, {"role": "assistant", "content": openai_response})


        # Preparando e enviando a resposta via Twilio
        chat_client.send_message(
            openai_response, 
            sender.phone_number,
            on_failure="Sorry, I didn't understand that. Please try again.",
        )
        logger.debug(f"Enviando resposta ao usuário: {openai_response}")

    except Exception as e:
        logger.error(f"Erro ao processar a mensagem: {e}")
        return jsonify({"error": str(e)}), 500
    
    return jsonify({"status": "ok"})

@app.route("/whatsapp/status", methods=["POST"])
def process_whatsapp_status():
    logger.info(f"Obtained request: {dict(request.values)}")
    return jsonify({"status": "ok"})