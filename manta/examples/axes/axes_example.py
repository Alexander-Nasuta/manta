import manim as m
import numpy as np

from color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from elements.axes_utils import AxesUtils
from slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyAxesExampleScene(AxesUtils, MinimalSlideTemplate):
    subtitle_color = CatppuccinMochaTheme.yellow
    title_seperator_color = CatppuccinMochaTheme.magenta

    def construct(self):
        self.play(
            self.set_title_row(
                title="Manta Axes",
                seperator=": ",
                subtitle="term_axes",
            ),
        )

        axes = self.term_axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )

        sin_graph = axes.plot(lambda x: np.sin(x), color=self.blue)
        cos_graph = axes.plot(lambda x: np.cos(x), color=self.red)

        self.play(
            m.AnimationGroup(
                m.FadeIn(axes),
                m.AnimationGroup(
                    m.Create(sin_graph),
                    m.Create(cos_graph),
                    lag_ratio=0.15,
                    run_time=1.25,
                ),
                lag_ratio=0.5,
            )
        )
        self.wait(1.5)

        axes_minimal = self.term_axes_minimal(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
        )

        self.play(
            self.change_subtitle("term_axes_minimal"),
            m.Transform(axes, axes_minimal),
        )

        self.fade_out_scene()


if __name__ == '__main__':
    MyAxesExampleScene.render_video_medium()
