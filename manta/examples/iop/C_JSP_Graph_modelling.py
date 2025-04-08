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

    GREY_DARK: str = "#1A1C1F"
    GREY_DARK_LIGHT: str = "#212328"
    GREY_OUTLINE: str = "#34373C"  # same as GREY_ICON_BACKGROUND

    GREY: str = "#242629"
    GREY_CHART_BACKGROUND: str = "#212121"
    GREY_ICON_BACKGROUND: str = "#35373C"

    GREY_ICON: str = "#909194"

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

    logo_paths = [
        "iop_logo.png"
    ]
    logo_height = 0.6
    index_prefix = "D "

def styled_text(t, **kwargs):
    default_params = {
        "font": "Iosevka Nerd Font",
        "color": C.DEFAULT_FONT
    }
    params = {**default_params, **kwargs}
    return m.Text(t, **params)

class C_IopGraphModellingIntro(RwthTheme, AxesUtils, GanttUtils, RwthSlideTemplate):

    # font_name = "IosevkaTermSlab Nerd Font Mono"

    logo_paths = [
        "iop_logo.png"
    ]
    logo_height = 0.6
    index_prefix = "C "

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
                title="Job Shop Scheduling",
                seperator=": ",
                subtitle="Modelling Approach"
            ),
            self.add_logos(),
            self.add_seperator_line_top(),
            self.add_seperator_line_bottom()
        )

        job0 = m.RoundedRectangle(
            corner_radius=0.125,
            height=2.625,
            width=5.5,
            fill_color=self.background_color,
            fill_opacity=1.0,
            stroke_color=self.outline_color,
            stroke_width=1.0
        )
        job1 = m.RoundedRectangle(
            corner_radius=0.125,
            height=2.625,
            width=5.5,
            fill_color=self.background_color,
            fill_opacity=1.0,
            stroke_color=self.outline_color,
            stroke_width=1.0
        )

        x_shift = 3.5
        job0.move_to(x_shift * m.LEFT + 1.5 * m.UP)
        job1.move_to(x_shift * m.RIGHT + 1.5 * m.UP)

        hammer_m1_name = styled_text("Band Saw", color=C.BLUE)
        hammer_m2_name = styled_text("Drill Press", color=C.ORANGE_DARK)
        hammer_m3_name = styled_text("Milling Machine", color=C.GREEN)
        hammer_m4_name = styled_text("Grinding Machine", color=C.TEAL)

        hammer_m1_dur = styled_text("11 min", color=C.BLUE)
        hammer_m2_dur = styled_text("3 min", color=C.ORANGE_DARK)
        hammer_m3_dur = styled_text("3 min", color=C.GREEN)
        hammer_m4_dur = styled_text("12 min", color=C.TEAL)

        hammer_m1_order = styled_text("1.", color=C.BLUE)
        hammer_m2_order = styled_text("2.", color=C.ORANGE_DARK)
        hammer_m3_order = styled_text("3.", color=C.GREEN)
        hammer_m4_order = styled_text("4.", color=C.TEAL)

        job0_table = m.MobjectTable(
            [[hammer_m1_order, hammer_m1_name, hammer_m1_dur],
             [hammer_m2_order, hammer_m2_name, hammer_m2_dur],
             [hammer_m3_order, hammer_m3_name, hammer_m3_dur],
             [hammer_m4_order, hammer_m4_name, hammer_m4_dur]],
            v_buff=0.375
        ).scale_to_fit_width(5.5).move_to(job0.get_center())
        job0_table.remove(*job0_table.get_vertical_lines())
        job0_table.remove(*job0_table.get_horizontal_lines())

        table_y_shift = hammer_m4_order.get_bottom()[1] - hammer_m4_name.get_bottom()[1]
        hammer_m3_name.shift(table_y_shift * m.DOWN)
        hammer_m4_name.shift(table_y_shift * m.DOWN)

        job0_title = styled_text("Job 0").scale(0.5)
        job0_title.move_to(job0.get_top())

        job0_title_rectangle = m.RoundedRectangle(
            corner_radius=0.125,
            height=3.0,
            width=5.5,
            fill_color=self.background_color,
            fill_opacity=1.0,
            stroke_color=self.outline_color,
            stroke_width=1.0
        ).scale_to_fit_height(job0_title.height + 0.5).move_to(job0_title.get_center())

        NMM_m1_name = styled_text("Band Saw", color=C.BLUE)
        NMM_m2_name = styled_text("Milling Machine", color=C.GREEN)
        NMM_m3_name = styled_text("Drill Press", color=C.ORANGE_DARK)
        NMM_m4_name = styled_text("Grinding Machine", color=C.TEAL)

        NMM_m1_dur = styled_text("5 min", color=C.BLUE)
        NMM_m2_dur = styled_text("16 min", color=C.GREEN)
        NMM_m3_dur = styled_text("7 min", color=C.ORANGE_DARK)
        NMM_m4_dur = styled_text("4 min", color=C.TEAL)

        NMM_m1_order = styled_text("1.", color=C.BLUE)
        NMM_m2_order = styled_text("2.", color=C.GREEN)
        NMM_m3_order = styled_text("3.", color=C.ORANGE_DARK)
        NMM_m4_order = styled_text("4.", color=C.TEAL)

        job1_table = m.MobjectTable(
            [[NMM_m1_order, NMM_m1_name, NMM_m1_dur],
             [NMM_m2_order, NMM_m2_name, NMM_m2_dur],
             [NMM_m3_order, NMM_m3_name, NMM_m3_dur],
             [NMM_m4_order, NMM_m4_name, NMM_m4_dur]],
            v_buff=0.375
        ).scale_to_fit_width(5.5).move_to(job1.get_center())
        job1_table.remove(*job1_table.get_vertical_lines())
        job1_table.remove(*job1_table.get_horizontal_lines())

        NMM_m4_name.shift(table_y_shift * m.DOWN)

        job1_title = styled_text("Job 1").scale(0.5)
        job1_title.move_to(job1.get_top())

        job1_title_rectangle = m.RoundedRectangle(
            corner_radius=0.125,
            height=3.0,
            width=5.5,
            fill_color=self.background_color,
            fill_opacity=1.0,
            stroke_color=self.outline_color,
            stroke_width=1.0
        ).scale_to_fit_height(job1_title.height + 0.5).move_to(job1_title.get_center())

        m.VGroup(
            job0,
            job0_table,
            job0_title_rectangle,
            job0_title,
        ).scale(0.75)

        m.VGroup(
            job1,
            job1_table,
            job1_title_rectangle,
            job1_title,
        ).scale(0.75)

        self.play(
            m.Write(job0),
            m.FadeIn(job0_table),
            m.FadeIn(job0_title_rectangle),
            m.Write(job0_title),

            m.Write(job1),
            m.FadeIn(job1_table),
            m.FadeIn(job1_title_rectangle),
            m.Write(job1_title),
        )

        t1_text_table = styled_text("Task 1", color=C.BLUE).scale_to_fit_height(hammer_m1_order.height) \
            .move_to(hammer_m1_order.get_center()).shift(m.RIGHT * 0.25)
        t2_text_table = styled_text("Task 2", color=C.ORANGE_DARK).scale_to_fit_height(hammer_m1_order.height) \
            .move_to(hammer_m2_order.get_center()).shift(m.RIGHT * 0.25)
        t3_text_table = styled_text("Task 3", color=C.GREEN).scale_to_fit_height(hammer_m1_order.height) \
            .move_to(hammer_m3_order.get_center()).shift(m.RIGHT * 0.25)
        t4_text_table = styled_text("Task 4", color=C.TEAL).scale_to_fit_height(hammer_m1_order.height) \
            .move_to(hammer_m4_order.get_center()).shift(m.RIGHT * 0.25)

        hammer_names = [hammer_m1_name, hammer_m2_name, hammer_m3_name, hammer_m4_name]
        for obj in hammer_names:
            obj.generate_target()
            obj.target.shift(m.RIGHT * 0.25)

        self.play(
            m.Transform(hammer_m1_order, t1_text_table),
            m.Transform(hammer_m2_order, t2_text_table),
            m.Transform(hammer_m3_order, t3_text_table),
            m.Transform(hammer_m4_order, t4_text_table),
            *[m.MoveToTarget(obj) for obj in hammer_names]
        )

        t5_text_table = styled_text("Task 5", color=C.BLUE).scale_to_fit_height(hammer_m1_order.height).move_to(
            NMM_m1_order.get_center()).shift(m.RIGHT * 0.25)
        t6_text_table = styled_text("Task 6", color=C.GREEN).scale_to_fit_height(hammer_m1_order.height).move_to(
            NMM_m2_order.get_center()).shift(m.RIGHT * 0.25)
        t7_text_table = styled_text("Task 7", color=C.ORANGE_DARK).scale_to_fit_height(hammer_m1_order.height).move_to(
            NMM_m3_order.get_center()).shift(m.RIGHT * 0.25)
        t8_text_table = styled_text("Task 8", color=C.TEAL).scale_to_fit_height(hammer_m1_order.height).move_to(
            NMM_m4_order.get_center()).shift(m.RIGHT * 0.25)

        NMM_names = [NMM_m1_name, NMM_m2_name, NMM_m3_name, NMM_m4_name]
        for obj in NMM_names:
            obj.generate_target()
            obj.target.shift(m.RIGHT * 0.25)

        self.play(
            m.Transform(NMM_m1_order, t5_text_table),
            m.Transform(NMM_m2_order, t6_text_table),
            m.Transform(NMM_m3_order, t7_text_table),
            m.Transform(NMM_m4_order, t8_text_table),
            *[m.MoveToTarget(obj) for obj in NMM_names]
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
        row1_y = -0.75
        row2_y = -2.75

        t1_circle = m.Circle(stroke_color=C.YELLOW, **task_circle_kwargs)
        t1_text = m.Tex(r"$\mathtt{t_1}$", color=C.GREY_DARK).scale(0.5)
        t1_group = m.VGroup(t1_circle, t1_text)
        t1_group.move_to(np.array([-3, row1_y, 0]))

        t2_circle = m.Circle(stroke_color=C.YELLOW, **task_circle_kwargs)
        t2_text = m.Tex(r"$\mathtt{t_2}$", color=C.GREY_DARK).scale(0.5)
        t2_group = m.VGroup(t2_circle, t2_text)
        t2_group.move_to(np.array([-1, row1_y, 0]))

        t3_circle = m.Circle(stroke_color=C.YELLOW, **task_circle_kwargs)
        t3_text = m.Tex(r"$\mathtt{t_3}$", color=C.GREY_DARK).scale(0.5)
        t3_group = m.VGroup(t3_circle, t3_text)
        t3_group.move_to(np.array([1, row1_y, 0]))

        t4_circle = m.Circle(stroke_color=C.YELLOW, **task_circle_kwargs)
        t4_text = m.Tex(r"$\mathtt{t_4}$", color=C.GREY_DARK).scale(0.5)
        t4_group = m.VGroup(t4_circle, t4_text)
        t4_group.move_to(np.array([3, row1_y, 0]))


        t5_circle = m.Circle(stroke_color=C.YELLOW, **task_circle_kwargs)
        t5_text = m.Tex(r"$\mathtt{t_5}$", color=C.GREY_DARK).scale(0.5)
        t5_group = m.VGroup(t5_circle, t5_text)
        t5_group.move_to(np.array([-3, row2_y, 0]))

        t6_circle = m.Circle(stroke_color=C.YELLOW, **task_circle_kwargs)
        t6_text = m.Tex(r"$\mathtt{t_6}$", color=C.GREY_DARK).scale(0.5)
        t6_group = m.VGroup(t6_circle, t6_text)
        t6_group.move_to(np.array([-1, row2_y, 0]))

        t7_circle = m.Circle(stroke_color=C.YELLOW, **task_circle_kwargs)
        t7_text = m.Tex(r"$\mathtt{t_7}$", color=C.GREY_DARK).scale(0.5)
        t7_group = m.VGroup(t7_circle, t7_text)
        t7_group.move_to(np.array([1, row2_y, 0]))

        t8_circle = m.Circle(stroke_color=C.YELLOW, **task_circle_kwargs)
        t8_text = m.Tex(r"$\mathtt{t_8}$", color=C.GREY_DARK).scale(0.5)
        t8_group = m.VGroup(t8_circle, t8_text)
        t8_group.move_to(np.array([3, row2_y, 0]))

        # add fictions nodes
        t0_circle = m.Circle(stroke_color=C.DARK_FONT, **fictive_task_circle_kwargs)
        t0_text = m.Tex(r"$\mathtt{t_0}$", color=C.GREY_DARK).scale(0.5)
        t0_group = m.VGroup(t0_circle, t0_text)
        t0_group.move_to(np.array([-4.5, (row1_y + row2_y) * 0.5, 0]))

        t9_circle = m.Circle(stroke_color=C.DARK_FONT, **fictive_task_circle_kwargs)
        t9_text = m.Tex(r"$\mathsf{t_*}$", color=C.GREY_DARK).scale(0.5)
        t9_group = m.VGroup(t9_circle, t9_text)
        t9_group.move_to(np.array([4.5, (row1_y + row2_y) * 0.5, 0]))

        m.VGroup(
            t0_group,
            t1_group,
            t2_group,
            t3_group,
            t4_group,
            t5_group,
            t6_group,
            t7_group,
            t8_group,
            t9_group
        ).scale(0.725).shift(m.UP * 0.5)

        temp_group1 = m.VGroup(
            t1_text.copy(),
            t2_text.copy(),
            t3_text.copy(),
            t4_text.copy(),
        )
        temp_group1.z_index = 500
        self.add(temp_group1)
        self.play(
            m.Write(t1_group),
            m.Transform(t1_text_table, t1_text),
            m.Write(t2_group),
            m.Transform(t2_text_table, t2_text),
            m.Write(t3_group),
            m.Transform(t3_text_table, t3_text),
            m.Write(t4_group),
            m.Transform(t4_text_table, t4_text),
        )

        temp_group2 = m.VGroup(
            t5_text.copy(),
            t6_text.copy(),
            t7_text.copy(),
            t8_text.copy(),
        )
        temp_group2.z_index = 500
        self.add(temp_group2)

        self.play(
            m.Write(t5_group),
            m.Transform(t5_text_table, t5_text),
            m.Write(t6_group),
            m.Transform(t6_text_table, t6_text),
            m.Write(t7_group),
            m.Transform(t7_text_table, t7_text),
            m.Write(t8_group),
            m.Transform(t8_text_table, t8_text),
        )

        # color the circles
        t1_circle.generate_target()
        t1_circle.target.stroke_color = C.BLUE
        t1_circle_empty = t1_circle.copy().set_fill(C.GREY_DARK, opacity=0.0).set_stroke(C.BLUE)

        t2_circle.generate_target()
        t2_circle.target.stroke_color = C.ORANGE_DARK
        t2_circle_empty = t2_circle.copy().set_fill(C.GREY_DARK, opacity=0.0).set_stroke(C.ORANGE_DARK)

        t3_circle.generate_target()
        t3_circle.target.stroke_color = C.GREEN
        t3_circle_empty = t3_circle.copy().set_fill(C.GREY_DARK, opacity=0.0).set_stroke(C.GREEN)

        t4_circle.generate_target()
        t4_circle.target.stroke_color = C.TEAL
        t4_circle_empty = t4_circle.copy().set_fill(C.GREY_DARK, opacity=0.0).set_stroke(C.TEAL)

        t5_circle.generate_target()
        t5_circle.target.stroke_color = C.BLUE
        t5_circle_empty = t5_circle.copy().set_fill(C.GREY_DARK, opacity=0.0).set_stroke(C.BLUE)

        t6_circle.generate_target()
        t6_circle.target.stroke_color = C.GREEN
        t6_circle_empty = t6_circle.copy().set_fill(C.GREY_DARK, opacity=0.0).set_stroke(C.GREEN)

        t7_circle.generate_target()
        t7_circle.target.stroke_color = C.ORANGE_DARK
        t7_circle_empty = t7_circle.copy().set_fill(C.GREY_DARK, opacity=0.0).set_stroke(C.ORANGE_DARK)

        t8_circle.generate_target()
        t8_circle.target.stroke_color = C.TEAL
        t8_circle_empty = t8_circle.copy().set_fill(C.GREY_DARK, opacity=0.0).set_stroke(C.TEAL)

        # todo: replace copies and remove them properly after animation
        self.play(
            m.MoveToTarget(t1_circle),
            m.Transform(hammer_m1_name.copy(), t1_circle_empty, replace_mobject_with_target_in_scene=False),
            m.MoveToTarget(t2_circle),
            m.Transform(hammer_m2_name.copy(), t2_circle_empty, replace_mobject_with_target_in_scene=False),
            m.MoveToTarget(t3_circle),
            m.Transform(hammer_m3_name.copy(), t3_circle_empty, replace_mobject_with_target_in_scene=False),
            m.MoveToTarget(t4_circle),
            m.Transform(hammer_m4_name.copy(), t4_circle_empty, replace_mobject_with_target_in_scene=False),

            m.MoveToTarget(t5_circle),
            m.Transform(NMM_m1_name.copy(), t5_circle_empty, replace_mobject_with_target_in_scene=False),
            m.MoveToTarget(t6_circle),
            m.Transform(NMM_m2_name.copy(), t6_circle_empty, replace_mobject_with_target_in_scene=False),
            m.MoveToTarget(t7_circle),
            m.Transform(NMM_m3_name.copy(), t7_circle_empty, replace_mobject_with_target_in_scene=False),
            m.MoveToTarget(t8_circle),
            m.Transform(NMM_m4_name.copy(), t8_circle_empty, replace_mobject_with_target_in_scene=False),
        )

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

        self.play(
            *[
                m.Write(job_edge) for job_edge in [job_edge_1_2, job_edge_2_3, job_edge_3_4, job_edge_5_6,
                                                   job_edge_6_7, job_edge_7_8]
            ]
        )



        job_edge_0_1 = m.Arrow(start=t0_circle, end=t1_circle, **job_arrow_kwargs)
        job_edge_0_5 = m.Arrow(start=t0_circle, end=t5_circle, **job_arrow_kwargs)

        job_edge_4_9 = m.Arrow(start=t4_circle, end=t9_circle, **job_arrow_kwargs)
        job_edge_8_9 = m.Arrow(start=t8_circle, end=t9_circle, **job_arrow_kwargs)

        self.play(
            m.Write(t0_group),
            m.Write(t9_group),
            *[
                m.Write(job_edge) for job_edge in [job_edge_0_1, job_edge_0_5, job_edge_4_9, job_edge_8_9]
            ]
        )

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

        hammer_m1_dur_copy = hammer_m1_dur[0:2].copy()
        hammer_m2_dur_copy = hammer_m2_dur[:1].copy()
        hammer_m3_dur_copy = hammer_m3_dur[:1].copy()
        hammer_m4_dur_copy = hammer_m4_dur[:2].copy()

        NMM_m1_dur_copy = NMM_m1_dur[:1].copy()
        NMM_m2_dur_copy = NMM_m2_dur[:2].copy()
        NMM_m3_dur_copy = NMM_m3_dur[:1].copy()
        NMM_m4_dur_copy = NMM_m4_dur[:1].copy()

        self.play(
            m.Transform(hammer_m1_dur_copy, job_edge_1_2_label),
            m.Transform(hammer_m2_dur_copy, job_edge_2_3_label),
            m.Transform(hammer_m3_dur_copy, job_edge_3_4_label),
            m.Transform(hammer_m4_dur_copy, job_edge_4_9_label),

            m.Transform(NMM_m1_dur_copy, job_edge_5_6_label),
            m.Transform(NMM_m2_dur_copy, job_edge_6_7_label),
            m.Transform(NMM_m3_dur_copy, job_edge_7_8_label),
            m.Transform(NMM_m4_dur_copy, job_edge_8_9_label)
        )

        # add labels for src task
        self.play(
            m.Write(job_edge_0_1_label),
            m.Write(job_edge_0_5_label),
        )

        hammer_m1_dur_rect = m.SurroundingRectangle(hammer_m1_dur, buff=.1, color=C.YELLOW)
        NMM_m1_dur_rect = m.SurroundingRectangle(NMM_m1_dur, buff=.1, color=C.PINK)

        self.play(
            m.Create(hammer_m1_dur_rect),
            m.Create(NMM_m1_dur_rect),
        )

        job_edge_1_2_label_rect = m.SurroundingRectangle(job_edge_1_2_label, buff=.1, color=C.YELLOW)
        job_edge_5_6_label_rect = m.SurroundingRectangle(job_edge_5_6_label, buff=.1, color=C.PINK)

        self.play(
            m.Create(job_edge_1_2_label_rect),
            m.Create(job_edge_5_6_label_rect),
        )

        hammer_m2_dur_rect = m.SurroundingRectangle(hammer_m2_dur, buff=.1, color=C.YELLOW)
        job_edge_2_3_label_rect = m.SurroundingRectangle(job_edge_2_3_label, buff=.1, color=C.YELLOW)

        NMM_m2_dur_rect = m.SurroundingRectangle(NMM_m2_dur, buff=.1, color=C.PINK)
        job_edge_6_7_label_rect = m.SurroundingRectangle(job_edge_6_7_label, buff=.1, color=C.PINK)

        self.play(
            m.ReplacementTransform(hammer_m1_dur_rect, hammer_m2_dur_rect),
            m.ReplacementTransform(job_edge_1_2_label_rect, job_edge_2_3_label_rect),

            m.ReplacementTransform(NMM_m1_dur_rect, NMM_m2_dur_rect),
            m.ReplacementTransform(job_edge_5_6_label_rect, job_edge_6_7_label_rect),
        )

        hammer_m3_dur_rect = m.SurroundingRectangle(hammer_m3_dur, buff=.1, color=C.YELLOW)
        job_edge_3_4_label_rect = m.SurroundingRectangle(job_edge_3_4_label, buff=.1, color=C.YELLOW)

        NMM_m3_dur_rect = m.SurroundingRectangle(NMM_m3_dur, buff=.1, color=C.PINK)
        job_edge_7_8_label_rect = m.SurroundingRectangle(job_edge_7_8_label, buff=.1, color=C.PINK)

        self.play(
            m.ReplacementTransform(hammer_m2_dur_rect, hammer_m3_dur_rect),
            m.ReplacementTransform(job_edge_2_3_label_rect, job_edge_3_4_label_rect),

            m.ReplacementTransform(NMM_m2_dur_rect, NMM_m3_dur_rect),
            m.ReplacementTransform(job_edge_6_7_label_rect, job_edge_7_8_label_rect),
        )

        hammer_m4_dur_rect = m.SurroundingRectangle(hammer_m4_dur, buff=.1, color=C.YELLOW)
        job_edge_4_9_label_rect = m.SurroundingRectangle(job_edge_4_9_label, buff=.1, color=C.YELLOW)

        NMM_m4_dur_rect = m.SurroundingRectangle(NMM_m4_dur, buff=.1, color=C.PINK)
        job_edge_8_9_label_rect = m.SurroundingRectangle(job_edge_8_9_label, buff=.1, color=C.PINK)

        self.play(
            m.ReplacementTransform(hammer_m3_dur_rect, hammer_m4_dur_rect),
            m.ReplacementTransform(job_edge_3_4_label_rect, job_edge_4_9_label_rect),

            m.ReplacementTransform(NMM_m3_dur_rect, NMM_m4_dur_rect),
            m.ReplacementTransform(job_edge_7_8_label_rect, job_edge_8_9_label_rect),
        )

        self.play(
            m.Uncreate(hammer_m4_dur_rect),
            m.Uncreate(job_edge_4_9_label_rect),

            m.Uncreate(NMM_m4_dur_rect),
            m.Uncreate(job_edge_8_9_label_rect),
        )

        # fade out job boxes and create rectangles for the tasks

        # table to rects
        rect_scale = 0.05
        hammer_m1_rect = m.Rectangle(width=11, height=5, color=C.BLUE, fill_opacity=1) \
            .scale(rect_scale) \
            .move_to(hammer_m1_name.get_center())
        hammer_m2_rect = m.Rectangle(width=3, height=5, color=C.ORANGE_DARK, fill_opacity=1) \
            .scale(rect_scale) \
            .move_to(hammer_m2_name.get_center())
        hammer_m3_rect = m.Rectangle(width=3, height=5, color=C.GREEN, fill_opacity=1) \
            .scale(rect_scale) \
            .move_to(hammer_m3_name.get_center())
        hammer_m4_rect = m.Rectangle(width=12, height=5, color=C.TEAL, fill_opacity=1) \
            .scale(rect_scale) \
            .move_to(hammer_m4_name.get_center())

        NMM_m1_rect = m.Rectangle(width=5, height=5, color=C.BLUE, fill_opacity=1) \
            .scale(rect_scale) \
            .move_to(NMM_m1_name.get_center())
        NMM_m2_rect = m.Rectangle(width=16, height=5, color=C.GREEN, fill_opacity=1) \
            .scale(rect_scale) \
            .move_to(NMM_m2_name.get_center())
        NMM_m3_rect = m.Rectangle(width=7, height=5, color=C.ORANGE_DARK, fill_opacity=1) \
            .scale(rect_scale) \
            .move_to(NMM_m3_name.get_center())
        NMM_m4_rect = m.Rectangle(width=4, height=5, color=C.TEAL, fill_opacity=1) \
            .scale(rect_scale) \
            .move_to(NMM_m4_name.get_center())

        self.play(
            m.FadeOut(job0),
            m.FadeOut(job1),

            m.FadeOut(job0_title_rectangle),
            m.FadeOut(job1_title_rectangle),

            m.Transform(hammer_m1_name, hammer_m1_rect, replace_mobject_with_target_in_scene=True),
            m.Transform(hammer_m2_name, hammer_m2_rect, replace_mobject_with_target_in_scene=True),
            m.Transform(hammer_m3_name, hammer_m3_rect, replace_mobject_with_target_in_scene=True),
            m.Transform(hammer_m4_name, hammer_m4_rect, replace_mobject_with_target_in_scene=True),

            m.Transform(NMM_m1_name, NMM_m1_rect, replace_mobject_with_target_in_scene=True),
            m.Transform(NMM_m2_name, NMM_m2_rect, replace_mobject_with_target_in_scene=True),
            m.Transform(NMM_m3_name, NMM_m3_rect, replace_mobject_with_target_in_scene=True),
            m.Transform(NMM_m4_name, NMM_m4_rect, replace_mobject_with_target_in_scene=True),

            m.FadeOut(hammer_m1_order),
            m.FadeOut(hammer_m2_order),
            m.FadeOut(hammer_m3_order),
            m.FadeOut(hammer_m4_order),

            m.FadeOut(hammer_m1_dur),
            m.FadeOut(hammer_m2_dur),
            m.FadeOut(hammer_m3_dur),
            m.FadeOut(hammer_m4_dur),

            m.FadeOut(NMM_m1_dur),
            m.FadeOut(NMM_m2_dur),
            m.FadeOut(NMM_m3_dur),
            m.FadeOut(NMM_m4_dur),

            m.FadeOut(NMM_m1_order),
            m.FadeOut(NMM_m2_order),
            m.FadeOut(NMM_m3_order),
            m.FadeOut(NMM_m4_order),
        )

        # move rects to nodes
        buff = 0.25
        hammer_m1_rect.generate_target()
        hammer_m2_rect.generate_target()
        hammer_m3_rect.generate_target()
        hammer_m4_rect.generate_target()

        hammer_m1_rect.target.next_to(t1_group, m.UP, buff=buff)
        hammer_m2_rect.target.next_to(t2_group, m.UP, buff=buff)
        hammer_m3_rect.target.next_to(t3_group, m.UP, buff=buff)
        hammer_m4_rect.target.next_to(t4_group, m.UP, buff=buff)

        NMM_m1_rect.generate_target()
        NMM_m2_rect.generate_target()
        NMM_m3_rect.generate_target()
        NMM_m4_rect.generate_target()

        NMM_m1_rect.target.next_to(t5_group, m.DOWN, buff=buff)
        NMM_m2_rect.target.next_to(t6_group, m.DOWN, buff=buff)
        NMM_m3_rect.target.next_to(t7_group, m.DOWN, buff=buff)
        NMM_m4_rect.target.next_to(t8_group, m.DOWN, buff=buff)

        # adding axes
        class MyText(m.Text):
            def __init__(self, *tex_strings, **kwargs):
                super().__init__(*tex_strings, font="Iosevka Nerd Font", **kwargs)

        axes = m.Axes(
            x_range=[0, 41, 1],
            y_range=[0, 4, 1],
            x_length=10.5,
            y_length=1.5,
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
            },
        )

        axes.move_to([0.5, 1.75, 0])
        axes.set_color(C.DEFAULT_FONT)
        labels = axes.get_axis_labels(x_label=styled_text("time").scale(0.325), y_label='')
        labels.set_color(C.DEFAULT_FONT)

        labels.shift(0.25 * m.DOWN)

        job0_title.generate_target()
        job0_title.target.move_to(axes.c2p(-3, 2.5))
        job0_title.target.scale(1.0)

        job1_title.generate_target()
        job1_title.target.move_to(axes.c2p(-3, 1.5))
        job1_title.target.scale(1.0)

        self.play(
            *[
                m.MoveToTarget(obj) for obj in [hammer_m1_rect, hammer_m2_rect, hammer_m3_rect, hammer_m4_rect]
            ],
            *[
                m.MoveToTarget(obj) for obj in [NMM_m1_rect, NMM_m2_rect, NMM_m3_rect, NMM_m4_rect]
            ],
            m.FadeIn(axes),
            m.Write(labels),
            m.MoveToTarget(job0_title),
            m.MoveToTarget(job1_title),
        )

        # add start time labels

        s_0 = m.MathTex(r"\mathtt{s_0 ", r"= ", r"0}", color=C.DEFAULT_FONT).scale(0.5).next_to(t0_group, m.LEFT,
                                                                                                buff=0.25)
        s_9 = m.MathTex(r"\mathtt{s_* ", r"= ", r"~?}", color=C.DEFAULT_FONT).scale(0.5).next_to(t9_group, m.RIGHT,
                                                                                                 buff=0.25)

        s_1 = m.MathTex(r"\mathtt{s_1 ", r"= ", r"~?}", color=C.DEFAULT_FONT).scale(0.5).next_to(t1_group, m.UP,
                                                                                                 buff=buff)
        s_2 = m.MathTex(r"\mathtt{s_2 ", r"= ", r"~?}", color=C.DEFAULT_FONT).scale(0.5).next_to(t2_group, m.UP,
                                                                                                 buff=buff)
        s_3 = m.MathTex(r"\mathtt{s_3 ", r"= ", r"~?}", color=C.DEFAULT_FONT).scale(0.5).next_to(t3_group, m.UP,
                                                                                                 buff=buff)
        s_4 = m.MathTex(r"\mathtt{s_4 ", r"= ", r"~?}", color=C.DEFAULT_FONT).scale(0.5).next_to(t4_group, m.UP,
                                                                                                 buff=buff)

        s_5 = m.MathTex(r"\mathtt{s_5 ", r"= ", r"~?}", color=C.DEFAULT_FONT).scale(0.5).next_to(t5_group, m.DOWN,
                                                                                                 buff=buff)
        s_6 = m.MathTex(r"\mathtt{s_6 ", r"= ", r"~?}", color=C.DEFAULT_FONT).scale(0.5).next_to(t6_group, m.DOWN,
                                                                                                 buff=buff)
        s_7 = m.MathTex(r"\mathtt{s_7 ", r"= ", r"~?}", color=C.DEFAULT_FONT).scale(0.5).next_to(t7_group, m.DOWN,
                                                                                                 buff=buff)
        s_8 = m.MathTex(r"\mathtt{s_8 ", r"= ", r"~?}", color=C.DEFAULT_FONT).scale(0.5).next_to(t8_group, m.DOWN,
                                                                                                 buff=buff)

        # move rects up
        rects_UP = [hammer_m1_rect, hammer_m2_rect, hammer_m3_rect, hammer_m4_rect]
        rects_DOWN = [NMM_m1_rect, NMM_m2_rect, NMM_m3_rect, NMM_m4_rect]

        for rec in rects_UP:
            rec.generate_target()
            rec.target.shift(m.UP * 0.375)

        for rec in rects_DOWN:
            rec.generate_target()
            rec.target.shift(m.DOWN * 0.375)

        s_value_scale = 0.375
        s_value_buff = 0.125
        s_0_value = styled_text("0", color=C.DEFAULT_FONT).scale(s_value_scale).next_to(s_0[1], m.RIGHT,
                                                                                        buff=s_value_buff)
        self.play(
            m.FadeIn(s_0[:2]),
            m.FadeIn(s_0_value),
            m.FadeIn(s_9),
            *[
                m.FadeIn(start_time) for start_time in [s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8]
            ],
            *[
                m.MoveToTarget(rec) for rec in rects_UP
            ],
            *[
                m.MoveToTarget(rec) for rec in rects_DOWN
            ]
        )

        machine_arrow_kwargs = {
            "tip_shape": m.ArrowTriangleFilledTip,
            "tip_length": 0.175,
            "stroke_width": 3,
            "buff": 0,
        }

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

        # allocate task t_5
        s_5_value = styled_text("0", color=C.DEFAULT_FONT).scale(s_value_scale).next_to(s_5[1], m.RIGHT,
                                                                                        buff=s_value_buff)
        t5_circle.generate_target()
        t5_circle.target.set_fill(C.GREEN_LIGHT)

        self.play(
            m.Transform(NMM_m1_rect, j1_t1, replace_mobject_with_target_in_scene=True),
            m.Transform(s_5[2], s_5_value, replace_mobject_with_target_in_scene=True),
            m.MoveToTarget(t5_circle),
        )

        # allocate t_1
        s_1_value = styled_text("5", color=C.DEFAULT_FONT).scale(s_value_scale).next_to(s_1[1], m.RIGHT,
                                                                                        buff=s_value_buff)
        t1_circle.generate_target()
        t1_circle.target.set_fill(C.GREEN_LIGHT)

        machine_edge_5_1 = m.Arrow(start=t5_circle, end=t1_circle, color=C.BLUE, **machine_arrow_kwargs)
        machine_edge_5_1_label = styled_text("5", color=C.BLUE).scale(0.425).move_to(
            machine_edge_5_1.get_center() + m.RIGHT * 0.25)

        self.play(
            m.Transform(hammer_m1_rect, j0_t1, replace_mobject_with_target_in_scene=True),
            m.Transform(s_1[2], s_1_value, replace_mobject_with_target_in_scene=True),
            m.MoveToTarget(t1_circle),
            m.Write(machine_edge_5_1),
            m.Write(machine_edge_5_1_label),
        )

        # indicate the 5 of s_1
        s_1_indicator = m.SurroundingRectangle(s_1_value, buff=.1, color=C.PINK)

        self.play(
            m.Create(s_1_indicator),
        )

        # line in axes at x=5
        line_at_5 = m.Line(start=axes.c2p(5, 0), end=axes.c2p(5, 4), color=C.PINK, stroke_width=3)
        self.play(
            m.Create(line_at_5),
        )
        # indicate the longest path from s_0 to s_1

        longest_path_lines_kwargs = {
            "stroke_width": 15,
            "buff": -3,
            "color": C.PINK,
            "stroke_opacity": 0.75,
        }
        line_0_5 = m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_5_1 = m.Line(start=t5_circle, end=t1_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        longest_path_to_t_1 = m.VGroup(
            line_0_5,
            line_5_1
        )
        self.play(
            m.FadeIn(longest_path_to_t_1),
        )

        self.play(
            m.Transform(longest_path_to_t_1, s_1_indicator, replace_mobject_with_target_in_scene=True),
        )

        # allocate t_6
        s_6_value = styled_text("5", color=C.DEFAULT_FONT).scale(s_value_scale).next_to(s_6[1], m.RIGHT,
                                                                                        buff=s_value_buff)
        t6_circle.generate_target()
        t6_circle.target.set_fill(C.GREEN_LIGHT)

        # update starting time indicator
        s_6_indicator = m.SurroundingRectangle(s_6_value, buff=.1, color=C.PINK)

        line_0_5 = m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_5_6 = m.Line(start=t5_circle, end=t6_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        longest_path_to_t_6 = m.VGroup(
            line_0_5,
            line_5_6
        )

        self.play(
            m.Transform(NMM_m2_rect, j1_t2, replace_mobject_with_target_in_scene=True),
            m.Transform(s_6[2], s_6_value, replace_mobject_with_target_in_scene=True),
            m.MoveToTarget(t6_circle),
            m.Transform(s_1_indicator, s_6_indicator, replace_mobject_with_target_in_scene=True),
            m.FadeIn(longest_path_to_t_6),
        )
        self.play(
            m.Transform(longest_path_to_t_6, s_6_indicator, replace_mobject_with_target_in_scene=True),
        )

        # allocate t_2
        s_2_value = styled_text("16", color=C.DEFAULT_FONT).scale(s_value_scale).next_to(s_2[1], m.RIGHT,
                                                                                         buff=s_value_buff)
        t2_circle.generate_target()
        t2_circle.target.set_fill(C.GREEN_LIGHT)

        # update starting time indicator
        s_2_indicator = m.SurroundingRectangle(s_2_value, buff=.1, color=C.PINK)

        # line in axes at x=16
        line_at_16 = m.Line(start=axes.c2p(16, 0), end=axes.c2p(16, 4), color=C.PINK, stroke_width=3)

        line_0_5 = m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_5_1 = m.Line(start=t5_circle, end=t1_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_1_2 = m.Line(start=t1_circle, end=t2_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)

        longest_path_to_t_2 = m.VGroup(
            line_0_5,
            line_5_1,
            line_1_2
        )
        self.remove(s_1_indicator)
        self.play(
            m.Transform(hammer_m2_rect, j0_t2, replace_mobject_with_target_in_scene=True),
            m.Transform(s_2[2], s_2_value, replace_mobject_with_target_in_scene=True),
            m.MoveToTarget(t2_circle),
            m.Transform(s_6_indicator, s_2_indicator, replace_mobject_with_target_in_scene=True),
            m.ReplacementTransform(line_at_5, line_at_16),
            m.FadeIn(longest_path_to_t_2),
        )
        self.play(
            m.Transform(longest_path_to_t_2, s_2_indicator, replace_mobject_with_target_in_scene=True),
        )

        # allocate t_7
        s_7_value = styled_text("21", color=C.DEFAULT_FONT).scale(s_value_scale).next_to(s_7[1], m.RIGHT,
                                                                                         buff=s_value_buff)
        t7_circle.generate_target()
        t7_circle.target.set_fill(C.GREEN_LIGHT)

        # update starting time indicator
        s_7_indicator = m.SurroundingRectangle(s_7_value, buff=.1, color=C.PINK)

        machine_edge_2_7 = m.Arrow(start=t2_circle, end=t7_circle, color=C.ORANGE_DARK, **machine_arrow_kwargs)
        machine_edge_2_7_label = styled_text("3", color=C.ORANGE_DARK).scale(0.425).move_to(
            machine_edge_2_7.get_center() + np.array([-0.25, 0.6, 0]))

        # line in axes at x=21
        line_at_21 = m.Line(start=axes.c2p(21, 0), end=axes.c2p(21, 4), color=C.PINK, stroke_width=3)

        line_0_5 = m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_5_6 = m.Line(start=t5_circle, end=t6_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_6_7 = m.Line(start=t6_circle, end=t7_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)

        longest_path_to_t_7 = m.VGroup(
            line_0_5,
            line_5_6,
            line_6_7
        )

        self.remove(s_2_indicator)
        self.remove(longest_path_to_t_2)
        self.remove(s_1_indicator)
        self.remove(longest_path_to_t_1)
        self.remove(s_6_indicator)
        self.play(
            m.Transform(NMM_m3_rect, j1_t3, replace_mobject_with_target_in_scene=True),
            m.Transform(s_7[2], s_7_value, replace_mobject_with_target_in_scene=True),
            m.MoveToTarget(t7_circle),
            m.ReplacementTransform(s_2_indicator, s_7_indicator),
            m.ReplacementTransform(line_at_16, line_at_21),
            m.FadeIn(longest_path_to_t_7),
            m.Write(machine_edge_2_7),
            m.Write(machine_edge_2_7_label),
        )
        self.play(
            m.Transform(longest_path_to_t_7, s_7_indicator, replace_mobject_with_target_in_scene=True),
        )

        # allocate t_3
        s_3_value = styled_text("21", color=C.DEFAULT_FONT).scale(s_value_scale).next_to(s_3[1], m.RIGHT,
                                                                                         buff=s_value_buff)
        t3_circle.generate_target()
        t3_circle.target.set_fill(C.GREEN_LIGHT)

        # update starting time indicator
        s_3_indicator = m.SurroundingRectangle(s_3_value, buff=.1, color=C.PINK)

        machine_edge_6_3 = m.Arrow(start=t6_circle, end=t3_circle, color=C.GREEN, **machine_arrow_kwargs)
        machine_edge_6_3_label = styled_text("16", color=C.GREEN).scale(0.425).move_to(
            machine_edge_6_3.get_center() + np.array([-0.25, -0.6, 0]))

        line_0_5 = m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_5_6 = m.Line(start=t5_circle, end=t6_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_6_3 = m.Line(start=t6_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)

        longest_path_to_t_3 = m.VGroup(
            line_0_5,
            line_5_6,
            line_6_3
        )

        self.remove(s_7_indicator)
        self.remove(longest_path_to_t_7)
        self.play(
            m.Transform(hammer_m3_rect, j0_t3, replace_mobject_with_target_in_scene=True),
            m.Transform(s_3[2], s_3_value, replace_mobject_with_target_in_scene=True),
            m.MoveToTarget(t3_circle),
            m.Transform(s_7_indicator, s_3_indicator, replace_mobject_with_target_in_scene=True),
            m.FadeIn(longest_path_to_t_3),
            m.Write(machine_edge_6_3),
            m.Write(machine_edge_6_3_label),
        )
        self.play(
            m.Transform(longest_path_to_t_3, s_3_indicator, replace_mobject_with_target_in_scene=True)
        )

        # allocate t_4
        s_4_value = styled_text("24", color=C.DEFAULT_FONT).scale(s_value_scale).next_to(s_4[1], m.RIGHT,
                                                                                         buff=s_value_buff)
        t4_circle.generate_target()
        t4_circle.target.set_fill(C.GREEN_LIGHT)

        # update starting time indicator
        s_4_indicator = m.SurroundingRectangle(s_4_value, buff=.1, color=C.PINK)

        # line in axes at x=24
        line_at_24 = m.Line(start=axes.c2p(24, 0), end=axes.c2p(24, 4), color=C.PINK, stroke_width=3)

        line_0_5 = m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_5_6 = m.Line(start=t5_circle, end=t6_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_6_3 = m.Line(start=t6_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_3_4 = m.Line(start=t3_circle, end=t4_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)

        longest_path_to_t_4 = m.VGroup(
            line_0_5,
            line_5_6,
            line_6_3,
            line_3_4
        )

        self.remove(s_3_indicator)
        self.remove(longest_path_to_t_3)
        self.play(
            m.Transform(hammer_m4_rect, j0_t4, replace_mobject_with_target_in_scene=True),
            m.Transform(s_4[2], s_4_value, replace_mobject_with_target_in_scene=True),
            m.MoveToTarget(t4_circle),
            m.Transform(s_3_indicator, s_4_indicator, replace_mobject_with_target_in_scene=True),
            m.ReplacementTransform(line_at_21, line_at_24),
            m.FadeIn(longest_path_to_t_4),
        )
        self.play(
            m.Transform(longest_path_to_t_4, s_4_indicator, replace_mobject_with_target_in_scene=True),
        )

        # allocate t_8
        s_8_value = styled_text("36", color=C.DEFAULT_FONT).scale(s_value_scale).next_to(s_8[1], m.RIGHT,
                                                                                         buff=s_value_buff)
        t8_circle.generate_target()
        t8_circle.target.set_fill(C.GREEN_LIGHT)

        # update starting time indicator
        s_8_indicator = m.SurroundingRectangle(s_8_value, buff=.1, color=C.PINK)

        machine_edge_4_8 = m.Arrow(start=t4_circle, end=t8_circle, color=C.TEAL, **machine_arrow_kwargs)
        machine_edge_4_8_label = styled_text("12", color=C.TEAL).scale(0.425).move_to(
            machine_edge_4_8.get_center() + m.LEFT * 0.25)

        # line in axes at x=36
        line_at_36 = m.Line(start=axes.c2p(36, 0), end=axes.c2p(36, 4), color=C.PINK, stroke_width=3)

        line_0_5 = m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_5_6 = m.Line(start=t5_circle, end=t6_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_6_3 = m.Line(start=t6_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_3_4 = m.Line(start=t3_circle, end=t4_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_4_8 = m.Line(start=t4_circle, end=t8_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)

        longest_path_to_t_8 = m.VGroup(
            line_0_5,
            line_5_6,
            line_6_3,
            line_3_4,
            line_4_8
        )

        self.remove(s_4_indicator)
        self.remove(longest_path_to_t_4)
        self.play(
            m.Transform(NMM_m4_rect, j1_t4, replace_mobject_with_target_in_scene=True),
            m.Transform(s_8[2], s_8_value, replace_mobject_with_target_in_scene=True),
            m.MoveToTarget(t8_circle),
            m.Transform(s_4_indicator, s_8_indicator, replace_mobject_with_target_in_scene=True),
            m.ReplacementTransform(line_at_24, line_at_36),
            m.FadeIn(longest_path_to_t_8),
            m.Write(machine_edge_4_8),
            m.Write(machine_edge_4_8_label),
        )
        self.play(
            m.Transform(longest_path_to_t_8, s_8_indicator, replace_mobject_with_target_in_scene=True),
        )

        # allocate t_9
        s_9_value = styled_text("40", color=C.DEFAULT_FONT).scale(s_value_scale).next_to(s_9[1], m.RIGHT,
                                                                                         buff=s_value_buff)
        t9_circle.generate_target()
        t9_circle.target.set_fill(C.GREEN_LIGHT)

        # update starting time indicator
        s_9_indicator = m.SurroundingRectangle(s_9_value, buff=.1, color=C.PINK)

        # line in axes at x=40
        line_at_40 = m.Line(start=axes.c2p(40, 0), end=axes.c2p(40, 4), color=C.PINK, stroke_width=3)

        line_0_5 = m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_5_6 = m.Line(start=t5_circle, end=t6_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_6_3 = m.Line(start=t6_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_3_4 = m.Line(start=t3_circle, end=t4_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_4_8 = m.Line(start=t4_circle, end=t8_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_8_9 = m.Line(start=t8_circle, end=t9_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)

        longest_path_to_t_9 = m.VGroup(
            line_0_5,
            line_5_6,
            line_6_3,
            line_3_4,
            line_4_8,
            line_8_9
        )

        self.remove(s_8_indicator)
        self.remove(longest_path_to_t_8)


        temp_group3 = m.VGroup(
            t9_text
        )
        temp_group3.z_index = 500
        self.add(temp_group3)

        self.play(
            m.Transform(s_9[2], s_9_value, replace_mobject_with_target_in_scene=True),
            m.MoveToTarget(t9_circle),
            m.Transform(s_8_indicator, s_9_indicator, replace_mobject_with_target_in_scene=True),
            m.ReplacementTransform(line_at_36, line_at_40),
            m.FadeIn(longest_path_to_t_9),
        )

        downshift = m.DOWN * 0.425

        # shift axes
        axes.generate_target()
        axes.target.shift(downshift)

        # shift job titles
        job0_title.generate_target()
        job0_title.target.shift(downshift)

        job1_title.generate_target()
        job1_title.target.shift(downshift)

        # shift axes rects
        j0_t1.generate_target()
        j0_t1.target.shift(downshift)

        j0_t2.generate_target()
        j0_t2.target.shift(downshift)

        j0_t3.generate_target()
        j0_t3.target.shift(downshift)

        j0_t4.generate_target()
        j0_t4.target.shift(downshift)

        j1_t1.generate_target()
        j1_t1.target.shift(downshift)

        j1_t2.generate_target()
        j1_t2.target.shift(downshift)

        j1_t3.generate_target()
        j1_t3.target.shift(downshift)

        j1_t4.generate_target()
        j1_t4.target.shift(downshift)

        # shift axes labels
        labels.generate_target()
        labels.target.shift(downshift)

        # shift line_at_40
        line_at_40.generate_target()
        line_at_40.target.shift(downshift)

        brace = m.BraceBetweenPoints(axes.c2p(0, 2.0), axes.c2p(40, 2.0), direction=m.UP)
        brace.set_color(C.PINK)

        makespan_text = styled_text("Makespan").scale(0.5)
        makespan_text.move_to(brace.get_center() + m.UP * 0.325)

        self.play(
            m.Write(brace),
            m.Write(makespan_text),
            *[
                m.MoveToTarget(mob) for mob in [
                    axes,
                    job0_title,
                    job1_title,
                    j0_t1,
                    j0_t2,
                    j0_t3,
                    j0_t4,
                    j1_t1,
                    j1_t2,
                    j1_t3,
                    j1_t4,
                    labels,
                    line_at_40
                ]
            ]
        )

        self.play(
            m.Indicate(makespan_text, color=C.YELLOW, scale_factor=1.05, rate_func=m.there_and_back_with_pause),
            m.Indicate(brace, color=C.YELLOW, scale_factor=1, rate_func=m.there_and_back_with_pause),
        )

        self.play(
            m.Indicate(s_9_indicator, color=C.YELLOW),
            m.Indicate(makespan_text, color=C.YELLOW, scale_factor=1.05, rate_func=m.there_and_back_with_pause),
        )

        self.play(
            m.Indicate(makespan_text, color=C.YELLOW, scale_factor=1.05, rate_func=m.there_and_back_with_pause),
            m.Indicate(longest_path_to_t_9, color=C.YELLOW, scale_factor=1, rate_func=m.there_and_back_with_pause),
        )

        self.play(
            self.overlay_scene()
        )




if __name__ == '__main__':
    C_IopGraphModellingIntro.save_sections_without_cache()