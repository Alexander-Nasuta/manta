from manta.color_theme.tokyo_night.tokyo_night import TokyoNight
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyTokyoNightScene(TokyoNight, MinimalSlideTemplate):

    def construct(self):
        self.play(
            self.set_title_row(
                title="Tokyo Night",
            )
        )

        self.add(
            self.color_theme_smoke_test_group()
        )


if __name__ == '__main__':
    MyTokyoNightScene.show_last_frame()
