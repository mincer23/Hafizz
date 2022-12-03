from twitter import *
from keys import *
import tweepy

# t = Twitter (auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

# t.search.tweets(q = "world cup")

# auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)

# api = tweepy.API(auth)

client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key,   consumer_secret= consumer_secret, 
    access_token=access_token, access_token_secret=access_token_secret)

muted = client.get_me()

print(muted)

# query = 'hafiz'

# tweets = client.search_recent_tweets(query=query)

# for tweet in tweets.data:
#     print(tweet.text)
#     if len(tweet.context_annotations) > 0:
#         print(tweet.context_annotations)