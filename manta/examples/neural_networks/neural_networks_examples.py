import manim as m

from color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from elements.neural_networks_utils import NeuralNetworkUtils
from slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyNeuralNetwork_example(NeuralNetworkUtils, MinimalSlideTemplate):
    subtitle_color = CatppuccinMochaTheme.yellow
    title_seperator_color = CatppuccinMochaTheme.magenta

    def construct(self):
        self.play(
            self.set_title_row(
                title="Nerual Networks",
            )
        )

        example_nn = self.simple_neural_network()

        self.play(
            m.AnimationGroup(
                self.change_subtitle("Simple Neural Network"),
                m.FadeIn(example_nn),
                lag_ratio=0.85
            )
        )

        self.play(
            m.AnimationGroup(
                self.change_subtitle("Simple Neural Network Forward Pass Animation"),
                self.simple_neural_network_forward_animation(example_nn, color=self.yellow_bright),
                lag_ratio=0.85
            )
        )

        self.play(
            m.AnimationGroup(
                self.change_subtitle("Simple Neural Network with different architecture"),
                m.Transform(
                    example_nn,
                    self.simple_neural_network(
                        input_layer_dim=7,
                        hidden_layer_dim=5,
                        hidden_layer_n=3,
                        output_layer_dim=3,
                    )
                ),
                lag_ratio=0.85
            )
        )

        self.play(
            m.AnimationGroup(
                self.change_subtitle("Two Headed Neural Network"),
                m.Transform(
                    example_nn,
                    self.two_headed_network()
                ),
                lag_ratio=0.85
            )
        )

        self.play(
            m.AnimationGroup(
                self.change_subtitle("Two Headed Neural Network with different architecture"),
                m.Transform(
                    example_nn,
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
                ),
                lag_ratio=0.85
            )
        )

        self.fade_out_scene()


if __name__ == '__main__':
    MyNeuralNetwork_example.render_video_medium()
