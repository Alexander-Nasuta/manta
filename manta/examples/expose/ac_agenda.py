import manim as m

from color_theme.carolus.corolus_theme import CarolusTheme
from manta.slide_templates.title_slide import TitleSlide


class ExposeAgenda(CarolusTheme,TitleSlide):

    font_name = "IosevkaTermSlab Nerd Font Mono"

    def construct(self):

        agenda_point_a = self.icon_textbox(
            text="Motivation",
            #icon='alpha-a-box-outline',
            icon="head-lightbulb-outline",
            width=self.content_width,
        )
        agenda_point_a.to_edge(m.UP, buff=1.0)

        agenda_point_b = self.icon_textbox(
            text="Scientific Goal and Research Questions",
            #icon='alpha-b-box-outline',
            icon="goal",
            width=self.content_width,
        )
        agenda_point_b.next_to(agenda_point_a, m.DOWN, buff=self.med_large_buff)

        agenda_point_c = self.icon_textbox(
            text="Dissertation Placement",
            #icon='alpha-c-box-outline',
            icon="map-marker-radius",
            width=self.content_width,
        )
        agenda_point_c.next_to(agenda_point_b, m.DOWN, buff=self.med_large_buff)

        agenda_point_d = self.icon_textbox(
            text="Timeline and Milestones",
            icon='chart-timeline',
            width=self.content_width,
        )
        agenda_point_d.next_to(agenda_point_c, m.DOWN, buff=self.med_large_buff)

        animation_group = m.AnimationGroup(
            *[m.FadeIn(elem) for elem in [agenda_point_a, agenda_point_b, agenda_point_c, agenda_point_d]],
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
            agenda_point_a,
            corner_radius=0.125, color=self.blue)

        # self.play(m.Create(surrounding_rect))

        self.wait(0.1)
        self.fade_out_scene()


if __name__ == '__main__':
    # uncomment this line if you want to render the scene in video format
    # MyAgenda.render_video_medium()

    # this line will show the last frame of the scene when the script is run
    ExposeAgenda.save_sections_without_cache()