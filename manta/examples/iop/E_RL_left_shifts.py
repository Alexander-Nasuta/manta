import manim as m
import numpy as np

from color_theme.carolus.corolus_theme import CarolusTheme
from color_theme.rwth.rwth_theme import RwthTheme
from components.axes_utils import AxesUtils
from components.gantt_utils import GanttUtils
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate
from slide_templates.rwth.rwth_slide_template import RwthSlideTemplate

class C:
    DARK_FONT: str = RwthTheme.rwth_blau_50
    DEFAULT_FONT: str = RwthTheme.rwth_blau_75

    GREY_DARK: str = RwthTheme.rwth_schwarz_75
    GREY_DARK_LIGHT: str = RwthTheme.rwth_schwarz_50
    GREY_OUTLINE: str = RwthTheme.outline_color

    GREY: str = RwthTheme.rwth_schwarz_50
    GREY_CHART_BACKGROUND: str = "#212121"
    GREY_ICON_BACKGROUND: str = "#35373C"

    GREY_ICON: str = RwthTheme.rwth_schwarz_50

    YELLOW: str = RwthTheme.rwth_gelb_75

    ORANGE_LIGHT: str = RwthTheme.rwth_gelb_75
    ORANGE_DARK: str = RwthTheme.rwth_orange_100

    PINK: str = RwthTheme.rwth_magenta_75

    BLUE: str = RwthTheme.rwth_blau_75
    BLUE_LIGHT: str = RwthTheme.rwth_blau_50

    TEAL: str = RwthTheme.rwth_tuerkis_75
    TEAL_DARK: str = RwthTheme.rwth_tuerkis_50

    GREEN: str =  RwthTheme.rwth_gruen_75
    GREEN_DARK: str = RwthTheme.rwth_gruen_100
    GREEN_LIGHT: str = RwthTheme.rwth_gruen_50

def styled_text(t, **kwargs):
    default_params = {
        "font": "Iosevka Nerd Font",
        "color": C.DEFAULT_FONT
    }
    params = {**default_params, **kwargs}
    return m.Text(t, **params)

