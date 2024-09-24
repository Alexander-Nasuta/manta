import itertools
from typing import Sequence

import manim as m
from manim import config

from manta.logger import log

from manta.elements.shapes import ShapeUtils


class AxesUtils(ShapeUtils):

    @staticmethod
    def term_axes_minimal(x_range: Sequence[float] | None = None,
                          y_range: Sequence[float] | None = None,
                          x_length: float | None = round(config.frame_width) - 2,
                          y_length: float | None = round(config.frame_height) - 2,
                          **kwargs
                          ) -> m.Axes:
        default_kwargs = {
            "x_range": x_range,
            "y_range": y_range,
            "x_length": x_length,
            "y_length": y_length,
            "y_axis_config": {"tick_size": 0},
            "x_axis_config": {"tick_size": 0},
            "axis_config": {"include_numbers": False, "tip_width": 0.125, "tip_height": 0.25},
        }
        merged_kwargs = {**default_kwargs, **kwargs}

        return m.Axes(**merged_kwargs)

    def term_axes(self, x_range: Sequence[float] | None = None,
                  y_range: Sequence[float] | None = None,
                  x_length: float | None = round(config.frame_width) - 2,
                  y_length: float | None = round(config.frame_height) - 2,
                  y_axis_config=None,
                  x_axis_config=None,
                  axis_config=None,
                  **kwargs) -> m.Axes:
        if axis_config is None:
            axis_config = {}
        if x_axis_config is None:
            x_axis_config = {}
        if y_axis_config is None:
            y_axis_config = {}

        manta_font_name = self.font_name

        class MantaTermText(m.Text):
            def __init__(self, *tex_strings, **kwargs):
                super().__init__(*tex_strings, font=manta_font_name, **kwargs)

        default_kwargs = {
            "x_range": x_range,
            "y_range": y_range,
            "x_length": x_length,
            "y_length": y_length,
            "y_axis_config": {
                "tick_size": 0.0425,
                **y_axis_config,
            },
            "x_axis_config": {
                "tick_size": 0.0425,
                # "numbers_to_include": [0, 5, 10, 15, 20, 25, 30, 35, 40],
                # "numbers_with_elongated_ticks": [0, 5, 10, 15, 20, 25, 30, 35, 40],
                "font_size": 16,
                # "exclude_origin_tick": False,
                # "numbers_to_exclude": [],
                **x_axis_config,
            },
            "axis_config": {
                "include_numbers": False,
                "tip_width": 0.125,
                "tip_height": 0.25,
                "label_constructor": MantaTermText,
                **axis_config,
            },
        }
        merged_kwargs = {**default_kwargs, **kwargs}
        return m.Axes(**merged_kwargs)
