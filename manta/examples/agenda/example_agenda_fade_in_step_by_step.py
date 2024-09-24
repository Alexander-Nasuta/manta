import manim as m

from elements.rectangle_utils import RectangleUtils
from slide_templates.title_slide import TitleSlide


class Agenda(RectangleUtils, TitleSlide):

    def construct(self):
        self.play(
            self.set_title_row(
                title="Agenda",
                # seperator=":",
                # subtitle="What we will learn today"
            ),
        )

        agenda_point_a = self.icon_textbox(
            text="Introduction",
            icon='numeric-1-box-outline',
            width=self.content_width,
        )
        agenda_point_a.to_edge(m.UP, buff=1.0)
        self.play(
            m.FadeIn(agenda_point_a)
        )

        agenda_point_b = self.icon_textbox(
            text="Motivation",
            icon='numeric-2-box-outline',
            width=self.content_width,
        )
        agenda_point_b.next_to(agenda_point_a, m.DOWN, buff=self.med_large_buff)
        self.play(
            m.FadeIn(agenda_point_b)
        )

        agenda_point_c = self.icon_textbox(
            text="Cool Stuff",
            icon='numeric-3-box-outline',
            width=self.content_width,
        )
        agenda_point_c.next_to(agenda_point_b, m.DOWN, buff=self.med_large_buff)
        self.play(
            m.FadeIn(agenda_point_c)
        )

        agenda_point_d = self.icon_textbox(
            text="Summary",
            icon='numeric-4-box-outline',
            width=self.content_width,
        )
        agenda_point_d.next_to(agenda_point_c, m.DOWN, buff=self.med_large_buff)
        self.play(
            m.FadeIn(agenda_point_d)
        )

        self.fade_out_scene()


if __name__ == '__main__':
    Agenda.render_video_medium()
