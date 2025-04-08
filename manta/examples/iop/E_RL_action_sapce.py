import manim as m
import numpy as np
from PIL.ImageChops import overlay

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

class EIopRlActionSpace(RwthTheme, AxesUtils, GanttUtils, RwthSlideTemplate):

    # font_name = "IosevkaTermSlab Nerd Font Mono"
    logo_paths = [
        "iop_logo.png"
    ]
    logo_height = 0.6
    index_prefix = "F "

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

    def construct(self):
        self.play(
            self.set_title_row(
                title="RL Approach",
                seperator=": ",
                subtitle="State Representation"
            ),
            self.add_logos(),
            self.add_seperator_line_top(),
            self.add_seperator_line_bottom()
        )

        task_circle_kwargs = {
            "radius": 0.25,
            "stroke_width": 6,
            "fill_color": C.YELLOW,
            "fill_opacity": 1.0
        }
        fictive_task_circle_kwargs = {
            "radius": 0.25,
            "stroke_width": 6,
            "fill_color": C.GREEN_LIGHT,
            "fill_opacity": 1.0
        }
        row1_y = -1.0 + 0.125
        row2_y = -3.0 + 0.125

        t1_circle = m.Circle(stroke_color=C.BLUE, **task_circle_kwargs)
        t1_text = m.Tex(r"$\mathsf{t_1}$", color=C.GREY_DARK).scale(0.5)
        t1_group = m.VGroup(t1_circle, t1_text)
        t1_group.move_to(np.array([-3, row1_y, 0]))

        t2_circle = m.Circle(stroke_color=C.ORANGE_DARK, **task_circle_kwargs)
        t2_text = m.Tex(r"$\mathsf{t_2}$", color=C.GREY_DARK).scale(0.5)
        t2_group = m.VGroup(t2_circle, t2_text)
        t2_group.move_to(np.array([-1, row1_y, 0]))

        t3_circle = m.Circle(stroke_color=C.GREEN, **task_circle_kwargs)
        t3_text = m.Tex(r"$\mathsf{t_3}$", color=C.GREY_DARK).scale(0.5)
        t3_group = m.VGroup(t3_circle, t3_text)
        t3_group.move_to(np.array([1, row1_y, 0]))

        t4_circle = m.Circle(stroke_color=C.TEAL, **task_circle_kwargs)
        t4_text = m.Tex(r"$\mathsf{t_4}$", color=C.GREY_DARK).scale(0.5)
        t4_group = m.VGroup(t4_circle, t4_text)
        t4_group.move_to(np.array([3, row1_y, 0]))

        t5_circle = m.Circle(stroke_color=C.BLUE, **task_circle_kwargs)
        t5_text = m.Tex(r"$\mathsf{t_5}$", color=C.GREY_DARK).scale(0.5)
        t5_group = m.VGroup(t5_circle, t5_text)
        t5_group.move_to(np.array([-3, row2_y, 0]))

        t6_circle = m.Circle(stroke_color=C.GREEN, **task_circle_kwargs)
        t6_text = m.Tex(r"$\mathsf{t_6}$", color=C.GREY_DARK).scale(0.5)
        t6_group = m.VGroup(t6_circle, t6_text)
        t6_group.move_to(np.array([-1, row2_y, 0]))

        t7_circle = m.Circle(stroke_color=C.ORANGE_DARK, **task_circle_kwargs)
        t7_text = m.Tex(r"$\mathsf{t_7}$", color=C.GREY_DARK).scale(0.5)
        t7_group = m.VGroup(t7_circle, t7_text)
        t7_group.move_to(np.array([1, row2_y, 0]))

        t8_circle = m.Circle(stroke_color=C.TEAL, **task_circle_kwargs)
        t8_text = m.Tex(r"$\mathsf{t_8}$", color=C.GREY_DARK).scale(0.5)
        t8_group = m.VGroup(t8_circle, t8_text)
        t8_group.move_to(np.array([3, row2_y, 0]))

        # add job edges

        job_arrow_kwargs = {
            "tip_shape": m.ArrowTriangleFilledTip,
            "tip_length": 0.175,
            "stroke_width": 3,
            "buff": 0,
            "color": C.DARK_FONT
        }

        job_edge_1_2 = m.Arrow(start=t1_circle, end=t2_circle, **job_arrow_kwargs)
        job_edge_2_3 = m.Arrow(start=t2_circle, end=t3_circle, **job_arrow_kwargs)
        job_edge_3_4 = m.Arrow(start=t3_circle, end=t4_circle, **job_arrow_kwargs)

        job_edge_5_6 = m.Arrow(start=t5_circle, end=t6_circle, **job_arrow_kwargs)
        job_edge_6_7 = m.Arrow(start=t6_circle, end=t7_circle, **job_arrow_kwargs)
        job_edge_7_8 = m.Arrow(start=t7_circle, end=t8_circle, **job_arrow_kwargs)

        # add fictions nodes
        t0_circle = m.Circle(stroke_color=C.DARK_FONT, **fictive_task_circle_kwargs)
        t0_text = m.Tex(r"$\mathsf{t_0}$", color=C.GREY_DARK).scale(0.5)
        t0_group = m.VGroup(t0_circle, t0_text)
        t0_group.move_to(np.array([-4.5, (row1_y + row2_y) * 0.5, 0]))

        t9_circle = m.Circle(stroke_color=C.DARK_FONT, **fictive_task_circle_kwargs)
        t9_text = m.Tex(r"$\mathsf{t_*}$", color=C.GREY_DARK).scale(0.5)
        t9_group = m.VGroup(t9_circle, t9_text)
        t9_group.move_to(np.array([4.5, (row1_y + row2_y) * 0.5, 0]))

        job_edge_0_1 = m.Arrow(start=t0_circle, end=t1_circle, **job_arrow_kwargs)
        job_edge_0_5 = m.Arrow(start=t0_circle, end=t5_circle, **job_arrow_kwargs)

        job_edge_4_9 = m.Arrow(start=t4_circle, end=t9_circle, **job_arrow_kwargs)
        job_edge_8_9 = m.Arrow(start=t8_circle, end=t9_circle, **job_arrow_kwargs)

        # add durations

        job_edge_0_1_label = styled_text("0", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_0_1.get_center() + m.UL * 0.2)
        job_edge_0_5_label = styled_text("0", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_0_5.get_center() + m.DL * 0.2)

        job_edge_4_9_label = styled_text("12", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_4_9.get_center() + m.UR * 0.2)
        job_edge_8_9_label = styled_text("4", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_8_9.get_center() + m.DR * 0.2)

        job_edge_1_2_label = styled_text("11", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_1_2.get_center() + m.UP * 0.25)
        job_edge_2_3_label = styled_text("3", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_2_3.get_center() + m.UP * 0.25)
        job_edge_3_4_label = styled_text("3", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_3_4.get_center() + m.UP * 0.25)

        job_edge_5_6_label = styled_text("5", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_5_6.get_center() + m.DOWN * 0.25)
        job_edge_6_7_label = styled_text("16", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_6_7.get_center() + m.DOWN * 0.25)
        job_edge_7_8_label = styled_text("7", color=C.DARK_FONT).scale(0.425).move_to(
            job_edge_7_8.get_center() + m.DOWN * 0.25)

        graph = m.VGroup(
            t1_group,
            t2_group,
            t3_group,
            t4_group,
            t5_group,
            t6_group,
            t7_group,
            t8_group,
            t0_group,
            t9_group,
            job_edge_0_1,
            job_edge_0_5,
            job_edge_4_9,
            job_edge_8_9,
            job_edge_1_2,
            job_edge_2_3,
            job_edge_3_4,
            job_edge_5_6,
            job_edge_6_7,
            job_edge_7_8,
            job_edge_0_1_label,
            job_edge_0_5_label,
            job_edge_4_9_label,
            job_edge_8_9_label,
            job_edge_1_2_label,
            job_edge_2_3_label,
            job_edge_3_4_label,
            job_edge_5_6_label,
            job_edge_6_7_label,
            job_edge_7_8_label
        )

        graph.move_to(np.array([0, 0, 0]))

        self.play(
            m.FadeIn(graph)
        )


        machine_arrow_kwargs = {
            "tip_shape": m.ArrowTriangleFilledTip,
            "tip_length": 0.175,
            "stroke_width": 3,
            "buff": 0,
        }

        machine_edge_7_2 = m.Arrow(start=t7_circle, end=t2_circle, color=C.ORANGE_DARK, **machine_arrow_kwargs)
        machine_edge_7_2_label = styled_text("7", color=C.ORANGE_DARK).scale(0.425).move_to(
            machine_edge_7_2.get_center() + np.array([-0.25, +0.6, 0]))

        machine_edge_3_6 = m.Arrow(start=t3_circle, end=t6_circle, color=C.GREEN, **machine_arrow_kwargs)
        machine_edge_3_6_label = styled_text("3", color=C.GREEN).scale(0.425).move_to(
            machine_edge_3_6.get_center() + np.array([-0.25, -0.6, 0]))

        self.play(
            m.FadeIn(machine_edge_7_2),
            m.FadeIn(machine_edge_7_2_label),
            m.FadeIn(machine_edge_3_6),
            m.FadeIn(machine_edge_3_6_label),
        )


        cycle_path_lines_kwargs = {
            "stroke_width": 10,
            "buff": -3,
            "color": C.PINK,
            "stroke_opacity": 0.75,
        }

        line_6_7 = m.Line(start=t6_circle, end=t7_circle, z_index=t1_circle.z_index - 1, **cycle_path_lines_kwargs)
        line_7_2 = m.Line(start=t7_circle, end=t2_circle, z_index=t1_circle.z_index - 1, **cycle_path_lines_kwargs)
        line_2_3 = m.Line(start=t2_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **cycle_path_lines_kwargs)
        line_3_6 = m.Line(start=t3_circle, end=t6_circle, z_index=t1_circle.z_index - 1, **cycle_path_lines_kwargs)

        rt = 0.25
        self.play_without_section(m.Create(line_6_7, run_time=rt))
        self.play_without_section(m.Create(line_7_2, run_time=rt))
        self.play_without_section(m.Create(line_2_3, run_time=rt))
        self.play_without_section(m.Create(line_3_6, run_time=rt))

        self.play(
            m.FadeOut(line_6_7),
            m.FadeOut(line_7_2),
            m.FadeOut(line_2_3),
            m.FadeOut(line_3_6),
            m.FadeOut(machine_edge_7_2),
            m.FadeOut(machine_edge_7_2_label),
            m.FadeOut(machine_edge_3_6),
            m.FadeOut(machine_edge_3_6_label),
        )


        class MyText(m.Text):
            def __init__(self, *tex_strings, **kwargs):
                super().__init__(*tex_strings, font="Larabiefont", **kwargs)

        axes = m.Axes(
            x_range=[0, 41, 1],
            y_range=[0, 4, 1],
            x_length=10.5,
            y_length=2.0,
            y_axis_config={"tick_size": 0},
            x_axis_config={
                "tick_size": 0.0425,
                "numbers_to_include": [0, 5, 10, 15, 20, 25, 30, 35, 40],
                "numbers_with_elongated_ticks": [0, 5, 10, 15, 20, 25, 30, 35, 40],
                "font_size": 16,
                "exclude_origin_tick": False,
                "numbers_to_exclude": [],
            },
            axis_config={
                "include_numbers": False,
                "tip_width": 0.125,
                "tip_height": 0.25,
                "label_constructor": MyText,
                "color": RwthTheme.rwth_schwarz_75
            },
        )
        axes.move_to([0.5, -2.0, 0])

        job0_title = styled_text("Job 0", color=C.DEFAULT_FONT).scale(0.5)
        job0_title.move_to(axes.c2p(-4, 2.5))
        job0_title.scale(1.25)

        job1_title = styled_text("Job 1", color=C.DEFAULT_FONT).scale(0.5)
        job1_title.move_to(axes.c2p(-4, 1.5))
        job1_title.scale(1.25)

        graph.generate_target()
        graph.target.move_to(np.array([0, 1.25, 0]))

        self.play(
            m.MoveToTarget(graph),
            m.FadeIn(axes),
            m.FadeIn(job0_title),
            m.FadeIn(job1_title),
        )

        reset_graph = graph.copy()

        mask_invalid_circle_kwargs = {
            "radius": 0.475,
            "stroke_width": 0,
            "fill_color": C.PINK,
            "fill_opacity": 1.0
        }

        mask_valid_circle_kwargs = {
            "radius": 0.475,
            "stroke_width": 0,
            "fill_color": C.GREEN_DARK,
            "fill_opacity": 1.0
        }

        t1_circle_mask = m.Circle(stroke_color=C.PINK, **mask_valid_circle_kwargs)
        t1_circle_mask.move_to(t1_circle.get_center())

        t2_circle_mask = m.Circle(stroke_color=C.PINK, **mask_invalid_circle_kwargs)
        t2_circle_mask.move_to(t2_circle.get_center())
        t3_circle_mask = m.Circle(stroke_color=C.PINK, **mask_invalid_circle_kwargs)
        t3_circle_mask.move_to(t3_circle.get_center())
        t4_circle_mask = m.Circle(stroke_color=C.PINK, **mask_invalid_circle_kwargs)
        t4_circle_mask.move_to(t4_circle.get_center())

        t5_circle_mask = m.Circle(stroke_color=C.PINK, **mask_valid_circle_kwargs)
        t5_circle_mask.move_to(t5_circle.get_center())

        t6_circle_mask = m.Circle(stroke_color=C.PINK, **mask_invalid_circle_kwargs)
        t6_circle_mask.move_to(t6_circle.get_center())
        t7_circle_mask = m.Circle(stroke_color=C.PINK, **mask_invalid_circle_kwargs)
        t7_circle_mask.move_to(t7_circle.get_center())
        t8_circle_mask = m.Circle(stroke_color=C.PINK, **mask_invalid_circle_kwargs)
        t8_circle_mask.move_to(t8_circle.get_center())

        graph_copy = graph.copy()
        graph_copy.z_index = 500

        self.play(
            m.FadeIn(t1_circle_mask),
            m.FadeIn(t2_circle_mask),
            m.FadeIn(t3_circle_mask),
            m.FadeIn(t4_circle_mask),
            m.FadeIn(t5_circle_mask),
            m.FadeIn(t6_circle_mask),
            m.FadeIn(t7_circle_mask),
            m.FadeIn(t8_circle_mask),
            m.FadeIn(graph_copy)
        )

        self.remove(graph)
        graph = graph_copy


        # axes rects
        j0_t1 = m.Polygon(*[
            axes.c2p(5 + 11, 3),
            axes.c2p(5, 3),
            axes.c2p(5, 2),
            axes.c2p(16, 2),
        ], color=C.BLUE, fill_opacity=1, stroke_width=1)

        j0_t2 = m.Polygon(*[
            axes.c2p(16 + 3, 3),
            axes.c2p(16, 3),
            axes.c2p(16, 2),
            axes.c2p(19, 2),
        ], color=C.ORANGE_DARK, fill_opacity=1, stroke_width=1)

        j0_t3 = m.Polygon(*[
            axes.c2p(24, 3),
            axes.c2p(21, 3),
            axes.c2p(21, 2),
            axes.c2p(24, 2),
        ], color=C.GREEN, fill_opacity=1, stroke_width=1)

        j0_t4 = m.Polygon(*[
            axes.c2p(36, 3),
            axes.c2p(24, 3),
            axes.c2p(24, 2),
            axes.c2p(36, 2),
        ], color=C.TEAL, fill_opacity=1, stroke_width=1)

        j1_t1 = m.Polygon(*[
            axes.c2p(5, 2),
            axes.c2p(0, 2),
            axes.c2p(0, 1),
            axes.c2p(5, 1),
        ], color=C.BLUE, fill_opacity=1, stroke_width=1)

        j1_t2 = m.Polygon(*[
            axes.c2p(21, 2),
            axes.c2p(5, 2),
            axes.c2p(5, 1),
            axes.c2p(21, 1),
        ], color=C.GREEN, fill_opacity=1, stroke_width=1)

        j1_t3 = m.Polygon(*[
            axes.c2p(28, 2),
            axes.c2p(21, 2),
            axes.c2p(21, 1),
            axes.c2p(28, 1),
        ], color=C.ORANGE_DARK, fill_opacity=1, stroke_width=1)

        j1_t4 = m.Polygon(*[
            axes.c2p(40, 2),
            axes.c2p(36, 2),
            axes.c2p(36, 1),
            axes.c2p(40, 1),
        ], color=C.TEAL, fill_opacity=1, stroke_width=1)

        t5_circle.generate_target()
        t5_circle.target.set_fill(C.GREEN_LIGHT)

        t5_circle_mask.generate_target()
        t5_circle_mask.target.set_fill(mask_invalid_circle_kwargs["fill_color"])

        t6_circle_mask.generate_target()
        t6_circle_mask.target.set_fill(mask_valid_circle_kwargs["fill_color"])

        self.play(
            m.Circumscribe(t5_circle_mask, color=RwthTheme.rwth_magenta_75),
            m.MoveToTarget(t5_circle),
            m.MoveToTarget(t5_circle_mask),
            m.MoveToTarget(t6_circle_mask),
            m.FadeIn(j1_t1),
        )

        t1_circle.generate_target()
        t1_circle.target.set_fill(C.GREEN_LIGHT)

        machine_edge_5_1 = m.Arrow(start=t5_circle, end=t1_circle, color=C.BLUE, **machine_arrow_kwargs)
        machine_edge_5_1_label = styled_text("5", color=C.BLUE).scale(0.425).move_to(
            machine_edge_5_1.get_center() + m.RIGHT * 0.25)

        t1_circle_mask.generate_target()
        t1_circle_mask.target.set_fill(mask_invalid_circle_kwargs["fill_color"])

        t2_circle_mask.generate_target()
        t2_circle_mask.target.set_fill(mask_valid_circle_kwargs["fill_color"])

        self.play(
            m.Circumscribe(t1_circle_mask, color=RwthTheme.rwth_magenta_75),
            m.MoveToTarget(t1_circle),
            m.Write(machine_edge_5_1),
            m.FadeIn(machine_edge_5_1_label),
            m.FadeIn(j0_t1),
            m.MoveToTarget(t1_circle_mask),
            m.MoveToTarget(t2_circle_mask),
        )


        t6_circle.generate_target()
        t6_circle.target.set_fill(C.GREEN_LIGHT)

        t6_circle_mask.generate_target()
        t6_circle_mask.target.set_fill(mask_invalid_circle_kwargs["fill_color"])

        t7_circle_mask.generate_target()
        t7_circle_mask.target.set_fill(mask_valid_circle_kwargs["fill_color"])

        self.play(
            m.Circumscribe(t6_circle_mask, color=RwthTheme.rwth_magenta_75),
            m.MoveToTarget(t6_circle),
            m.FadeIn(j1_t2),
            m.MoveToTarget(t6_circle_mask),
            m.MoveToTarget(t7_circle_mask),
        )


        t2_circle.generate_target()
        t2_circle.target.set_fill(C.GREEN_LIGHT)

        t2_circle_mask.generate_target()
        t2_circle_mask.target.set_fill(mask_invalid_circle_kwargs["fill_color"])

        t3_circle_mask.generate_target()
        t3_circle_mask.target.set_fill(mask_valid_circle_kwargs["fill_color"])

        self.play(
            m.Circumscribe(t2_circle_mask , color=RwthTheme.rwth_magenta_75),
            m.MoveToTarget(t2_circle),
            m.FadeIn(j0_t2),
            m.MoveToTarget(t2_circle_mask),
            m.MoveToTarget(t3_circle_mask),
        )


        t7_circle.generate_target()
        t7_circle.target.set_fill(C.GREEN_LIGHT)

        # update starting time indicator
        machine_edge_2_7 = m.Arrow(start=t2_circle, end=t7_circle, color=C.ORANGE_DARK, **machine_arrow_kwargs)
        machine_edge_2_7_label = styled_text("3", color=C.ORANGE_DARK).scale(0.425).move_to(
            machine_edge_2_7.get_center() + np.array([-0.25, 0.6, 0]))

        t7_circle_mask.generate_target()
        t7_circle_mask.target.set_fill(mask_invalid_circle_kwargs["fill_color"])

        t8_circle_mask.generate_target()
        t8_circle_mask.target.set_fill(mask_valid_circle_kwargs["fill_color"])

        self.play(
            m.Circumscribe(t7_circle_mask , color=RwthTheme.rwth_magenta_75),
            m.MoveToTarget(t7_circle),
            m.Write(machine_edge_2_7),
            m.FadeIn(machine_edge_2_7_label),
            m.FadeIn(j1_t3),
            m.MoveToTarget(t7_circle_mask),
            m.MoveToTarget(t8_circle_mask),
        )


        t3_circle.generate_target()
        t3_circle.target.set_fill(C.GREEN_LIGHT)

        machine_edge_6_3 = m.Arrow(start=t6_circle, end=t3_circle, color=C.GREEN, **machine_arrow_kwargs)
        machine_edge_6_3_label = styled_text("16", color=C.GREEN).scale(0.425).move_to(
            machine_edge_6_3.get_center() + np.array([-0.25, -0.6, 0]))

        t3_circle_mask.generate_target()
        t3_circle_mask.target.set_fill(mask_invalid_circle_kwargs["fill_color"])

        t4_circle_mask.generate_target()
        t4_circle_mask.target.set_fill(mask_valid_circle_kwargs["fill_color"])

        self.play(
            m.Circumscribe(t3_circle_mask , color=RwthTheme.rwth_magenta_75),
            m.MoveToTarget(t3_circle),
            m.Write(machine_edge_6_3),
            m.FadeIn(machine_edge_6_3_label),
            m.FadeIn(j0_t3),
            m.MoveToTarget(t3_circle_mask),
            m.MoveToTarget(t4_circle_mask),
        )


        t4_circle.generate_target()
        t4_circle.target.set_fill(C.GREEN_LIGHT)

        t4_circle_mask.generate_target()
        t4_circle_mask.target.set_fill(mask_invalid_circle_kwargs["fill_color"])

        self.play(
            m.Circumscribe(t4_circle_mask , color=RwthTheme.rwth_magenta_75),
            m.MoveToTarget(t4_circle),
            m.FadeIn(j0_t4),
            m.MoveToTarget(t4_circle_mask),
        )


        t8_circle.generate_target()
        t8_circle.target.set_fill(C.GREEN_LIGHT)

        t8_circle_mask.generate_target()
        t8_circle_mask.target.set_fill(mask_invalid_circle_kwargs["fill_color"])

        machine_edge_4_8 = m.Arrow(start=t4_circle, end=t8_circle, color=C.TEAL, **machine_arrow_kwargs)
        machine_edge_4_8_label = styled_text("12", color=C.TEAL).scale(0.425).move_to(
            machine_edge_4_8.get_center() + m.LEFT * 0.25)

        self.play(
            m.Circumscribe(t8_circle_mask , color=RwthTheme.rwth_magenta_75),
            m.MoveToTarget(t8_circle),
            m.FadeIn(j1_t4),
            m.MoveToTarget(t8_circle_mask),
            m.Write(machine_edge_4_8),
            m.FadeIn(machine_edge_4_8_label),
        )


        t1_circle_mask.generate_target()
        t1_circle_mask.target.set_fill(mask_valid_circle_kwargs["fill_color"])

        t5_circle_mask.generate_target()
        t5_circle_mask.target.set_fill(mask_valid_circle_kwargs["fill_color"])

        self.play(
            m.FadeOut(axes),
            m.FadeOut(job0_title),
            m.FadeOut(job1_title),
            m.FadeOut(machine_edge_5_1),
            m.FadeOut(machine_edge_5_1_label),
            m.FadeOut(machine_edge_2_7),
            m.FadeOut(machine_edge_2_7_label),
            m.FadeOut(machine_edge_6_3),
            m.FadeOut(machine_edge_6_3_label),
            m.FadeOut(machine_edge_4_8),
            m.FadeOut(machine_edge_4_8_label),
            m.FadeOut(j0_t1),
            m.FadeOut(j0_t2),
            m.FadeOut(j0_t3),
            m.FadeOut(j0_t4),
            m.FadeOut(j1_t1),
            m.FadeOut(j1_t2),
            m.FadeOut(j1_t3),
            m.FadeOut(j1_t4),
            m.Transform(graph, reset_graph),
            m.MoveToTarget(t1_circle_mask),
            m.MoveToTarget(t5_circle_mask),
        )


        action_space_tasks = m.Tex(r"$\mathcal{A}_{task}$", r"$\mathsf{\:= \{}$",
                                   r"$\:\mathsf{t_1}\:$", r"$,$",
                                   r"$\:\mathsf{t_2}\:$", r"$,$",
                                   r"$\:\mathsf{t_3}\:$", r"$,$",
                                   r"$\:\mathsf{t_4}\:$", r"$,$",
                                   r"$\:\mathsf{t_5}\:$", r"$,$",
                                   r"$\:\mathsf{t_6}\:$", r"$,$",
                                   r"$\:\mathsf{t_7}\:$", r"$,$",
                                   r"$\:\mathsf{t_8}\:$",
                                   r"$\mathsf{\}}$",
                                   color=C.DEFAULT_FONT
                                   ).scale(0.75)
        action_space_tasks.move_to(np.array([0, -1.25, 0]))

        action_space_job = m.Tex(r"$\mathcal{A}_{job}$", r"$\mathsf{\:= \{}$",
                                 r"$\:\mathsf{J_0}\:$", r"$,$",
                                 r"$\:\mathsf{J_1}\:$", r"$\mathsf{\}}$",
                                   color=C.DEFAULT_FONT).scale(0.75)
        action_space_job.move_to(np.array([0, -2.25, 0]))

        self.play(
            m.FadeIn(action_space_tasks),
            m.FadeIn(action_space_job),
        )


        self.play(
            *[m.Indicate(e, color=C.BLUE) for e in
              [t1_text, t2_text, t3_text, t4_text, t5_text, t6_text, t7_text, t8_text]],
            *[m.Indicate(e, color=C.BLUE) for e in [
                action_space_tasks[2],
                action_space_tasks[4],
                action_space_tasks[6],
                action_space_tasks[8],
                action_space_tasks[10],
                action_space_tasks[12],
                action_space_tasks[14],
                action_space_tasks[16],
            ]],
        )


        self.play(
            m.Indicate(action_space_job[2], color=RwthTheme.rwth_lila_75),
            m.Circumscribe(m.VGroup(t1_group, t4_group), color=RwthTheme.rwth_lila_75, buff=0.25),
            m.Indicate(action_space_job[4], color=RwthTheme.rwth_magenta_75),
            m.Circumscribe(m.VGroup(t5_group, t8_group), color=RwthTheme.rwth_magenta_75, buff=0.25),
        )


        for e in [
            action_space_tasks[4],
            action_space_tasks[6],
            action_space_tasks[8],
            action_space_tasks[12],
            action_space_tasks[14],
            action_space_tasks[16]]:
            e.generate_target()
            e.target.set_color(C.PINK)

        for e in [action_space_tasks[2],
                  action_space_tasks[10]]:
            e.generate_target()
            e.target.set_color(C.GREEN_DARK)

        for e in [action_space_job[2],
                  action_space_job[4]]:
            e.generate_target()
            e.target.set_color(C.GREEN_DARK)

        self.play(
            *[m.MoveToTarget(e) for e in [
                action_space_tasks[2], action_space_tasks[4], action_space_tasks[6], action_space_tasks[8],
                action_space_tasks[10], action_space_tasks[12], action_space_tasks[14], action_space_tasks[16]]
              ],
            *[m.MoveToTarget(e) for e in [action_space_job[2], action_space_job[4]]],
        )


        t5_circle.generate_target()
        t5_circle.target.set_fill(C.GREEN_LIGHT)

        t5_circle_mask.generate_target()
        t5_circle_mask.target.set_fill(mask_invalid_circle_kwargs["fill_color"])

        t6_circle_mask.generate_target()
        t6_circle_mask.target.set_fill(mask_valid_circle_kwargs["fill_color"])

        action_space_tasks[10].generate_target()
        action_space_tasks[10].target.set_color(C.PINK)

        action_space_tasks[12].generate_target()
        action_space_tasks[12].target.set_color(C.GREEN_DARK)

        self.play(
            m.Circumscribe(t5_circle_mask, color=RwthTheme.rwth_magenta_75),
            m.Circumscribe(action_space_tasks[10], color=RwthTheme.rwth_magenta_75),
            m.Circumscribe(action_space_job[4], color=RwthTheme.rwth_magenta_75),

            m.MoveToTarget(action_space_tasks[10]),
            m.MoveToTarget(action_space_tasks[12]),

            m.MoveToTarget(t5_circle),
            m.MoveToTarget(t5_circle_mask),
            m.MoveToTarget(t6_circle_mask),
        )


        t1_circle.generate_target()
        t1_circle.target.set_fill(C.GREEN_LIGHT)

        machine_edge_5_1 = m.Arrow(start=t5_circle, end=t1_circle, color=C.BLUE, **machine_arrow_kwargs)
        machine_edge_5_1_label = styled_text("5", color=C.BLUE).scale(0.425).move_to(
            machine_edge_5_1.get_center() + m.RIGHT * 0.25)

        t1_circle_mask.generate_target()
        t1_circle_mask.target.set_fill(mask_invalid_circle_kwargs["fill_color"])

        t2_circle_mask.generate_target()
        t2_circle_mask.target.set_fill(mask_valid_circle_kwargs["fill_color"])

        action_space_tasks[2].generate_target()
        action_space_tasks[2].target.set_color(C.PINK)

        action_space_tasks[4].generate_target()
        action_space_tasks[4].target.set_color(C.GREEN_DARK)

        self.play(
            m.Circumscribe(t1_circle_mask, color=RwthTheme.rwth_magenta_75),
            m.Circumscribe(action_space_tasks[2], color=RwthTheme.rwth_magenta_75),
            m.Circumscribe(action_space_job[2], color=RwthTheme.rwth_magenta_75),

            m.MoveToTarget(action_space_tasks[2]),
            m.MoveToTarget(action_space_tasks[4]),

            m.MoveToTarget(t1_circle),
            m.Write(machine_edge_5_1),
            m.FadeIn(machine_edge_5_1_label),
            m.MoveToTarget(t1_circle_mask),
            m.MoveToTarget(t2_circle_mask),
        )


        t6_circle.generate_target()
        t6_circle.target.set_fill(C.GREEN_LIGHT)

        t6_circle_mask.generate_target()
        t6_circle_mask.target.set_fill(mask_invalid_circle_kwargs["fill_color"])

        t7_circle_mask.generate_target()
        t7_circle_mask.target.set_fill(mask_valid_circle_kwargs["fill_color"])

        action_space_tasks[12].generate_target()
        action_space_tasks[12].target.set_color(C.PINK)

        action_space_tasks[14].generate_target()
        action_space_tasks[14].target.set_color(C.GREEN_DARK)

        self.play(
            m.Circumscribe(t6_circle_mask, color=RwthTheme.rwth_magenta_75),
            m.Circumscribe(action_space_tasks[12], color=RwthTheme.rwth_magenta_75),
            m.Circumscribe(action_space_job[4], color=RwthTheme.rwth_magenta_75),

            m.MoveToTarget(action_space_tasks[12]),
            m.MoveToTarget(action_space_tasks[14]),
            m.MoveToTarget(t6_circle),
            m.MoveToTarget(t6_circle_mask),
            m.MoveToTarget(t7_circle_mask),
        )


        t2_circle.generate_target()
        t2_circle.target.set_fill(C.GREEN_LIGHT)

        t2_circle_mask.generate_target()
        t2_circle_mask.target.set_fill(mask_invalid_circle_kwargs["fill_color"])

        t3_circle_mask.generate_target()
        t3_circle_mask.target.set_fill(mask_valid_circle_kwargs["fill_color"])

        action_space_tasks[4].generate_target()
        action_space_tasks[4].target.set_color(C.PINK)

        action_space_tasks[6].generate_target()
        action_space_tasks[6].target.set_color(C.GREEN_DARK)

        self.play(
            m.Circumscribe(t2_circle_mask, color=RwthTheme.rwth_magenta_75),
            m.Circumscribe(action_space_tasks[4], color=RwthTheme.rwth_magenta_75),
            m.Circumscribe(action_space_job[2], color=RwthTheme.rwth_magenta_75),

            m.MoveToTarget(action_space_tasks[4]),
            m.MoveToTarget(action_space_tasks[6]),

            m.MoveToTarget(t2_circle),
            m.MoveToTarget(t2_circle_mask),
            m.MoveToTarget(t3_circle_mask),
        )


        t7_circle.generate_target()
        t7_circle.target.set_fill(C.GREEN_LIGHT)

        # update starting time indicator
        machine_edge_2_7 = m.Arrow(start=t2_circle, end=t7_circle, color=C.ORANGE_DARK, **machine_arrow_kwargs)
        machine_edge_2_7_label = styled_text("3", color=C.ORANGE_DARK).scale(0.425).move_to(
            machine_edge_2_7.get_center() + np.array([-0.25, 0.6, 0]))

        t7_circle_mask.generate_target()
        t7_circle_mask.target.set_fill(mask_invalid_circle_kwargs["fill_color"])

        t8_circle_mask.generate_target()
        t8_circle_mask.target.set_fill(mask_valid_circle_kwargs["fill_color"])

        action_space_tasks[14].generate_target()
        action_space_tasks[14].target.set_color(C.PINK)

        action_space_tasks[16].generate_target()
        action_space_tasks[16].target.set_color(C.GREEN_DARK)

        self.play(
            m.Circumscribe(t7_circle_mask, color=RwthTheme.rwth_magenta_75),
            m.Circumscribe(action_space_tasks[14] , color=RwthTheme.rwth_magenta_75),
            m.Circumscribe(action_space_job[4], color=RwthTheme.rwth_magenta_75),

            m.MoveToTarget(action_space_tasks[14]),
            m.MoveToTarget(action_space_tasks[16]),

            m.MoveToTarget(t7_circle),
            m.Write(machine_edge_2_7),
            m.FadeIn(machine_edge_2_7_label),
            m.MoveToTarget(t7_circle_mask),
            m.MoveToTarget(t8_circle_mask),
        )


        t3_circle.generate_target()
        t3_circle.target.set_fill(C.GREEN_LIGHT)

        machine_edge_6_3 = m.Arrow(start=t6_circle, end=t3_circle, color=C.GREEN, **machine_arrow_kwargs)
        machine_edge_6_3_label = styled_text("16", color=C.GREEN).scale(0.425).move_to(
            machine_edge_6_3.get_center() + np.array([-0.25, -0.6, 0]))

        t3_circle_mask.generate_target()
        t3_circle_mask.target.set_fill(mask_invalid_circle_kwargs["fill_color"])

        t4_circle_mask.generate_target()
        t4_circle_mask.target.set_fill(mask_valid_circle_kwargs["fill_color"])

        action_space_tasks[6].generate_target()
        action_space_tasks[6].target.set_color(C.PINK)

        action_space_tasks[8].generate_target()
        action_space_tasks[8].target.set_color(C.GREEN_DARK)

        self.play(
            m.Circumscribe(t3_circle_mask , color=RwthTheme.rwth_magenta_75),
            m.Circumscribe(action_space_tasks[6] , color=RwthTheme.rwth_magenta_75),
            m.Circumscribe(action_space_job[2] , color=RwthTheme.rwth_magenta_75),

            m.MoveToTarget(action_space_tasks[6]),
            m.MoveToTarget(action_space_tasks[8]),

            m.MoveToTarget(t3_circle),
            m.Write(machine_edge_6_3),
            m.FadeIn(machine_edge_6_3_label),
            m.MoveToTarget(t3_circle_mask),
            m.MoveToTarget(t4_circle_mask),
        )


        t4_circle.generate_target()
        t4_circle.target.set_fill(C.GREEN_LIGHT)

        t4_circle_mask.generate_target()
        t4_circle_mask.target.set_fill(mask_invalid_circle_kwargs["fill_color"])

        action_space_tasks[8].generate_target()
        action_space_tasks[8].target.set_color(C.PINK)

        action_space_job[2].generate_target()
        action_space_job[2].target.set_color(C.PINK)

        self.play(
            m.Circumscribe(t4_circle_mask , color=RwthTheme.rwth_magenta_75),
            m.Circumscribe(action_space_tasks[8] , color=RwthTheme.rwth_magenta_75),
            m.Circumscribe(action_space_job[2] , color=RwthTheme.rwth_magenta_75),

            m.MoveToTarget(action_space_tasks[8]),
            m.MoveToTarget(action_space_job[2]),

            m.MoveToTarget(t4_circle),
            m.MoveToTarget(t4_circle_mask),
        )


        t8_circle.generate_target()
        t8_circle.target.set_fill(C.GREEN_LIGHT)

        t8_circle_mask.generate_target()
        t8_circle_mask.target.set_fill(mask_invalid_circle_kwargs["fill_color"])

        machine_edge_4_8 = m.Arrow(start=t4_circle, end=t8_circle, color=C.TEAL, **machine_arrow_kwargs)
        machine_edge_4_8_label = styled_text("12", color=C.TEAL).scale(0.425).move_to(
            machine_edge_4_8.get_center() + m.LEFT * 0.25)

        action_space_tasks[16].generate_target()
        action_space_tasks[16].target.set_color(C.PINK)

        action_space_job[4].generate_target()
        action_space_job[4].target.set_color(C.PINK)

        self.play(
            m.Circumscribe(t8_circle_mask, color=RwthTheme.rwth_magenta_75),
            m.Circumscribe(action_space_tasks[16], color=RwthTheme.rwth_magenta_75),
            m.Circumscribe(action_space_job[4], color=RwthTheme.rwth_magenta_75),

            m.MoveToTarget(action_space_tasks[16]),
            m.MoveToTarget(action_space_job[4]),

            m.MoveToTarget(t8_circle),
            m.MoveToTarget(t8_circle_mask),
            m.Write(machine_edge_4_8),
            m.FadeIn(machine_edge_4_8_label),
        )

        self.play(
            self.overlay_scene()
        )



if __name__ == '__main__':
    EIopRlActionSpace.save_sections_without_cache()