import manim as m

from manta.components.qr_code_utils import QrCodeUtils
from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyQrCodeScene(QrCodeUtils, MinimalSlideTemplate):
    subtitle_color = CatppuccinMochaTheme.yellow
    title_seperator_color = CatppuccinMochaTheme.magenta

    def construct(self):

        qr_code_without_icon = self.qr_code("https://fishshell.com")
        qr_code_with_icon = self.qr_code(
            payload="https://fishshell.com",
            icon='terminal',
            icon_size=6
        )

        qr_code_group = m.VGroup(
            qr_code_without_icon,
            qr_code_with_icon).arrange(m.RIGHT, buff=self.med_large_buff)

        self.play(
            self.set_title_row(
                title="QR Code",
            ),
            m.FadeIn(qr_code_group)
        )


if __name__ == '__main__':
    MyQrCodeScene.render_video_medium()
