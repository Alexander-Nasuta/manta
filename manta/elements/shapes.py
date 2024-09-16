import manim as m

from manta.color_theme.color_theme_ABC import ColorThemeABC
from manta.elements.text import TextUtils
from manta.font_style.fontABC import FontABC

import math
import numpy as np


class ShapeUtils(TextUtils, ColorThemeABC, FontABC):
    rectangle_default_fill_color = None
    rectangle_default_stroke_color = None

    def rounded_rectangle(self, width, height, corner_radius=0.1, **kwargs):
        return m.RoundedRectangle(
            corner_radius=0.125,
            height=height,
            width=width,

            fill_color=self.background_color_bright if self.rectangle_default_fill_color is None
            else self.rectangle_default_fill_color,

            fill_opacity=1.0,

            stroke_color=self.outline_color if self.rectangle_default_stroke_color is None
            else self.rectangle_default_stroke_color,

            stroke_width=1.0
        )

    def rectangle(self, width, height, **kwargs):
        default_params = {
            "height": height,
            "width": width,

            "fill_color": self.background_color_bright if self.rectangle_default_fill_color is None
            else self.rectangle_default_fill_color,

            "fill_opacity": 1.0,

            "stroke_color": self.outline_color if self.rectangle_default_stroke_color is None
            else self.rectangle_default_stroke_color,

            "stroke_width": 1.0,
            "corner_radius": 0.0,
        }
        merged_params = {**default_params, **kwargs}
        return m.RoundedRectangle(**merged_params)

    def circle(self, radius: float, **kwargs):
        default_params = {
            "radius": radius,

            "fill_color": self.background_color_bright if self.rectangle_default_fill_color is None
            else self.rectangle_default_fill_color,

            "fill_opacity": 1.0,

            "stroke_color": self.outline_color if self.rectangle_default_stroke_color is None
            else self.rectangle_default_stroke_color,

            "stroke_width": 1.0
        }
        merged_params = {**default_params, **kwargs}
        return m.Circle(**merged_params)

    def math_circle(self, math_text: str, radius=0.25, font_color=None, text_kwargs=None, **kwargs) \
            -> m.VGroup | m.Circle:
        if text_kwargs is None:
            text_kwargs = {}
        default_text_kwargs = {
            "font_size": self.font_size_large,
            "font_color": self.font_color if font_color is None else font_color,
        }
        text_params = {**default_text_kwargs, **text_kwargs}

        default_params = {
            "radius": radius,
            "stroke_width": 6,
            "stroke_color": self.yellow,
            "fill_color": self.background_color_bright,
            "fill_opacity": 1.0
        }
        params = {**default_params, **kwargs}
        circle = m.Circle(**params)

        text_none_values = [None, "", " "]
        if math_text in text_none_values:
            return circle

        circle_text = self.term_math_text(math_text, **text_params)
        return m.VGroup(circle, circle_text)

    def math_arrow(self, *args, color: str = None, **kwargs) -> m.Arrow:

        if color is None:
            color = self.outline_color

        class EngineerArrowTip(m.ArrowTip, m.Polygon):
            def __init__(self, length=0.35, **kwargs):
                # Define the vertices for a 30-degree arrow tip
                arrow_tip_angle = math.radians(15)
                vertices = [
                    m.ORIGIN - m.RIGHT * length / 2,
                    length * np.array([math.cos(arrow_tip_angle), math.sin(arrow_tip_angle), 0]) - m.RIGHT * length / 2,
                    length * np.array(
                        [math.cos(arrow_tip_angle), -math.sin(arrow_tip_angle), 0]) - m.RIGHT * length / 2,
                ]
                m.Polygon.__init__(self, *vertices, **kwargs)
                m.Polygon.set_fill(self, color=color, opacity=1.0)

        arrow_default_kwargs = {
            "tip_shape": EngineerArrowTip,
            "tip_length": 0.1,
            "stroke_width": 3,
            "buff": 0,
            "fill_color": color,
            "color": color
        }
        arrow_kwargs = {**arrow_default_kwargs, **kwargs}
        return m.Arrow(*args, **arrow_kwargs)
