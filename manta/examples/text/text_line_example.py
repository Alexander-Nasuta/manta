import manim as m

from slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyShapesExamplesScene(MinimalSlideTemplate):

    def construct(self):
        self.play(
            self.set_title_row(
                title="Text Utils",
                seperator=": ",
                subtitle="Text Line"
            )
        )

        segment1, segment2, segment3 = self.text_line("Hello", ", ", "World!", font_size=36)

        self.play(
            m.FadeIn(segment1),
            m.FadeIn(segment2),
            m.FadeIn(segment3),
        )

        segment1.generate_target()
        segment1.target.set_color(self.magenta)
        segment1.target.to_edge(m.LEFT, buff=self.med_large_buff)

        segment2.generate_target()
        segment2.target.set_color(self.green)
        segment2.target.to_edge(m.DOWN, buff=self.med_large_buff)

        segment3.generate_target()
        segment3.target.set_color(self.cyan)
        segment3.target.to_edge(m.RIGHT, buff=self.med_large_buff)

        self.play(
            m.MoveToTarget(segment1),
            m.MoveToTarget(segment2),
            m.MoveToTarget(segment3),
        )

        circle1 = self.math_circle(math_text=r"s_1", color=self.magenta)
        circle2 = self.math_circle(math_text=r"s_2", color=self.green)
        circle3 = self.math_circle(math_text=r"s_3", color=self.cyan)

        circle_group = (m.VGroup(circle1, circle2, circle3)
                        .arrange(m.RIGHT, buff=self.med_large_buff)
                        .move_to(m.ORIGIN))

        self.play(
            m.ReplacementTransform(segment1, circle1),
            m.ReplacementTransform(segment2, circle2),
            m.ReplacementTransform(segment3, circle3),
        )







if __name__ == '__main__':
    MyShapesExamplesScene.render_video_medium()
