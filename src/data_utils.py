import json
from pathlib import Path

from src.web_utils import get_image_url

URL_LIST_FNAME = "urls.txt"
APP_LIST_FNAME = "apps.json"
FILTERED_INDEX_FNAME = "filtered_indices.json"
FILTERED_APP_LIST_FNAME = 'filtered_apps.json'
TOP_100_OUTPUT_FOLDER = "similar_to_top_100"


def load_data(fname):
    with Path(fname).open() as f:
        data = json.load(f)
    return data


def save_app_list(app_ids, fname=APP_LIST_FNAME):
    with Path(fname).open('w') as f:
        json.dump(app_ids, f)


def save_list(elements, fname):
    with Path(fname).open('w') as f:
        for e in elements:
            f.write(f'{e}\n')


def save_image_list(app_ids, fname=URL_LIST_FNAME):
    elements = [get_image_url(app_id) for app_id in app_ids]
    save_list(elements, fname)


def get_top_100_fname(model_name, file_extension=".json"):
    Path(TOP_100_OUTPUT_FOLDER).mkdir(parents=True, exist_ok=True)
    return f"{TOP_100_OUTPUT_FOLDER}/{model_name}{file_extension}"
