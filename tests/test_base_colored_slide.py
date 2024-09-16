import manim as m

from manta.color_theme.catppucin.catppuccin_latte import CatppuccinLatteTheme
from manta.color_theme.tokyo_night.tokyo_night import TokyoNight
from manta.slide_templates.base.base_colored_slide import BaseColorSlide


class ExampleColorSlide(BaseColorSlide):

    def construct(self):
        text_mobj = m.Text("Hello, World!")
        self.play(
            m.FadeIn(text_mobj),
        )

        self.play(
            m.Transform(text_mobj, m.Text("Hello, Manim!")),
        )


class ExampleColorSlideTokyoNight(TokyoNight, BaseColorSlide):

    def construct(self):
        text_mobj = m.Text("Hello, World!")
        self.play(
            m.FadeIn(text_mobj),
        )

        self.play(
            m.Transform(text_mobj, m.Text("Hello, Manim!")),
        )


class ExampleColorSlideCatppucinLatte(CatppuccinLatteTheme, BaseColorSlide):

    def construct(self):
        text_mobj = m.Text("Hello, World!")
        self.play(
            m.FadeIn(text_mobj),
        )

        self.play(
            # NOTE: this text is white on a light background
            m.Transform(text_mobj, m.Text("Hello, Manim!")),
        )


def test_color_slide():
    ExampleColorSlide.rendering_test()


def test_color_slide_tokyo_night():
    ExampleColorSlideTokyoNight.rendering_test()


def test_color_slide_catppucin():
    ExampleColorSlideCatppucinLatte.rendering_test()
