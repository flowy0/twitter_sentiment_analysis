import tweepy
from dotenv import dotenv_values
import logging
import utils

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level='INFO')


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
    utils.create_dir(folder=OUTPUT_DIR)
    utils.export_json(input_dict=tweets, file_path=OUTPUT_FILE)
