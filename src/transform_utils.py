from torchvision import transforms

# Code copied from:
# https://github.com/woctezuma/feature-extractor/blob/minimal/src/transform_utils.py

# Reference: https://github.com/facebookresearch/dinov2/blob/main/dinov2/data/transforms.py

IMAGENET_DEFAULT_MEAN = (0.485, 0.456, 0.406)
IMAGENET_DEFAULT_STD = (0.229, 0.224, 0.225)


def get_target_image_size(resize_size=256, keep_ratio=True):
    return resize_size if keep_ratio else (resize_size, resize_size)


def get_transform(
    resize_size=256,
    keep_ratio=True,
    crop_size=224,
    interpolation=transforms.InterpolationMode.BICUBIC,
):
    transforms_list = [
        transforms.Resize(
            get_target_image_size(resize_size, keep_ratio),
            interpolation=interpolation,
        ),
        transforms.CenterCrop(crop_size),
        transforms.ToTensor(),
        transforms.Normalize(mean=IMAGENET_DEFAULT_MEAN, std=IMAGENET_DEFAULT_STD),
    ]
    return transforms.Compose(transforms_list)
