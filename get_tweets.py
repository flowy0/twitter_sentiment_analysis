import tweepy
from dotenv import dotenv_values
import logging
import utils
import csv

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level='INFO')


def get_tweets_from_user(username, output_dir, config_key=dotenv_values(), tweet_limit=250):
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

    LOGGER.info(f"{return_tweets=}")

    # tweets_dict = {'tweet': []}
    # for tweet in return_tweets:
        # LOGGER.info(tweet.text)
        # tweets_dict['tweet'].append(tweet.text)

    # export json
    # utils.create_dir(output_dir)
    # LOGGER.info(f"Output Dir: {output_dir}")

    # utils.create_dir(f"{output_dir}/json")
    # output_json = f"{output_dir}/json/tweets_{username}.json"
    # utils.export_json(tweets_dict, output_json)

    utils.create_dir(f"{output_dir}/csv")
    output_csv = f"{output_dir}/csv/tweets_{username}.csv"

    #export csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in return_tweets]
    # LOGGER.info(f"{outtweets=}")
    # write the csv
    with open(output_csv, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(outtweets)
    LOGGER.info(f"data saved to {output_csv}")

    # return tweets_dict



if __name__ == '__main__':
    OUTPUT_DIR = 'data'

    list_usernames = ['Microsoft', 'amazon', 'googledevs', 'googlenews', 'ChannelNewsAsia']
    # list_usernames = ['ChannelNewsAsia']

    for user in list_usernames:
        get_tweets_from_user(username=user, output_dir=OUTPUT_DIR)

