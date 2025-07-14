import tweepy
import os
import time
import openai
from openai import OpenAI
from requests.exceptions import ConnectionError
from dotenv import load_dotenv

load_dotenv()

USER_ID = int(os.getenv("USER_ID"))

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

twitter_client = tweepy.Client(
    bearer_token=os.getenv("BEARER_TOKEN"),
    consumer_key=os.getenv("CONSUMER_KEY"),
    consumer_secret=os.getenv("CONSUMER_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

def gerar_resposta(tweet_text):
    if not tweet_text:
        return None
    
    prompt = f"Responda de forma engraçada, amigável e breve ao seguinte tweet:\n{tweet_text}"
    try:
        resposta = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return resposta.choices[0].message.content.strip()

    except Exception as e:
        print(f"Erro com a OpenAI API: {type(e).__name__} - {e}")
        return None

ultimo_tweet_id = None

print("Bot iniciado... monitorando a conta.")

while True:
    try:
        tweets = twitter_client.get_users_tweets(id=USER_ID, max_results=5)

        if tweets.data:
            tweet = tweets.data[0]

            if tweet.id != ultimo_tweet_id and not tweet.text.startswith("RT "):
                print(f"Novo tweet detectado: {tweet.text}")
                
                resposta = gerar_resposta(tweet.text)
                if resposta and resposta.strip():
                    twitter_client.create_tweet(
                        text=resposta,
                        in_reply_to_tweet_id=tweet.id
                    )
                    print(f"Respondido com: {resposta}")
                    ultimo_tweet_id = tweet.id
                else:
                    print("Resposta em branco ou erro ao gerar.")

            else:
                print("Nenhum novo tweet encontrado ou é retweet.")
        else:
            print("Nenhum tweet encontrado na conta.")

        time.sleep(300)

    except tweepy.TooManyRequests:
        print("Limite de requisições atingido. Timeout de 15 minutos...")
        time.sleep(15 * 60)

    except ConnectionError:
        print("Problema de conexão com a internet. Timeout de 1 minuto...")
        time.sleep(60)

    except Exception as e:
        print(f"Não sei o que deu: {type(e).__name__} - {e}")
        time.sleep(60)
