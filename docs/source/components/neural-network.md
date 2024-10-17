# Neural Networks


```{eval-rst}
.. manim:: MySimpleNeuralNetworkScene
    :save_last_frame:
    
    import manim as m

    from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
    from manta.components.neural_networks_utils import NeuralNetworkUtils
    from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


    class MySimpleNeuralNetworkScene(NeuralNetworkUtils, MinimalSlideTemplate):
        subtitle_color = CatppuccinMochaTheme.yellow
        title_seperator_color = CatppuccinMochaTheme.magenta

        def construct(self):
            nn = self.simple_neural_network()
            nn.scale(2.0) # make the network a bit bigger

            self.play(
                self.set_title_row(
                    title="NeuralNetworkUtils",
                    seperator=": ",
                    subtitle="Simple Neural Network"
                ),
                m.FadeIn(nn),
            )


    if __name__ == '__main__':
        MySimpleNeuralNetworkScene.render_video_medium()

```

```{eval-rst}
.. manim:: MyTwoHeadedNeuralNetworkScene
    :save_last_frame:
    
    import manim as m

    from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
    from manta.components.neural_networks_utils import NeuralNetworkUtils
    from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


    class MyTwoHeadedNeuralNetworkScene(NeuralNetworkUtils, MinimalSlideTemplate):
        subtitle_color = CatppuccinMochaTheme.yellow
        title_seperator_color = CatppuccinMochaTheme.magenta

        def construct(self):
            nn = self.two_headed_network()
            nn.scale(1.5) # make the network a bit bigger

            self.play(
                self.set_title_row(
                    title="NeuralNetworkUtils",
                    seperator=": ",
                    subtitle="Two Headed Neural Network",
                ),
                m.FadeIn(nn),
            )


    if __name__ == '__main__':
        MyTwoHeadedNeuralNetworkScene.render_video_medium()

```


```{eval-rst}
.. manim:: MyNetworkAnimationScene

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

```

```{eval-rst}
.. manim:: MyTwoHeadedNeuralNetworkAnimationScene
    
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

```

```{eval-rst}
.. manim:: MyNeuralNetworkExample

    import manim as m

    from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
    from manta.components.neural_networks_utils import NeuralNetworkUtils
    from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


    class MyNeuralNetworkExample(NeuralNetworkUtils, MinimalSlideTemplate):
        subtitle_color = CatppuccinMochaTheme.yellow
        title_seperator_color = CatppuccinMochaTheme.magenta

        def construct(self):
            self.play(
                self.set_title_row(
                    title="Neural Networks",
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
                    self.change_subtitle("Two Headed Neural Network"),
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
        MyNeuralNetworkExample.render_video_medium()

```
