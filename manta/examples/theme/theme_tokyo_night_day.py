from manta.color_theme.tokyo_night.tokyo_night_day import TokyoNightDay
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyTokyoNightDayScene(TokyoNightDay, MinimalSlideTemplate):

    def construct(self):
        self.play(
            self.set_title_row(
                title="Tokyo Night Day",
            )
        )

        self.add(
            self.color_theme_smoke_test_group()
        )


if __name__ == '__main__':
    MyTokyoNightDayScene.show_last_frame()
