from manta.font_style.fontABC import FontABC


class LatexFontSizing12(FontABC):
    font_name: str = "IosevkaTerm Nerd Font Mono"

    # for a base font size of 12pt
    font_size_tiny: int = 6
    font_size_script: int = 8
    font_size_footnote: int = 10
    font_size_small: int = 11
    font_size_normal: int = 12
    font_size_large: int = 14
    font_size_Large: int = 17
    font_size_LARGE: int = 20
    font_size_huge: int = 25
    font_size_Huge: int = 30
