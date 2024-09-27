from abc import ABC, abstractmethod


class ColorThemeABC(ABC):
    f"""
    
    ColorThemeABC is an abstract base class for configuring default colors for the presentation.
    
    The configuration is inspired by the configuring colors for terminal applications like Alacritty or 
    Wezterm. 
    Terminal applications are often configured with a color scheme that defines 16 ANSI colors.
    
    Color themes for manta have to at least define the following colors:
    
    - background_color
    - background_color_bright
    - surface_color
    - outline_color
    - font_color
    - font_color_secondary
    - black
    - black_bright
    - red
    - red_bright
    - green
    - green_bright
    - yellow
    - yellow_bright
    - blue
    - blue_bright
    - magenta
    - magenta_bright
    - cyan
    - cyan_bright
    - white
    - white_bright
    
    The colors are defined as hex strings.
    
    Manta defines a default color theme in the color_theme module.
    These color theme might define additional colors. For example catpuccin theme defines colors
    like 'rosewater' or 'flamingo' among other. 
    
    """
    background_color: str
    background_color_bright: str

    surface_color: str
    outline_color: str

    font_color: str
    font_color_secondary: str

    black: str
    black_bright: str

    red: str
    red_bright: str

    green: str
    green_bright: str

    yellow: str
    yellow_bright: str

    blue: str
    blue_bright: str

    magenta: str
    magenta_bright: str

    cyan: str
    cyan_bright: str

    white: str
    white_bright: str
