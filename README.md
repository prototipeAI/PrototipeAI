# PrototipeAI

Este aplicativo faz a integração de forma fácil entre Twilio, OpenAI, e WhatsApp, possibilitando aos usuários receber mensagens no WhatsApp e deixar a inteligência artificial responder automaticamente, baseado em seu prompt.

## Pré-requisitos

Antes de iniciar, certifique-se de ter o Python instalado em seu sistema e todos os requirements atualizados. Além disso, você precisará de contas no Twilio e na OpenAI, pois elas fornecerão as chaves API necessárias para o funcionamento do aplicativo no whatsapp. Caso opte por testar localmente a única chave necessária é a da openAI no .env .

## Configuração

### Dados Necessários

Você precisará configurar as seguintes variáveis de ambiente antes de iniciar o aplicativo. Para sua conveniência, deixei um arquivo `.env.exemplo` no repositório. Copie este arquivo para um novo chamado `.env` e preencha com suas informações:


* [Caso use Whatsapp]TWILIO_ACCOUNT_SID=seu_account_sid_aqui
* [Caso use Whatsapp]TWILIO_AUTH_TOKEN=seu_auth_token_aqui
* [Necessário]OPENAI_API_KEY=sua_api_key_openai_aqui
* [Caso use Whatsapp]TWILLIO_WHATSAPP_NUMBER=+14155238886

## Instalação

Clone o repositório e instale as dependências necessárias:


1. `git clone https://github.com/prototipeAI/PrototipeAI `
2.  `cd PrototipeAI `
3.  `pip install -r requirements.txt` [Para pegar todas as necessidades do projeto]


## Configuração do Ngrok

Para que o Twilio consiga se comunicar com seu aplicativo local, você precisará do Ngrok, que cria um túnel para o seu localhost.

1. Baixe e instale o Ngrok do [site oficial](https://ngrok.com/).
2. Inicie o Ngrok na porta que seu aplicativo estará escutando (geralmente 5000):


`ngrok http 3000 (em nosso caso)`

3. Copie a URL fornecida pelo Ngrok (por exemplo, \`https://abc123.ngrok.io\`) e configure no seu painel do Twilio para o webhook do WhatsApp com essa URL, seguida pelo caminho específico que o aplicativo utiliza para receber mensagens.

As rotas ficam em POST e usam https://abc123.ngrok.io/reply/messages para receber devolver as mensagens e https://abc123.ngrok.io/reply/status para recuperar o status da mensagem.

## Como Rodar o Aplicativo

Após configurar todas as variáveis e o Ngrok, você pode iniciar o aplicativo com o seguinte comando:

`python3 -m app.whatsapp`

## Uso

### Whatsapp
Com o aplicativo rodando, qualquer mensagem recebida pelo seu número do WhatsApp configurado será automaticamente respondida pela inteligência artificial baseada nos parâmetros definidos em seu código.

### Local
Qualquer mensagem enviada na caixa de mensagens será processada, utilizando o prompt no arquivo open_ai_message_prompting.py, conforme a realização de alterações nos arquivos derrube o servidor utilizando (CTRL+C) e comece novamente.
