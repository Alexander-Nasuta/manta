from manta.color_theme.color_theme_ABC import ColorThemeABC


class CarolusTheme(ColorThemeABC):
    """
    CarolusTheme defines colors specified by CarolusTheme. It is inspired by the color scheme of the weights and biases
    website: https://wandb.ai/site
    """
    background_color: str = "#1A1C1F"
    background_color_bright: str = "#212328"

    font_color: str = "#FFFFFF"
    font_color_secondary: str = "#ADB0B5"

    black: str = "#1A1C1F"
    black_bright: str = "#212328"

    red: str = "#EC5E80"
    red_bright: str = "#EC5E80"

    green: str = "#54AE9D"
    green_bright: str = "#46c9d2"

    yellow: str = "#F7CE55"
    yellow_bright: str = "#fede8d"

    blue: str = "#618DE7"
    blue_bright: str = "#7DB0D8"

    magenta: str = "#cf47f9"
    magenta_bright: str = "#cf47f9"

    cyan: str = "#4FACBF"
    cyan_bright: str = "#304F5B"

    white: str = "#FFFFFF"
    white_bright: str = "#FFFFFF"