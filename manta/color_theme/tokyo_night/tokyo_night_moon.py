from manta.color_theme.tokyo_night.tokyo_night_ABC import TokyoNightABC


class TokyoNightMoon(TokyoNightABC):
    # ColorThemeABC
    background_color: str = "#222436"
    background_color_bright: str = "#2a2b3c"

    font_color: str = "#c8d3f5"
    font_color_secondary: str = "#b4f9f8"

    surface_color: str = "#2a2b3c"
    outline_color: str = "#565f89"

    black: str = "#1e2030"
    black_bright: str = "#2a2b3c"

    red: str = "#ff757f"
    red_bright: str = "#ff7a93"

    green: str = "#c3e88d"
    green_bright: str = "#b9f27c"

    yellow: str = "#ffc777"
    yellow_bright: str = "#ff9e64"

    blue: str = "#82aaff"
    blue_bright: str = "#7dcfff"

    magenta: str = "#c099ff"
    magenta_bright: str = "#c0caf5"

    cyan: str = "#86e1fc"
    cyan_bright: str = "#a9b1d6"

    white: str = "#d9e0ee"
    white_bright: str = "#c0caf5"

    # TokyoNightABC
    night: str = "#222436"
    storm: str = "#2a2b3c"
    moon: str = "#c8d3f5"
    dragon: str = "#ff757f"
    spring: str = "#c3e88d"
    wave: str = "#82aaff"
    sakura: str = "#c099ff"
    autumn: str = "#ffc777"
    winter: str = "#ff9e64"
    summer: str = "#86e1fc"

    text: str = "#c8d3f5"
    subtext1: str = "#b4f9f8"
    subtext0: str = "#a9b1d6"
    overlay2: str = "#565f89"
    overlay1: str = "#414868"
    overlay0: str = "#2a2b3c"
    surface2: str = "#1e2030"
    surface1: str = "#222436"
    surface0: str = "#2a2b3c"
    base: str = "#222436"
    mantle: str = "#1e2030"
    crust: str = "#1a1b26"