
import manim as m

from color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from elements.iqs_utils import IQS_Utils
from slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyIQSExampleScene(IQS_Utils, MinimalSlideTemplate):
    subtitle_color = CatppuccinMochaTheme.yellow
    title_seperator_color = CatppuccinMochaTheme.magenta

    def construct(self):
        self.play(
            self.set_title_row(
                title="IQS_Utils",
                seperator=": ",
                subtitle="igs_hexagon",
            ),
        )

        iqs_logo = self.igs_hexagon()

        self.play(
            m.FadeIn(iqs_logo),
        )

        self.fade_out_scene()


if __name__ == '__main__':
    MyIQSExampleScene.render_video_medium()
