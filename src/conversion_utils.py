from pathlib import Path

IMAGE_SUFFIX = ".jpg"


def to_image_index(image_name, image_suffix=IMAGE_SUFFIX):
    index_as_str = Path(image_name).name.removesuffix(image_suffix)
    return int(index_as_str)
