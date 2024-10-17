import manim as m

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

class MyWrapWithRectanlgeExampleScene(UmlUtils, NeuralNetworkUtils, MinimalSlideTemplate):
    subtitle_color = CatppuccinMochaTheme.yellow
    title_seperator_color = CatppuccinMochaTheme.magenta

    def construct(self):

        text = self.term_text("This is a "
                              "multiline text")

        wrapped_text = self.wrap_with_rectangle(text)

        text_circuit = self.term_paragraph(ascii_art)

        wrapped_ascii_art = self.wrap_with_rectangle(text_circuit)


        wrapper_group = m.VGroup(wrapped_text, wrapped_ascii_art).arrange(direction=m.RIGHT)
        wrapper_group.move_to(m.ORIGIN)

        self.play(
            self.set_title_row(
                title="RectangleUtils",
                seperator=": ",
                subtitle="wrap_with_rectangle",
            ),
            m.FadeIn(
                wrapper_group
            )
        )



if __name__ == '__main__':
    MyWrapWithRectanlgeExampleScene.render_video_medium()
