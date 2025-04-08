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

class EIopRlState(RwthTheme, AxesUtils, GanttUtils, RwthSlideTemplate):
    logo_paths = [
        "iop_logo.png"
    ]
    logo_height = 0.6
    index_prefix = "E "

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
        b_task_circle_kwargs = {
            "radius": 0.25,
            "stroke_width": 6,
            "fill_color": C.YELLOW,
            "fill_opacity": 1.0
        }
        b_fictive_task_circle_kwargs = {
            "radius": 0.25,
            "stroke_width": 6,
            "fill_color": C.GREEN_LIGHT,
            "fill_opacity": 1.0
        }
        row1_y = -1.0 + 0.125
        row2_y = -3.0 + 0.125

        b_t1_circle = m.Circle(stroke_color=C.BLUE, **b_task_circle_kwargs)
        b_t1_text = m.Tex(r"$\mathsf{t_1}$", color=C.GREY_DARK).scale(0.5)
        b_t1_group = m.VGroup(b_t1_circle, b_t1_text)
        b_t1_group.move_to(np.array([-3, row1_y, 0]))

        b_t2_circle = m.Circle(stroke_color=C.ORANGE_DARK, **b_task_circle_kwargs)
        b_t2_text = m.Tex(r"$\mathsf{t_2}$", color=C.GREY_DARK).scale(0.5)
        b_t2_group = m.VGroup(b_t2_circle, b_t2_text)
        b_t2_group.move_to(np.array([-1, row1_y, 0]))

        b_t3_circle = m.Circle(stroke_color=C.GREEN, **b_task_circle_kwargs)
        b_t3_text = m.Tex(r"$\mathsf{t_3}$", color=C.GREY_DARK).scale(0.5)
        b_t3_group = m.VGroup(b_t3_circle, b_t3_text)
        b_t3_group.move_to(np.array([1, row1_y, 0]))

        b_t4_circle = m.Circle(stroke_color=C.TEAL, **b_task_circle_kwargs)
        b_t4_text = m.Tex(r"$\mathsf{t_4}$", color=C.GREY_DARK).scale(0.5)
        b_t4_group = m.VGroup(b_t4_circle, b_t4_text)
        b_t4_group.move_to(np.array([3, row1_y, 0]))

        b_t5_circle = m.Circle(stroke_color=C.BLUE, **b_task_circle_kwargs)
        b_t5_text = m.Tex(r"$\mathsf{t_5}$", color=C.GREY_DARK).scale(0.5)
        b_t5_group = m.VGroup(b_t5_circle, b_t5_text)
        b_t5_group.move_to(np.array([-3, row2_y, 0]))

        b_t6_circle = m.Circle(stroke_color=C.GREEN, **b_task_circle_kwargs)
        b_t6_text = m.Tex(r"$\mathsf{t_6}$", color=C.GREY_DARK).scale(0.5)
        b_t6_group = m.VGroup(b_t6_circle, b_t6_text)
        b_t6_group.move_to(np.array([-1, row2_y, 0]))

        b_t7_circle = m.Circle(stroke_color=C.ORANGE_DARK, **b_task_circle_kwargs)
        b_t7_text = m.Tex(r"$\mathsf{t_7}$", color=C.GREY_DARK).scale(0.5)
        b_t7_group = m.VGroup(b_t7_circle, b_t7_text)
        b_t7_group.move_to(np.array([1, row2_y, 0]))

        b_t8_circle = m.Circle(stroke_color=C.TEAL, **b_task_circle_kwargs)
        b_t8_text = m.Tex(r"$\mathsf{t_8}$", color=C.GREY_DARK).scale(0.5)
        b_t8_group = m.VGroup(b_t8_circle, b_t8_text)
        b_t8_group.move_to(np.array([3, row2_y, 0]))

        # add job edges

        b_job_arrow_kwargs = {
            "tip_shape": m.ArrowTriangleFilledTip,
            "tip_length": 0.175,
            "stroke_width": 3,
            "buff": 0,
            "color": C.DARK_FONT
        }

        b_job_edge_1_2 = m.Arrow(start=b_t1_circle, end=b_t2_circle, **b_job_arrow_kwargs)
        b_job_edge_2_3 = m.Arrow(start=b_t2_circle, end=b_t3_circle, **b_job_arrow_kwargs)
        b_job_edge_3_4 = m.Arrow(start=b_t3_circle, end=b_t4_circle, **b_job_arrow_kwargs)

        b_job_edge_5_6 = m.Arrow(start=b_t5_circle, end=b_t6_circle, **b_job_arrow_kwargs)
        b_job_edge_6_7 = m.Arrow(start=b_t6_circle, end=b_t7_circle, **b_job_arrow_kwargs)
        b_job_edge_7_8 = m.Arrow(start=b_t7_circle, end=b_t8_circle, **b_job_arrow_kwargs)

        # add fictions nodes
        b_t0_circle = m.Circle(stroke_color=C.DARK_FONT, **b_fictive_task_circle_kwargs)
        b_t0_text = m.Tex(r"$\mathsf{t_0}$", color=C.GREY_DARK).scale(0.5)
        b_t0_group = m.VGroup(b_t0_circle, b_t0_text)
        b_t0_group.move_to(np.array([-4.5, (row1_y + row2_y) * 0.5, 0]))

        b_t9_circle = m.Circle(stroke_color=C.DARK_FONT, **b_fictive_task_circle_kwargs)
        b_t9_text = m.Tex(r"$\mathsf{t_*}$", color=C.GREY_DARK).scale(0.5)
        b_t9_group = m.VGroup(b_t9_circle, b_t9_text)
        b_t9_group.move_to(np.array([4.5, (row1_y + row2_y) * 0.5, 0]))

        b_job_edge_0_1 = m.Arrow(start=b_t0_circle, end=b_t1_circle, **b_job_arrow_kwargs)
        b_job_edge_0_5 = m.Arrow(start=b_t0_circle, end=b_t5_circle, **b_job_arrow_kwargs)

        b_job_edge_4_9 = m.Arrow(start=b_t4_circle, end=b_t9_circle, **b_job_arrow_kwargs)
        b_job_edge_8_9 = m.Arrow(start=b_t8_circle, end=b_t9_circle, **b_job_arrow_kwargs)

        # add durations

        b_job_edge_0_1_label = styled_text("0", color=C.DARK_FONT).scale(0.425).move_to(
            b_job_edge_0_1.get_center() + m.UL * 0.2)
        b_job_edge_0_5_label = styled_text("0", color=C.DARK_FONT).scale(0.425).move_to(
            b_job_edge_0_5.get_center() + m.DL * 0.2)

        b_job_edge_4_9_label = styled_text("12", color=C.DARK_FONT).scale(0.425).move_to(
            b_job_edge_4_9.get_center() + m.UR * 0.2)
        b_job_edge_8_9_label = styled_text("4", color=C.DARK_FONT).scale(0.425).move_to(
            b_job_edge_8_9.get_center() + m.DR * 0.2)

        b_job_edge_1_2_label = styled_text("11", color=C.DARK_FONT).scale(0.425).move_to(
            b_job_edge_1_2.get_center() + m.UP * 0.25)
        b_job_edge_2_3_label = styled_text("3", color=C.DARK_FONT).scale(0.425).move_to(
            b_job_edge_2_3.get_center() + m.UP * 0.25)
        b_job_edge_3_4_label = styled_text("3", color=C.DARK_FONT).scale(0.425).move_to(
            b_job_edge_3_4.get_center() + m.UP * 0.25)

        b_job_edge_5_6_label = styled_text("5", color=C.DARK_FONT).scale(0.425).move_to(
            b_job_edge_5_6.get_center() + m.DOWN * 0.25)
        b_job_edge_6_7_label = styled_text("16", color=C.DARK_FONT).scale(0.425).move_to(
            b_job_edge_6_7.get_center() + m.DOWN * 0.25)
        b_job_edge_7_8_label = styled_text("7", color=C.DARK_FONT).scale(0.425).move_to(
            b_job_edge_7_8.get_center() + m.DOWN * 0.25)

        big_graph = m.VGroup(
            b_t1_group,
            b_t2_group,
            b_t3_group,
            b_t4_group,
            b_t5_group,
            b_t6_group,
            b_t7_group,
            b_t8_group,
            b_t0_group,
            b_t9_group,
            b_job_edge_0_1,
            b_job_edge_0_5,
            b_job_edge_4_9,
            b_job_edge_8_9,
            b_job_edge_1_2,
            b_job_edge_2_3,
            b_job_edge_3_4,
            b_job_edge_5_6,
            b_job_edge_6_7,
            b_job_edge_7_8,
            b_job_edge_0_1_label,
            b_job_edge_0_5_label,
            b_job_edge_4_9_label,
            b_job_edge_8_9_label,
            b_job_edge_1_2_label,
            b_job_edge_2_3_label,
            b_job_edge_3_4_label,
            b_job_edge_5_6_label,
            b_job_edge_6_7_label,
            b_job_edge_7_8_label
        )

        big_graph.move_to(np.array([0, 0.0, 0]))

        self.play(
            m.FadeIn(big_graph)
        )

        ##
        ## small graph
        ##

        task_circle_kwargs = {
            "radius": 0.125,
            "stroke_width": 3,
            "fill_color": C.YELLOW,
            "fill_opacity": 1.0
        }
        fictive_task_circle_kwargs = {
            "radius": 0.125,
            "stroke_width": 3,
            "fill_color": C.GREEN_LIGHT,
            "fill_opacity": 1.0
        }

        x_scaling = 0.5
        t_text_scale = 0.325

        row1_y = -0.5
        row2_y = -1.5

        t1_circle = m.Circle(stroke_color=C.BLUE, **task_circle_kwargs)
        t1_text = m.Tex(r"$\mathsf{t_1}$", color=C.GREY_DARK).scale(t_text_scale)
        t1_group = m.VGroup(t1_circle, t1_text)
        t1_group.move_to(np.array([-3 * x_scaling, row1_y, 0]))

        t2_circle = m.Circle(stroke_color=C.ORANGE_DARK, **task_circle_kwargs)
        t2_text = m.Tex(r"$\mathsf{t_2}$", color=C.GREY_DARK).scale(t_text_scale)
        t2_group = m.VGroup(t2_circle, t2_text)
        t2_group.move_to(np.array([-1 * x_scaling, row1_y, 0]))

        t3_circle = m.Circle(stroke_color=C.GREEN, **task_circle_kwargs)
        t3_text = m.Tex(r"$\mathsf{t_3}$", color=C.GREY_DARK).scale(t_text_scale)
        t3_group = m.VGroup(t3_circle, t3_text)
        t3_group.move_to(np.array([1 * x_scaling, row1_y, 0]))

        t4_circle = m.Circle(stroke_color=C.TEAL, **task_circle_kwargs)
        t4_text = m.Tex(r"$\mathsf{t_4}$", color=C.GREY_DARK).scale(t_text_scale)
        t4_group = m.VGroup(t4_circle, t4_text)
        t4_group.move_to(np.array([3 * x_scaling, row1_y, 0]))

        t5_circle = m.Circle(stroke_color=C.BLUE, **task_circle_kwargs)
        t5_text = m.Tex(r"$\mathsf{t_5}$", color=C.GREY_DARK).scale(t_text_scale)
        t5_group = m.VGroup(t5_circle, t5_text)
        t5_group.move_to(np.array([-3 * x_scaling, row2_y, 0]))

        t6_circle = m.Circle(stroke_color=C.GREEN, **task_circle_kwargs)
        t6_text = m.Tex(r"$\mathsf{t_6}$", color=C.GREY_DARK).scale(t_text_scale)
        t6_group = m.VGroup(t6_circle, t6_text)
        t6_group.move_to(np.array([-1 * x_scaling, row2_y, 0]))

        t7_circle = m.Circle(stroke_color=C.ORANGE_DARK, **task_circle_kwargs)
        t7_text = m.Tex(r"$\mathsf{t_7}$", color=C.GREY_DARK).scale(t_text_scale)
        t7_group = m.VGroup(t7_circle, t7_text)
        t7_group.move_to(np.array([1 * x_scaling, row2_y, 0]))

        t8_circle = m.Circle(stroke_color=C.TEAL, **task_circle_kwargs)
        t8_text = m.Tex(r"$\mathsf{t_8}$", color=C.GREY_DARK).scale(t_text_scale)
        t8_group = m.VGroup(t8_circle, t8_text)
        t8_group.move_to(np.array([3 * x_scaling, row2_y, 0]))

        # add fictions nodes
        t0_circle = m.Circle(stroke_color=C.DARK_FONT, **fictive_task_circle_kwargs)
        t0_text = m.Tex(r"$\mathsf{t_0}$", color=C.GREY_DARK).scale(t_text_scale)
        t0_group = m.VGroup(t0_circle, t0_text)
        t0_group.move_to(np.array([-4.5 * x_scaling, (row1_y + row2_y) * 0.5, 0]))

        t9_circle = m.Circle(stroke_color=C.DARK_FONT, **fictive_task_circle_kwargs)
        t9_text = m.Tex(r"$\mathsf{t_*}$", color=C.GREY_DARK).scale(t_text_scale)
        t9_group = m.VGroup(t9_circle, t9_text)
        t9_group.move_to(np.array([4.5 * x_scaling, (row1_y + row2_y) * 0.5, 0]))

        job_arrow_kwargs = {
            "tip_shape": m.ArrowTriangleFilledTip,
            "tip_length": 0.175 * 0.5,
            "stroke_width": 3 * 0.5,
            "buff": 0,
            "color": C.DARK_FONT
        }

        job_edge_0_1 = m.Arrow(start=t0_circle, end=t1_circle, **job_arrow_kwargs)
        job_edge_0_5 = m.Arrow(start=t0_circle, end=t5_circle, **job_arrow_kwargs)

        job_edge_4_9 = m.Arrow(start=t4_circle, end=t9_circle, **job_arrow_kwargs)
        job_edge_8_9 = m.Arrow(start=t8_circle, end=t9_circle, **job_arrow_kwargs)

        job_edge_1_2 = m.Arrow(start=t1_circle, end=t2_circle, **job_arrow_kwargs)
        job_edge_2_3 = m.Arrow(start=t2_circle, end=t3_circle, **job_arrow_kwargs)
        job_edge_3_4 = m.Arrow(start=t3_circle, end=t4_circle, **job_arrow_kwargs)

        job_edge_5_6 = m.Arrow(start=t5_circle, end=t6_circle, **job_arrow_kwargs)
        job_edge_6_7 = m.Arrow(start=t6_circle, end=t7_circle, **job_arrow_kwargs)
        job_edge_7_8 = m.Arrow(start=t7_circle, end=t8_circle, **job_arrow_kwargs)

        # add durations
        label_scale = 0.5
        shift_scale = label_scale

        job_edge_0_1_label = styled_text("0", color=C.DARK_FONT).scale(0.425 * label_scale).move_to(
            job_edge_0_1.get_center() + m.UL * 0.2 * shift_scale)
        job_edge_0_5_label = styled_text("0", color=C.DARK_FONT).scale(0.425 * label_scale).move_to(
            job_edge_0_5.get_center() + m.DL * 0.2 * shift_scale)

        job_edge_4_9_label = styled_text("12", color=C.DARK_FONT).scale(0.425 * label_scale).move_to(
            job_edge_4_9.get_center() + m.UR * 0.2 * shift_scale)
        job_edge_8_9_label = styled_text("4", color=C.DARK_FONT).scale(0.425 * label_scale).move_to(
            job_edge_8_9.get_center() + m.DR * 0.2 * shift_scale)

        job_edge_1_2_label = styled_text("11", color=C.DARK_FONT).scale(0.425 * label_scale).move_to(
            job_edge_1_2.get_center() + m.UP * 0.25 * shift_scale)
        job_edge_2_3_label = styled_text("3", color=C.DARK_FONT).scale(0.425 * label_scale).move_to(
            job_edge_2_3.get_center() + m.UP * 0.25 * shift_scale)
        job_edge_3_4_label = styled_text("3", color=C.DARK_FONT).scale(0.425 * label_scale).move_to(
            job_edge_3_4.get_center() + m.UP * 0.25 * shift_scale)

        job_edge_5_6_label = styled_text("5", color=C.DARK_FONT).scale(0.425 * label_scale).move_to(
            job_edge_5_6.get_center() + m.DOWN * 0.25 * shift_scale)
        job_edge_6_7_label = styled_text("16", color=C.DARK_FONT).scale(0.425 * label_scale).move_to(
            job_edge_6_7.get_center() + m.DOWN * 0.25 * shift_scale)
        job_edge_7_8_label = styled_text("7", color=C.DARK_FONT).scale(0.425 * label_scale).move_to(
            job_edge_7_8.get_center() + m.DOWN * 0.25 * shift_scale)

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

        graph.move_to(np.array([0, 2.0, 0]))

        self.play(
            m.ReplacementTransform(big_graph, graph),
        )

        header_color = RwthTheme.rwth_lila_75
        zero_color = RwthTheme.rwth_schwarz_50
        non_zero_color = RwthTheme.rwth_blau_75

        initially_hidden_kwargs = {

        }

        cell_scaling = 0.3125

        tXX = m.Tex(r"", color=header_color).scale(0.5)
        tX0 = m.Tex(r"$\mathsf{t_0}$", color=header_color).scale(0.5)
        tX1 = m.Tex(r"$\mathsf{t_1}$", color=header_color).scale(0.5)
        tX2 = m.Tex(r"$\mathsf{t_2}$", color=header_color).scale(0.5)
        tX3 = m.Tex(r"$\mathsf{t_3}$", color=header_color).scale(0.5)
        tX4 = m.Tex(r"$\mathsf{t_4}$", color=header_color).scale(0.5)
        tX5 = m.Tex(r"$\mathsf{t_5}$", color=header_color).scale(0.5)
        tX6 = m.Tex(r"$\mathsf{t_6}$", color=header_color).scale(0.5)
        tX7 = m.Tex(r"$\mathsf{t_7}$", color=header_color).scale(0.5)
        tX8 = m.Tex(r"$\mathsf{t_8}$", color=header_color).scale(0.5)
        tX9 = m.Tex(r"$\mathsf{t_*}$", color=header_color).scale(0.5)
        tXM0 = m.Tex(r"$\mathsf{m}$", color=header_color).scale(0.5).set_opacity(0.0)
        tXM1 = m.Tex(r"$\mathsf{d}$", color=header_color).scale(0.5).set_opacity(0.0)
        tXM2 = m.Tex(r"$\mathsf{m_2}$", color=C.GREEN).scale(0.5).set_opacity(0.0)
        tXM3 = m.Tex(r"$\mathsf{m_3}$", color=C.TEAL).scale(0.5).set_opacity(0.0)
        tXD = m.Tex(r"$\mathsf{d}$", color=header_color).scale(0.5).set_opacity(0.0)

        header_row = [tXX, tX0, tX1, tX2, tX3, tX4, tX5, tX6, tX7, tX8, tX9, tXM0, tXM1, tXM2, tXM3, tXD]

        t0X = m.Tex(r"$\mathsf{t_0}$", color=header_color).scale(0.5)
        t00 = styled_text("0", color=zero_color).scale(cell_scaling)
        t01 = styled_text("1", color=non_zero_color).scale(cell_scaling)
        t02 = styled_text("0", color=zero_color).scale(cell_scaling)
        t03 = styled_text("0", color=zero_color).scale(cell_scaling)
        t04 = styled_text("0", color=zero_color).scale(cell_scaling)
        t05 = styled_text("1", color=non_zero_color).scale(cell_scaling)
        t06 = styled_text("0", color=zero_color).scale(cell_scaling)
        t07 = styled_text("0", color=zero_color).scale(cell_scaling)
        t08 = styled_text("0", color=zero_color).scale(cell_scaling)
        t09 = styled_text("0", color=zero_color).scale(cell_scaling)
        t0M0 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t0M1 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t0M2 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t0M3 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t0D = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)

        zero_row = [t0X, t00, t01, t02, t03, t04, t05, t06, t07, t08, t09, t0M0, t0M1, t0M2, t0M3, t0D]

        t1X = m.Tex(r"$\mathsf{t_1}$", color=header_color).scale(0.5)
        t10 = styled_text("0", color=zero_color).scale(cell_scaling)
        t11 = styled_text("0", color=zero_color).scale(cell_scaling)
        t12 = styled_text("1", color=non_zero_color).scale(cell_scaling)
        t13 = styled_text("0", color=zero_color).scale(cell_scaling)
        t14 = styled_text("0", color=zero_color).scale(cell_scaling)
        t15 = styled_text("0", color=zero_color).scale(cell_scaling)
        t16 = styled_text("0", color=zero_color).scale(cell_scaling)
        t17 = styled_text("0", color=zero_color).scale(cell_scaling)
        t18 = styled_text("0", color=zero_color).scale(cell_scaling)
        t19 = styled_text("0", color=zero_color).scale(cell_scaling)
        t1M0 = styled_text("0", color=C.BLUE).scale(cell_scaling).set_opacity(0.0)
        t1M1 = styled_text("11", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t1M2 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t1M3 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t1D = styled_text("11", color=non_zero_color).scale(cell_scaling).set_opacity(0.0)

        first_row = [t1X, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t1M0, t1M1, t1M2, t1M3, t1D]

        t2X = m.Tex(r"$\mathsf{t_2}$", color=header_color).scale(0.5)
        t20 = styled_text("0", color=zero_color).scale(cell_scaling)
        t21 = styled_text("0", color=zero_color).scale(cell_scaling)
        t22 = styled_text("0", color=zero_color).scale(cell_scaling)
        t23 = styled_text("1", color=non_zero_color).scale(cell_scaling)
        t24 = styled_text("0", color=zero_color).scale(cell_scaling)
        t25 = styled_text("0", color=zero_color).scale(cell_scaling)
        t26 = styled_text("0", color=zero_color).scale(cell_scaling)
        t27 = styled_text("0", color=zero_color).scale(cell_scaling)
        t28 = styled_text("0", color=zero_color).scale(cell_scaling)
        t29 = styled_text("0", color=zero_color).scale(cell_scaling)
        t2M0 = styled_text("1", color=C.ORANGE_DARK).scale(cell_scaling).set_opacity(0.0)
        t2M1 = styled_text("3", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t2M2 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t2M3 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t2D = styled_text("3", color=non_zero_color).scale(cell_scaling).set_opacity(0.0)

        second_row = [t2X, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29, t2M0, t2M1, t2M2, t2M3, t2D]

        t3X = m.Tex(r"$\mathsf{t_3}$", color=header_color).scale(0.5)
        t30 = styled_text("0", color=zero_color).scale(cell_scaling)
        t31 = styled_text("0", color=zero_color).scale(cell_scaling)
        t32 = styled_text("0", color=zero_color).scale(cell_scaling)
        t33 = styled_text("0", color=zero_color).scale(cell_scaling)
        t34 = styled_text("1", color=non_zero_color).scale(cell_scaling)
        t35 = styled_text("0", color=zero_color).scale(cell_scaling)
        t36 = styled_text("0", color=zero_color).scale(cell_scaling)
        t37 = styled_text("0", color=zero_color).scale(cell_scaling)
        t38 = styled_text("0", color=zero_color).scale(cell_scaling)
        t39 = styled_text("0", color=zero_color).scale(cell_scaling)
        t3M0 = styled_text("2", color=C.GREEN).scale(cell_scaling).set_opacity(0.0)
        t3M1 = styled_text("3", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t3M2 = styled_text("1", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t3M3 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t3D = styled_text("3", color=non_zero_color).scale(cell_scaling).set_opacity(0.0)

        third_row = [t3X, t30, t31, t32, t33, t34, t35, t36, t37, t38, t39, t3M0, t3M1, t3M2, t3M3, t3D]

        t4X = m.Tex(r"$\mathsf{t_4}$", color=header_color).scale(0.5)
        t40 = styled_text("0", color=zero_color).scale(cell_scaling)
        t41 = styled_text("0", color=zero_color).scale(cell_scaling)
        t42 = styled_text("0", color=zero_color).scale(cell_scaling)
        t43 = styled_text("0", color=zero_color).scale(cell_scaling)
        t44 = styled_text("0", color=zero_color).scale(cell_scaling)
        t45 = styled_text("0", color=zero_color).scale(cell_scaling)
        t46 = styled_text("0", color=zero_color).scale(cell_scaling)
        t47 = styled_text("0", color=zero_color).scale(cell_scaling)
        t48 = styled_text("0", color=zero_color).scale(cell_scaling)
        t49 = styled_text("1", color=non_zero_color).scale(cell_scaling)
        t4M0 = styled_text("3", color=C.TEAL).scale(cell_scaling).set_opacity(0.0)
        t4M1 = styled_text("12", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t4M2 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t4M3 = styled_text("1", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t4D = styled_text("12", color=non_zero_color).scale(cell_scaling).set_opacity(0.0)

        fourth_row = [t4X, t40, t41, t42, t43, t44, t45, t46, t47, t48, t49, t4M0, t4M1, t4M2, t4M3, t4D]

        t5X = m.Tex(r"$\mathsf{t_5}$", color=header_color).scale(0.5)
        t50 = styled_text("0", color=zero_color).scale(cell_scaling)
        t51 = styled_text("0", color=zero_color).scale(cell_scaling)
        t52 = styled_text("0", color=zero_color).scale(cell_scaling)
        t53 = styled_text("0", color=zero_color).scale(cell_scaling)
        t54 = styled_text("0", color=zero_color).scale(cell_scaling)
        t55 = styled_text("0", color=zero_color).scale(cell_scaling)
        t56 = styled_text("1", color=non_zero_color).scale(cell_scaling)
        t57 = styled_text("0", color=zero_color).scale(cell_scaling)
        t58 = styled_text("0", color=zero_color).scale(cell_scaling)
        t59 = styled_text("0", color=zero_color).scale(cell_scaling)
        t5M0 = styled_text("0", color=C.BLUE).scale(cell_scaling).set_opacity(0.0)
        t5M1 = styled_text("5", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t5M2 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t5M3 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t5D = styled_text("5", color=non_zero_color).scale(cell_scaling).set_opacity(0.0)

        fifth_row = [t5X, t50, t51, t52, t53, t54, t55, t56, t57, t58, t59, t5M0, t5M1, t5M2, t5M3, t5D]

        t6X = m.Tex(r"$\mathsf{t_6}$", color=header_color).scale(0.5)
        t60 = styled_text("0", color=zero_color).scale(cell_scaling)
        t61 = styled_text("0", color=zero_color).scale(cell_scaling)
        t62 = styled_text("0", color=zero_color).scale(cell_scaling)
        t63 = styled_text("0", color=zero_color).scale(cell_scaling)
        t64 = styled_text("0", color=zero_color).scale(cell_scaling)
        t65 = styled_text("0", color=zero_color).scale(cell_scaling)
        t66 = styled_text("0", color=zero_color).scale(cell_scaling)
        t67 = styled_text("1", color=non_zero_color).scale(cell_scaling)
        t68 = styled_text("0", color=zero_color).scale(cell_scaling)
        t69 = styled_text("0", color=zero_color).scale(cell_scaling)
        t6M0 = styled_text("2", color=C.GREEN).scale(cell_scaling).set_opacity(0.0)
        t6M1 = styled_text("16", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t6M2 = styled_text("1", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t6M3 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t6D = styled_text("16", color=non_zero_color).scale(cell_scaling).set_opacity(0.0)

        sixth_row = [t6X, t60, t61, t62, t63, t64, t65, t66, t67, t68, t69, t6M0, t6M1, t6M2, t6M3, t6D]

        t7X = m.Tex(r"$\mathsf{t_7}$", color=header_color).scale(0.5)
        t70 = styled_text("0", color=zero_color).scale(cell_scaling)
        t71 = styled_text("0", color=zero_color).scale(cell_scaling)
        t72 = styled_text("0", color=zero_color).scale(cell_scaling)
        t73 = styled_text("0", color=zero_color).scale(cell_scaling)
        t74 = styled_text("0", color=zero_color).scale(cell_scaling)
        t75 = styled_text("0", color=zero_color).scale(cell_scaling)
        t76 = styled_text("0", color=zero_color).scale(cell_scaling)
        t77 = styled_text("0", color=zero_color).scale(cell_scaling)
        t78 = styled_text("1", color=non_zero_color).scale(cell_scaling)
        t79 = styled_text("0", color=zero_color).scale(cell_scaling)
        t7M0 = styled_text("1", color=C.ORANGE_DARK).scale(cell_scaling).set_opacity(0.0)
        t7M1 = styled_text("7", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t7M2 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t7M3 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t7D = styled_text("7", color=non_zero_color).scale(cell_scaling).set_opacity(0.0)

        seventh_row = [t7X, t70, t71, t72, t73, t74, t75, t76, t77, t78, t79, t7M0, t7M1, t7M2, t7M3, t7D]

        t8X = m.Tex(r"$\mathsf{t_8}$", color=header_color).scale(0.5)
        t80 = styled_text("0", color=zero_color).scale(cell_scaling)
        t81 = styled_text("0", color=zero_color).scale(cell_scaling)
        t82 = styled_text("0", color=zero_color).scale(cell_scaling)
        t83 = styled_text("0", color=zero_color).scale(cell_scaling)
        t84 = styled_text("0", color=zero_color).scale(cell_scaling)
        t85 = styled_text("0", color=zero_color).scale(cell_scaling)
        t86 = styled_text("0", color=zero_color).scale(cell_scaling)
        t87 = styled_text("0", color=zero_color).scale(cell_scaling)
        t88 = styled_text("0", color=zero_color).scale(cell_scaling)
        t89 = styled_text("1", color=non_zero_color).scale(cell_scaling)
        t8M0 = styled_text("3", color=C.TEAL).scale(cell_scaling).set_opacity(0.0)
        t8M1 = styled_text("4", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t8M2 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t8M3 = styled_text("1", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t8D = styled_text("4", color=non_zero_color).scale(cell_scaling).set_opacity(0.0)

        eighth_row = [t8X, t80, t81, t82, t83, t84, t85, t86, t87, t88, t89, t8M0, t8M1, t8M2, t8M3, t8D]

        t9X = m.Tex(r"$\mathsf{t_*}$", color=header_color).scale(0.5)
        t90 = styled_text("0", color=zero_color).scale(cell_scaling)
        t91 = styled_text("0", color=zero_color).scale(cell_scaling)
        t92 = styled_text("0", color=zero_color).scale(cell_scaling)
        t93 = styled_text("0", color=zero_color).scale(cell_scaling)
        t94 = styled_text("0", color=zero_color).scale(cell_scaling)
        t95 = styled_text("0", color=zero_color).scale(cell_scaling)
        t96 = styled_text("0", color=zero_color).scale(cell_scaling)
        t97 = styled_text("0", color=zero_color).scale(cell_scaling)
        t98 = styled_text("0", color=zero_color).scale(cell_scaling)
        t99 = styled_text("0", color=zero_color).scale(cell_scaling)
        t9M0 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t9M1 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t9M2 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t9M3 = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)
        t9D = styled_text("0", color=zero_color).scale(cell_scaling).set_opacity(0.0)

        ninth_row = [t9X, t90, t91, t92, t93, t94, t95, t96, t97, t98, t99, t9M0, t9M1, t9M2, t9M3, t9D]

        state_table = m.MobjectTable(
            [[tXX, tX0, tX1, tX2, tX3, tX4, tX5, tX6, tX7, tX8, tX9, tXM0, tXM1, tXM2, tXM3, tXD],
             [t0X, t00, t01, t02, t03, t04, t05, t06, t07, t08, t09, t0M0, t0M1, t0M2, t0M3, t0D],
             [t1X, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t1M0, t1M1, t1M2, t1M3, t1D],
             [t2X, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29, t2M0, t2M1, t2M2, t2M3, t2D],
             [t3X, t30, t31, t32, t33, t34, t35, t36, t37, t38, t39, t3M0, t3M1, t3M2, t3M3, t3D],
             [t4X, t40, t41, t42, t43, t44, t45, t46, t47, t48, t49, t4M0, t4M1, t4M2, t4M3, t4D],
             [t5X, t50, t51, t52, t53, t54, t55, t56, t57, t58, t59, t5M0, t5M1, t5M2, t5M3, t5D],
             [t6X, t60, t61, t62, t63, t64, t65, t66, t67, t68, t69, t6M0, t6M1, t6M2, t6M3, t6D],
             [t7X, t70, t71, t72, t73, t74, t75, t76, t77, t78, t79, t7M0, t7M1, t7M2, t7M3, t7D],
             [t8X, t80, t81, t82, t83, t84, t85, t86, t87, t88, t89, t8M0, t8M1, t8M2, t8M3, t8D],
             [t9X, t90, t91, t92, t93, t94, t95, t96, t97, t98, t99, t9M0, t9M1, t9M2, t9M3, t9D]],
            v_buff=0.175,
            h_buff=0.5,
        ).scale_to_fit_width(10.0).to_edge(m.DOWN, buff=1.25)

        state_table.remove(*state_table.get_vertical_lines())
        state_table.remove(*state_table.get_horizontal_lines())

        x_offset = m.SurroundingRectangle(m.VGroup(tXX, t9X, tX9, t99), buff=0.0, color=C.PINK).get_center()[0]
        x_offset_m0 = m.SurroundingRectangle(m.VGroup(tXX, t9X, tXM0, t9M0), buff=0.0, color=C.PINK).get_center()[0]
        x_offset_m0_d = m.SurroundingRectangle(m.VGroup(tXX, t9X, tXM1, t9M1), buff=0.0, color=C.PINK).get_center()[0]
        x_offset_m3_d = m.SurroundingRectangle(m.VGroup(tXX, t9X, tXD, t9D), buff=0.0, color=C.PINK).get_center()[0]

        y_offset = state_table.get_center()[1]

        state_table.move_to(np.array([-x_offset, y_offset, 0]))

        graph_tasks = m.VGroup(t0_text, t1_text, t2_text, t3_text, t4_text, t5_text, t6_text, t7_text, t8_text, t9_text)

        x_col = m.VGroup(tXX, t0X, t1X, t2X, t3X, t4X, t5X, t6X, t7X, t8X, t9X)

        self.play(
            m.ReplacementTransform(graph_tasks.copy(), x_col),
        )

        x_row = m.VGroup(tX0, tX1, tX2, tX3, tX4, tX5, tX6, tX7, tX8, tX9)

        self.play(
            m.ReplacementTransform(graph_tasks.copy(), x_row),
        )

        indicator_buff = 0.075

        from_rect_graph = m.SurroundingRectangle(t0_circle, buff=indicator_buff, color=C.YELLOW)
        to_rect_graph = m.SurroundingRectangle(t1_circle, buff=indicator_buff, color=C.PINK)

        self.play(
            m.Create(from_rect_graph),
            m.Create(to_rect_graph),
        )

        from_rect_table = m.SurroundingRectangle(t0X, buff=indicator_buff, color=C.YELLOW)
        to_rect_table = m.SurroundingRectangle(tX1, buff=indicator_buff, color=C.PINK)

        self.play(
            m.Create(from_rect_table),
            m.Create(to_rect_table),
        )

        self.play(
            m.ReplacementTransform(job_edge_0_1.copy(), t01)
        )

        self.play(
            m.Transform(from_rect_graph, m.SurroundingRectangle(t1_circle, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_graph, m.SurroundingRectangle(t2_circle, buff=indicator_buff, color=C.PINK)),
            m.Transform(from_rect_table, m.SurroundingRectangle(t1X, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_table, m.SurroundingRectangle(tX2, buff=indicator_buff, color=C.PINK)),
        )

        self.play(
            m.ReplacementTransform(job_edge_1_2.copy(), t12)
        )

        self.play(
            m.Transform(from_rect_graph, m.SurroundingRectangle(t2_circle, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_graph, m.SurroundingRectangle(t3_circle, buff=indicator_buff, color=C.PINK)),
            m.Transform(from_rect_table, m.SurroundingRectangle(t2X, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_table, m.SurroundingRectangle(tX3, buff=indicator_buff, color=C.PINK)),
        )

        self.play(
            m.ReplacementTransform(job_edge_2_3.copy(), t23)
        )

        self.play(
            m.Transform(from_rect_graph, m.SurroundingRectangle(t3_circle, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_graph, m.SurroundingRectangle(t4_circle, buff=indicator_buff, color=C.PINK)),
            m.Transform(from_rect_table, m.SurroundingRectangle(t3X, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_table, m.SurroundingRectangle(tX4, buff=indicator_buff, color=C.PINK)),
        )

        self.play(
            m.ReplacementTransform(job_edge_3_4.copy(), t34)
        )

        self.play(
            m.Transform(from_rect_graph, m.SurroundingRectangle(t4_circle, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_graph, m.SurroundingRectangle(t9_circle, buff=indicator_buff, color=C.PINK)),
            m.Transform(from_rect_table, m.SurroundingRectangle(t4X, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_table, m.SurroundingRectangle(tX9, buff=indicator_buff, color=C.PINK)),
        )

        self.play(
            m.ReplacementTransform(job_edge_4_9.copy(), t49)
        )

        self.play(
            m.Transform(from_rect_graph, m.SurroundingRectangle(t0_circle, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_graph, m.SurroundingRectangle(t5_circle, buff=indicator_buff, color=C.PINK)),
            m.Transform(from_rect_table, m.SurroundingRectangle(t0X, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_table, m.SurroundingRectangle(tX5, buff=indicator_buff, color=C.PINK)),
        )

        self.play(
            m.ReplacementTransform(job_edge_0_5.copy(), t05)
        )

        self.play(
            m.Transform(from_rect_graph, m.SurroundingRectangle(t5_circle, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_graph, m.SurroundingRectangle(t6_circle, buff=indicator_buff, color=C.PINK)),
            m.Transform(from_rect_table, m.SurroundingRectangle(t5X, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_table, m.SurroundingRectangle(tX6, buff=indicator_buff, color=C.PINK)),
        )

        self.play(
            m.ReplacementTransform(job_edge_5_6.copy(), t56)
        )

        self.play(
            m.Transform(from_rect_graph, m.SurroundingRectangle(t6_circle, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_graph, m.SurroundingRectangle(t7_circle, buff=indicator_buff, color=C.PINK)),
            m.Transform(from_rect_table, m.SurroundingRectangle(t6X, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_table, m.SurroundingRectangle(tX7, buff=indicator_buff, color=C.PINK)),
        )

        self.play(
            m.ReplacementTransform(job_edge_6_7.copy(), t67)
        )

        self.play(
            m.Transform(from_rect_graph, m.SurroundingRectangle(t7_circle, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_graph, m.SurroundingRectangle(t8_circle, buff=indicator_buff, color=C.PINK)),
            m.Transform(from_rect_table, m.SurroundingRectangle(t7X, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_table, m.SurroundingRectangle(tX8, buff=indicator_buff, color=C.PINK)),
        )

        self.play(
            m.ReplacementTransform(job_edge_7_8.copy(), t78)
        )

        self.play(
            m.Transform(from_rect_graph, m.SurroundingRectangle(t8_circle, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_graph, m.SurroundingRectangle(t9_circle, buff=indicator_buff, color=C.PINK)),
            m.Transform(from_rect_table, m.SurroundingRectangle(t8X, buff=indicator_buff, color=C.YELLOW)),
            m.Transform(to_rect_table, m.SurroundingRectangle(tX9, buff=indicator_buff, color=C.PINK)),
        )

        self.play(
            m.ReplacementTransform(job_edge_8_9.copy(), t89)
        )

        rest_tasks_in_table = [t00, t02, t03, t04, t06, t07, t08, t09, t10, t11, t13, t14, t15, t16, t17, t18, t19, t20,
                               t21, t22, t24, t25, t26, t27, t28, t29, t30, t31, t32, t33, t35, t36, t37, t38, t39, t40,
                               t41, t42, t43, t44, t45, t46, t47, t48, t50, t51, t52, t53, t54, t55, t57, t58, t59, t60,
                               t61, t62, t63, t64, t65, t66, t68, t69, t70, t71, t72, t73, t74, t75, t76, t77, t79, t80,
                               t81, t82, t83, t84, t85, t86, t87, t88, t90, t91, t92, t93, t94, t95, t96, t97, t98, t99]
        self.play(
            *[m.FadeIn(task) for task in rest_tasks_in_table],
            m.Uncreate(from_rect_graph),
            m.Uncreate(to_rect_graph),
            m.Uncreate(from_rect_table),
            m.Uncreate(to_rect_table),
        )

        # replace ones with duration
        self.play(
            m.Transform(t01, styled_text("0", color=non_zero_color).scale_to_fit_height(t01.height).move_to(
                t01.get_center())),
            m.Transform(t12, styled_text("11", color=non_zero_color).scale_to_fit_height(t12.height).move_to(
                t12.get_center())),
            m.Transform(t23, styled_text("3", color=non_zero_color).scale_to_fit_height(t23.height).move_to(
                t23.get_center())),
            m.Transform(t34, styled_text("3", color=non_zero_color).scale_to_fit_height(t34.height).move_to(
                t34.get_center())),
            m.Transform(t49, styled_text("12", color=non_zero_color).scale_to_fit_height(t49.height).move_to(
                t49.get_center())),

            m.Transform(t05, styled_text("0", color=non_zero_color).scale_to_fit_height(t05.height).move_to(
                t05.get_center())),
            m.Transform(t56, styled_text("5", color=non_zero_color).scale_to_fit_height(t56.height).move_to(
                t56.get_center())),
            m.Transform(t67, styled_text("16", color=non_zero_color).scale_to_fit_height(t67.height).move_to(
                t67.get_center())),
            m.Transform(t78, styled_text("7", color=non_zero_color).scale_to_fit_height(t78.height).move_to(
                t78.get_center())),
            m.Transform(t89, styled_text("4", color=non_zero_color).scale_to_fit_height(t89.height).move_to(
                t89.get_center())),
        )

        self.play(
            m.Circumscribe(t12, color=C.PINK),
            m.Circumscribe(job_edge_1_2_label, color=C.PINK),
        )

        self.play(
            m.Circumscribe(t56, color=C.PINK),
            m.Circumscribe(job_edge_5_6_label, color=C.PINK),
        )

        state_table.generate_target()
        state_table.target.move_to(np.array([-x_offset_m0, y_offset, 0]))

        self.play(
            m.MoveToTarget(state_table),
        )

        for elem in [tXM0, t0M0, t1M0, t2M0, t3M0, t4M0, t5M0, t6M0, t7M0, t8M0, t9M0]:
            elem.generate_target()
            elem.target.set_opacity(1.0)

        self.play(
            *[m.MoveToTarget(e) for e in [tXM0, t0M0, t1M0, t2M0, t3M0, t4M0, t5M0, t6M0, t7M0, t8M0, t9M0]]
        )

        self.play(
            m.Circumscribe(t1M0, color=C.BLUE),
            m.Circumscribe(t1_circle, color=C.BLUE),
            m.Circumscribe(t5M0, color=C.BLUE),
            m.Circumscribe(t5_circle, color=C.BLUE),
        )

        self.play(
            m.Circumscribe(t2M0, color=C.ORANGE_DARK),
            m.Circumscribe(t2_circle, color=C.ORANGE_DARK),
            m.Circumscribe(t7M0, color=C.ORANGE_DARK),
            m.Circumscribe(t7_circle, color=C.ORANGE_DARK),
        )

        self.play(
            m.Circumscribe(t3M0, color=C.GREEN),
            m.Circumscribe(t3_circle, color=C.GREEN),
            m.Circumscribe(t6M0, color=C.GREEN),
            m.Circumscribe(t6_circle, color=C.GREEN),
        )

        self.play(
            m.Circumscribe(t4M0, color=C.TEAL),
            m.Circumscribe(t4_circle, color=C.TEAL),
            m.Circumscribe(t8M0, color=C.TEAL),
            m.Circumscribe(t8_circle, color=C.TEAL),
        )

        state_table.generate_target()
        state_table.target.move_to(np.array([-x_offset_m0_d, y_offset, 0]))

        self.play(
            m.MoveToTarget(state_table),
        )

        for elem in [tXM1, t0M1, t1M1, t2M1, t3M1, t4M1, t5M1, t6M1, t7M1, t8M1, t9M1]:
            elem.generate_target()
            elem.target.set_opacity(1.0)
            if elem not in [tXM1, t0M1, t9M1]:
                elem.target.set_color(non_zero_color)

        for elem in [t1M0, t2M0, t3M0, t4M0, t5M0, t6M0, t7M0, t8M0]:
            elem.generate_target()
            elem.target.set_color(non_zero_color)

        self.play(
            *[m.MoveToTarget(e) for e in [tXM1, t0M1, t1M1, t2M1, t3M1, t4M1, t5M1, t6M1, t7M1, t8M1, t9M1]],
            *[m.MoveToTarget(e) for e in [t1M0, t2M0, t3M0, t4M0, t5M0, t6M0, t7M0, t8M0]]
        )

        self.play(
            m.Circumscribe(m.VGroup(t00, t9M1), color=C.YELLOW, buff=0.15),
        )

        machine_arrow_kwargs = {
            "tip_shape": m.ArrowTriangleFilledTip,
            "tip_length": 0.175 * 0.5,
            "stroke_width": 3 * 0.5,
            "buff": 0,
        }
        machine_edge_5_1 = m.Arrow(start=t5_circle, end=t1_circle, color=C.BLUE, **machine_arrow_kwargs)
        machine_edge_2_7 = m.Arrow(start=t2_circle, end=t7_circle, color=C.ORANGE_DARK, **machine_arrow_kwargs)
        machine_edge_6_3 = m.Arrow(start=t6_circle, end=t3_circle, color=C.GREEN, **machine_arrow_kwargs)
        machine_edge_4_8 = m.Arrow(start=t4_circle, end=t8_circle, color=C.TEAL, **machine_arrow_kwargs)

        machine_edge_5_1_label = styled_text("5", color=C.BLUE).scale(0.425 * label_scale).move_to(
            machine_edge_5_1.get_center() + m.RIGHT * 0.25 * shift_scale)

        t5_circle.generate_target()
        t5_circle.target.set_fill(C.GREEN_LIGHT)

        t5_text_copy = t5_text.copy()
        t5_text_copy.z_index = 500
        self.add(t5_text_copy)

        self.play(
            m.MoveToTarget(t5_circle)
        )

        t1_circle.generate_target()
        t1_circle.target.set_fill(C.GREEN_LIGHT)

        t1_text_copy = t1_text.copy()
        t1_text_copy.z_index = 500
        self.add(t1_text_copy)

        self.play(
            m.Create(machine_edge_5_1),
            m.FadeIn(machine_edge_5_1_label),
            m.MoveToTarget(t1_circle),
            m.Transform(t51, styled_text("5", color=non_zero_color).scale_to_fit_height(t05.height).move_to(
                t51.get_center())),
        )

        self.play(
            m.Circumscribe(t51, color=C.BLUE),
            m.Circumscribe(machine_edge_5_1_label, color=C.BLUE),
        )

        state_table.generate_target()
        state_table.target.move_to(np.array([-x_offset_m3_d, y_offset, 0]))

        self.play(
            m.MoveToTarget(state_table),
        )

        for elem in [t0M1, t1M1, t2M1, t3M1, t4M1, t5M1, t6M1, t7M1, t8M1, t9M1]:
            elem.generate_target()
            elem.target.set_opacity(0.0)

        # copy of d col

        tXD_copy = tXD.copy().set_opacity(1.0)
        t0D_copy = t0D.copy().set_opacity(1.0)
        t1D_copy = t1D.copy().set_opacity(1.0)
        t2D_copy = t2D.copy().set_opacity(1.0)
        t3D_copy = t3D.copy().set_opacity(1.0)
        t4D_copy = t4D.copy().set_opacity(1.0)
        t5D_copy = t5D.copy().set_opacity(1.0)
        t6D_copy = t6D.copy().set_opacity(1.0)
        t7D_copy = t7D.copy().set_opacity(1.0)
        t8D_copy = t8D.copy().set_opacity(1.0)
        t9D_copy = t9D.copy().set_opacity(1.0)

        t2M0_copy = styled_text("0", color=zero_color).scale_to_fit_height(t2M0.height).move_to(
            t2M0.get_center())
        t3M0_copy = styled_text("0", color=zero_color).scale_to_fit_height(t3M0.height).move_to(
            t3M0.get_center())
        t4M0_copy = styled_text("0", color=zero_color).scale_to_fit_height(t4M0.height).move_to(
            t4M0.get_center())
        t6M0_copy = styled_text("0", color=zero_color).scale_to_fit_height(t6M0.height).move_to(
            t6M0.get_center())
        t7M0_copy = styled_text("0", color=zero_color).scale_to_fit_height(t7M0.height).move_to(
            t7M0.get_center())
        t8M0_copy = styled_text("0", color=zero_color).scale_to_fit_height(t8M0.height).move_to(
            t8M0.get_center())

        for elem in [tXM1, t0M1, t1M1, t2M1, t3M1, t4M1, t5M1, t6M1, t7M1, t8M1, t9M1]:
            elem.generate_target()
            elem.target.set_opacity(0.0)

        self.play(
            *[
                m.ReplacementTransform(m1_col.copy(), d_col.set_opacity(1.0))
                for m1_col, d_col in zip(
                    [tXM1, t0M1, t1M1, t2M1, t3M1, t4M1, t5M1, t6M1, t7M1, t8M1, t9M1],
                    [tXD_copy, t0D_copy, t1D_copy, t2D_copy, t3D_copy, t4D_copy, t5D_copy, t6D_copy, t7D_copy, t8D_copy,
                     t9D_copy],
                )
            ],
            *[
                m.MoveToTarget(e, run_time=0.01) for e in
                [tXM1, t0M1, t1M1, t2M1, t3M1, t4M1, t5M1, t6M1, t7M1, t8M1, t9M1]
            ]
        )

        tXM0_copy = m.Tex(r"$\mathsf{m_0}$", color=C.BLUE).scale_to_fit_height(tXM3.height).move_to(
            tXM0.get_center())

        tXM1_copy = m.Tex(r"$\mathsf{m_1}$", color=C.ORANGE_DARK).scale_to_fit_height(tXM3.height).move_to(
            tXM1.get_center())

        for elem in [tXM2, tXM3]:
            elem.generate_target()
            elem.target.set_opacity(1.0)
            elem.target.scale_to_fit_height(tXM3.height)

        t1M0_copy = styled_text("1", color=non_zero_color).scale_to_fit_height(t1M0.height).move_to(
            t1M0.get_center())

        t2M1_copy = styled_text("1", color=non_zero_color).scale_to_fit_height(t2M1.height).move_to(
            t2M1.get_center())

        t3M2_copy = styled_text("1", color=non_zero_color).scale_to_fit_height(t3M2.height).move_to(
            t3M2.get_center())

        t4M3_copy = styled_text("1", color=non_zero_color).scale_to_fit_height(t4M3.height).move_to(
            t4M3.get_center())

        t5M0_copy = styled_text("1", color=non_zero_color).scale_to_fit_height(t5M0.height).move_to(
            t5M0.get_center())

        t6M2_copy = styled_text("1", color=non_zero_color).scale_to_fit_height(t6M2.height).move_to(
            t6M2.get_center())

        t7M1_copy = styled_text("1", color=non_zero_color).scale_to_fit_height(t7M1.height).move_to(
            t7M1.get_center())

        t8M3_copy = styled_text("1", color=non_zero_color).scale_to_fit_height(t8M3.height).move_to(
            t8M3.get_center())

        self.play(
            m.ReplacementTransform(tXM0, tXM0_copy),
            m.ReplacementTransform(tXM1, tXM1_copy),
            m.MoveToTarget(tXM2),
            m.MoveToTarget(tXM3),
            m.ReplacementTransform(t1M0, t1M0_copy),
            m.ReplacementTransform(t2M0, t2M1_copy),
            m.ReplacementTransform(t3M0, t3M2_copy),
            m.ReplacementTransform(t4M0, t4M3_copy),

            m.ReplacementTransform(t5M0, t5M0_copy),
            m.ReplacementTransform(t6M0, t6M2_copy),
            m.ReplacementTransform(t7M0, t7M1_copy),
            m.ReplacementTransform(t8M0, t8M3_copy),

            m.FadeOut(t0M0),
            m.FadeOut(t9M0),
        )

        # fade in zero elements in m0 to m3 cols

        t1M1_copy = styled_text("0", color=zero_color).scale_to_fit_height(t1M1.height).move_to(
            t1M1.get_center())
        t3M1_copy = styled_text("0", color=zero_color).scale_to_fit_height(t3M1.height).move_to(
            t3M1.get_center())
        t4M1_copy = styled_text("0", color=zero_color).scale_to_fit_height(t4M1.height).move_to(
            t4M1.get_center())
        t5M1_copy = styled_text("0", color=zero_color).scale_to_fit_height(t5M1.height).move_to(
            t5M1.get_center())
        t6M1_copy = styled_text("0", color=zero_color).scale_to_fit_height(t6M1.height).move_to(
            t6M1.get_center())
        t8M1_copy = styled_text("0", color=zero_color).scale_to_fit_height(t8M1.height).move_to(
            t8M1.get_center())

        zero_elems = [
            t0M3, t1M3, t2M3, t3M3, t4M3, t5M3, t6M3, t7M3, t8M3, t9M3,
            t0M2, t1M2, t2M2, t3M2, t4M2, t5M2, t6M2, t7M2, t8M2, t9M2,
            t0M1, t9M1,
            t0M0, t9M0,
        ]

        for elem in zero_elems:
            elem.generate_target()
            elem.target.set_opacity(1.0)

        self.play(
            *[m.MoveToTarget(e) for e in zero_elems],
            *[m.FadeIn(e) for e in [t1M1_copy, t3M1_copy, t4M1_copy, t5M1_copy, t6M1_copy, t8M1_copy]],
            *[m.FadeIn(e) for e in [t2M0_copy, t3M0_copy, t4M0_copy, t6M0_copy, t7M0_copy, t8M0_copy]],
            m.FadeIn(t0M0),
            m.FadeIn(t9M0),
        )

        # indicate the longest task
        self.play(
            m.Circumscribe(t67, color=C.GREEN),
            m.Circumscribe(t6D_copy, color=C.GREEN)
        )

        # make cells fractions
        t12_frac = styled_text(f"{11 / 16:.2f}", color=non_zero_color).scale_to_fit_height(t12.height).move_to(
            t12.get_center())
        t23_frac = styled_text(f"{3 / 16:.2f}", color=non_zero_color).scale_to_fit_height(t23.height).move_to(
            t23.get_center())
        t34_frac = styled_text(f"{3 / 16:.2f}", color=non_zero_color).scale_to_fit_height(t34.height).move_to(
            t34.get_center())
        t49_frac = styled_text(f"{12 / 16:.2f}", color=non_zero_color).scale_to_fit_height(t49.height).move_to(
            t49.get_center())

        t56_frac = styled_text(f"{5 / 16:.2f}", color=non_zero_color).scale_to_fit_height(t56.height).move_to(
            t56.get_center())
        t67_frac = styled_text(f"{1}", color=non_zero_color).scale_to_fit_height(t67.height).move_to(
            t67.get_center())
        t78_frac = styled_text(f"{7 / 16:.2f}", color=non_zero_color).scale_to_fit_height(t78.height).move_to(
            t78.get_center())
        t89_frac = styled_text(f"{4 / 16:.2f}", color=non_zero_color).scale_to_fit_height(t89.height).move_to(
            t89.get_center())

        t51_frac = styled_text(f"{5 / 16:.2f}", color=non_zero_color).scale_to_fit_height(t51.height).move_to(
            t51.get_center())

        t1D_frac = styled_text(f"{11 / 16:.2f}", color=non_zero_color).scale_to_fit_height(t1D_copy.height).move_to(
            t1D_copy.get_center())
        t2D_frac = styled_text(f"{3 / 16:.2f}", color=non_zero_color).scale_to_fit_height(t2D_copy.height).move_to(
            t2D_copy.get_center())
        t3D_frac = styled_text(f"{3 / 16:.2f}", color=non_zero_color).scale_to_fit_height(t3D_copy.height).move_to(
            t3D_copy.get_center())
        t4D_frac = styled_text(f"{12 / 16:.2f}", color=non_zero_color).scale_to_fit_height(t4D_copy.height).move_to(
            t4D_copy.get_center())
        t5D_frac = styled_text(f"{5 / 16:.2f}", color=non_zero_color).scale_to_fit_height(t5D_copy.height).move_to(
            t5D_copy.get_center())
        t6D_frac = styled_text(f"{1}", color=non_zero_color).scale_to_fit_height(t6D_copy.height).move_to(
            t6D_copy.get_center())
        t7D_frac = styled_text(f"{7 / 16:.2f}", color=non_zero_color).scale_to_fit_height(t7D_copy.height).move_to(
            t7D_copy.get_center())
        t8D_frac = styled_text(f"{4 / 16:.2f}", color=non_zero_color).scale_to_fit_height(t8D_copy.height).move_to(
            t8D_copy.get_center())

        # set color for m cols
        for elem in [tXM0_copy, tXM1_copy, tXM2, tXM3]:
            elem.generate_target()
            elem.target.set_color(header_color)

        self.play(
            *[
                m.ReplacementTransform(from_elem, frac_elem)
                for from_elem, frac_elem in zip(
                    [t12, t23, t34, t49, t56, t67, t78, t89, t51],
                    [t12_frac, t23_frac, t34_frac, t49_frac, t56_frac, t67_frac, t78_frac, t89_frac, t51_frac],
                )
            ],
            *[
                m.ReplacementTransform(from_elem, frac_elem)
                for from_elem, frac_elem in zip(
                    [t1D_copy, t2D_copy, t3D_copy, t4D_copy, t5D_copy, t6D_copy, t7D_copy, t8D_copy],
                    [t1D_frac, t2D_frac, t3D_frac, t4D_frac, t5D_frac, t6D_frac, t7D_frac, t8D_frac],
                )
            ],
            *[m.MoveToTarget(e) for e in [tXM0_copy, tXM1_copy, tXM2, tXM3]],
        )

        self.play(
            m.Circumscribe(m.VGroup(t00, t9D_copy), color=C.YELLOW, buff=0.25),
        )

        self.play(
            self.overlay_scene()
        )


if __name__ == '__main__':
    EIopRlState.render_video_low()