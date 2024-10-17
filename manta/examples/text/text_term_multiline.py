import manim as m

from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyTermTextMultilineExampleScene(MinimalSlideTemplate):

    def construct(self):


        my_text = self.term_text("Hello \n World!", font_size=self.font_size_huge, font_color=self.yellow)

        wine_text = """Wine is not 
        an emulator"""

        wine_text = self.term_text(wine_text, font_size=self.font_size_huge, color=self.magenta)

        text_group = m.VGroup(my_text, wine_text).arrange(m.RIGHT, buff=self.med_large_buff)
        text_group.move_to(m.ORIGIN)


        self.play(
            self.set_title_row(
                title="Text Utils",
                seperator=": ",
                subtitle="term_text (multiline)",
                subtitle_kwargs={
                    "t2c": {"(multiline)": self.magenta}
                }
            ),
            m.FadeIn(text_group),
        )






if __name__ == '__main__':
    MyTermTextMultilineExampleScene.render_video_medium()
