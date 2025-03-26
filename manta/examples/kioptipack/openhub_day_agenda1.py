import manim as m

from color_theme.carolus.corolus_theme import CarolusTheme
from examples.kioptipack.KIOptipack_theme import OptiPackTheme
from manta.slide_templates.title_slide import TitleSlide


class OpenHubDaysAgenda1(CarolusTheme, TitleSlide):

    default_icon_color = CarolusTheme.yellow

    def construct(self):

        #agenda_point_a = self.icon_textbox(
        #   text="Motivation",
        #   icon='alpha-a-box-outline',
        #   width=self.content_width,
        #)
        #agenda_point_a.to_edge(m.UP, buff=1.0)

        agenda_point_b = self.icon_textbox(
            text="Datenfluss im Datenraum",
            #icon='alpha-b-box-outline',
            #icon="package",
            icon="database-export-outline",
            width=self.content_width,
        )
        agenda_point_b.to_edge(m.UP, buff=1.0)

        agenda_point_c = self.icon_textbox(
            text="Machine Learning im Datenraum",
            #icon='alpha-c-box-outline',
            icon="chart-timeline-variant-shimmer",
            width=self.content_width,
        )
        agenda_point_c.next_to(agenda_point_b, m.DOWN, buff=self.med_large_buff)

        agenda_point_d = self.icon_textbox(
            text="Verknüpfung zu einem Gesamtsytem",
            #icon='alpha-d-box-outline',
            icon="globe",
            width=self.content_width,
        )
        agenda_point_d.next_to(agenda_point_c, m.DOWN, buff=self.med_large_buff)

        animation_group = m.AnimationGroup(
            *[m.FadeIn(elem) for elem in [
                # agenda_point_a,
                agenda_point_b,
                agenda_point_c,
                agenda_point_d
            ]
            ],
            lag_ratio=0.15
        )

        self.play(
            self.set_title_row(
                title="Agenda",
            ),
            animation_group
        )

        # indicate a agenda point
        # self.play(
        #    m.Circumscribe(agenda_point_a, color=self.blue)
        # )

        # alternatively, you can use the following code to indicate a agenda point
        surrounding_rect = m.SurroundingRectangle(
            agenda_point_b,
            corner_radius=0.125, color=self.blue)
        self.play(
            m.Create(surrounding_rect)
        )

        self.wait(0.1)
        self.fade_out_scene()


if __name__ == '__main__':
    # uncomment this line if you want to render the scene in video format
    # MyAgenda.render_video_medium()

    # this line will show the last frame of the scene when the script is run
    OpenHubDaysAgenda1.save_sections_without_cache()