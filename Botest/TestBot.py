import tweepy
import config

client = tweepy.Client(consumer_key=config.API_Key,
                       consumer_secret=config.API_Secret,
                       access_token=config.Access_Token,
                       access_token_secret=config.Access_Token_Secret)

response = client.create_tweet(text='Hello World!!!')

print(response)