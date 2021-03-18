
import twitter
from dotenv import dotenv_values
import logging

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level='INFO')
# LOGGER.info(config)
# LOGGER.info(config['API_KEY'])

# load_dotenv()
# consumer_key=


def test_keys():
    config = dotenv_values(".env")
    try:
        api = twitter.Api(consumer_key=config['API_KEY'],
                          consumer_secret=config['API_KEY_SECRET'],
                          access_token_key=config['ACCESS_TOKEN'],
                          access_token_secret=config['ACCESS_SECRET'])
        LOGGER.info(api)
    except Exception as e:
        LOGGER.info(e)


if __name__ == '__main__':

    test_keys()
