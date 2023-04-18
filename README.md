# Steam DINOv2: match banners with Meta AI's DINOv2

This repository contains Python code to retrieve Steam games with similar store banners, using [Meta AI's DINOv2][fb-dinov2-demo].

Image similarity is assessed by the cosine similarity between image features encoded by DINOv2.

![Similar vertical banners][wiki-cover]

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

[fb-dino-blog]: <https://ai.facebook.com/blog/dino-paws-computer-vision-with-self-supervised-transformers-and-10x-more-efficient-training>
[fb-dino-code]: <https://github.com/facebookresearch/dino>
[fb-dino-paper]: <https://arxiv.org/abs/2104.14294>

[fb-dinov2-demo]: <https://dinov2.metademolab.com/>
[fb-dinov2-blog]: <https://ai.facebook.com/blog/dino-v2-computer-vision-self-supervised-learning/>
[fb-dinov2-code]: <https://github.com/facebookresearch/dinov2>
[fb-dinov2-paper]: <https://arxiv.org/abs/2304.07193>

[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
