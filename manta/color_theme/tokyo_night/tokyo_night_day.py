from manta.color_theme.tokyo_night.tokyo_night_ABC import TokyoNightABC


class TokyoNightDay(TokyoNightABC):
    # ColorThemeABC
    background_color: str = "#d5d6db"
    background_color_bright: str = "#e1e2e7"

    surface_color: str = "#a6adc8"
    outline_color: str = "#7f849c"

    font_color: str = "#4c505e"
    font_color_secondary: str = "#5c6370"

    black: str = "#4c505e"
    black_bright: str = "#5c6370"

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
    night: str = "#d5d6db"
    storm: str = "#e1e2e7"
    moon: str = "#4c505e"
    dragon: str = "#f7768e"
    spring: str = "#9ece6a"
    wave: str = "#7aa2f7"
    sakura: str = "#bb9af7"
    autumn: str = "#ff9e64"
    winter: str = "#e0af68"
    summer: str = "#7dcfff"

    text: str = "#4c505e"
    subtext1: str = "#5c6370"
    subtext0: str = "#6c7086"
    overlay2: str = "#7f849c"
    overlay1: str = "#9399b2"
    overlay0: str = "#a6adc8"
    surface2: str = "#bcc0cc"
    surface1: str = "#d5d6db"
    surface0: str = "#e1e2e7"
    base: str = "#f2f3f5"
    mantle: str = "#f7f8fa"
    crust: str = "#ffffff"