from slide_templates.minimal.minimal_intro_slide import MinimalIntroSlide


class ExampleIntroSlide(MinimalIntroSlide):
    title = "Title 1337"
    subtitle = "Subtitle row 1 \n Subtitle row 2"

    def construct(self):
        self.play(
            self.fade_in_slide()
        )


def test_classic_intro_slide():
    ExampleIntroSlide.rendering_test()
