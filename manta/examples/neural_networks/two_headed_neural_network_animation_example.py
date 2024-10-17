import manim as m

from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from manta.components.neural_networks_utils import NeuralNetworkUtils
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyTwoHeadedNeuralNetworkAnimationScene(NeuralNetworkUtils, MinimalSlideTemplate):
    subtitle_color = CatppuccinMochaTheme.yellow
    title_seperator_color = CatppuccinMochaTheme.magenta

    def construct(self):
        two_headed_nn = self.two_headed_network()

        self.play(
            self.set_title_row(
                title="NeuralNetworkUtils",
                seperator=": ",
                subtitle="two_headed_neural_network_forward_animation",
            ),
            m.FadeIn(two_headed_nn),
        )

        self.play(
            self.two_headed_neural_network_forward_animation(
                two_headed_nn,
                color=self.cyan
            ),
        )

        self.play(
            m.Transform(
                two_headed_nn,
                self.two_headed_network(
                    shared_network_kwargs={
                        "input_layer_dim": 12,
                        "hidden_layer_dim": 10,
                        "hidden_layer_n": 3,
                        "output_layer_dim": 9,
                    },
                    shared_network_color=self.green,
                    top_head_network_kwargs={
                        "input_layer_dim": 4,
                        "hidden_layer_dim": 3,
                        "hidden_layer_n": 2,
                        "output_layer_dim": 2,
                    },
                    top_head_network_color=self.cyan,
                    bottom_networks_kwargs={
                        "input_layer_dim": 2,
                        "hidden_layer_dim": 2,
                        "hidden_layer_n": 3,
                        "output_layer_dim": 2,
                    },
                    bottom_networks_color=self.magenta,
                )
            )
        )

        self.play(
            self.two_headed_neural_network_forward_animation(
                two_headed_nn,
                color=self.green,
                run_time=2.0
            ),
        )


if __name__ == '__main__':
    MyTwoHeadedNeuralNetworkAnimationScene.render_video_medium()
