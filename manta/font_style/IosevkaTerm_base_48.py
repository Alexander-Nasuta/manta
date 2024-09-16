from manta.font_style.fontABC import FontABC


class LatexFontSizing48(FontABC):

    font_name: str = "IosevkaTerm Nerd Font Mono"

    # for a base font size of 48pt
    font_size_tiny: int = 24
    font_size_script: int = 32
    font_size_footnote: int = 40
    font_size_small: int = 44
    font_size_normal: int = 48
    font_size_large: int = 56
    font_size_Large: int = 68
    font_size_LARGE: int = 80
    font_size_huge: int = 100
    font_size_Huge: int = 120