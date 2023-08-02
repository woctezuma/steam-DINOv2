from src.conversion_utils import convert_faiss_indices_to_app_ids
from src.feature_utils import get_features
from src.match_utils import search_faiss_index
from src.utils import retrieve_file_index


def find_similar_app_ids(
    query_app_id,
    preprocess,
    model,
    index,
    base_apps,
    base_indices,
    num_neighbors=10,
):
    query_vector = get_features(query_app_id, preprocess, model)
    scores, indices = search_faiss_index(index, query_vector, num_neighbors)

    return convert_faiss_indices_to_app_ids(indices, base_apps, base_indices)


def get_matches(
    app_id,
    precomputed_matches,
    filtered_app_ids,
    preprocess,
    model,
    index,
    base_apps,
    base_indices,
    num_neighbors=10,
    verbose=False,
):
    file_index = retrieve_file_index(app_id, filtered_app_ids)

    if file_index is None:
        similar_app_ids = find_similar_app_ids(
            app_id,
            preprocess,
            model,
            index,
            base_apps,
            base_indices,
            num_neighbors,
        )
        if verbose:
            print(f'[{app_id}] Computing features from scratch.')
    else:
        faiss_indices = precomputed_matches[file_index]
        similar_app_ids = convert_faiss_indices_to_app_ids(
            [faiss_indices],
            base_apps,
            base_indices,
        )[0]
        if verbose:
            print(
                f'[{app_id}] Looking up pre-computed features at position {file_index}.',
            )

    if verbose:
        print(f"[{app_id}] -> {similar_app_ids}")

    return similar_app_ids
