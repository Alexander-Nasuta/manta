import manim as m
import numpy as np

from color_theme.carolus.corolus_theme import CarolusTheme
from color_theme.rwth.rwth_theme import RwthTheme
from components.axes_utils import AxesUtils
from components.gantt_utils import GanttUtils
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate
from slide_templates.rwth.rwth_slide_template import RwthSlideTemplate


class BMotivationHistory(RwthTheme, AxesUtils, GanttUtils, RwthSlideTemplate):

    # font_name = "IosevkaTermSlab Nerd Font Mono"

    logo_paths = [
        "iop_logo.png"
    ]
    logo_height = 0.6
    index_prefix = "A "

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
                title="Motivation",
                seperator=": ",
                subtitle="Evolution of Production"
            ),
            self.add_logos(),
            self.add_seperator_line_top(),
            self.add_seperator_line_bottom()
        )

        axes = self.term_axes_minimal(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=8.5,
            y_length=5.0,
            y_axis_config={"tick_size": 0},
            x_axis_config={"tick_size": 0},
            axis_config={
                "include_numbers": False,
                "tip_width": 0.125,
                "tip_height": 0.25,
                "color": RwthTheme.rwth_schwarz_75,
            },

        )

        axes.move_to([0.5, 0.0, 0])

        x_label = self.term_text(
            "Product Variety",
            font_size = self.font_size_small,
            font_color=RwthTheme.rwth_blau_100
        )
        x_label.next_to(axes.x_axis.get_end(), m.DOWN, buff=0.25)

        y_label = self.term_text(
            "Product Volume \n per Variant",
            font_size=self.font_size_small,
            font_color = RwthTheme.rwth_blau_100
        )
        y_label.next_to(axes.y_axis.get_end(), m.LEFT, buff=0.25)


        # dots = [m.Dot(point, color=C.PINK) for point in manim_points]

        coord_pre_1850 = axes.c2p(9, 0.6)
        coord_1850 = axes.c2p(8.25, 0.6)
        coord_1913 = axes.c2p(1.675, 3.75)
        coord_1955 = axes.c2p(1.375, 8.75)
        coord_1980 = axes.c2p(4.5, 7.6)
        coord_2000 = axes.c2p(6.6, 5.7)
        coord_post_2000 = axes.c2p(9, 2.7)

        dot_label_scale = 0.325
        phase_label_scale = 0.325
        curve_color = RwthTheme.rwth_blau_75
        dot_color = RwthTheme.rwth_blau_100

        # bezier curve from pre 1850 to 1850
        bezier_pre_1850_to_1850 = m.CubicBezier(
            coord_pre_1850,
            coord_1850,
            coord_1850,
            coord_1850,
            color=curve_color,
            stroke_width=3
        )

        dot_1850 = m.Dot(coord_1850, color=dot_color)
        dot_1850_label = self.term_text("1850", color=dot_color, font_size=self.font_size_script).next_to(dot_1850, m.UP, buff=0.1)


        # bezier curve from 1850 to 1913
        bezier_1850_to_1913 = m.CubicBezier(
            coord_1850,
            coord_1850 + m.LEFT * 2.2,
            coord_1913 + m.DOWN * 1.7 + m.RIGHT * 1.1,
            coord_1913,
            color=curve_color,
            stroke_width=3
        )

        # set z index to dot_1850 -1
        # bezier_1850_to_1913.set_z_index(dot_1850.z_index - 1)

        dot_1913 = m.Dot(coord_1913, color=dot_color)
        dot_1913_label = self.term_text("1913", color=dot_color, font_size=self.font_size_script).next_to(dot_1913, m.UR, buff=0.1)


        phase_text_1850_to_1913 = self.term_text("Craft Production", color=dot_color, font_size=self.font_size_script)
        phase_text_1850_to_1913.next_to(bezier_1850_to_1913.point_from_proportion(0.75), m.UR, buff=0.1)


        bezier_1913_to_1955 = m.CubicBezier(
            coord_1913,
            coord_1913 + m.UP * 1.7 * 0.4 + m.LEFT * 1.1 * 0.4,
            coord_1955 + m.DOWN * 0.7 + m.LEFT * 0.7,
            coord_1955,
            color=curve_color,
            stroke_width=3
        )

        # set z index to dot_1913 -1
        # bezier_1913_to_1955.set_z_index(dot_1913.z_index - 1)

        dot_1955 = m.Dot(coord_1955, color=dot_color)
        dot_1955_label = self.term_text("1955", color=dot_color, font_size=self.font_size_script).next_to(dot_1955, m.DR, buff=0.1)


        bezier_1955_to_1980 = m.CubicBezier(
            coord_1955,
            coord_1955 + m.UP * 0.7 * 0.55 + m.RIGHT * 0.7 * 0.55,
            coord_1980 + m.UP * 0.8 + m.LEFT * 1.3,
            coord_1980,
            color=curve_color,
            stroke_width=3
        )

        # set z index to dot_1955 -1
        # bezier_1955_to_1980.set_z_index(dot_1955.z_index - 1)

        dot_1980 = m.Dot(coord_1980, color=dot_color)
        dot_1980_label = self.term_text("1980", color=dot_color, font_size=self.font_size_script).next_to(dot_1980, m.DOWN, buff=0.1)


        phase_text_1980 = self.term_text("Mass Production", color=dot_color, font_size=self.font_size_script)
        phase_text_1980.next_to(bezier_1955_to_1980.point_from_proportion(0.5), m.UP, buff=0.2)


        bezier_1980_to_2000 = m.CubicBezier(
            coord_1980,
            (coord_1980 + coord_2000) / 2,
            (coord_2000 + coord_1980) / 2,
            # coord_1980 + m.DOWN * 0.6 * 0.2 + m.RIGHT * 1.3 * 0.2,
            # coord_2000 + m.UP * 0.8 + m.LEFT * 1.3,
            coord_2000,
            color=curve_color,
            stroke_width=3
        )

        # set z index
        #bezier_1980_to_2000.set_z_index(dot_1980.z_index - 1)

        dot_2000 = m.Dot(coord_2000, color=dot_color)
        dot_2000_label = self.term_text("2000", color=dot_color, font_size=self.font_size_script).next_to(dot_2000, m.DOWN, buff=0.1)


        phase_text_1980_to_2000 = self.term_text("Mass Customization", color=dot_color, font_size=self.font_size_script)
        phase_text_1980_to_2000.next_to(bezier_1980_to_2000.point_from_proportion(0.5), m.UR, buff=0.15)


        bezier_2000_to_post_2000 = m.CubicBezier(
            coord_2000,
            coord_2000 + m.DOWN * 0.8 * 0.4 + m.RIGHT * 1.3 * 0.4,
            coord_post_2000 + m.UP * 0.9 + m.LEFT * 0.8,
            coord_post_2000, color=curve_color,
            stroke_width=3
        )
        # set z index to dot_2000 -1
        #bezier_2000_to_post_2000.set_z_index(dot_2000.z_index - 1)

        arrow = m.Arrow(
            start=coord_post_2000,
            end=coord_post_2000 + m.DOWN * 0.9 * 0.5 + m.RIGHT * 0.8 * 0.5,
            buff=0,
            color=curve_color,
            stroke_width=3
        )


        phase_text_post_2000 = self.term_text("Personalized Production", color=dot_color, font_size=self.font_size_script)
        phase_text_post_2000.next_to(bezier_2000_to_post_2000.point_from_proportion(0.5), m.UR, buff=0.1)


        curve_animation_group = m.AnimationGroup(
            *[
                m.Create(curve, run_time=curve.get_arc_length() / 20, rate_func=m.linear)
                for curve in [
                    bezier_pre_1850_to_1850,
                    bezier_1850_to_1913,
                    bezier_1913_to_1955,
                    bezier_1955_to_1980,
                    bezier_1980_to_2000,
                    bezier_2000_to_post_2000,
                ]
            ],
            lag_ratio=1,
        )
        dot_animation_group = m.AnimationGroup(
            m.FadeIn(dot_1850),
            m.FadeIn(dot_1913),
            m.FadeIn(dot_1955),
            m.FadeIn(dot_1980),
            m.FadeIn(dot_2000),
            lag_ratio=0.1
        )
        dot_label_animations = m.AnimationGroup(
            m.FadeIn(dot_1850_label),
            m.FadeIn(dot_1913_label),
            m.FadeIn(dot_1955_label),
            m.FadeIn(dot_1980_label),
            m.FadeIn(dot_2000_label),
            lag_ratio=0.1
        )

        phase_label_animations = m.AnimationGroup(
            m.FadeIn(phase_text_1850_to_1913),
            m.FadeIn(phase_text_1980),
            m.FadeIn(phase_text_1980_to_2000),
            m.FadeIn(phase_text_post_2000),
            lag_ratio=0.15
        )


        axes_creation_group = m.AnimationGroup(
            m.GrowFromEdge(axes, edge=m.DL),
            m.FadeIn(y_label),
            m.FadeIn(x_label),
            lag_ratio=0.1,
        )


        chart_animation_group = m.AnimationGroup(
            axes_creation_group,
            m.AnimationGroup(
                curve_animation_group,
                dot_animation_group,
                dot_label_animations,
                phase_label_animations
            ),
            lag_ratio=0.35
        )


        self.play(
            chart_animation_group
        )

        # group axes, dots and curves
        chart_group = m.VGroup(
            axes,
            bezier_pre_1850_to_1850,
            bezier_1850_to_1913,
            bezier_1913_to_1955,
            bezier_1980_to_2000,
            bezier_2000_to_post_2000,
            dot_1850,
            dot_1850_label,
            dot_1913,
            dot_1913_label,
            phase_text_1850_to_1913,
            dot_1955,
            dot_1955_label,
            bezier_1955_to_1980,
            dot_1980,
            dot_1980_label,
            phase_text_1980,
            dot_2000,
            dot_2000_label,
            phase_text_1980_to_2000,
            phase_text_post_2000,
        )

        chart_group.generate_target()
        chart_group.target.scale(0.6)
        chart_group.target.to_edge(m.RIGHT, buff=self.med_large_buff)
        chart_group.target.to_edge(m.UP, buff=1.3)


        # Trends towards customised and personalised products
        bullet0 = self.icon_textbox(
            "Trends towards customised and personalised products",
            icon=0xF0C0,
            width=7.25,
            height=1.0,
            font_size=16,
        )
        bullet0.next_to(self._title_mobject, m.DOWN, buff=self.med_large_buff, aligned_edge=m.LEFT)

        bullet1 =  self.icon_textbox(
            "Product variety yields combinatorial optimization\n problems",
            width=7.25,
            height=1.0,
            icon=0xF08D6,
            font_size = 16,
        )
        bullet1.next_to(bullet0, m.DOWN, buff=self.med_small_buff, aligned_edge=m.LEFT)

        bullet2 = self.icon_textbox(
            "Increased need for systems capable of dealing with dynamic\n circumstances",
            width=7.25,
            height=1.0,
            icon=0xF05CE,
            font_size=16,
        )
        bullet2.next_to(bullet1, m.DOWN, buff=self.med_small_buff, aligned_edge=m.LEFT)


        fade_in_bullets = m.AnimationGroup(
            m.FadeIn(bullet0),
            m.FadeIn(bullet1),
            m.FadeIn(bullet2),
            lag_ratio=0.15
        )


        chart_transition = m.AnimationGroup(
            m.MoveToTarget(chart_group),
            m.FadeOut(x_label),
            m.FadeOut(y_label),
        )

        self.play(
            self.change_subtitle("Situation"),
            m.AnimationGroup(
                chart_transition,
                fade_in_bullets,
                lag_ratio=0.35
            )
        )


        rect_examples_shift = 0.175
        rect_example_width = (self.content_width - 2 * self.med_large_buff) / 3

        gantt_data = [
            {'Task': 'Job 0', 'Start': 5, 'Finish': 16, 'Resource': 'Machine 0'},
            {'Task': 'Job 0', 'Start': 28, 'Finish': 31, 'Resource': 'Machine 1'},
            {'Task': 'Job 0', 'Start': 31, 'Finish': 34, 'Resource': 'Machine 2'},
            {'Task': 'Job 0', 'Start': 34, 'Finish': 46, 'Resource': 'Machine 3'},
            {'Task': 'Job 1', 'Start': 0, 'Finish': 5, 'Resource': 'Machine 0'},
            {'Task': 'Job 1', 'Start': 5, 'Finish': 21, 'Resource': 'Machine 2'},
            {'Task': 'Job 1', 'Start': 21, 'Finish': 28, 'Resource': 'Machine 1'},
            {'Task': 'Job 1', 'Start': 28, 'Finish': 32, 'Resource': 'Machine 3'}
        ]

        gantt_chart = self.gantt_chart_without_ticks(
            width=4, height=2, data=gantt_data, n_machines=4, resource_naming="Machine",
            axis_config_kwargs={
                "color": RwthTheme.rwth_schwarz_75,
            }
        ).scale_to_fit_width(rect_example_width - 2 * self.med_large_buff)

        gantt_chart_rect = self.wrap_with_rectangle(
            gantt_chart,
            # if with is not set, the width will be calculated automatically
            # same for height
            width=rect_example_width,
            height=5.75,
        ).next_to(self._title_mobject, m.DOWN, buff=self.med_large_buff, aligned_edge=m.LEFT)


        gantt_chart_rect_title = self.term_text("Scheduling", font_size=self.font_size_small)
        gantt_chart_rect_title.next_to(gantt_chart_rect.get_top(), m.DOWN, buff=0.175)

        gantt_chart_rect_line = m.Line(gantt_chart_rect.get_left(), gantt_chart_rect.get_right(), color=self.outline_color, stroke_width=1.0)
        gantt_chart_rect_line.next_to(gantt_chart_rect.get_top(), m.DOWN, buff=0.6)

        gantt_rect_group = m.VGroup(
            gantt_chart_rect, gantt_chart_rect_title, gantt_chart_rect_line
        )



        assignment_circle_radius = 0.25
        worker_color = self.blue
        task_color = self.red

        worker_circle_0 = self.math_circle("w_0", radius=assignment_circle_radius, fill_color=self.yellow, stroke_color=worker_color, font_color=self.black)
        worker_circle_1 =  self.math_circle("w_1", radius=assignment_circle_radius, fill_color=self.yellow, stroke_color=worker_color, font_color=self.black)
        worker_circle_2 =  self.math_circle("w_2", radius=assignment_circle_radius, fill_color=self.yellow, stroke_color=worker_color, font_color=self.black)
        worker_circle_3 =  self.math_circle("w_3", radius=assignment_circle_radius, fill_color=self.yellow, stroke_color=worker_color, font_color=self.black)

        task_circle_0 =  self.math_circle("t_0", radius=assignment_circle_radius, stroke_color=task_color, fill_color=self.yellow, font_color=self.black)
        task_circle_1 =  self.math_circle("t_1", radius=assignment_circle_radius, stroke_color=task_color, fill_color=self.yellow, font_color=self.black)
        task_circle_2 =  self.math_circle("t_2", radius=assignment_circle_radius, stroke_color=task_color, fill_color=self.yellow, font_color=self.black)
        task_circle_3 =  self.math_circle("t_3", radius=assignment_circle_radius, stroke_color=task_color, fill_color=self.yellow, font_color=self.black)

        worker_circle_1.next_to(worker_circle_0, m.DOWN, buff=self.med_small_buff)
        worker_circle_2.next_to(worker_circle_1, m.DOWN, buff=self.med_small_buff)
        worker_circle_3.next_to(worker_circle_2, m.DOWN, buff=self.med_small_buff)

        task_circle_0.next_to(worker_circle_0, m.RIGHT, buff=1)
        task_circle_1.next_to(worker_circle_1, m.RIGHT, buff=1)
        task_circle_2.next_to(worker_circle_2, m.RIGHT, buff=1)
        task_circle_3.next_to(worker_circle_3, m.RIGHT, buff=1)

        arrow_kwargs = {
            "tip_shape": m.ArrowTriangleFilledTip,
            "tip_length": 0.175,
            "stroke_width": 3,
            "buff": 0,
            "color": self.font_color_secondary
        }

        # arrows
        # w0 -> t_2
        # w1 -> t_0
        # w2 -> t_3
        # w3 -> t_1

        arrow_w0_t2 = m.Arrow(
            start=worker_circle_0.get_right(),
            end=task_circle_2.get_left(),
            **arrow_kwargs
        )

        arrow_w1_t0 = m.Arrow(
            start=worker_circle_1.get_right(),
            end=task_circle_0.get_left(),
            **arrow_kwargs
        )

        arrow_w2_t3 = m.Arrow(
            start=worker_circle_2.get_right(),
            end=task_circle_3.get_left(),
            **arrow_kwargs
        )

        arrow_w3_t1 = m.Arrow(
            start=worker_circle_3.get_right(),
            end=task_circle_1.get_left(),
            **arrow_kwargs
        )

        assignment_group = m.VGroup(
            arrow_w0_t2, arrow_w1_t0, arrow_w2_t3, arrow_w3_t1,
            worker_circle_0, worker_circle_1, worker_circle_2, worker_circle_3,
            task_circle_0, task_circle_1, task_circle_2, task_circle_3,
        )

        assignment_group_rect = self.wrap_with_rectangle(
            assignment_group,
            width=rect_example_width,
            height=5.75,
        ).next_to(gantt_chart_rect, m.RIGHT, buff=self.med_large_buff)


        assignment_group_title = self.term_text("Personal Assignment", font_size=self.font_size_small)
        assignment_group_title.next_to(assignment_group_rect.get_top(), m.DOWN, buff=0.175)

        assignment_group_line = m.Line(assignment_group_rect.get_left(), assignment_group_rect.get_right(), color=self.outline_color, stroke_width=1.0)
        assignment_group_line.next_to(assignment_group_rect.get_top(), m.DOWN, buff=0.6)

        assignment_group2 = m.VGroup(
            assignment_group_rect, assignment_group_title, assignment_group_line
        )



        tsp_circle_radius = 0.25
        tsp_node_0 = self.math_circle("A", radius=tsp_circle_radius, fill_color=self.yellow, stroke_color=worker_color, font_color=self.black)
        tsp_node_1 = self.math_circle("B", radius=tsp_circle_radius, fill_color=self.yellow, stroke_color=worker_color, font_color=self.black)
        tsp_node_2 = self.math_circle("C", radius=tsp_circle_radius, fill_color=self.yellow, stroke_color=worker_color, font_color=self.black)
        tsp_node_3 = self.math_circle("D", radius=tsp_circle_radius, fill_color=self.yellow, stroke_color=worker_color, font_color=self.black)
        tsp_node_4 = self.math_circle("E", radius=tsp_circle_radius, fill_color=self.yellow, stroke_color=worker_color, font_color=self.black)

        scale_shift = 0.625
        tsp_node_1.move_to(np.array([1, -3, 0]) * scale_shift)
        tsp_node_2.move_to(np.array([2.5, -2, 0]) * scale_shift)
        tsp_node_3.move_to(np.array([3.5, -4, 0]) * scale_shift)
        tsp_node_4.move_to(np.array([3.75, 1, 0]) * scale_shift)

        # tsp edges
        # A-B-E-D-C-A
        tsp_edge_1 = m.Line(tsp_node_0.get_center(), tsp_node_1.get_center(), color=self.font_color_secondary, stroke_width=3)
        tsp_edge_2 = m.Line(tsp_node_1.get_center(), tsp_node_4.get_center(), color=self.font_color_secondary, stroke_width=3)
        tsp_edge_3 = m.Line(tsp_node_4.get_center(), tsp_node_3.get_center(), color=self.font_color_secondary, stroke_width=3)
        tsp_edge_4 = m.Line(tsp_node_3.get_center(), tsp_node_2.get_center(), color=self.font_color_secondary, stroke_width=3)
        tsp_edge_5 = m.Line(tsp_node_2.get_center(), tsp_node_0.get_center(), color=self.font_color_secondary, stroke_width=3)

        tsp_edges = m.VGroup(
            tsp_edge_1, tsp_edge_2, tsp_edge_3, tsp_edge_4, tsp_edge_5
        )

        tsp_group = m.VGroup(tsp_edges,
                             tsp_node_0, tsp_node_1, tsp_node_2, tsp_node_3, tsp_node_4
                             )

        tsp_rect = self.wrap_with_rectangle(
            tsp_group,
            width=rect_example_width,
            height=5.75,
        ).next_to(assignment_group_rect, m.RIGHT, buff=self.med_large_buff)


        tsp_title = self.term_text("Routing", font_size=self.font_size_small)
        tsp_title.next_to(tsp_rect.get_top(), m.DOWN, buff=0.175)

        tsp_line = m.Line(tsp_rect.get_left(), tsp_rect.get_right(), color=self.outline_color, stroke_width=1.0)
        tsp_line.next_to(tsp_rect.get_top(), m.DOWN, buff=0.6)

        tsp_rect_group = m.VGroup(
            tsp_rect, tsp_title, tsp_line
        )



        slide_fade_out = m.AnimationGroup(
            self.change_subtitle("Example Problems"),
            m.FadeOut(bullet0),
            m.FadeOut(bullet1),
            m.FadeOut(bullet2),
            m.FadeOut(chart_group),
            lag_ratio=0.15
        )


        slide_fade_in = m.AnimationGroup(
            m.FadeIn(gantt_rect_group),
            m.FadeIn(assignment_group2),
            m.FadeIn(tsp_rect_group),
            lag_ratio=0.15
        )


        self.play(
            m.AnimationGroup(
                slide_fade_out,
                slide_fade_in,
                lag_ratio=0.65
            )
        )

        scale_graph = 0.675

        graph_shift = 1.0
        shift_offset = 0.375 * m.DOWN

        tsp_group.generate_target()
        tsp_group.target.scale(scale_graph)
        tsp_group.target.to_edge(m.RIGHT, buff=0.6)
        tsp_group.target.shift(m.UP * graph_shift + shift_offset)

        assignment_group.generate_target()
        assignment_group.target.scale(scale_graph)
        assignment_group.target.next_to(tsp_group.target, m.LEFT, buff=0.6)
        assignment_group.target.shift(m.UP * graph_shift + shift_offset)

        gantt_chart.generate_target()
        gantt_chart.target.to_edge(m.RIGHT, buff=0.6)
        gantt_chart.target.scale_to_fit_width(m.VGroup(assignment_group.target, tsp_group.target).width - 0.05)
        gantt_chart.target.shift(m.DOWN * graph_shift + shift_offset)

        bullet_rect_example_width = m.VGroup(gantt_rect_group, assignment_group2).width

        offline_bullet_point_rect = self.icon_title_bulletpoints_textbox(
            [
                ("Offline Approaches", ["Time-intensive approaches", "manual adjustments for short-term changes"]),
            ],
            icon='router-wireless-off',
            icon_color=self.red,
            bullet_icon_color=self.red,
            font_size=18,
            bullet_icon_kwargs={},
            width=bullet_rect_example_width,
        )

        offline_bullet_point_rect.next_to(self._title_mobject, m.DOWN, buff=self.med_large_buff, aligned_edge=m.LEFT)

        online_bullet_point_rect = self.icon_title_bulletpoints_textbox(
            [
                ("Online Approaches", ["Heuristics", "Reinforcement Learning", "Search Algorithms"]),
            ],
            icon='router-wireless',
            icon_color=self.green,
            bullet_icon_color=self.green,
            font_size=18,
            width=bullet_rect_example_width,
        )

        online_bullet_point_rect.next_to(offline_bullet_point_rect, m.DOWN, buff=self.med_large_buff, aligned_edge=m.LEFT)

        slide_fade_out = m.AnimationGroup(
            m.FadeOut(gantt_chart_rect),
            m.FadeOut(gantt_chart_rect_title),
            m.FadeOut(gantt_chart_rect_line),

            m.FadeOut(assignment_group_rect),
            m.FadeOut(assignment_group_title),
            m.FadeOut(assignment_group_line),

            m.FadeOut(tsp_rect),
            m.FadeOut(tsp_title),
            m.FadeOut(tsp_line),

            m.MoveToTarget(tsp_group),
            m.MoveToTarget(assignment_group),
            m.MoveToTarget(gantt_chart),
        )

        self.play(
            self.change_subtitle("Solution Approaches"),
            m.AnimationGroup(
                slide_fade_out,
                m.AnimationGroup(
                    m.FadeIn(offline_bullet_point_rect),
                    m.FadeIn(online_bullet_point_rect),
                    lag_ratio=0.15
                ),
                lag_ratio=0.35
            )
        )

        # tsp_group
        tsp_group.scale(scale_graph)
        tsp_group.to_edge(m.RIGHT, buff=0.6)
        tsp_group.shift(m.UP * graph_shift + shift_offset)

        # assignment_group.generate_target()
        assignment_group.scale(scale_graph)
        assignment_group.next_to(tsp_group.target, m.LEFT, buff=0.6)
        assignment_group.shift(m.UP * graph_shift + shift_offset)

        #gantt_chart.generate_target()
        gantt_chart.to_edge(m.RIGHT, buff=0.6)
        gantt_chart.scale_to_fit_width(m.VGroup(assignment_group.target, tsp_group.target).width - 0.05)
        gantt_chart.shift(m.DOWN * graph_shift + shift_offset)


        summary_box1 = self.icon_title_bulletpoints_textbox(
            [
                ("Personalized production yields a high degree of flexibility in the production\nenvironment",
                 [
                     "Assigning tasks to machines",
                     "Assigning personal to machines",
                     "Offline approach es are not feasible",
                 ]),
            ],
            icon='factory',
            icon_color=RwthTheme.rwth_blau_75,
            bullet_icon_color=RwthTheme.rwth_blau_75,
            font_size=18,
            bullet_icon_kwargs={},
            width=self.content_width,
        )
        summary_box1.next_to(self._title_mobject, m.DOWN, buff=self.med_large_buff, aligned_edge=m.LEFT)

        summary_box2 = self.icon_title_bulletpoints_textbox(
            [
                ("The resulting optimization problem have a few minutes of time budget",
                 [
                     "RL approaches can solve problems quickly once trained",
                     "MCTS is a anytime algorithm, that can make use of the time budget effectively",
                 ]),
            ],
            icon='timer',
            icon_color=RwthTheme.rwth_blau_75,
            bullet_icon_color=RwthTheme.rwth_blau_75,
            font_size=18,
            bullet_icon_kwargs={},
            width=self.content_width,
        )

        summary_box2.next_to(summary_box1, m.DOWN, buff=self.med_large_buff, aligned_edge=m.LEFT)

        self.play(
            self.set_title_row("Interim Summary", None, None),
            m.FadeOut(assignment_group),
            m.FadeOut(tsp_group),
            m.FadeOut(gantt_chart),
            m.ReplacementTransform(offline_bullet_point_rect, summary_box1),
            m.ReplacementTransform(online_bullet_point_rect, summary_box2),
        )

        self.play(
            self.overlay_scene()
        )


if __name__ == '__main__':
    BMotivationHistory.save_sections_without_cache()