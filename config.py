from keys import *
import tweepy
import logging


def create_api():
    logger = logging.getLogger()

    auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
    )

    api = tweepy.API(auth, wait_on_rate_limit=True)

    logger.info("API created")
    return api


# client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)



# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
