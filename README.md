# Steam DINOv2: match banners with Meta AI's DINOv2

This repository contains Python code to retrieve Steam games with similar store banners, using [Meta AI's DINOv2][fb-dinov2-demo].

Image similarity is assessed by the cosine similarity between image features encoded by DINOv2.

![Similar vertical banners][wiki-cover]

## Data

Data consists of **vertical** Steam banners (`library_600x900.jpg` at 300x450 resolution).

### Pre-processing

DINOv2 follows torchvision's [pre-processing pipeline][dinov2-pre-process] for classification:
- [resize][resize] to 256 resolution, i.e. the **smallest** edge of the image will match this number,
- [center-crop][centercrop] at 224 resolution, i.e. a **square** crop is made,
- normalize intensity.

```python
transforms_list = [
    transforms.Resize(resize_size, interpolation=interpolation),
    transforms.CenterCrop(crop_size),
    MaybeToTensor(),
    make_normalize_transform(mean=mean, std=std),
]
```

Therefore, downloaded images can be resized to 256x384 resolution before being stored to disk.

As discussed in [this Github issue][dinov2-pre-process-issue], the crop of DINOv2 can be made less agressive by resizing to 224 instead of 256 resolution.
In this case, downloaded images can be resized to 224x336 resolution before being stored to disk.

### Snapshot

A snapshot of image data was downloaded **on July 20, 2023** and stored as [a Github release][input-data-github-release].

If you wish to re-create this data snapshot, run [`download_steam_images.ipynb`][input-data-colab-notebook].
[![Open In Colab][colab-badge]][input-data-colab-notebook]

### Filtering (optional)

If you wish to filter the image dataset, identify issues with [`find_dataset_issues.ipynb`][cleanvision-colab-notebook].
[![Open In Colab][colab-badge]][cleanvision-colab-notebook]

## Usage

Run [`match_steam_images.ipynb`][match-colab-notebook].
[![Open In Colab][colab-badge]][match-colab-notebook]

## References

-   A [feature extractor][feature-extractor] for Github repositories which include a `hubconf.py` file.
-   A [feature matcher][feature-matcher] based on the `faiss` library.
-   [`match-steam-banners`][github-match-steam-banners]: retrieve games with similar store banners.
-   Facebook's DINO:
    - [Official blog post][fb-dino-blog]
    - [Official Github repository][fb-dino-code]
    - [Caron, Mathilde, et al. *Emerging Properties in Self-Supervised Vision Transformers*. arXiv 2021.][fb-dino-paper] 
-   Facebook's DINOv2:
    - [Official demo][fb-dinov2-demo]
    - [Official blog post][fb-dinov2-blog]
    - [Official Github repository][fb-dinov2-code]
    - [Oquab, Maxime, et al. *DINOv2: Learning Robust Visual Features without Supervision*. arXiv 2023.][fb-dinov2-paper] 

<!-- Definitions -->

[wiki-cover]: <https://github.com/woctezuma/steam-DINOv2/wiki/img/illustration.jpg>

[dinov2-pre-process]: <https://github.com/facebookresearch/dinov2/blob/f8969297dbe53373b4041bf47d997a8dcc8d2077/dinov2/data/transforms.py#L86-L91>

[fb-dino-blog]: <https://ai.facebook.com/blog/dino-paws-computer-vision-with-self-supervised-transformers-and-10x-more-efficient-training>
[fb-dino-code]: <https://github.com/facebookresearch/dino>
[fb-dino-paper]: <https://arxiv.org/abs/2104.14294>

[fb-dinov2-demo]: <https://dinov2.metademolab.com/>
[fb-dinov2-blog]: <https://ai.facebook.com/blog/dino-v2-computer-vision-self-supervised-learning/>
[fb-dinov2-code]: <https://github.com/facebookresearch/dinov2>
[fb-dinov2-paper]: <https://arxiv.org/abs/2304.07193>

[resize]: <https://pytorch.org/vision/main/generated/torchvision.transforms.Resize.html>
[centercrop]: <https://pytorch.org/vision/main/generated/torchvision.transforms.CenterCrop.html>
[dinov2-pre-process-issue]: <https://github.com/facebookresearch/dinov2/issues/86#issuecomment-1537198785>

[feature-extractor]: <https://github.com/woctezuma/feature-extractor>
[feature-matcher]: <https://github.com/woctezuma/feature-matcher>
[github-match-steam-banners]: <https://github.com/woctezuma/match-steam-banners>

[input-data-github-release]: <https://github.com/woctezuma/steam-DINOv2/releases/tag/input>
[input-data-colab-notebook]: <https://colab.research.google.com/github/woctezuma/steam-DINOv2/blob/main/download_steam_images.ipynb>
[cleanvision-colab-notebook]: <https://colab.research.google.com/github/woctezuma/steam-DINOv2/blob/main/find_dataset_issues.ipynb>
[match-colab-notebook]: <https://colab.research.google.com/github/woctezuma/steam-DINOv2/blob/main/match_steam_images.ipynb>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
