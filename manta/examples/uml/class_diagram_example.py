import manim as m

from color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from elements.neural_networks_utils import NeuralNetworkUtils
from elements.uml_utils import UmlUtils
from slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyUmlClassDiagramScene(UmlUtils, NeuralNetworkUtils, MinimalSlideTemplate):
    subtitle_color = CatppuccinMochaTheme.yellow
    title_seperator_color = CatppuccinMochaTheme.magenta

    def construct(self):
        self.play(
            self.set_title_row(
                title="UML Utils",
                seperator=": ",
                subtitle="Class Diagram",
            ),
        )

        class Person:
            name: str
            _age: int | float | None

            def say_hello(self) -> str:
                return f"Hello, my name is {self.name}."

        person_uml_class_diagram = self.uml_class_diagram(Person).scale(0.5)

        self.play(
            m.FadeIn(
                person_uml_class_diagram
            )
        )
        self.wait(1.5)

        self.play(
            m.Transform(
                person_uml_class_diagram,
                self.uml_class_diagram(Person,
                                       visibility_color=self.red,
                                        fields_color=self.blue,
                                       type_color=self.yellow,
                                       parameters_color=self.green,
                                       color_python_keyword=False,
                                       type_t2c={"float": self.blue, "None": self.red}
                                       ).scale(0.5)
            )
        )
        self.wait(1.5)

        # make sure to install gymnasium with `pip install gymnasium` before running this example
        import gymnasium as gym

        gym_class_uml_diagram = self.uml_class_diagram(gym.Env, class_name="gymnasium.Env").scale(0.5)

        self.play(
            m.ReplacementTransform(person_uml_class_diagram, gym_class_uml_diagram),
        )
        self.wait(1.5)

        self.fade_out_scene()


if __name__ == '__main__':
    MyUmlClassDiagramScene.render_video_medium()
