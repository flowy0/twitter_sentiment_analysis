import tweepy
from dotenv import dotenv_values
import logging
import utils

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level='INFO')


def get_tweets_from_user(username, output_dir, config_key=dotenv_values(), tweet_limit=50):
    consumer_key = config_key['API_KEY']
    consumer_secret = config_key['API_KEY_SECRET']
    access_token_key = config_key['ACCESS_TOKEN']
    access_token_secret = config_key['ACCESS_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api_call = tweepy.API(auth, wait_on_rate_limit=True)

    return_tweets = tweepy.Cursor(api_call.user_timeline,
                                  screen_name=username,
                                  count=None,
                                  since_id=None,
                                  max_id=None,
                                  trim_user=True,
                                  exclude_replies=True,
                                  contributor_details=False,
                                  include_entities=False
                                  ).items(tweet_limit)
    tweets_dict = {'tweet': []}
    for tweet in return_tweets:
        # LOGGER.info(tweet.text)
        tweets_dict['tweet'].append(tweet.text)

    # export
    utils.create_dir(output_dir)
    LOGGER.info(f"Output Dir: {output_dir}")

    output_file = f"{output_dir}/tweets_{username}.json"

    utils.export_json(tweets_dict, output_file)


if __name__ == '__main__':
    OUTPUT_DIR = 'data'

    list_usernames = ['Microsoft', 'amazon', 'googledevs', 'googlenews', 'ChannelNewsAsia']
    for user in list_usernames:
        get_tweets_from_user(username=user, output_dir=OUTPUT_DIR)


