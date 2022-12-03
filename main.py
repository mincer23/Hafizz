
import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")

            # if not tweet.user.following:
            #     tweet.user.follow()

            api.update_status(
                status="Please reach us via DM",
                in_reply_to_status_id=tweet.id,
            )
    return new_since_id

def check_sport(api):
    tweets = api.get_favorites()

    vals = []

    for tweet in tweepy.Cursor(api.home_timeline).items():
        if "sports" in tweet.text:
            vals.append[tweet]


def get_location(api):
    locations = api.reverse_geocode(lat='35.7219', long = '51.3347')
    # 272596500e51c07a


            

def main():
    api = create_api()
    get_location(api)
    # since_id = 1
    # while True:
    #     since_id = check_mentions(api, ["help", "support"], since_id)
    #     logger.info("Waiting...")
    #     time.sleep(60)

if __name__ == "__main__":
    main()


