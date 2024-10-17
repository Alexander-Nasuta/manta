import manim as m

from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from manta.components.neural_networks_utils import NeuralNetworkUtils
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MySimpleNeuralNetworkScene(NeuralNetworkUtils, MinimalSlideTemplate):
    subtitle_color = CatppuccinMochaTheme.yellow
    title_seperator_color = CatppuccinMochaTheme.magenta

    def construct(self):
        nn = self.simple_neural_network()

        self.play(
            self.set_title_row(
                title="Neural Network Animation",
            ),
            m.FadeIn(nn),
        )


if __name__ == '__main__':
    MySimpleNeuralNetworkScene.render_video_medium()
