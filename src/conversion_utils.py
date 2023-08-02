from pathlib import Path

IMAGE_SUFFIX = ".jpg"


def to_image_index(image_name, image_suffix=IMAGE_SUFFIX):
    index_as_str = Path(image_name).name.removesuffix(image_suffix)
    return int(index_as_str)


def convert_faiss_single_output_to_app_id(i, base_apps, base_indices):
    return base_apps[base_indices[i]]


def convert_faiss_indices_to_app_ids(faiss_indices, base_apps, base_indices):
    result = []

    for small_list in faiss_indices:
        app_ids = [
            convert_faiss_single_output_to_app_id(i, base_apps, base_indices)
            for i in small_list
        ]
        result.append(app_ids)

    return result
