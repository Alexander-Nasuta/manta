import manim as m

from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from manta.components.neural_networks_utils import NeuralNetworkUtils
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyNetworkAnimationScene(NeuralNetworkUtils, MinimalSlideTemplate):
    subtitle_color = CatppuccinMochaTheme.yellow
    title_seperator_color = CatppuccinMochaTheme.magenta

    def construct(self):
        nn = self.simple_neural_network(
            # make the blue for more contrast
            arrow_kwargs={"color": self.blue,},
            neuron_circle_kwargs={"stroke_color": self.blue, "fill_color": self.green, "fill_opacity": 0.2},
        )
        nn.scale(2.0) # scale the neural network

        self.play(
            self.set_title_row(
                title="NeuralNetworkUtils",
                seperator=": ",
                subtitle="simple_neural_network_forward_animation",
            ),
            m.FadeIn(nn),
        )

        self.play(
            self.simple_neural_network_forward_animation(nn),
        )

        self.play(
            self.simple_neural_network_forward_animation(
                nn,
                color=self.red,
                run_time=2.5
            ),
        )

        self.play(
            self.simple_neural_network_forward_animation(
                nn,
                color=self.yellow,
                run_time=2.5
            ),
        )
        self.wait(0.25)


        self.fade_out_scene()


if __name__ == '__main__':
    MyNetworkAnimationScene.render_video_medium()
