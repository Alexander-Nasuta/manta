from manta.color_theme.tokyo_night.tokyo_night_moon import TokyoNightMoon
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyTokyoNightMoonScene(TokyoNightMoon, MinimalSlideTemplate):

    def construct(self):
        self.play(
            self.set_title_row(
                title="Tokyo Night Moon",
            )
        )

        self.add(
            self.color_theme_smoke_test_group()
        )


if __name__ == '__main__':
    MyTokyoNightMoonScene.show_last_frame()
