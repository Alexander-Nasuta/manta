import manim as m

from color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from elements.neural_networks_utils import NeuralNetworkUtils
from slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyNetworkAnimationScene(NeuralNetworkUtils, MinimalSlideTemplate):
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

        self.play(
            self.simple_neural_network_forward_animation(nn),
        )

        self.play(
            self.simple_neural_network_forward_animation(
                nn,
                color=self.cyan,
                run_time=2.5
            ),
        )


if __name__ == '__main__':
    MyNetworkAnimationScene.render_video_medium()
