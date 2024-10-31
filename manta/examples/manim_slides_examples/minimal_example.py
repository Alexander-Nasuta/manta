import manim as m

from manta.components.qr_code_utils import QrCodeUtils
from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyQrCodeScene(QrCodeUtils, MinimalSlideTemplate):
    subtitle_color = CatppuccinMochaTheme.yellow
    title_seperator_color = CatppuccinMochaTheme.magenta

    def construct(self):


        self.play(
            self.set_title_row(
                title="Manim Slides",
            ),

        )

        self.play(
            self.set_title_row(
                title="Manim Slides 2",
            ),

        )





if __name__ == '__main__':
    MyQrCodeScene.manim_slides_html_medium()
