import mediapy as media

from src.web_utils import get_image_url


def get_image(app_id):
    return media.read_image(get_image_url(app_id))
