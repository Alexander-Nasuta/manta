from manta.color_theme.tokyo_night.tokyo_night_ABC import TokyoNightABC


class TokyoNightStorm(TokyoNightABC):
    # ColorThemeABC
    background_color: str = "#1f2335"
    background_color_bright: str = "#3b4261"

    font_color: str = "#7982a9"
    font_color_secondary: str = "#a9b1d6"

    surface_color: str = "#3b4261"
    outline_color: str = "#565f89"

    black: str = "#3b4261"
    black_bright: str = "#3b4261"

    red: str = "#f7768e"
    red_bright: str = "#f7768e"

    green: str = "#73daca"
    green_bright: str = "#73daca"

    yellow: str = "#e0af68"
    yellow_bright: str = "#e0af68"

    blue: str = "#7aa2f7"
    blue_bright: str = "#7aa2f7"

    magenta: str = "#bb9af7"
    magenta_bright: str = "#bb9af7"

    cyan: str = "#7dcfff"
    cyan_bright: str = "#7dcfff"

    white: str = "#7982a9"
    white_bright: str = "#a9b1d6"

    # TokyoNightABC
    night: str = "#1f2335"
    storm: str = "#3b4261"
    moon: str = "#7982a9"
    dragon: str = "#f7768e"
    spring: str = "#73daca"
    wave: str = "#7aa2f7"
    sakura: str = "#bb9af7"
    autumn: str = "#e0af68"
    winter: str = "#e0af68"
    summer: str = "#7dcfff"

    text: str = "#7982a9"
    subtext1: str = "#a9b1d6"
    subtext0: str = "#9aa5ce"
    overlay2: str = "#565f89"
    overlay1: str = "#414868"
    overlay0: str = "#3b4261"
    surface2: str = "#1d202f"
    surface1: str = "#1f2335"
    surface0: str = "#3b4261"
    base: str = "#1f2335"
    mantle: str = "#1d202f"
    crust: str = "#1a1b26"