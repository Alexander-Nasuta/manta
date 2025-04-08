import manim as m

from manta.slide_templates.title_slide import TitleSlide
from slide_templates.rwth.rwth_slide_template import RwthSlideTemplate


class EAgenda(
    RwthSlideTemplate  # this is the base class for creating a slide which has title and subtitle elements
):
    logo_paths = [
        "iop_logo.png"
    ]
    logo_height = 0.6
    index_prefix = "X "

    index_color=RwthSlideTemplate.background_color
    default_icon_color = RwthSlideTemplate.rwth_blau_75

    def construct(self):

        self.play(
            self.set_title_row(
                title="Agenda",
            ),
            self.add_seperator_line_top(),
            self.add_seperator_line_bottom(),
            self.add_logos(),
        )

        rect_kwargs = {
            "font_size": 16,
            "icon_kwargs": {
                "font_size": 16,
            },
            "h_buff": 0.25,
            "v_buff": 0.125,
        }

        agenda_point_a = self.icon_textbox(
            text="Job Shop Scheduling Problem (JSP) Motivation",
            icon='factory',
            width=self.content_width,
            **rect_kwargs
        )
        agenda_point_a.to_edge(m.UP, buff=1.125)

        agenda_point_b = self.icon_textbox(
            text="JSP Modelling Approach",
            icon='chart-timeline',
            width=self.content_width,
            **rect_kwargs
        )
        agenda_point_b.next_to(agenda_point_a, m.DOWN, buff=self.med_small_buff)

        agenda_point_c = self.icon_textbox(
            text="Hands On: Manual Scheduling and Exact Solvers",
            icon='language-python',
            icon_color=RwthSlideTemplate.rwth_orange_100,
            width=self.content_width,
            fill_color=RwthSlideTemplate.rwth_blau_25,
            **rect_kwargs
        )
        agenda_point_c.next_to(agenda_point_b, m.DOWN, buff=self.med_small_buff)

        agenda_point_d = self.icon_textbox(
            text="Reinforcement Learning for the JSP",
            icon='brain#2',
            width=self.content_width,
            **rect_kwargs
        )
        agenda_point_d.next_to(agenda_point_c, m.DOWN, buff=self.med_small_buff)

        agenda_point_e = self.icon_textbox(
            text="Hands On: Reinforcement Learning for the JSP",
            icon='language-python',
            icon_color=RwthSlideTemplate.rwth_orange_100,
            width=self.content_width,
            fill_color=RwthSlideTemplate.rwth_blau_25,
            **rect_kwargs
        )
        agenda_point_e.next_to(agenda_point_d, m.DOWN, buff=self.med_small_buff)

        agenda_point_f = self.icon_textbox(
            text="Neural Monte Carlo Tree Search for the JSP",
            icon='graph-outline',
            width=self.content_width,
            **rect_kwargs
        )
        agenda_point_f.next_to(agenda_point_e, m.DOWN, buff=self.med_small_buff)

        agenda_point_g = self.icon_textbox(
            text="Hands On: Monte Carlo Tree Search for the JSP",
            icon='language-python',
            width=self.content_width,
            icon_color=RwthSlideTemplate.rwth_orange_100,
            fill_color=RwthSlideTemplate.rwth_blau_25,
            **rect_kwargs
        )
        agenda_point_g.next_to(agenda_point_f, m.DOWN, buff=self.med_small_buff)

        animation_group = m.AnimationGroup(
            *[m.FadeIn(elem) for elem in [
                agenda_point_a,
                agenda_point_b,
                agenda_point_c,
                agenda_point_d,
                agenda_point_e,
                agenda_point_f,
                agenda_point_g
            ]],
            lag_ratio=0.15
        )

        self.play(
            animation_group
        )

        # indicate a agenda point
        # self.play(
        #    m.Circumscribe(agenda_point_a, color=self.blue)
        # )

        # alternatively, you can use the following code to indicate a agenda point
        surrounding_rect = m.SurroundingRectangle(
            agenda_point_d,
            corner_radius=0.125, color=self.rwth_orange_75)
        self.play(
            m.Create(surrounding_rect)
        )

        self.play(
            self.overlay_scene()
        )



if __name__ == '__main__':
    # uncomment this line if you want to render the scene in video format
    # MyAgenda.render_video_medium()

    # this line will show the last frame of the scene when the script is run
    EAgenda.save_sections_without_cache()