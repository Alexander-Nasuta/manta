import manim as m
from pyrr.rectangle import width

from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from manta.components.neural_networks_utils import NeuralNetworkUtils
from manta.components.uml_utils import UmlUtils
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


# https://www.asciiart.eu/video-games/pacman
ascii_art = r"""
================================================.
     .-.   .-.     .--.                         |
    | OO| | OO|   / _.-' .-.   .-.  .-.   .''.  |
    |   | |   |   \  '-. '-'   '-'  '-'   '..'  |
    '^^^' '^^^'    '--'                         |
===============.  .-.  .================.  .-.  |
               | |   | |                |  '-'  |
               | |   | |                |       |
               | ':-:' |                |  .-.  |
               |  '-'  |                |  '-'  |
==============='       '================'       |
"""

class MyWrapWithRectanlgeAndIconExampleScene(UmlUtils, NeuralNetworkUtils, MinimalSlideTemplate):
    subtitle_color = CatppuccinMochaTheme.yellow
    title_seperator_color = CatppuccinMochaTheme.magenta

    def construct(self):
        text = self.term_text("This is a \n multiline text")

        wrapped_text = self.wrap_with_icon_and_rectangle(
            text,
            icon='users',
            # if with is not set, the width will be calculated automatically
            # same for height
            width=6,
            height=2
        )

        text_ascii_art = self.term_paragraph(ascii_art).scale_to_fit_width(3)

        wrapped_ascii_art = self.wrap_with_icon_and_rectangle(text_ascii_art, direction='up', icon='ghost')


        wrapper_group = m.VGroup(wrapped_text, wrapped_ascii_art).arrange(direction=m.RIGHT)


        self.play(
            self.set_title_row(
                title="RectangleUtils",
                seperator=": ",
                subtitle="wrap_with_icon_and_rectangle",
            ),
            m.FadeIn(
                wrapper_group
            )
        )



if __name__ == '__main__':
    MyWrapWithRectanlgeAndIconExampleScene.render_video_medium()
