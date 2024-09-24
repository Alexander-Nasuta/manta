from manta.color_theme.tokyo_night.tokyo_night_storm import TokyoNightStorm
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyTokyoNightStormScene(TokyoNightStorm, MinimalSlideTemplate):

    def construct(self):
        self.play(
            self.set_title_row(
                title="Tokyo Night Storm",
            )
        )

        self.add(
            self.color_theme_smoke_test_group()
        )


if __name__ == '__main__':
    MyTokyoNightStormScene.show_last_frame()
