from manta.color_theme.color_theme_ABC import ColorThemeABC


class CatppuccinThemeABC(ColorThemeABC):
    """
    The CatppuccinThemeABC defines the color scheme of the Catppuccino color theme.
    It defines additional color colors to the ones defined in the ColorThemeABC.

    The colors are taken from: https://github.com/catppuccin/catppuccin

    """
    rosewater: str
    flamingo: str
    pink: str
    mauve: str
    red: str
    maroon: str
    peach: str
    yellow: str
    green: str
    teal: str
    sky: str
    sapphire: str
    blue: str
    lavender: str
    text: str
    subtext1: str
    subtext0: str
    overlay2: str
    overlay1: str
    overlay0: str
    surface2: str
    surface1: str
    surface0: str
    base: str
    mantle: str
    crust: str