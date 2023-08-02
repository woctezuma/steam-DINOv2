import numpy as np
import torch
from torchvision import transforms

from src.image_utils import get_image


def get_features(app_id, preprocess, model):
    img = get_image(app_id)

    if isinstance(img, np.ndarray):
        img = transforms.ToPILImage()(img)

    img = preprocess(img)

    # There is only one query appID. So we add a batch dimension.
    img = img[None, :]

    with torch.no_grad():
        features = model(img.cuda()).cpu()

    return features.numpy()
