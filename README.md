# PrototipeAI

Este aplicativo faz a integração de forma fácil entre Twilio, OpenAI, e WhatsApp, possibilitando aos usuários receber mensagens no WhatsApp e deixar a inteligência artificial responder automaticamente, baseado em seu prompt.

## Pré-requisitos

Antes de iniciar, certifique-se de ter o Python instalado em seu sistema. Além disso, você precisará de contas no Twilio e na OpenAI, pois elas fornecerão as chaves API necessárias para o funcionamento do aplicativo.

## Configuração

### Dados Necessários

Você precisará configurar as seguintes variáveis de ambiente antes de iniciar o aplicativo. Para sua conveniência, deixei um arquivo `.env.exemplo` no repositório. Copie este arquivo para um novo chamado `.env` e preencha com suas informações:


* TWILIO_ACCOUNT_SID=seu_account_sid_aqui
* TWILIO_AUTH_TOKEN=seu_auth_token_aqui
* OPENAI_API_KEY=sua_api_key_openai_aqui
* TWILLIO_WHATSAPP_NUMBER=+14155238886

## Instalação

Clone o repositório e instale as dependências necessárias:


1. `git clone https://github.com/prototipaai/Prototipaai.git`
2.  `cd prototipaai`
3.  `pip install -r requirements.txt` [Para pegar todas as necessidades do projeto]


## Configuração do Ngrok

Para que o Twilio consiga se comunicar com seu aplicativo local, você precisará do Ngrok, que cria um túnel para o seu localhost.

1. Baixe e instale o Ngrok do [site oficial](https://ngrok.com/).
2. Inicie o Ngrok na porta que seu aplicativo estará escutando (geralmente 5000):


`ngrok http 3000 (em nosso caso)`

3. Copie a URL fornecida pelo Ngrok (por exemplo, \`https://abc123.ngrok.io\`) e configure no seu painel do Twilio para o webhook do WhatsApp com essa URL, seguida pelo caminho específico que o aplicativo utiliza para receber mensagens (por exemplo, \`https://abc123.ngrok.io/messages\`).

## Como Rodar o Aplicativo

Após configurar todas as variáveis e o Ngrok, você pode iniciar o aplicativo com o seguinte comando:

`python3 -m app.whatsapp`

## Uso

Com o aplicativo rodando, qualquer mensagem recebida pelo seu número do WhatsApp configurado será automaticamente respondida pela inteligência artificial baseada nos parâmetros definidos em seu código.
