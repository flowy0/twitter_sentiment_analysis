import tweepy
from dotenv import dotenv_values
import json
import os
import logging

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level='INFO')


def export_json(file_path):
    with open(file_path, 'w') as outfile:
        json.dump(tweets, outfile)
        LOGGER.info(f"file saved to {file_path}")


def create_dir(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
        LOGGER.info(f"dir {folder} created")


def get_public_tweets(config):
    consumer_key = config['API_KEY']
    consumer_secret = config['API_KEY_SECRET']
    access_token_key = config['ACCESS_TOKEN']
    access_token_secret = config['ACCESS_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    LOGGER.info(f"data type: {type(public_tweets)}")
    LOGGER.info(f"number of tweets: {len(public_tweets)}")
    tweets_dict = {'tweet': []}
    for tweet in public_tweets:
        # LOGGER.info(tweet.text)
        tweets_dict['tweet'].append(tweet.text)

    return tweets_dict


if __name__ == '__main__':
    OUTPUT_FILE = 'data/tweets.json'
    OUTPUT_DIR = OUTPUT_FILE.split("/")[0]
    LOGGER.info(f"Output Dir: {OUTPUT_DIR}")

    env_vars = dotenv_values(".env")
    tweets = get_public_tweets(config=env_vars)
    create_dir(folder=OUTPUT_DIR)
    export_json(file_path=OUTPUT_FILE)
