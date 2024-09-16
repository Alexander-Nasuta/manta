import manim as m
import pytest

from manta.slide_templates.logo_slide import LogoSlide


class ExampleLogoSlide(LogoSlide):
    logo_paths = ["../resources/logos/Manim_icon.svg", "../resources/logos/logo.png"]

    def construct(self):
        self.play(
            self.add_logos()
        )

        self.wait(2)

        self.play(
            m.FadeOut(self.logos)
        )


@pytest.mark.skip(
    reason="Don‘t know how to specify the path to the logo properly, when it's in the resources folder of the "
           "project. Somehow running the test on its own works, but not when running all tests."
           "I guess its becouse of some shenanigans with the current working directory what is used when "
           "calling 'poetry run pytest'.")
def test_logo_slide():
    ExampleLogoSlide.rendering_test()
