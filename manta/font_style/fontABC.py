from abc import ABC


class FontABC(ABC):
    font_name: str

    font_size_tiny: int
    font_size_script: int
    font_size_footnote: int
    font_size_small: int
    font_size_normal: int
    font_size_large: int
    font_size_Large: int
    font_size_LARGE: int
    font_size_huge: int
