from manta.slide_templates.title_slide import TitleSlide


class ExampleTitleSlide(TitleSlide):
    def construct(self):
        self.play(
            self.set_title_row(
                title="Hallo"
            )
        )

        self.play(
            self.set_title_row(
                title="Hallo Welt",
                seperator=":",
                subtitle="Subtitle"
            )
        )

        self.play(
            self.set_title_row(
                title="Hallo Welt",
                seperator=":",
                subtitle="another subtitle"
            )
        )

        self.play(
            self.set_title_row(),
        )

        self.wait(0.1)


def test_title_slide():
    ExampleTitleSlide.rendering_test()
