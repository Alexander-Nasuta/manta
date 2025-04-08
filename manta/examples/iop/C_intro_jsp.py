import manim as m
import numpy as np

from color_theme.carolus.corolus_theme import CarolusTheme
from color_theme.rwth.rwth_theme import RwthTheme
from components.axes_utils import AxesUtils
from components.gantt_utils import GanttUtils
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate
from slide_templates.rwth.rwth_slide_template import RwthSlideTemplate


class CJspIntro(RwthTheme, AxesUtils, GanttUtils, RwthSlideTemplate):

    # font_name = "IosevkaTermSlab Nerd Font Mono"

    logo_paths = [
        "iop_logo.png"
    ]
    logo_height = 0.6
    index_prefix = "B "

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
                subtitle="Introduction"
            ),
            self.add_logos(),
            self.add_seperator_line_top(),
            self.add_seperator_line_bottom()
        )

        NMM_color = RwthTheme.rwth_blau_75
        hammer_color = RwthTheme.rwth_blau_75

        # points
        LU = np.array([-4, 2.3, 0])
        LD = np.array([-4, 1.7, 0])

        MU = np.array([0, 4, 0])
        MM = np.array([0, 0.6, 0])
        MD = np.array([0, 0, 0])

        RU = np.array([4, 2.3, 0])
        RD = np.array([4, 1.7, 0])

        shadow_color = RwthTheme.rwth_blau_25
        # outer sides
        front_left = m.Polygon(*[MD, LD, LU, MM], color=NMM_color, fill_color=shadow_color)
        front_right = m.Polygon(*[MD, RD, RU, MM], color=NMM_color, fill_color=shadow_color)
        top = m.Polygon(*[MM, LU, MU, RU], color=NMM_color, fill_color=shadow_color)
        NMM_sides = m.VGroup(front_left, front_right, top)

        # drilling points

        D_O_L = np.array([-3, 2.3, 0])  # Drilling Outer Left
        D_O_R = np.array([3, 2.3, 0])  # Drilling Outer Right
        D_O_U = np.array([0, 3.55, 0])  # Drilling Outer Up
        D_O_D = np.array([0, 1, 0])  # Drilling Outer Down

        D_M_L = np.array([-2, 2.3, 0])  # Drilling Middle Left
        D_M_R = np.array([2, 2.3, 0])  # Drilling Middle Right
        D_M_U = np.array([0, 3.175, 0])  # Drilling Middle Up
        D_M_D = np.array([0, 1.425, 0])  # Drilling Middle Down

        D_I_L = np.array([-1, 2.3, 0])  # Drilling Inner Left
        D_I_R = np.array([1, 2.3, 0])  # Drilling Inner Right
        D_I_U = np.array([0, 2.7025, 0])  # Drilling Inner Up
        D_I_D = np.array([0, 1.8975, 0])  # Drilling Inner Down

        # milled edges

        game_field_outer = m.Polygon(*[D_O_D, D_O_L, D_O_U, D_O_R], color=NMM_color)
        game_field_middle = m.Polygon(*[D_M_D, D_M_L, D_M_U, D_M_R], color=NMM_color)
        game_field_inner = m.Polygon(*[D_I_D, D_I_L, D_I_U, D_I_R], color=NMM_color)

        game_lines = m.VGroup(
            m.Line(
                0.5 * (D_O_L - D_O_D) + D_O_D,
                0.5 * (D_I_L - D_I_D) + D_I_D,
                color=NMM_color
            ),
            m.Line(
                0.5 * (D_O_R - D_O_D) + D_O_D,
                0.5 * (D_I_R - D_I_D) + D_I_D,
                color=NMM_color
            ),
            m.Line(
                0.5 * (D_O_L - D_O_U) + D_O_U,
                0.5 * (D_I_L - D_I_U) + D_I_U,
                color=NMM_color
            ),
            m.Line(
                0.5 * (D_O_R - D_O_U) + D_O_U,
                0.5 * (D_I_R - D_I_U) + D_I_U,
                color=NMM_color
            ),
        )

        milled_edges = m.VGroup(
            game_field_outer,
            game_field_middle,
            game_field_inner,

            game_lines
        )

        drilling_points = [
            D_O_L,
            D_O_R,
            D_O_U,
            D_O_D,

            D_M_L,
            D_M_R,
            D_M_U,
            D_M_D,

            D_I_L,
            D_I_R,
            D_I_U,
            D_I_D,

            *[line.get_start() for line in game_lines],
            *[line.get_end() for line in game_lines],
            *[line.get_midpoint() for line in game_lines]
        ]

        drilling_ellipses = m.VGroup(
            *[m.Ellipse(width=0.3, height=0.15, color=NMM_color, fill_color=shadow_color, fill_opacity=1).move_to(pos)
              for pos in drilling_points]
        )

        # nine man moris
        NMM = m.VGroup(NMM_sides, milled_edges, drilling_ellipses)

        # self.add(NMM)

        # hammer
        hammer_head_outer = m.Polygon(*[
            np.array([-2, 0, 0]),
            np.array([-2, -0.25, 0]),
            np.array([-2, -0.70, 0]),
            np.array([-1.9, -0.8, 0]),
            np.array([-1.6, -0.8, 0]),
            np.array([-1.5, -0.7, 0]),
            np.array([-1.5, -0.25, 0]),
            np.array([-1.5, 0, 0]),
            np.array([-1.5, 0.3, 0]),
            np.array([-1.7, 1, 0]),
            np.array([-1.8, 1, 0]),
            np.array([-2, 0.3, 0]),
        ], color=hammer_color, fill_color=shadow_color)

        hammer_head_inner = m.Polygon(*[
            np.array([-2, -0.25, 0]),
            np.array([-2, -0.70, 0]),
            np.array([-1.9, -0.7, 0]),
            np.array([-2, -0.70, 0]),
            np.array([-1.9, -0.8, 0]),
            np.array([-1.9, -0.7, 0]),
            np.array([-1.9, -0.8, 0]),
            np.array([-1.6, -0.8, 0]),
            np.array([-1.6, -0.7, 0]),
            np.array([-1.6, -0.8, 0]),
            np.array([-1.5, -0.7, 0]),
            np.array([-1.6, -0.7, 0]),
            np.array([-1.5, -0.7, 0]),
            np.array([-1.5, -0.25, 0]),
            np.array([-1.6, -0.7, 0]),
            np.array([-1.9, -0.7, 0]),
        ], color=hammer_color, stroke_width=3, fill_color=shadow_color, fill_opacity=0.5)

        hammer_top_part_rect = m.Polygon(*[
            np.array([-1.5, -0.25, 0]),
            np.array([-1.2, -0.25, 0]),
            np.array([-1.2, 0.25, 0]),
            np.array([-1.5, 0.25, 0]),
        ], color=hammer_color)

        hammer_top_part_line = m.Line(
            np.array([-1.45, -0.25, 0]),
            np.array([-1.45, 0.25, 0]),
            color=hammer_color)

        hammer_top_part = m.VGroup(hammer_top_part_rect, hammer_top_part_line)

        p1_1 = np.array([-1.5, -0.225, 0])
        p2_1 = np.array([2.0, -0.225, 0])
        bezier_1 = m.CubicBezier(p1_1, p1_1 + np.array([0.5, 0.1, 0]), p2_1 + np.array([-1.5, 0.05, 0]), p2_1)
        p1_2 = np.array([-1.5, 0.225, 0])
        p2_2 = np.array([2.0, 0.225, 0])
        bezier_2 = m.CubicBezier(p1_2, p1_2 + np.array([0.5, -0.1, 0]), p2_2 + np.array([-1.5, -0.05, 0]), p2_2)

        hammer_drill_segment = m.VGroup(
            m.Line(
                np.array([-2, -0.225, 0]),
                np.array([-2, 0.225, 0]),
                color=hammer_color
            ),
            m.Line(
                np.array([-1.5, -0.225, 0]),
                np.array([-1.5, 0.225, 0]),
                color=hammer_color
            )
        )

        line = m.Line(p2_1, p2_2)
        arc = m.ArcBetweenPoints(p2_1, p2_2)

        hammer_wood_part = m.VGroup(bezier_1, bezier_2, line, arc)

        hammer_shaft = m.VGroup(hammer_wood_part)
        hammer_shaft.color = hammer_color

        hammer = m.VGroup(hammer_shaft, hammer_head_outer, hammer_head_inner, hammer_drill_segment)

        NMM.scale(0.75)
        NMM.move_to(3.5 * m.RIGHT)

        hammer.scale(1.45)
        hammer.move_to(3.5 * m.LEFT)

        self.play(
            m.Write(NMM),
            m.DrawBorderThenFill(hammer),
        )

        rt = 1.25

        self.play(
            m.Indicate(NMM_sides, scale_factor=1, color=RwthTheme.rwth_bordeaux_75, rate_func=m.there_and_back_with_pause,
                       run_time=rt),
            m.Indicate(hammer_head_outer, scale_factor=1, color=RwthTheme.rwth_bordeaux_75,
                       rate_func=m.there_and_back_with_pause, run_time=rt),
            self.slide_index_transform()
        )

        self.add(hammer_head_inner)
        self.play(
            m.Indicate(milled_edges, scale_factor=1.05, color=RwthTheme.rwth_gruen_75, rate_func=m.there_and_back_with_pause,
                       run_time=rt),
            m.Indicate(hammer_head_inner, scale_factor=1.05, color=RwthTheme.rwth_gruen_75, rate_func=m.there_and_back_with_pause,
                       run_time=rt),
            self.slide_index_transform()
        )

        self.add(hammer_drill_segment)
        self.play(
            m.Indicate(drilling_ellipses, scale_factor=1.05, color=RwthTheme.rwth_orange_75, rate_func=m.there_and_back_with_pause,
                       run_time=rt),
            m.Indicate(hammer_drill_segment, scale_factor=1.05, color=RwthTheme.rwth_orange_75,
                       rate_func=m.there_and_back_with_pause,
                       run_time=rt),
            self.slide_index_transform()
        )

        NMM_sides.set_fill(opacity=0.5)
        hammer_head_outer.set_fill(opacity=0.5)
        self.add(hammer_head_outer, hammer_head_inner)
        self.play(
            m.Indicate(NMM_sides, scale_factor=1, color=RwthTheme.rwth_tuerkis_75, rate_func=m.there_and_back_with_pause, run_time=rt),
            m.Indicate(hammer_head_outer, scale_factor=1, color=RwthTheme.rwth_tuerkis_75, rate_func=m.there_and_back_with_pause,
                       run_time=rt),
            m.Indicate(hammer_head_inner, scale_factor=1, color=RwthTheme.rwth_tuerkis_75, rate_func=m.there_and_back_with_pause,
                       run_time=rt),
        )
        NMM_sides.set_fill(opacity=0)
        hammer_head_outer.set_fill(opacity=0)

        NMM.generate_target()
        NMM.target.move_to(3.5 * m.RIGHT + 1.75 * m.UP)
        NMM.target.scale(0.65)

        hammer.generate_target()
        hammer.target.move_to(3.5 * m.LEFT + 1.75 * m.UP)
        hammer.target.scale(0.65)

        self.play(
            m.MoveToTarget(NMM),
            m.MoveToTarget(hammer),
            self.slide_index_transform()
        )

        job0 = m.RoundedRectangle(
            corner_radius=0.125,
            height=3.0,
            width=5.5,
            fill_color=self.background_color_bright,
            fill_opacity=0.0,
            stroke_color=self.outline_color,
            stroke_width=1.0
        )
        job1 = m.RoundedRectangle(
            corner_radius=0.125,
            height=3.0,
            width=5.5,
            fill_color=self.background_color_bright,
            fill_opacity=0.0,
            stroke_color=self.outline_color,
            stroke_width=1.0
        )

        x_shift = 3.5
        job0.move_to(x_shift * m.LEFT - 1.5 * m.UP)
        job1.move_to(x_shift * m.RIGHT - 1.5 * m.UP)

        hammer_m1_name = self.term_text("Band Saw", color=RwthTheme.rwth_bordeaux_75)
        hammer_m2_name = self.term_text("Drill Press", color=RwthTheme.rwth_orange_75)
        hammer_m3_name = self.term_text("Milling Machine", color=RwthTheme.rwth_gruen_75)
        hammer_m4_name = self.term_text("Grinding Machine", color=RwthTheme.rwth_tuerkis_75)

        hammer_m1_dur = self.term_text("11 min", color=RwthTheme.rwth_bordeaux_75)
        hammer_m2_dur = self.term_text("3 min", color=RwthTheme.rwth_orange_75)
        hammer_m3_dur = self.term_text("3 min", color=RwthTheme.rwth_gruen_75)
        hammer_m4_dur = self.term_text("12 min", color=RwthTheme.rwth_tuerkis_75)

        hammer_m1_order = self.term_text("1.", color=RwthTheme.rwth_bordeaux_75)
        hammer_m2_order = self.term_text("2.", color=RwthTheme.rwth_orange_75)
        hammer_m3_order = self.term_text("3.", color=RwthTheme.rwth_gruen_75)
        hammer_m4_order = self.term_text("4.", color=RwthTheme.rwth_tuerkis_75)

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

        job0_title = self.term_text("Job 0").scale(1.0)
        job0_title.move_to(job0.get_top())

        job0_title_rectangle = m.RoundedRectangle(
            corner_radius=0.125,
            height=3.0,
            width=5.5,
            fill_color=self.background_color_bright,
            fill_opacity=1.0,
            stroke_color=self.outline_color,
            stroke_width=1.0
        ).scale_to_fit_height(job0_title.height + 0.5).move_to(job0_title.get_center())

        NMM_m1_name = self.term_text("Band Saw", color=RwthTheme.rwth_bordeaux_75)
        NMM_m2_name = self.term_text("Milling Machine", color=RwthTheme.rwth_gruen_75)
        NMM_m3_name = self.term_text("Drill Press", color=RwthTheme.rwth_orange_75)
        NMM_m4_name = self.term_text("Grinding Machine", color=RwthTheme.rwth_tuerkis_75)

        NMM_m1_dur = self.term_text("5 min", color=RwthTheme.rwth_bordeaux_75)
        NMM_m2_dur = self.term_text("16 min", color=RwthTheme.rwth_gruen_75)
        NMM_m3_dur = self.term_text("7 min", color=RwthTheme.rwth_orange_75)
        NMM_m4_dur = self.term_text("4 min", color=RwthTheme.rwth_tuerkis_75)

        NMM_m1_order = self.term_text("1.", color=RwthTheme.rwth_bordeaux_75)
        NMM_m2_order = self.term_text("2.", color=RwthTheme.rwth_gruen_75)
        NMM_m3_order = self.term_text("3.", color=RwthTheme.rwth_orange_75)
        NMM_m4_order = self.term_text("4.", color=RwthTheme.rwth_tuerkis_75)

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

        job1_title = self.term_text("Job 1").scale(1.0)
        job1_title.move_to(job1.get_top())

        job1_title_rectangle = m.RoundedRectangle(
            corner_radius=0.125,
            height=3.0,
            width=5.5,
            fill_color=self.background_color_bright,
            fill_opacity=1.0,
            stroke_color=self.outline_color,
            stroke_width=1.0
        ).scale_to_fit_height(job1_title.height + 0.5).move_to(job1_title.get_center())

        NMM_m1 = self.term_text("Cutting").scale(1.0).move_to(NMM_m1_name.get_center())
        NMM_m2 = self.term_text("Milling").scale(1.0).move_to(NMM_m2_name.get_center())
        NMM_m3 = self.term_text("Drilling").scale(1.0).move_to(NMM_m3_name.get_center())
        NMM_m4 = self.term_text("Grinding").scale(1.0).move_to(NMM_m4_name.get_center())

        hammer_m1 = self.term_text("Cutting").scale(1.0).move_to(hammer_m1_name)
        hammer_m2 = self.term_text("Drilling").scale(1.0).move_to(hammer_m2_name)
        hammer_m3 = self.term_text("Milling").scale(1.0).move_to(hammer_m3_name)
        hammer_m4 = self.term_text("Grinding").scale(1.0).move_to(hammer_m4_name)

        self.play(
            m.FadeIn(NMM_m1),
            m.FadeIn(NMM_m2),
            m.FadeIn(NMM_m3),
            m.FadeIn(NMM_m4),

            m.FadeIn(hammer_m1),
            m.FadeIn(hammer_m2),
            m.FadeIn(hammer_m3),
            m.FadeIn(hammer_m4),

        )

        # machine 1
        rt = 0.75
        hammer_m1.generate_target()
        hammer_m1.target.set_color(RwthTheme.rwth_bordeaux_75)
        NMM_m1.generate_target()
        NMM_m1.target.set_color(RwthTheme.rwth_bordeaux_75)

        self.play(
            m.Indicate(NMM_sides, scale_factor=1, color=RwthTheme.rwth_bordeaux_75, rate_func=m.there_and_back_with_pause,
                       run_time=rt),
            m.Indicate(hammer_head_outer, scale_factor=1, color=RwthTheme.rwth_bordeaux_75,
                       rate_func=m.there_and_back_with_pause, run_time=rt),
            m.MoveToTarget(hammer_m1, run_time=0.3 * rt),
            m.MoveToTarget(NMM_m1, run_time=0.3 * rt),
        )

        # machine 2
        hammer_m2.generate_target()
        hammer_m2.target.set_color(RwthTheme.rwth_orange_75)
        NMM_m2.generate_target()
        NMM_m2.target.set_color(RwthTheme.rwth_gruen_75)

        self.add(hammer_drill_segment)

        self.play(
            m.Indicate(milled_edges, scale_factor=1.05, color=RwthTheme.rwth_gruen_75, rate_func=m.there_and_back_with_pause,
                       run_time=rt),
            m.Indicate(hammer_drill_segment, scale_factor=1.05, color=RwthTheme.rwth_orange_75,
                       rate_func=m.there_and_back_with_pause,
                       run_time=rt),
            m.MoveToTarget(hammer_m2, run_time=0.3 * rt),
            m.MoveToTarget(NMM_m2, run_time=0.3 * rt),
        )

        # machine 3
        hammer_m3.generate_target()
        hammer_m3.target.set_color(RwthTheme.rwth_gruen_75)
        NMM_m3.generate_target()
        NMM_m3.target.set_color(RwthTheme.rwth_orange_75)

        self.add(hammer_head_inner)

        self.play(
            m.Indicate(drilling_ellipses, scale_factor=1.05, color=RwthTheme.rwth_orange_75,
                       rate_func=m.there_and_back_with_pause,
                       run_time=rt),
            m.Indicate(hammer_head_inner, scale_factor=1.05, color=RwthTheme.rwth_gruen_75,
                       rate_func=m.there_and_back_with_pause,
                       run_time=rt),
            m.MoveToTarget(hammer_m3, run_time=0.3 * rt),
            m.MoveToTarget(NMM_m3, run_time=0.3 * rt),
        )

        # machine 4

        hammer_m4.generate_target()
        hammer_m4.target.set_color(RwthTheme.rwth_tuerkis_75)
        NMM_m4.generate_target()
        NMM_m4.target.set_color(RwthTheme.rwth_tuerkis_75)

        NMM_sides.set_fill(opacity=0.5)
        hammer_head_outer.set_fill(opacity=0.5)
        self.add(hammer_head_outer)

        # machine 4

        hammer_m4.generate_target()
        hammer_m4.target.set_color(RwthTheme.rwth_tuerkis_75)
        NMM_m4.generate_target()
        NMM_m4.target.set_color(RwthTheme.rwth_tuerkis_75)

        NMM_sides.set_fill(opacity=0.5)
        hammer_head_outer.set_fill(opacity=0.5)
        self.add(hammer_head_outer)

        self.play(
            m.Indicate(NMM_sides, scale_factor=1, color=RwthTheme.rwth_tuerkis_75, rate_func=m.there_and_back_with_pause,
                       run_time=rt),
            m.Indicate(hammer_head_outer, scale_factor=1, color=RwthTheme.rwth_tuerkis_75,
                       rate_func=m.there_and_back_with_pause, run_time=rt),
            m.Indicate(hammer_head_inner, scale_factor=1, color=RwthTheme.rwth_tuerkis_75,
                       rate_func=m.there_and_back_with_pause, run_time=rt),
            m.MoveToTarget(hammer_m4, run_time=0.3 * rt),
            m.MoveToTarget(NMM_m4, run_time=0.3 * rt),
        )
        NMM_sides.set_fill(opacity=0)
        hammer_head_outer.set_fill(opacity=0)

        self.play(
            m.Transform(hammer_m1, hammer_m1_name),
            m.Transform(hammer_m2, hammer_m2_name),
            m.Transform(hammer_m3, hammer_m3_name),
            m.Transform(hammer_m4, hammer_m4_name),

            m.Transform(NMM_m1, NMM_m1_name),
            m.Transform(NMM_m2, NMM_m2_name),
            m.Transform(NMM_m3, NMM_m3_name),
            m.Transform(NMM_m4, NMM_m4_name),

        )

        self.play(
            m.FadeIn(job0_table),
            m.FadeIn(job1_table),
        )

        # add job frames
        job0.set_z_index(job0_table.z_index - 3)
        job0_title_rectangle.set_z_index(job0_table.z_index - 2)
        job0_title.set_z_index(job0_table.z_index - 1)

        job1.set_z_index(job1_table.z_index - 3)
        job1_title_rectangle.set_z_index(job1_table.z_index - 2)
        job1_title.set_z_index(job1_table.z_index - 1)

        self.remove(hammer_m1, hammer_m2, hammer_m3, hammer_m4, NMM_m1, NMM_m2, NMM_m3, NMM_m4)

        job0_group = m.VGroup(
            job0,
            job0_table,
            job0_title_rectangle,
            job0_title
        )
        job1_group = m.VGroup(
            job1,
            job1_table,
            job1_title_rectangle,
            job1_title
        )


        job1_table_copy = job1_table.copy()
        job0_table_copy = job0_table.copy()
        self.add(job1_table_copy, job0_table_copy)
        self.play(
            m.FadeIn(job0_group),
            m.FadeIn(job1_group),
        )
        self.remove(job1_table_copy, job0_table_copy)

        job0_group.generate_target()
        job0_group.target.move_to([-3.5, 1.655, 0]).scale(0.7)
        job1_group.generate_target()
        job1_group.target.move_to([3.5, 1.625, 0]).scale(0.7)

        self.play(
            m.FadeOut(hammer, run_time=0.5),
            m.FadeOut(NMM, run_time=0.5),
            m.MoveToTarget(job0_group),
            m.MoveToTarget(job1_group),
        )

        axes = m.Axes(
            x_range=[0, 41, 1],
            y_range=[0, 4, 1],
            x_length=10.5,
            y_length=3.25,
            y_axis_config={"tick_size": 0},
            x_axis_config={"tick_size": 0},
            axis_config={"include_numbers": False, "tip_width": 0.125, "tip_height": 0.25},

        )

        axes.move_to([0.5, -1.125, 0])
        axes.set_color(RwthTheme.rwth_schwarz_75)
        labels = axes.get_axis_labels(x_label=self.term_text("time").scale(1.0), y_label='')
        labels.set_color(RwthTheme.rwth_blau_75)

        job0_title.generate_target()
        job0_title.target.move_to(axes.c2p(-4, 2.5))
        job0_title.target.scale(1.25)

        job1_title.generate_target()
        job1_title.target.move_to(axes.c2p(-4, 1.5))
        job1_title.target.scale(1.25)

        job0.generate_target()
        job0.target.stroke_opacity = 0.0

        job1.generate_target()
        job1.target.stroke_opacity = 0.0


        self.play(
            m.DrawBorderThenFill(axes),
            m.DrawBorderThenFill(labels),
            m.MoveToTarget(job0_title),
            m.MoveToTarget(job1_title),

            m.FadeOut(job0_title_rectangle),
            m.FadeOut(job1_title_rectangle),

            m.FadeOut(job1),
            m.FadeOut(job0),
        )

        # table to rects
        rect_scale = 0.05
        hammer_m1_rect = m.Rectangle(width=11, height=5, color=RwthTheme.rwth_bordeaux_75, fill_opacity=1) \
            .scale(rect_scale) \
            .move_to(hammer_m1_name.get_center())
        hammer_m2_rect = m.Rectangle(width=3, height=5, color=RwthTheme.rwth_orange_75, fill_opacity=1) \
            .scale(rect_scale) \
            .move_to(hammer_m2_name.get_center())
        hammer_m3_rect = m.Rectangle(width=3, height=5, color=RwthTheme.rwth_gruen_75, fill_opacity=1) \
            .scale(rect_scale) \
            .move_to(hammer_m3_name.get_center())
        hammer_m4_rect = m.Rectangle(width=12, height=5, color=RwthTheme.rwth_tuerkis_75, fill_opacity=1) \
            .scale(rect_scale) \
            .move_to(hammer_m4_name.get_center())

        NMM_m1_rect = m.Rectangle(width=5, height=5, color=RwthTheme.rwth_bordeaux_75, fill_opacity=1) \
            .scale(rect_scale) \
            .move_to(NMM_m1_name.get_center())
        NMM_m2_rect = m.Rectangle(width=16, height=5, color=RwthTheme.rwth_gruen_75, fill_opacity=1) \
            .scale(rect_scale) \
            .move_to(NMM_m2_name.get_center())
        NMM_m3_rect = m.Rectangle(width=7, height=5, color=RwthTheme.rwth_orange_75, fill_opacity=1) \
            .scale(rect_scale) \
            .move_to(NMM_m3_name.get_center())
        NMM_m4_rect = m.Rectangle(width=4, height=5, color=RwthTheme.rwth_tuerkis_75, fill_opacity=1) \
            .scale(rect_scale) \
            .move_to(NMM_m4_name.get_center())

        self.play(
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

        # move rects to axes

        j0_t1 = m.Polygon(*[
            axes.c2p(5 + 11, 3),
            axes.c2p(5, 3),
            axes.c2p(5, 2),
            axes.c2p(16, 2),
        ], color=RwthTheme.rwth_bordeaux_75, fill_opacity=1, stroke_width=1)

        j0_t2 = m.Polygon(*[
            axes.c2p(16 + 3, 3),
            axes.c2p(16, 3),
            axes.c2p(16, 2),
            axes.c2p(19, 2),
        ], color=RwthTheme.rwth_orange_75, fill_opacity=1, stroke_width=1)

        j0_t3 = m.Polygon(*[
            axes.c2p(24, 3),
            axes.c2p(21, 3),
            axes.c2p(21, 2),
            axes.c2p(24, 2),
        ], color=RwthTheme.rwth_gruen_75, fill_opacity=1, stroke_width=1)

        j0_t4 = m.Polygon(*[
            axes.c2p(36, 3),
            axes.c2p(24, 3),
            axes.c2p(24, 2),
            axes.c2p(36, 2),
        ], color=RwthTheme.rwth_tuerkis_75, fill_opacity=1, stroke_width=1)

        j1_t1 = m.Polygon(*[
            axes.c2p(5, 2),
            axes.c2p(0, 2),
            axes.c2p(0, 1),
            axes.c2p(5, 1),
        ], color=RwthTheme.rwth_bordeaux_75, fill_opacity=1, stroke_width=1)

        j1_t2 = m.Polygon(*[
            axes.c2p(21, 2),
            axes.c2p(5, 2),
            axes.c2p(5, 1),
            axes.c2p(21, 1),
        ], color=RwthTheme.rwth_gruen_75, fill_opacity=1, stroke_width=1)

        j1_t3 = m.Polygon(*[
            axes.c2p(28, 2),
            axes.c2p(21, 2),
            axes.c2p(21, 1),
            axes.c2p(28, 1),
        ], color=RwthTheme.rwth_orange_75, fill_opacity=1, stroke_width=1)

        j1_t4 = m.Polygon(*[
            axes.c2p(40, 2),
            axes.c2p(36, 2),
            axes.c2p(36, 1),
            axes.c2p(40, 1),
        ], color=RwthTheme.rwth_tuerkis_75, fill_opacity=1, stroke_width=1)

        self.play(
            m.Transform(hammer_m1_rect, j0_t1, replace_mobject_with_target_in_scene=True),
            m.Transform(hammer_m2_rect, j0_t2, replace_mobject_with_target_in_scene=True),
            m.Transform(hammer_m3_rect, j0_t3, replace_mobject_with_target_in_scene=True),
            m.Transform(hammer_m4_rect, j0_t4, replace_mobject_with_target_in_scene=True),

            m.Transform(NMM_m1_rect, j1_t1, replace_mobject_with_target_in_scene=True),
            m.Transform(NMM_m2_rect, j1_t2, replace_mobject_with_target_in_scene=True),
            m.Transform(NMM_m3_rect, j1_t3, replace_mobject_with_target_in_scene=True),
            m.Transform(NMM_m4_rect, j1_t4, replace_mobject_with_target_in_scene=True),
        )

        self.play(
            self.overlay_scene()
        )



if __name__ == '__main__':
    CJspIntro.save_sections_without_cache()