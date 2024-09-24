import manim as m

from slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyShapesExamplesScene(MinimalSlideTemplate):

    def construct(self):
        self.play(
            self.set_title_row(
                title="Shapes",
                seperator=": ",
                subtitle="Useful shapes for your slides"
            )
        )

        self.wait(1)

        example_mobject = self.rounded_rectangle(width=4, height=1.25)
        self.play(
            m.FadeIn(example_mobject),
            self.change_subtitle("Rounded Rectangle")
        )

        self.play(
            m.Transform(example_mobject, self.rectangle(width=4, height=1.25)),
            self.change_subtitle("Rectangle")
        )

        self.play(
            m.Transform(example_mobject, self.circle(radius=1)),
            self.change_subtitle("Circle")
        )

        self.play(
            m.Transform(example_mobject, self.math_circle(math_text=r"\pi")),
            self.change_subtitle("Math Circle")
        )

        self.play(
            m.Transform(example_mobject, self.math_arrow(m.LEFT, m.RIGHT)),
            self.change_subtitle("Math Arrow (Engineers Arrow)")
        )


if __name__ == '__main__':
    MyShapesExamplesScene.render_video_medium()
