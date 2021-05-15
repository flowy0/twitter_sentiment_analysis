import tweepy
from dotenv import dotenv_values
import logging
import csv
import utils


LOGGER = logging.getLogger(__name__)
logging.basicConfig(level='INFO')


def get_public_tweets(config, filename):
    OUTPUT_DIR = filename.split("/")[0]
    utils.create_dir(folder=OUTPUT_DIR)

    consumer_key = config['API_KEY']
    consumer_secret = config['API_KEY_SECRET']
    access_token_key = config['ACCESS_TOKEN']
    access_token_secret = config['ACCESS_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth)

    # filename='data/csv/test_tweets.csv'

    public_tweets = api.user_timeline("BarackObama")
    LOGGER.info(f"data type: {type(public_tweets)}")
    LOGGER.info(f"number of tweets: {len(public_tweets)}")
    tweets_dict = {'tweet': []}
    for tweet in public_tweets:
        # LOGGER.info(tweet.text)
        tweets_dict['tweet'].append(tweet.text)

    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in public_tweets]
    # write the csv
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(outtweets)
    LOGGER.info(f"data saved to {filename}")

    return tweets_dict





if __name__ == '__main__':
    OUTPUT_FILE = 'data/csv/test_user_obama.csv'
    
    # LOGGER.info(f"Output Dir: {OUTPUT_DIR}")

    env_vars = dotenv_values(".env")
    tweets = get_public_tweets(config=env_vars, filename=OUTPUT_FILE)
    
    # utils.export_json(input_dict=tweets, file_path=OUTPUT_FILE)
