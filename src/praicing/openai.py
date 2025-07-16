import math
from pathlib import Path
from typing import Literal

from PIL import Image

BASE_TOKENS: dict[str, int] = {"gpt-4o-2024-08-06": 85}

TILE_TOKENS: dict[str, int] = {"gpt-4o-2024-08-06": 170}

PATCH_SIZE = 32
MAX_PATCHES = 1536

MULTIPLIERS = {"gpt-4.1-mini-2025-04-14": 1.62, "gpt-4.1-nano-2025-04-14": 2.46}


def count_tokens_for_image_with_detail(
    image: Path, model: str, detail: Literal["low", "high"]
) -> int:
    if detail == "low":
        # "Regardless of input size, low detail images are a fixed cost."
        return BASE_TOKENS[model]

    with Image.open(image) as img:
        width, height = img.size

    # "1. Scale to fit in a 2048px x 2048px square, maintaining original aspect ratio"
    max_dim = max(width, height)
    if max_dim > 2048:
        scale_factor = 2048 / max_dim
        width = int(width * scale_factor)
        height = int(height * scale_factor)

    # "2. Scale so that the image's shortest side is 768px long"
    min_dim = min(width, height)
    if min_dim > 768:
        scale_factor = 768 / min_dim
        width = int(width * scale_factor)
        height = int(height * scale_factor)

    # "3. Count the number of 512px squares in the image"
    tiles_wide = math.ceil(width / 512)
    tiles_high = math.ceil(height / 512)
    total_tiles = tiles_wide * tiles_high

    # "4. Add the base tokens to the total"
    tiles_tokens = total_tiles * TILE_TOKENS[model]
    total_tokens = tiles_tokens + BASE_TOKENS[model]

    return total_tokens


def count_tokens_for_image(image: Path, model: str) -> int:
    with Image.open(image) as img:
        width, height = img.size

    # "A. Calculate the number of 32px x 32px patches that are needed to fully cover the image"
    raw_patches_width = math.ceil(width / PATCH_SIZE)
    raw_patches_height = math.ceil(height / PATCH_SIZE)
    raw_patches = raw_patches_width * raw_patches_height

    # "B. If the number of patches exceeds 1536, we scale down the image so that it can be covered by no more than 1536 patches"
    if raw_patches > MAX_PATCHES:
        r = math.sqrt((PATCH_SIZE**2) * MAX_PATCHES / (width * height))

        r = r * min(
            math.floor(width * r / PATCH_SIZE) / (width * r / PATCH_SIZE),
            math.floor(height * r / PATCH_SIZE) / (height * r / PATCH_SIZE),
        )

        width = width * r
        height = height * r

    # "C. The token cost is the number of patches, capped at a maximum of 1536 tokens"
    patches_width = math.ceil(width / PATCH_SIZE)
    patches_height = math.ceil(height / PATCH_SIZE)
    patches = patches_width * patches_height
    patches = min(patches, MAX_PATCHES)

    total_tokens = math.ceil(patches * MULTIPLIERS[model])

    return total_tokens
