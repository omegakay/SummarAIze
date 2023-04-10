import tweepy
import config

client = tweepy.Client(consumer_key=config.API_Key,
                       consumer_secret=config.API_Secret,
                       access_token=config.Access_Token,
                       access_token_secret=config.Access_Token_Secret,
                       bearer_token=config.Bearer_Token)


# Get tweets that contain the hashtag #petday
# -is:retweet means I don't want retweets
# lang:en is asking for the tweets to be in english
query = '#petday -is:retweet lang:en'
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

"""
What context_annotations are: 
https://developer.twitter.com/en/docs/twitter-api/annotations/overview
"""
for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)