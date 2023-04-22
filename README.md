# Steam DINOv2: match banners with Meta AI's DINOv2

This repository contains Python code to retrieve Steam games with similar store banners, using [Meta AI's DINOv2][fb-dinov2-demo].

Image similarity is assessed by the cosine similarity between image features encoded by DINOv2.

![Similar vertical banners][wiki-cover]

## Data

Data consists of **vertical** Steam banners (`library_600x900.jpg` at 300x450 resolution).

### Pre-processing

Indeed, DINOv2 follows torchvision's [pre-processing pipeline][dinov2-pre-process] for classification:
- resize to 256 resolution,
- center-crop at 224 resolution,
- normalize intensity.

```python
transforms_list = [
    transforms.Resize(resize_size, interpolation=interpolation),
    transforms.CenterCrop(crop_size),
    MaybeToTensor(),
    make_normalize_transform(mean=mean, std=std),
]
```

Therefore, downloaded images can be resized to 256x256 resolution before being store to disk.

## References

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

[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
