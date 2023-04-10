import tweepy
import requests
import re
import openai

# Variables de autenticación de la API de Twitter
consumer_key = "TU_CONSUMER_KEY"
consumer_secret = "TU_CONSUMER_SECRET"
access_token = "TU_ACCESS_TOKEN"
access_token_secret = "TU_ACCESS_TOKEN_SECRET"

# Variables de autenticación de OpenAI
openai.api_key = "TU_API_KEY"

# Autenticación de la API de Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Función para obtener el resumen de un artículo utilizando ChatGPT
def obtener_resumen(texto):
    respuesta = openai.Completion.create(
        engine="davinci",
        prompt=(f"Resumen del artículo:\n{texto}\n\nResumen:"),
        temperature=0.5,
        max_tokens=50,
        n=1,
        stop=None,
        timeout=10,
    )
    return respuesta.choices[0].text.strip()

# Función para analizar los tweets y generar respuestas
def analizar_tweet(tweet):
    # Buscar enlaces en el tweet
    enlaces = re.findall('(https?://[^\s]+)', tweet.text)
    for enlace in enlaces:
        # Descargar el contenido de la página
        respuesta = requests.get(enlace)
        if respuesta.status_code == 200:
            # Extraer el texto del artículo
            texto = re.findall('<p>(.*?)</p>', respuesta.text)
            texto = "\n".join(texto)
            # Generar el resumen utilizando ChatGPT
            resumen = obtener_resumen(texto)
            # Responder al tweet con el resumen
            respuesta = f"@{tweet.user.screen_name} Aquí tienes un resumen: {resumen}"
            api.update_status(
                status=respuesta,
                in_reply_to_status_id=tweet.id
            )

# Función para responder a menciones
def responder_mencion():
    menciones = api.mentions_timeline()
    for mencion in menciones:
        analizar_tweet(mencion)

# Ejecución del bot
while True:
    responder_mencion()
