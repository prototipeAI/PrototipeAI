import os, logging
from flask import Flask, request, jsonify
from clients.twilio import TwilioWhatsAppClient, TwilioWhatsAppMessage
from twilio.twiml.messaging_response import MessagingResponse  # Certifique-se de ter essa importação
from app.utils.open_ai_integration import chat_completion
from app.utils.open_ai_message_prompting import create_messages_for_openai
from dotenv import load_dotenv
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
    from_number=("TWILLIO_WHATSAPP_NUMBER", "+14155238886"),
)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health_check():
    return "App is running!"

@app.route("/whatsapp/reply", methods=["POST"])
def reply_to_whatsapp_message():
    try:
        incoming_msg = request.values.get('Body', '').strip()
        logger.debug(f"Recebendo mensagem: {incoming_msg}")

        # Construindo mensagens para a conversa
        messages = create_messages_for_openai(incoming_msg)
        
        # Obtendo a resposta da OpenAI
        openai_response = chat_completion(messages)

        # Preparando e enviando a resposta via Twilio
        resp = MessagingResponse()
        resp.message(openai_response)
        logger.debug(f"Enviando resposta ao usuário: {openai_response}")
        
        return str(resp)
    except Exception as e:
        logger.error(f"Erro ao processar a mensagem: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/whatsapp/status", methods=["POST"])
def process_whatsapp_status():
    logger.info(f"Obtained request: {dict(request.values)}")
    return jsonify({"status": "ok"})

