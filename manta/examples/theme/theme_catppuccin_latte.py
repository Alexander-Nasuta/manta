from manta.color_theme.catppucin.catppuccin_latte import CatppuccinLatteTheme
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyCatppuccinLatteScene(CatppuccinLatteTheme, MinimalSlideTemplate):

    def construct(self):
        self.play(
            self.set_title_row(
                title="Catppuccin Latte",
            )
        )

        self.add(
            self.color_theme_smoke_test_group()
        )


if __name__ == '__main__':
    MyCatppuccinLatteScene.show_last_frame()
