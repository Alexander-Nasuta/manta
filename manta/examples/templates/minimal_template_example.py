from slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyMinimalSlideTemplateExample(MinimalSlideTemplate):

    def construct(self):
        self.play(
            self.set_title_row(
                title="Lucky Numbers",
            )
        )

        self.play(
            self.change_subtitle("Uncovering the Magic and Math Behind Good Fortune!"),
        )

        self.wait(2) # wait increases the index of the slide

        self.fade_out_scene()


if __name__ == '__main__':
    MyMinimalSlideTemplateExample.render_video_medium()
