from slide_templates.minimal.minimal_intro_slide import MinimalIntroSlide


class ExampleIntroSlide(MinimalIntroSlide):

    title = "Manta"
    subtitle = "A Framework for creating Presentation Slides \n with Manim"

    def construct(self):
        self.play(
            self.fade_in_slide()
        )
        self.wait(2)

        self.fade_out_scene()


if __name__ == '__main__':
    ExampleIntroSlide.render_video_medium()
