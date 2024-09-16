import manim as m
import numpy as np

from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class ClassicSlideTemplate(MinimalSlideTemplate):
    seperator_line_top_mobject: m.Mobject = None
    seperator_line_top_vertical_buff: float = 0.85

    seperator_line_bottom_mobject: m.Mobject = None
    seperator_line_bottom_vertical_buff: float = None

    seperator_line_kwargs: dict = {}

    def add_seperator_line_top(self, transformation: m.Transform | None = None,
                               **kwargs) -> m.AnimationGroup | m.Transform:
        if transformation is None:
            transformation = m.FadeIn

        if self.seperator_line_top_mobject is None:
            default_params = {
                "start": np.array([-self.content_width * 0.5 - self.small_buff, 0, 0]),
                "end": np.array([self.content_width * 0.5 + self.small_buff, 0, 0]),
                "color": self.font_color,
                "stroke_width": 1
            }
            additional_kwargs = {} if self.seperator_line_kwargs is None else self.seperator_line_kwargs
            merged_kwargs = {**default_params, **additional_kwargs}

            self.seperator_line_top_mobject = m.Line(**merged_kwargs)
            vertical_buff = 0.85 if self.seperator_line_top_vertical_buff is None else self.seperator_line_top_vertical_buff
            self.seperator_line_top_mobject.to_edge(m.UP, buff=vertical_buff)

        return transformation(self.seperator_line_top_mobject, **kwargs)

    def add_seperator_line_bottom(self, transformation: m.Transform | None = None,
                                  **kwargs) -> m.AnimationGroup | m.Transform:
        if transformation is None:
            transformation = m.FadeIn

        if self.seperator_line_bottom_mobject is None:
            default_params = {
                "start": np.array([-self.content_width * 0.5 - self.small_buff, 0, 0]),
                "end": np.array([self.content_width * 0.5 + self.small_buff, 0, 0]),
                "color": self.font_color,
                "stroke_width": 1
            }
            additional_kwargs = {} if self.seperator_line_kwargs is None else self.seperator_line_kwargs
            merged_kwargs = {**default_params, **additional_kwargs}

            self.seperator_line_bottom_mobject = m.Line(**merged_kwargs)
            vertical_buff = 0.85 if self.seperator_line_bottom_vertical_buff is None else self.seperator_line_bottom_vertical_buff
            self.seperator_line_bottom_mobject.to_edge(m.DOWN, buff=vertical_buff)

        return transformation(self.seperator_line_bottom_mobject, **kwargs)

    def remove_seperator_line_top(self, transformation: m.Transform | None = None,
                                  **kwargs) -> m.AnimationGroup | m.Transform:
        if transformation is None:
            transformation = m.FadeOut
        if self.is_in_scene(self.seperator_line_top_mobject):
            return transformation(self.seperator_line_top_mobject, **kwargs)
        else:
            raise ValueError("Seperator line top is not in the scene")

    def remove_seperator_line_bottom(self, transformation: m.Transform | None = None,
                                     **kwargs) -> m.AnimationGroup | m.Transform:
        if transformation is None:
            transformation = m.FadeOut
        if self.is_in_scene(self.seperator_line_bottom_mobject):
            return transformation(self.seperator_line_bottom_mobject, **kwargs)
        else:
            raise ValueError("Seperator line bottom is not in the scene")


class TestClassicSlide(ClassicSlideTemplate):
    logo_paths = [
        "../../../resources/logos/Manim_icon.svg",
        "../../../resources/logos/logo.png"
    ]

    def construct(self):
        self.play(
            self.set_title_row(
                title="Hallo Welt",
                seperator=":",
                subtitle="Subtitle"
            ),
            self.add_logos(),
            self.add_seperator_line_top(),
            self.add_seperator_line_bottom()
        )

        self.wait(1)


if __name__ == '__main__':
    # example for a classic slide
    TestClassicSlide.render_video_medium()
