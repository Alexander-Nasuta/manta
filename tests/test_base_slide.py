import manim as m

from manta.padding_style.manta_padding import MantaPadding
from manta.slide_templates.base.base_slide import BaseSlide


class ExampleMantaBaseSlide(MantaPadding, BaseSlide):
    def construct(self):
        text_mobj = m.Text("Hello, World!")
        self.play(
            m.FadeIn(text_mobj),
        )

        self.wait(0.1)


def test_base_slide():
    ExampleMantaBaseSlide.rendering_test()
