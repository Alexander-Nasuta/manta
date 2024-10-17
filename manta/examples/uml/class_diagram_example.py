import manim as m

from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from manta.components.neural_networks_utils import NeuralNetworkUtils
from manta.components.uml_utils import UmlUtils
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


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
        self.wait(2.0)


        self.fade_out_scene()


if __name__ == '__main__':
    MyUmlClassDiagramScene.render_video_medium()
