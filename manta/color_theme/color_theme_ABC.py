from abc import ABC, abstractmethod


class ColorThemeABC(ABC):
    f"""
    
    Abstract Base Class for Color Themes
    
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
