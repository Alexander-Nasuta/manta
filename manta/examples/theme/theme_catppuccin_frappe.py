from color_theme.catppucin.catppuccin_frappe import CatppuccinFrappeTheme
from slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyCatppuccinFrappeScene(CatppuccinFrappeTheme, MinimalSlideTemplate):

    def construct(self):
        self.play(
            self.set_title_row(
                title="Catppuccin Frappe",
            )
        )

        self.add(
            self.color_theme_smoke_test_group()
        )


if __name__ == '__main__':
    MyCatppuccinFrappeScene.show_last_frame()
