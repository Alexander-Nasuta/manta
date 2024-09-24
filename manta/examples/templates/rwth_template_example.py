from slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate
from slide_templates.rwth.rwth_slide_template import RwthSlideTemplate


class MyMinimalSlideTemplateExample(RwthSlideTemplate):
    def construct(self):
        self.play(
            self.set_title_row(
                title="RWTH Aachen",
                seperator=":",
                subtitle="Rheinisch-Westfälische Technische Hochschule Aachen"
            ),
            self.add_logos(),
            self.add_seperator_lines(),
        )

        self.play(
            self.change_subtitle("Die Universität, die sich Hochschule nennt!"),
        )

        self.wait(2)  # wait increases the index of the slide

        self.fade_out_scene()


if __name__ == '__main__':
    MyMinimalSlideTemplateExample.render_video_medium()
