from manta.color_theme.tokyo_night.tokyo_night_ABC import TokyoNightABC


class TokyoNight(TokyoNightABC):
    # ColorThemeABC
    background_color: str = "#1a1b26"
    background_color_bright: str = "#414868"

    font_color: str = "#c0caf5"
    font_color_secondary: str = "#a9b1d6"

    black: str = "#15161e"
    black_bright: str = "#414868"

    red: str = "#f7768e"
    red_bright: str = "#f7768e"

    green: str = "#9ece6a"
    green_bright: str = "#9ece6a"

    yellow: str = "#e0af68"
    yellow_bright: str = "#e0af68"

    blue: str = "#7aa2f7"
    blue_bright: str = "#7aa2f7"

    magenta: str = "#bb9af7"
    magenta_bright: str = "#bb9af7"

    cyan: str = "#7dcfff"
    cyan_bright: str = "#7dcfff"

    white: str = "#a9b1d6"
    white_bright: str = "#c0caf5"

    # TokyoNightABC
    night: str = "#1a1b26"
    storm: str = "#414868"
    moon: str = "#c0caf5"
    dragon: str = "#f7768e"
    spring: str = "#9ece6a"
    wave: str = "#7aa2f7"
    sakura: str = "#bb9af7"
    autumn: str = "#ff9e64"
    winter: str = "#e0af68"
    summer: str = "#7dcfff"

    text: str = "#a9b1d6"
    subtext1: str = "#b4f9f8"
    subtext0: str = "#c0caf5"
    overlay2: str = "#565f89"
    overlay1: str = "#414868"
    overlay0: str = "#24283b"
    surface2: str = "#1a1b26"
    surface1: str = "#1a1b26"
    surface0: str = "#1a1b26"
    base: str = "#1a1b26"
    mantle: str = "#1a1b26"
    crust: str = "#1a1b26"