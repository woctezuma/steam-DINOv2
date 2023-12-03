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

> [!Note]
> For the same appID, there can exist some differences between matches computed on the fly and pre-computed matches, because matches are obtained based on features extracted from images resized with different interpolation algorithms:
> - for on-the-fly matching, images are resized with [`transforms.InterpolationMode.BICUBIC`][dinov2-bicubic-interpolation],
> - for pre-computed matches, images were resized by [`img2dataset`][img2dataset-downscale-interpolation] with [`cv2.INTER_AREA`][opencv-interpolation-flags], as suggested [in the doc][opencv-resize] of OpenCV for downscale interpolation.

## Results

For each game in the top 100 most played games in the past 2 weeks, the 10 most similar games are retrieved with:
- [ViT-S/14 distilled][wiki-results-ViTS],
- [ViT-B/14 distilled][wiki-results-ViTB],
- [ViT-L/14 distilled][wiki-results-ViTL].

AppIDs for all these apps can be found in JSON files in [`data/similar_to_top_100/`](data/similar_to_top_100/).

> [!Note]
> The linked pages contain a lot of images and might be slow to load depending on your Internet bandwidth.

### Examples obtained with ViT-L

#### Same visual theme

Basket ball:

![NBA](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/nba.jpg)

Cartoony monsters:

![Binding of Isaac](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/isaac.jpg)

Colorful:

![Fall Guys](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/fall_guys.jpg)

Far West:

![Red Dead Redemption](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/red_dead.jpg)

Paladins in anime style:

![Paladins](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/paladins.jpg)

#### Same character

Armed persons with helmets:

![Counter-Strike Global Offensive](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/cs_go.jpg)

Dinosaurs:

![Dinosaurs](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/ark.jpg)

Knights:

![Terraria](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/terraria.jpg)

Robots:

![Robocraft](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/robocraft.jpg)

#### Same item

Bows:

![Bow](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/tomb_raider.jpg)

Cars:

![Rocket League](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/rocket_league.jpg)

Castles:

![Hogwarts](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/hogwarts.jpg)

Farms:

![Stardew Valley](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/stardew_valley.jpg)

Tanks:

![World of Tanks](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/world_of_tanks.jpg)

Tools:

![Raft](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/raft.jpg)

#### Same franchise

Borderlands:

![Borderlands](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/borderlands.jpg)

Cities (with skyscrapers):

![Skyscrapers](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/cities.jpg)

Hollow Knight:

![Hollow Knight](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/hollow_knight.jpg)

Left 4 Dead (with hands):

![Left 4 Dead](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/l4d.jpg)

Monster Hunter (with dragons):

![Monster Hunter](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/monster_hunter.jpg)

Mount & Blade (with horses):

![Mount & Blade](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/mount_blade.jpg)

Naraka:

![Naraka](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/naraka.jpg)

Payday:

![Payday](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/payday.jpg)

The Witcher (with Geralt of Rivia):

![The Witcher 3](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/witcher.jpg)

Truck simulators:

![EuroTruck](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/eurotruck.jpg)

War planes:

![Warplanes](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/warplanes.jpg)

War vehicles:

![Warthunder](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-L/warthunder.jpg)

### Comparison of ViT-S, ViT-B and ViT-L

Each model performs reasonably well in terms of image retrieval.

#### ViT-S

The following results are obtained with ViT-S.

Cars in *Rocket League*:

![Rocket League](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-S/rocket_league.jpg)

Cars in *Wallpaper Engine*:

![Wallpaper Engine](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-S/wallpaper_engine.jpg)

Dinosaurs:

![Ark](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-S/ark.jpg)

Farms:

![Stardew Valley](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-S/stardew_valley.jpg)

Persons standing in a forest:

![Stardew Valley](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-S/valheim.jpg)

Robots:

![Robocraft](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-S/robocraft.jpg)

Sailing:

![Raft](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-S/raft.jpg)

Tanks:

![War Thunder](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-S/war_thunder.jpg)

Interestingly, the results for *The Binding of Isaac* may be better than with ViT-L.

![Binding of Isaac](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-S/isaac.jpg)

The first match for *Sekiro* reveals a similarity between Wolf in *Sekiro* and Mitsurugi in *Soul Calibur*.

![Sekiro](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-S/sekiro.jpg)

Most matches for *Naraka* include a sword-like weapon with a blue glow:

![Naraka](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-S/naraka.jpg)

#### ViT-B

The following results are obtained with ViT-B.

Bows:

![Tomb Raider](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-B/tomb_raider.jpg)

Cartoon characters with a white mask:

![Hollow Knight](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-B/hollow_knight.jpg)

Colorful:

![Fall Guys](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-B/fall_guys.jpg)

Dinosaurs:

![Ark](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-B/ark.jpg)

Interestingly, the first match for *Monster Hunter* is correctly in the same franchise.

![Monster Hunter](https://github.com/woctezuma/steam-DINOv2/wiki/img/ViT-B/monster_hunter.jpg)

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

[dinov2-bicubic-interpolation]: <https://github.com/facebookresearch/dinov2/blob/c3c2683a13cde94d4d99f523cf4170384b00c34c/dinov2/data/transforms.py#L81>
[opencv-interpolation-flags]: <https://docs.opencv.org/4.8.0/da/d54/group__imgproc__transform.html#ga5bb5a1fea74ea38e1a5445ca803ff121>
[img2dataset-downscale-interpolation]: <https://github.com/rom1504/img2dataset/blob/f0188aedb897f94eb0d39ccefba641174244b927/img2dataset/resizer.py#L88>
[opencv-resize]: <https://docs.opencv.org/4.8.0/da/d54/group__imgproc__transform.html#ga47a974309e9102f5f08231edc7e7529d>

[wiki-results-ViTS]: <https://github.com/woctezuma/steam-DINOv2/wiki/Benchmark-top100-ViT%E2%80%90S-14>
[wiki-results-ViTB]: <https://github.com/woctezuma/steam-DINOv2/wiki/Benchmark-top100-ViT%E2%80%90B-14>
[wiki-results-ViTL]: <https://github.com/woctezuma/steam-DINOv2/wiki/Benchmark-top100-ViT%E2%80%90L-14>

[input-data-github-release]: <https://github.com/woctezuma/steam-DINOv2/releases/tag/input>
[input-data-colab-notebook]: <https://colab.research.google.com/github/woctezuma/steam-DINOv2/blob/main/download_steam_images.ipynb>
[cleanvision-colab-notebook]: <https://colab.research.google.com/github/woctezuma/steam-DINOv2/blob/main/find_dataset_issues.ipynb>
[match-colab-notebook]: <https://colab.research.google.com/github/woctezuma/steam-DINOv2/blob/main/match_steam_images.ipynb>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
