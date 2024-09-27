import pytest

from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class ExampleMinimalSlideTemplate(MinimalSlideTemplate):
    def construct(self):
        self.play(
            self.set_title_row(
                title="Hallo Welt",
                seperator=":",
                subtitle="Subtitle"
            )
        )


class ExampleMinimalSlideTemplateWithLogos(MinimalSlideTemplate):
    logo_paths = ["../resources/logos/Manim_icon.svg", "../resources/logos/logo.png"]

    def construct(self):
        self.play(
            self.set_title_row(
                title="Hallo Welt",
                seperator=":",
                subtitle="Subtitle"
            ),
            self.add_logos()
        )


def test_minimal_slide_template():
    ExampleMinimalSlideTemplate.rendering_test()


@pytest.mark.skip(
    reason="Don‘t know how to specify the path to the logo properly, when it's in the resources folder of the "
           "project. Somehow running the test on its own works, but not when running all tests."
           "I guess its becouse of some shenanigans with the current working directory what is used when "
           "calling 'poetry run pytest'.")
def test_minimal_slide_template_with_logos():
    ExampleMinimalSlideTemplateWithLogos.rendering_test()
