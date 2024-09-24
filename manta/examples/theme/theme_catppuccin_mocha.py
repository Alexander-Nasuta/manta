from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


# Catppuccin Mocha is the default theme, so we don't need to import it.
class MyCatppuccinMochaScene(MinimalSlideTemplate):

    def construct(self):
        self.play(
            self.set_title_row(
                title="Catppuccin Mocha",
            )
        )

        self.add(
            self.color_theme_smoke_test_group()
        )


if __name__ == '__main__':
    MyCatppuccinMochaScene.show_last_frame()
