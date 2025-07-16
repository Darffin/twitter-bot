# Twitter Reply Bot com OpenAI (GPT) ou Gemini (Melhor plano gratuito!)

Este projeto é um bot automatizado que monitora uma conta do Twitter (X), detecta novos tweets (exceto retweets) e responde automaticamente com uma mensagem gerada pela API do Gemini (ou pela OpenAI, o que preferir), de forma amigável e divertida.

## 🛠️ Funcionalidades

- Monitora uma conta específica do Twitter.
- Ignora retweets.
- Gera respostas curtas e criativas com IA.
- Publica automaticamente como resposta ao tweet original.
- Lida com erros comuns de conexão e limites de uso da API.

## 📦 Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Tweepy](https://www.tweepy.org/) — integração com a API do Twitter.
- [OpenAI Python SDK](https://github.com/openai/openai-python) — geração de respostas com IA.
- [python-dotenv](https://pypi.org/project/python-dotenv/) — para gerenciamento de variáveis de ambiente.

## 📁 Estrutura

📦 Twitter-OpenAI-Bot
├── .env # Credenciais (NÃO SUBA ISSO NO GITHUB!)
├── .gitignore
├── main.py # Código principal do bot
├── requirements.txt # Lista de dependências
└── README.md # Este arquivo

## 🔧 Como usar

```bash
# Clone o repositório

git clone https://github.com/Darffin/twitter-bot.git
cd twitter-bot

# Criar e ative um ambiente virtual (opcional, mas recomendado)
python -m venv venv 
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Crie um arquivo .env na raiz com o seguinte conteúdo (preencha com suas chaves):

BEARER_TOKEN=...
CONSUMER_KEY=...
CONSUMER_SECRET=...
ACCESS_TOKEN=...
ACCESS_TOKEN_SECRET=...
OPENAI_API_KEY=...
GEMINI_API_KEY=...
USER_ID=123456789 # ID do Twitter
# Para obter o USER_ID de uma conta basta usar o Tweepy!
# user = client.get_user("UmCaraDaora") # Username dentro das aspas
# userID = user.data.id

# Execute o bot
python main.py


