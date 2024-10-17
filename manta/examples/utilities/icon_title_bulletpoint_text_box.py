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
