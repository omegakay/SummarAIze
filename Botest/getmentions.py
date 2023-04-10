import tweepy
import config

client = tweepy.Client(consumer_key=config.API_Key,
                       consumer_secret=config.API_Secret,
                       access_token=config.Access_Token,
                       access_token_secret=config.Access_Token_Secret,
                       bearer_token=config.Bearer_Token)


# Get User's Mentions

# This endpoint/method returns Tweets mentioning a single user specified by the
# requested user ID

user_id = 1645354319657541632

response = client.get_users_mentions(user_id)

# By default, only the ID and text fields of each Tweet will be returned
for tweet in response.data:
    print(tweet.id)
    print(tweet.text)

# By default, the 10 most recent Tweets will be returned
# You can retrieve up to 100 Tweets by specifying max_results
response = client.get_users_mentions(user_id, max_results=1)