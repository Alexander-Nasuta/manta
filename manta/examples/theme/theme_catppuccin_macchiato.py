import manim as m

from manta.color_theme.catppucin.catppuccin_macchiato import CatppuccinMacchiatoTheme
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyThemedSceneCatppuccinMacchiato(CatppuccinMacchiatoTheme, MinimalSlideTemplate):

    def construct(self):
        self.play(
            self.set_title_row(
                title="Catppuccin Macchiato",
            )
        )

        self.add(
            self.color_theme_smoke_test_group()
        )


if __name__ == '__main__':
    MyThemedSceneCatppuccinMacchiato.show_last_frame()
