import json
import logging
import os

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level='INFO')


def export_json(input_dict, file_path):
    with open(file_path, 'w') as outfile:
        json.dump(input_dict, outfile)
        LOGGER.info(f"file saved to {file_path}")


def create_dir(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
        LOGGER.info(f"dir {folder} created")