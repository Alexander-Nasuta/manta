from color_theme.tokyo_night.tokyo_night import TokyoNight
from slide_templates.rwth.rwth_slide_template import RwthSlideTemplate


class RwthWZLSlideTemplate(RwthSlideTemplate):
    logo_paths = ["wzl.svg"]


class TestRwthSlideTemplate(RwthWZLSlideTemplate):
    def construct(self):
        self.play(
            self.set_title_row(
                title="Title",
                seperator=":",
                subtitle="Subtitle"
            ),
            self.add_logos(),
            self.add_seperator_line_top(),
            self.add_seperator_line_bottom()
        )

        self.wait(1)


if __name__ == '__main__':
    TestRwthSlideTemplate.render_video_medium()
