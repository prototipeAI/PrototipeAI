// app/whatsapp/static/js/scripts.js
document.addEventListener('DOMContentLoaded', function() {
    // Função para adicionar mensagem ao chat
    function addMessage(content, sender) {
        const chatWindow = document.getElementById('chat-window');
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);
        messageDiv.innerText = content;
        chatWindow.appendChild(messageDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    // Função para adicionar mensagem de carregamento
    function addLoadingMessage() {
        const chatWindow = document.getElementById('chat-window');
        const loadingDiv = document.createElement('div');
        loadingDiv.classList.add('message', 'agent', 'loading');
        loadingDiv.innerText = 'Agente está digitando...';
        chatWindow.appendChild(loadingDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    // Função para remover mensagem de carregamento
    function removeLoadingMessage() {
        const loadingMessage = document.querySelector('.message.loading');
        if (loadingMessage) {
            loadingMessage.remove();
        }
    }

    // Função para obter parâmetros do formulário de configuração
    function getParameters() {
        const form = document.getElementById('parameter-form');
        const formData = new FormData(form);
        const params = {};
        
        formData.forEach((value, key) => {
            if (value !== '') {
                params[key] = value;
            }
        });

        // Converter valores para os tipos corretos
        if (params.temperature) {
            params.temperature = parseFloat(params.temperature);
        }
        if (params.top_p) {
            params.top_p = parseFloat(params.top_p);
        }
        if (params.frequency_penalty) {
            params.frequency_penalty = parseFloat(params.frequency_penalty);
        }
        if (params.presence_penalty) {
            params.presence_penalty = parseFloat(params.presence_penalty);
        }
        if (params.max_tokens) {
            params.max_tokens = parseInt(params.max_tokens);
        }

        return params;
    }

    // Função para lidar com o envio de mensagens
    function handleSendMessage() {
        const sendButton = document.getElementById('send-button');
        const messageText = document.getElementById('message-text');

        // Função para enviar mensagem
        function sendMessage() {
            const message = messageText.value.trim();
            if (message === '') return;

            // Adicionar a mensagem do usuário no chat
            addMessage(message, 'user');

            // Limpar o campo de texto
            messageText.value = '';

            // Adicionar mensagem de carregamento
            addLoadingMessage();

            // Obter parâmetros configuráveis
            const parameters = getParameters();

            // Enviar a mensagem e os parâmetros para o servidor
            const formData = new URLSearchParams();
            formData.append('message', message);
            for (const [key, value] of Object.entries(parameters)) {
                formData.append(key, value);
            }

            fetch('/test/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Remover mensagem de carregamento
                removeLoadingMessage();

                if (data.response) {
                    addMessage(data.response, 'agent');
                } else if (data.error) {
                    addMessage(`Erro: ${data.error}`, 'agent');
                }
            })
            .catch(error => {
                // Remover mensagem de carregamento
                removeLoadingMessage();
                addMessage(`Erro: ${error}`, 'agent');
            });
        }

        // Evento de clique no botão de envio
        sendButton.addEventListener('click', function() {
            sendMessage();
        });

        // Evento de tecla pressionada no textarea
        messageText.addEventListener('keydown', function(event) {
            if (event.key === 'Enter') {
                if (event.shiftKey) {
                    // Permitir a inserção de uma nova linha
                    return;
                } else {
                    // Evitar a inserção de uma nova linha e enviar a mensagem
                    event.preventDefault();
                    sendMessage();
                }
            }
        });
    }

    // Inicializar o envio de mensagens
    handleSendMessage();
});
