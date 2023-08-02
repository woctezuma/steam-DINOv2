from src.steam_store_utils import get_store_url
from src.web_utils import get_image_url as get_banner_url

# Code copied from:
# https://github.com/woctezuma/match-steam-banners/blob/master/print_utils.py

DEFAULT_IMAGE_WIDTH = 150
DEFAULT_APP_NAME = "Unknown"


def get_bb_code_linked_image(app_id):
    image_link_str = '[url={}][img="width:{}px;"]{}[/img][/url]'

    bb_code_linked_image = image_link_str.format(
        get_store_url(app_id),
        DEFAULT_IMAGE_WIDTH,
        get_banner_url(app_id),
    )

    return bb_code_linked_image


def get_html_linked_image(app_id, app_name=None):
    if app_name is None:
        app_name = DEFAULT_APP_NAME

    # Reference: https://stackoverflow.com/a/14747656
    image_link_str = '[<img alt="{}" src="{}" width="{}">]({})'

    html_linked_image = image_link_str.format(
        app_name,
        get_banner_url(app_id),
        DEFAULT_IMAGE_WIDTH,
        get_store_url(app_id),
    )

    return html_linked_image


def print_ranking_for_app_id(
    query_app_id,
    reference_app_id_counter,
    num_elements_displayed=10,
):
    html_linked_image = get_html_linked_image(query_app_id)

    print(f"\nQuery:\n\n{html_linked_image}\n\n")

    for rank, app_id in enumerate(reference_app_id_counter, start=1):
        html_linked_image = get_html_linked_image(app_id)

        print(html_linked_image, end="")

        # Display results on two rows
        if rank == num_elements_displayed / 2:
            print("\n")

        if rank >= num_elements_displayed:
            break

    print("\n")
