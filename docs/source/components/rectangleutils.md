# Rectangle Utilities


```{eval-rst}
.. manim:: MyWrapWithRectanlgeExampleScene
    :save_last_frame:
   
   
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

```

```{eval-rst}
.. manim:: MyWrapWithRectanlgeAndIconExampleScene
    :save_last_frame:
 
 
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

```


```{eval-rst}
.. manim:: MyIconTextBoxExampleScene
    :save_last_frame:
   
    import manim as m
    from pyrr.rectangle import width, height
    
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
    
    class MyIconTextBoxExampleScene(UmlUtils, NeuralNetworkUtils, MinimalSlideTemplate):
        subtitle_color = CatppuccinMochaTheme.yellow
        title_seperator_color = CatppuccinMochaTheme.magenta
    
        def construct(self):
    
            icon_text_box1 = self.icon_textbox("Im an introvert.", icon='user')
            icon_text_box2 = self.icon_textbox(
                "Im an extrovert. \n I love to talk to people.",
                icon='users',
                icon_color=self.magenta,
                # if with is not set, the width will be calculated automatically
                # same for height
                width=5,
                height=2.5,
                t2c={"extrovert": self.blue},
                # this is an alternative to t2c
                # just type the words you want to colorize
                # and specify the color
                t2c_strs=["talk", "people"],
                t2c_color=self.green,
            )
    
            wrapper_group = m.VGroup(icon_text_box1, icon_text_box2).arrange(direction=m.DOWN)
    
            self.play(
                self.set_title_row(
                    title="RectangleUtils",
                    seperator=": ",
                    subtitle="icon_textbox",
                ),
                m.FadeIn(
                    wrapper_group
                )
            )
    
    
    
    if __name__ == '__main__':
        MyIconTextBoxExampleScene.render_video_medium()

```


```{eval-rst}
.. manim:: MyIconBulletpointTextBoxExampleScene
    :save_last_frame:
   

    import manim as m
    from pyrr.rectangle import width, height
    
    from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
    from manta.components.neural_networks_utils import NeuralNetworkUtils
    from manta.components.uml_utils import UmlUtils
    from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate
    
    
    class MyIconBulletpointTextBoxExampleScene(UmlUtils, NeuralNetworkUtils, MinimalSlideTemplate):
        subtitle_color = CatppuccinMochaTheme.yellow
        title_seperator_color = CatppuccinMochaTheme.magenta
    
        def construct(self):
    
            icon_text_box1 = self.icon_bulletpoints_textbox(
                ["Im an introvert.", "It's exhausting for me to talk to people."],
                icon='user'
            )
            icon_text_box2 = self.icon_bulletpoints_textbox(
                ["Im an extrovert.", " I love to talk to people."],
                icon='users',
                bullet_icon='users',
                icon_color=self.magenta,
                # if with is not set, the width will be calculated automatically
                # same for height
                width=10,
                height=2.5,
                t2c={"extrovert": self.blue},
                # this is an alternative to t2c
                # just type the words you want to colorize
                # and specify the color
                t2c_strs=["talk", "people"],
                t2c_color=self.green,
            )
    
            wrapper_group = m.VGroup(icon_text_box1, icon_text_box2).arrange(direction=m.DOWN)
    
            self.play(
                self.set_title_row(
                    title="RectangleUtils",
                    seperator=": ",
                    subtitle="icon_bulletpoints_textbox",
                ),
                m.FadeIn(
                    wrapper_group
                )
            )
    
    
    
    if __name__ == '__main__':
        MyIconBulletpointTextBoxExampleScene.render_video_medium()

```


```{eval-rst}
.. manim:: MyTitledIconBulletpointTextBoxExampleScene
    :save_last_frame:

    import manim as m
    from pyrr.rectangle import width, height
    
    from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
    from manta.components.neural_networks_utils import NeuralNetworkUtils
    from manta.components.uml_utils import UmlUtils
    from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate
    
    
    class MyTitledIconBulletpointTextBoxExampleScene(UmlUtils, NeuralNetworkUtils, MinimalSlideTemplate):
        subtitle_color = CatppuccinMochaTheme.yellow
        title_seperator_color = CatppuccinMochaTheme.magenta
    
        def construct(self):
    
            icon_text_box1 = self.icon_title_bulletpoints_textbox(
                [
                    ("Extrovert", ["Im an extrovert.", "I love to talk to people."]),
                ],
                icon='users',
            )
            icon_text_box2 = self.icon_title_bulletpoints_textbox(
                [
                    ("Introvert", ["Im an introvert.", "It's exhausting for me to talk to people."]),
                    ("Misanthrope", ["I dislike the presence of other people.", "Please leave me alone."]),
                ],
                icon='user',
                bullet_icon='user',
                icon_color=self.magenta,
                # if with is not set, the width will be calculated automatically
                # same for height
                width=10,
                height=4.0,
                t2c={
                    "extrovert": self.blue,
                    "Please leave me alone": self.red,
                },
                # this is an alternative to t2c
                # just type the words you want to colorize
                # and specify the color
                t2c_strs=["talk", "people"],
                t2c_color=self.green,
            )
    
            wrapper_group = m.VGroup(icon_text_box1, icon_text_box2).arrange(direction=m.DOWN)
    
            self.play(
                self.set_title_row(
                    title="RectangleUtils",
                    seperator=": ",
                    subtitle="icon_title_bulletpoints_textbox",
                ),
                m.FadeIn(
                    wrapper_group
                )
            )
    
    
    
    if __name__ == '__main__':
        MyTitledIconBulletpointTextBoxExampleScene.render_video_medium()

```
