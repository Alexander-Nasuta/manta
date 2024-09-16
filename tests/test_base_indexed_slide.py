import manim as m

from manta.padding_style.manta_padding import MantaPadding
from manta.slide_templates.base.base_indexed_slide import BaseIndexedSlide


class ExampleIndexedSlide(MantaPadding, BaseIndexedSlide):

    def construct(self):
        text_mobj = m.Text("Hello, World!")
        self.play(
            m.FadeIn(text_mobj),
        )

        self.play(
            m.Transform(text_mobj, m.Text("Hello, Manim!")),
        )

        self.wait(0.1)


def test_indexed_slide():
    ExampleIndexedSlide.rendering_test()
