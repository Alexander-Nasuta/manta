import manim as m

from color_theme.tokyo_night.tokyo_night import TokyoNight
from slide_templates.classic.classic_slide_template import ClassicSlideTemplate


class MyMinimalSlideTemplateExample(
    TokyoNight,  # TokyoNight is a color theme
    ClassicSlideTemplate  # ClassicSlideTemplate is a slide template
):

    # The following class variables can be used to override the default colors of the title row
    subtitle_color = TokyoNight.magenta
    title_color = TokyoNight.blue
    title_seperator_color = TokyoNight.yellow

    def construct(self):
        self.play(
            self.set_title_row(title="Perfect Numbers", seperator=":", subtitle="very pretty numbers"),
            self.add_seperator_lines()
        )

        self.wait(2)  # wait increases the index of the slide

        self.fade_out_scene()


if __name__ == '__main__':
    MyMinimalSlideTemplateExample.render_video_medium()
