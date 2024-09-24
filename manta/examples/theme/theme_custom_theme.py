from slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate

from manta.color_theme.color_theme_ABC import ColorThemeABC


# useful link: https://windowsterminalthemes.dev/
class MyCustomCyberdyneTheme(ColorThemeABC):
    background_color: str = "#151144"
    background_color_bright: str = "#2e2e2e"

    font_color: str = "#00ff92"
    font_color_secondary: str = "#00ff9c"

    black: str = "#080808"
    black_bright: str = "#2e2e2e"

    red: str = "#ff8373"
    red_bright: str = "#ffc4be"

    green: str = "#00c172"
    green_bright: str = "#d6fcba"

    yellow: str = "#d2a700"
    yellow_bright: str = "#fffed5"

    blue: str = "#0071cf"
    blue_bright: str = "#c2e3ff"

    magenta: str = "#ff90fe"
    magenta_bright: str = "#ffb2fe"

    cyan: str = "#6bffdd"
    cyan_bright: str = "#e6e7fe"

    white: str = "#f1f1f1"
    white_bright: str = "#ffffff"


class MyCustomThemedScene(MyCustomCyberdyneTheme, MinimalSlideTemplate):

    def construct(self):
        self.play(
            self.set_title_row(
                title="Custom Theme",
                seperator=": ",
                subtitle="Cyberdyne",
            )
        )

        self.add(
            self.color_theme_smoke_test_group()
        )


if __name__ == '__main__':
    MyCustomThemedScene.show_last_frame()
