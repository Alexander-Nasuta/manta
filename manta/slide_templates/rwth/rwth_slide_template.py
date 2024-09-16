from color_theme.rwth.rwth_theme import RwthTheme
from slide_templates.classic.classic_slide_template import ClassicSlideTemplate


class RwthSlideTemplate(RwthTheme, ClassicSlideTemplate):
    logo_paths = ["RWTH_Logo.svg"]

    default_icon_color = RwthTheme.blue

    title_color = RwthTheme.blue
    subtitle_color = RwthTheme.blue
    title_seperator_color = RwthTheme.blue

    index_color = RwthTheme.blue


class TestRwthSlideTemplate(RwthSlideTemplate):
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
