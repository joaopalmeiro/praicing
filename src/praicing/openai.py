import math
from pathlib import Path
from typing import Literal

from PIL import Image

BASE_TOKENS: dict[str, int] = {"gpt-4o-2024-08-06": 85}

TILE_TOKENS: dict[str, int] = {"gpt-4o-2024-08-06": 170}


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
