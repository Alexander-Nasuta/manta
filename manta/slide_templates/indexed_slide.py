import manim as m

from manta.elements.rectangle_utils import RectangleUtils
from manta.font_style.IosevkaTerm_base_24 import LatexFontSizing24
from manta.slide_templates.base.base_colored_slide import BaseColorSlide


class IndexedSlide(LatexFontSizing24, RectangleUtils, BaseColorSlide):
    _index_mobject: m.Mobject | None = None
    index_prefix: str = ""
    index_position: str = "left"  # 'left' , 'right' are the only valid values for TermSlide
    index_counter: int = 1  # start from 1
    index_color: str = None
    index_font_size: float = None
    index_vertical_buff: float = None
    index_horizontal_buff: float = None

    def slide_index_transform(self):
        font_color = self.font_color if self.index_color is None else self.index_color
        font_size = self.font_size_normal if self.index_font_size is None else self.index_font_size

        index_vertical_buff = self.med_small_buff if self.index_vertical_buff is None else self.index_vertical_buff
        index_horizontal_buff = self.med_large_buff if self.index_horizontal_buff is None else self.index_horizontal_buff
        index_position = 'left' if self.index_position is None else self.index_position

        def position_slide_index(temp: m.Mobject) -> None:
            temp.to_edge(m.DOWN, buff=index_vertical_buff)
            temp.to_edge(
                m.LEFT if index_position == 'left' else m.RIGHT,
                buff=index_horizontal_buff
            )

        # case: slide index is not set yet
        if self._index_mobject is None:
            slide_index_text = self.get_slide_index_indication()
            self._index_mobject = self.term_text(slide_index_text, font_color=font_color, font_size=font_size)

            position_slide_index(temp=self._index_mobject)

            return m.FadeIn(self._index_mobject)

        # case: slide index is already set
        self.index_counter += 1
        slide_index_text = self.get_slide_index_indication()

        # target is the new slide index after the transformation
        target = self.term_text(slide_index_text, font_color=font_color, font_size=font_size)
        position_slide_index(temp=target)

        transform = m.Transform(self._index_mobject, target)
        return transform

    def get_slide_index_indication(self) -> str:
        return f"{self.index_prefix}{self.index_counter:02}"

    def play(
            self,
            *args,
            subcaption=None,
            subcaption_duration=None,
            subcaption_offset=0,
            **kwargs,
    ):
        super().play(*args, self.slide_index_transform(), **kwargs)


class TestIndexedSlide(IndexedSlide):

    def construct(self):
        text_mobj = self.term_text("Hello, World!")
        self.play(
            m.FadeIn(text_mobj),
        )

        self.play_without_section(
            m.Transform(text_mobj, self.term_text("Hello, Manim! No Section Increment")),
        )

        self.play(
            m.Transform(text_mobj, self.term_text("Hello, Manim!")),
        )

        self.wait(0.1)


if __name__ == '__main__':
    TestIndexedSlide.render_video_medium()
