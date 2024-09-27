from manta.slide_templates.classic.classic_slide_template import ClassicSlideTemplate


class ExampleClassicSlide(ClassicSlideTemplate):
    def construct(self):
        self.play(
            self.set_title_row(
                title="Hallo Welt",
                seperator=":",
                subtitle="Subtitle"
            ),
            # self.add_logos(), # commented out because the logo paths are not set
            self.add_seperator_line_top(),
            self.add_seperator_line_bottom()
        )

        self.wait(1)


def test_classic_slide():
    ExampleClassicSlide.render_video_medium()