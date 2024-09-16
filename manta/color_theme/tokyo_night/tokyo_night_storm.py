from manta.color_theme.tokyo_night.tokyo_night_ABC import TokyoNightABC


class TokyoNightStorm(TokyoNightABC):
    # ColorThemeABC
    background_color: str = "#1f2335"
    background_color_bright: str = "#24283b"

    font_color: str = "#c0caf5"
    font_color_secondary: str = "#a9b1d6"

    surface_color: str = "#24283b"
    outline_color: str = "#565f89"

    black: str = "#1d202f"
    black_bright: str = "#2e3440"

    red: str = "#f7768e"
    red_bright: str = "#ff7a93"

    green: str = "#9ece6a"
    green_bright: str = "#b9f27c"

    yellow: str = "#e0af68"
    yellow_bright: str = "#ff9e64"

    blue: str = "#7aa2f7"
    blue_bright: str = "#7dcfff"

    magenta: str = "#bb9af7"
    magenta_bright: str = "#c0caf5"

    cyan: str = "#7dcfff"
    cyan_bright: str = "#a9b1d6"

    white: str = "#a9b1d6"
    white_bright: str = "#c0caf5"

    # TokyoNightABC
    night: str = "#1f2335"
    storm: str = "#24283b"
    moon: str = "#c0caf5"
    dragon: str = "#f7768e"
    spring: str = "#9ece6a"
    wave: str = "#7aa2f7"
    sakura: str = "#bb9af7"
    autumn: str = "#ff9e64"
    winter: str = "#e0af68"
    summer: str = "#7dcfff"

    text: str = "#c0caf5"
    subtext1: str = "#a9b1d6"
    subtext0: str = "#9aa5ce"
    overlay2: str = "#565f89"
    overlay1: str = "#414868"
    overlay0: str = "#24283b"
    surface2: str = "#1d202f"
    surface1: str = "#1f2335"
    surface0: str = "#24283b"
    base: str = "#1f2335"
    mantle: str = "#1d202f"
    crust: str = "#1a1b26"