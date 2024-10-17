# Shapes

The 'ShapeUtils' class provides a set of useful shapes that can be used in your slides. 
The shapes are designed to be used with the Manta slide templates and can be easily added to your scenes.
The main difference between manta and manim slides is, that manta performs some additional styling and formating 
to the shapes, which are consistent with the specified theme.
Manta also provides some additional shapes that are not included in the manim library 
(like 'math_circle' or 'math_arrow').

```{eval-rst}
.. manim:: MyShapesExamplesScene

    
    import manim as m

    from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


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
            self.wait(1)

            self.play(
                m.Transform(example_mobject, self.rectangle(width=4, height=1.25)),
                self.change_subtitle("Rectangle")
            )
            self.wait(1)

            self.play(
                m.Transform(example_mobject, self.circle(radius=1)),
                self.change_subtitle("Circle")
            )
            self.wait(1)

            self.play(
                m.Transform(example_mobject, self.math_circle(math_text=r"\pi")),
                self.change_subtitle("Math Circle")
            )
            self.wait(1)

            self.play(
                m.Transform(example_mobject, self.math_arrow(m.LEFT, m.RIGHT)),
                self.change_subtitle("Math Arrow (Engineers Arrow)")
            )
            self.wait(1)


    if __name__ == '__main__':
        MyShapesExamplesScene.render_video_medium()

```