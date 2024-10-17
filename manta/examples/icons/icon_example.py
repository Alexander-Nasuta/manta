import manim as m

from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyIconExamplesScene(MinimalSlideTemplate):

    def construct(self):

        hamburger_icon = self.symbol("hamburger")
        coffee_icon = self.symbol(0xEC15)

        icon_group = m.VGroup(hamburger_icon, coffee_icon)
        icon_group.arrange(m.RIGHT, buff=self.med_large_buff)
        icon_group.move_to(m.ORIGIN)

        self.play(
            self.set_title_row(
                title="NerdfontIconUtils",
                seperator=": ",
                subtitle="symbol"
            ),
            m.FadeIn(icon_group),
        )



if __name__ == '__main__':
    MyIconExamplesScene.render_video_medium()
