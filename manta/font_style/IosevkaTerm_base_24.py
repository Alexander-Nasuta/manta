from manta.font_style.fontABC import FontABC


class LatexFontSizing24(FontABC):

    font_name: str = "IosevkaTerm Nerd Font Mono"

    # for a base font size of 24pt
    font_size_tiny: int = 12
    font_size_script: int = 16
    font_size_footnote: int = 20
    font_size_small: int = 22
    font_size_normal: int = 24
    font_size_large: int = 28
    font_size_Large: int = 34
    font_size_LARGE: int = 40
    font_size_huge: int = 50
    font_size_Huge: int = 60