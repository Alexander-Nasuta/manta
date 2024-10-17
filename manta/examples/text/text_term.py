import manim as m

from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyTermTextExamplesScene(MinimalSlideTemplate):

    def construct(self):

        self.play(
            self.set_title_row(
                title="Text Utils",
                seperator=": ",
                subtitle="term_text"
            )
        )

        my_text= self.term_text("Hello World!", font_size=36)

        self.play(
            m.FadeIn(my_text),
        )



if __name__ == '__main__':
    MyTermTextExamplesScene.render_video_medium()
