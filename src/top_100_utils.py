from urllib.error import HTTPError

from src.pipeline_utils import get_matches
from src.print_utils import print_ranking_for_app_id


def retrieve_similar_app_ids_for_app_id_batch(
    app_id_batch,
    precomputed_matches,
    filtered_app_ids,
    preprocess,
    model,
    index,
    base_apps,
    base_indices,
    num_neighbors,
    verbose=False,
):
    dict_of_similar_app_ids = {}

    for app_id in app_id_batch:
        try:
            similar_app_ids = get_matches(
                app_id,
                precomputed_matches,
                filtered_app_ids,
                preprocess,
                model,
                index,
                base_apps,
                base_indices,
                num_neighbors,
                verbose=verbose,
            )
        except (HTTPError, RuntimeError) as e:
            print(f"[ERROR] appID = {app_id}")
            continue

        dict_of_similar_app_ids[app_id] = similar_app_ids[0]

    return dict_of_similar_app_ids


def show_similar_app_ids_for_app_id_batch(dict_of_similar_app_ids):
    for k, v in dict_of_similar_app_ids.items():
        print_ranking_for_app_id(k, v)
