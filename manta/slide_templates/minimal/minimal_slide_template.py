from manta.slide_templates.indexed_slide import IndexedSlide
from manta.slide_templates.logo_slide import LogoSlide
from manta.slide_templates.title_slide import TitleSlide


class MinimalSlideTemplate(TitleSlide, LogoSlide, IndexedSlide):
    def construct(self):
        pass


class TestMinimalSlideTemplate(MinimalSlideTemplate):
    def construct(self):
        self.play(
            self.set_title_row(
                title="Hallo Welt",
                seperator=":",
                subtitle="Subtitle"
            )
        )


class TestMinimalSlideTemplateWithLogos(MinimalSlideTemplate):
    logo_paths = ["../../resources/logos/Manim_icon.svg", "../../resources/logos/logo.png"]

    def construct(self):
        self.play(
            self.set_title_row(
                title="Hallo Welt",
                seperator=":",
                subtitle="Subtitle"
            ),
            self.add_logos()
        )


if __name__ == '__main__':
    TestMinimalSlideTemplate.render_video_medium()
