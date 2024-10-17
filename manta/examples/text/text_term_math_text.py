import manim as m

from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyTermMathTextExampleScene(MinimalSlideTemplate):

    def construct(self):

        self.play(
            self.set_title_row(
                title="Text Utils",
                seperator=": ",
                subtitle="term_math_text"
            )
        )

        cubic_polynomial = self.term_math_text("ax^3 + bx^2 + cx + d")
        cubic_polynomial.scale(2.5)

        self.play(
            m.FadeIn(cubic_polynomial ),
        )



if __name__ == '__main__':
    MyTermMathTextExampleScene.render_video_medium()
