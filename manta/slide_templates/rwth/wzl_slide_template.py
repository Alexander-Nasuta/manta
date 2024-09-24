from color_theme.tokyo_night.tokyo_night import TokyoNight
from slide_templates.rwth.rwth_slide_template import RwthSlideTemplate

import manta.docbuild.image_path_utils as path_utils


class RwthWZLSlideTemplate(RwthSlideTemplate):
    logo_paths = [path_utils.get_wzl_logo_abs_path()]


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