class EIopLeftShift(RwthTheme, AxesUtils, GanttUtils, RwthSlideTemplate):

    # font_name = "IosevkaTermSlab Nerd Font Mono"

    subtitle_color = RwthTheme.rwth_blau_75
    title_seperator_color = RwthTheme.rwth_blau_100

    font_size_tiny: int = 12
    font_size_script: int = 16
    font_size_footnote: int = 20
    font_size_small: int = 22

    font_size_normal: int = 24

    font_size_large: int = 28
    font_size_Large: int = 34
    font_size_LARGE: int = 40
    font_size_huge: int = 50
    font_size_Huge: int = 60

    font_color = RwthTheme.rwth_blau_100
    font_color_secondary = RwthTheme.rwth_blau_75

    logo_paths = [
        "iop_logo.png"
    ]
    logo_height = 0.6
    index_prefix = "G "

    def construct(self):
        self.play(
            self.set_title_row(
                title="RL Approach",
                seperator=": ",
                subtitle="Left Shift"
            ),
            self.add_logos(),
            self.add_seperator_line_top(),
            self.add_seperator_line_bottom()
        )

        class MyText(m.Text):
            def __init__(self, *tex_strings, **kwargs):
                super().__init__(*tex_strings, font="Larabiefont", **kwargs)

        axes = m.Axes(
            x_range=[0, 12, 1],
            y_range=[0, 5, 1],
            x_length=10.5,
            y_length=2.0,
            y_axis_config={"tick_size": 0},
            x_axis_config={
                "tick_size": 0.0425,
                "numbers_to_include": [0, 5, 10],
                "numbers_with_elongated_ticks": [0, 5, 10],
                "font_size": 16,
                "exclude_origin_tick": False,
                "numbers_to_exclude": [],
            },
            axis_config={
                "include_numbers": False,
                "tip_width": 0.125,
                "tip_height": 0.25,
                "label_constructor": MyText,
            },
        )

        axes.move_to([0.5, 1.3125, 0])
        axes.set_color(C.DEFAULT_FONT)
        labels = axes.get_axis_labels(x_label=styled_text("time").scale(0.5), y_label='')
        labels.set_color(C.DEFAULT_FONT)

        job0_title = styled_text("Job 0", color=C.DEFAULT_FONT).scale(0.5)
        job0_title.move_to(axes.c2p(-0.75, 3.5))

        job1_title = styled_text("Job 1", color=C.DEFAULT_FONT).scale(0.5)
        job1_title.move_to(axes.c2p(-0.75, 2.5))

        job2_title = styled_text("Job 2", color=C.DEFAULT_FONT).scale(0.5)
        job2_title.move_to(axes.c2p(-0.75, 1.5))

        j0_t1 = m.Polygon(*[
            axes.c2p(2, 4),
            axes.c2p(0, 4),
            axes.c2p(0, 3),
            axes.c2p(2, 3),
        ], color=C.BLUE, fill_opacity=1, stroke_width=1)
        j0_t1.z_index = axes.z_index - 1

        j0_t2 = m.Polygon(*[
            axes.c2p(2 + 4, 4),
            axes.c2p(2, 4),
            axes.c2p(2, 3),
            axes.c2p(6, 3),
        ], color=C.TEAL, fill_opacity=1, stroke_width=1)

        j1_t1 = m.Polygon(*[
            axes.c2p(5, 3),
            axes.c2p(0, 3),
            axes.c2p(0, 2),
            axes.c2p(5, 2),
        ], color=C.ORANGE_DARK, fill_opacity=1, stroke_width=1)
        j1_t1.z_index = axes.z_index - 1

        j1_t2 = m.Polygon(*[
            axes.c2p(5 + 3, 3),
            axes.c2p(5, 3),
            axes.c2p(5, 2),
            axes.c2p(8, 2),
        ], color=C.BLUE, fill_opacity=1, stroke_width=1)

        tasks_gant = m.VGroup(j0_t1, j0_t2, j1_t1, j1_t2)

        task_circle_kwargs = {
            "radius": 0.25 * 0.75,
            "stroke_width": 6,
            "fill_color": C.YELLOW,
            "fill_opacity": 1.0
        }
        fictive_task_circle_kwargs = {
            "radius": 0.25 * 0.75,
            "stroke_width": 6,
            "fill_color": C.GREEN_LIGHT,
            "fill_opacity": 1.0
        }
        x_scaling = 2.25
        y_scaling = 1.125

        row1_y = 1 * y_scaling
        row2_y = 0 * y_scaling
        row3_y = -1 * y_scaling

        t0_circle = m.Circle(stroke_color=C.DARK_FONT, **fictive_task_circle_kwargs)
        t0_text = m.MathTex("\mathtt{t_0}", color=C.GREY_DARK).scale(0.5)
        t0_group = m.VGroup(t0_circle, t0_text)
        t0_group.move_to(np.array([-2 * x_scaling, row2_y, 0]))

        t10_circle = m.Circle(stroke_color=C.DARK_FONT, **fictive_task_circle_kwargs)
        t10_text = m.MathTex("\mathtt{t_*}", color=C.GREY_DARK).scale(0.5)
        t10_group = m.VGroup(t10_circle, t10_text)
        t10_group.move_to(np.array([2 * x_scaling, row2_y, 0]))

        t1_circle = m.Circle(stroke_color=C.BLUE, **task_circle_kwargs)
        t1_text = m.MathTex("\mathtt{t_1}", color=C.GREY_DARK).scale(0.5)
        t1_group = m.VGroup(t1_circle, t1_text)
        t1_group.move_to(np.array([-1 * x_scaling, row1_y, 0]))
        t1_circle.set_fill(C.GREEN_LIGHT)

        t2_circle = m.Circle(stroke_color=C.TEAL, **task_circle_kwargs)
        t2_text = m.MathTex("\mathtt{t_2}", color=C.GREY_DARK).scale(0.5)
        t2_group = m.VGroup(t2_circle, t2_text)
        t2_group.move_to(np.array([0 * x_scaling, row1_y, 0]))
        t2_circle.set_fill(C.GREEN_LIGHT)

        t3_circle = m.Circle(stroke_color=C.ORANGE_DARK, **task_circle_kwargs)
        t3_text = m.MathTex("\mathtt{t_3}", color=C.GREY_DARK).scale(0.5)
        t3_group = m.VGroup(t3_circle, t3_text)
        t3_group.move_to(np.array([1 * x_scaling, row1_y, 0]))

        t4_circle = m.Circle(stroke_color=C.ORANGE_DARK, **task_circle_kwargs)
        t4_text = m.MathTex("\mathtt{t_4}", color=C.GREY_DARK).scale(0.5)
        t4_group = m.VGroup(t4_circle, t4_text)
        t4_group.move_to(np.array([-1 * x_scaling, row2_y, 0]))
        t4_circle.set_fill(C.GREEN_LIGHT)

        t5_circle = m.Circle(stroke_color=C.BLUE, **task_circle_kwargs)
        t5_text = m.MathTex("\mathtt{t_5}", color=C.GREY_DARK).scale(0.5)
        t5_group = m.VGroup(t5_circle, t5_text)
        t5_group.move_to(np.array([0 * x_scaling, row2_y, 0]))
        t5_circle.set_fill(C.GREEN_LIGHT)

        t6_circle = m.Circle(stroke_color=C.TEAL, **task_circle_kwargs)
        t6_text = m.MathTex("\mathtt{t_6}", color=C.GREY_DARK).scale(0.5)
        t6_group = m.VGroup(t6_circle, t6_text)
        t6_group.move_to(np.array([1 * x_scaling, row2_y, 0]))

        t7_circle = m.Circle(stroke_color=C.BLUE, **task_circle_kwargs)
        t7_text = m.MathTex("\mathtt{t_7}", color=C.GREY_DARK).scale(0.5)
        t7_group = m.VGroup(t7_circle, t7_text)
        t7_group.move_to(np.array([-1 * x_scaling, row3_y, 0]))

        t8_circle = m.Circle(stroke_color=C.ORANGE_DARK, **task_circle_kwargs)
        t8_text = m.MathTex("\mathtt{t_8}", color=C.GREY_DARK).scale(0.5)
        t8_group = m.VGroup(t8_circle, t8_text)
        t8_group.move_to(np.array([0 * x_scaling, row3_y, 0]))

        t9_circle = m.Circle(stroke_color=C.TEAL, **task_circle_kwargs)
        t9_text = m.MathTex("\mathtt{t_9}", color=C.GREY_DARK).scale(0.5)
        t9_group = m.VGroup(t9_circle, t9_text)
        t9_group.move_to(np.array([1 * x_scaling, row3_y, 0]))

        job_arrow_kwargs = {
            "tip_shape": m.ArrowTriangleFilledTip,
            "tip_length": 0.175,
            "stroke_width": 3,
            "buff": 0,
            "color": C.DARK_FONT
        }

        job_edge_0_1 = m.Arrow(start=t0_circle, end=t1_circle, **job_arrow_kwargs)
        job_edge_0_4 = m.Arrow(start=t0_circle, end=t4_circle, **job_arrow_kwargs)
        job_edge_0_7 = m.Arrow(start=t0_circle, end=t7_circle, **job_arrow_kwargs)

        job_edge_1_2 = m.Arrow(start=t1_circle, end=t2_circle, **job_arrow_kwargs)
        job_edge_2_3 = m.Arrow(start=t2_circle, end=t3_circle, **job_arrow_kwargs)
        job_edge_3_10 = m.Arrow(start=t3_circle, end=t10_circle, **job_arrow_kwargs)

        job_edge_4_5 = m.Arrow(start=t4_circle, end=t5_circle, **job_arrow_kwargs)
        job_edge_5_6 = m.Arrow(start=t5_circle, end=t6_circle, **job_arrow_kwargs)
        job_edge_6_10 = m.Arrow(start=t6_circle, end=t10_circle, **job_arrow_kwargs)

        job_edge_7_8 = m.Arrow(start=t7_circle, end=t8_circle, **job_arrow_kwargs)
        job_edge_8_9 = m.Arrow(start=t8_circle, end=t9_circle, **job_arrow_kwargs)
        job_edge_9_10 = m.Arrow(start=t9_circle, end=t10_circle, **job_arrow_kwargs)

        # job edge labels
        job_edge_0_1_label = styled_text("0", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_0_1.get_center() + m.UL * 0.2)

        job_edge_0_4_label = styled_text("0", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_0_4.get_center() + m.UP * 0.2)

        job_edge_0_7_label = styled_text("0", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_0_7.get_center() + m.DL * 0.2)

        job_edge_1_2_label = styled_text("2", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_1_2.get_center() + m.UP * 0.2)

        job_edge_2_3_label = styled_text("4", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_2_3.get_center() + m.UP * 0.2)

        job_edge_3_10_label = styled_text("3", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_3_10.get_center() + m.UR * 0.2)

        job_edge_4_5_label = styled_text("5", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_4_5.get_center() + m.UP * 0.2)

        job_edge_5_6_label = styled_text("3", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_5_6.get_center() + m.UP * 0.2)

        job_edge_6_10_label = styled_text("2", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_6_10.get_center() + m.UP * 0.2)

        job_edge_7_8_label = styled_text("2", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_7_8.get_center() + m.DOWN * 0.2)

        job_edge_8_9_label = styled_text("1", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_8_9.get_center() + m.DOWN * 0.2)

        job_edge_9_10_label = styled_text("4", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_9_10.get_center() + m.DR * 0.2)

        machine_arrow_kwargs = {
            "tip_shape": m.ArrowTriangleFilledTip,
            "tip_length": 0.175,
            "stroke_width": 3,
            "buff": 0,
        }
        curved_machine_arrow_kwargs = {
            "tip_shape": m.ArrowTriangleFilledTip,
            "tip_length": 0.175,
            "stroke_width": 3,
        }

        machine_edge_1_5 = m.Arrow(start=t1_circle, end=t5_circle, color=C.BLUE, **machine_arrow_kwargs)
        machine_edge_1_5_label = styled_text("2", color=C.BLUE).scale(0.425).move_to(
            machine_edge_1_5.get_center() + m.UP * 0.2)

        graph = m.VGroup(
            t0_group,
            t10_group,

            t1_group,
            t2_group,
            t3_group,

            t4_group,
            t5_group,
            t6_group,

            t7_group,
            t8_group,
            t9_group,

            job_edge_0_1,
            job_edge_0_4,
            job_edge_0_7,
            job_edge_1_2,
            job_edge_2_3,
            job_edge_3_10,
            job_edge_4_5,
            job_edge_5_6,
            job_edge_6_10,
            job_edge_7_8,
            job_edge_8_9,
            job_edge_9_10,

            job_edge_0_1_label,
            job_edge_0_4_label,
            job_edge_0_7_label,

            job_edge_1_2_label,
            job_edge_2_3_label,
            job_edge_3_10_label,

            job_edge_4_5_label,
            job_edge_5_6_label,
            job_edge_6_10_label,

            job_edge_7_8_label,
            job_edge_8_9_label,
            job_edge_9_10_label,

            machine_edge_1_5,
            machine_edge_1_5_label,
        )


        graph.scale(0.8)
        graph.shift(m.DOWN * 1.5)





        self.play(
            m.FadeIn(axes),
            m.FadeIn(job0_title),
            m.FadeIn(job1_title),
            m.FadeIn(job2_title),
            m.FadeIn(tasks_gant),
            m.FadeIn(graph),
        )

        temp_text_group = m.VGroup(
            t0_text,
            t1_text,
            t2_text,
            t3_text,
            t4_text,
            t5_text,
            t6_text,
            t7_text,
            t8_text,
            t9_text,
            t10_text,
        )
        temp_text_group.z_index = 500

        self.add(
            temp_text_group
        )

        j2_t1_without_ls = m.Polygon(*[
            axes.c2p(8 + 2, 2),
            axes.c2p(8, 2),
            axes.c2p(8, 1),
            axes.c2p(10, 1),
        ], color=C.BLUE, fill_opacity=1, stroke_width=1)

        j2_t1_with_ls = m.Polygon(*[
            axes.c2p(2 + 2, 2),
            axes.c2p(2, 2),
            axes.c2p(2, 1),
            axes.c2p(4, 1),
        ], color=C.BLUE, fill_opacity=1, stroke_width=1)

        t7_circle.generate_target()
        t7_circle.target.set_fill(C.GREEN_LIGHT)

        machine_edge_5_7 = m.Arrow(start=t5_circle, end=t7_circle, color=C.BLUE, **machine_arrow_kwargs)
        machine_edge_5_7_label = styled_text("2", color=C.BLUE).scale(0.425).move_to(
            machine_edge_5_7.get_center() + m.DOWN * 0.2)

        machine_edge_7_5 = m.Arrow(start=t7_circle, end=t5_circle, color=C.BLUE, **machine_arrow_kwargs)

        curved_machine_edge_1_7 = m.CurvedArrow(start_point=job_edge_0_1.get_end(), end_point=job_edge_0_7.get_end(),
                                                color=C.BLUE, **curved_machine_arrow_kwargs)
        curved_machine_edge_1_7_label = styled_text("2", color=C.BLUE).scale(0.425).move_to(
            curved_machine_edge_1_7.get_end() + m.UP * 0.5 + m.LEFT * 0.125)

        self.play(
            m.FadeIn(j2_t1_without_ls),
            m.MoveToTarget(t7_circle),
            m.Write(machine_edge_5_7),
            m.FadeIn(machine_edge_5_7_label),
        )


        self.play(
            m.Transform(j2_t1_without_ls, j2_t1_with_ls, replace_mobject_with_target_in_scene=True),
            m.Transform(machine_edge_1_5, curved_machine_edge_1_7, replace_mobject_with_target_in_scene=True),
            m.Transform(machine_edge_1_5_label, curved_machine_edge_1_7_label,
                        replace_mobject_with_target_in_scene=True),
            m.Transform(machine_edge_5_7, machine_edge_7_5, replace_mobject_with_target_in_scene=True),
        )

        self.play(
            self.overlay_scene()
        )





if __name__ == '__main__':
    EIopLeftShift.save_sections_without_cache()