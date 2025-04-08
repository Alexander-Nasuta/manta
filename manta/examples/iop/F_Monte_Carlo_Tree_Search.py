import manim as m
import numpy as np
from jsp_instance_utils.jsp_or_tools_solver import solve_jsp

from color_theme.rwth.rwth_theme import RwthTheme
from components.axes_utils import AxesUtils
from components.gantt_utils import GanttUtils
from slide_templates.rwth.rwth_slide_template import RwthSlideTemplate


import theme_elements as TE
import theme_silde as TS
import theme_plot_utils as PU

import graph_jsp_env.disjunctive_graph_jsp_env as GJE

class TC:
    DARK_FONT: str = RwthTheme.rwth_blau_50
    DEFAULT_FONT: str = RwthTheme.rwth_blau_75

    GREY_DARK: str = RwthTheme.rwth_schwarz_75
    GREY_DARK_LIGHT: str = RwthTheme.rwth_schwarz_10
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
        "color": TC.DEFAULT_FONT
    }
    params = {**default_params, **kwargs}
    return m.Text(t, **params)

class FIopMCTSVanilla(RwthTheme, AxesUtils, GanttUtils, RwthSlideTemplate):

    # font_name = "IosevkaTermSlab Nerd Font Mono"

    logo_paths = [
        "iop_logo.png"
    ]
    logo_height = 0.6
    index_prefix = "I "

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
                title="MCTS Approach",
                seperator=": ",
                subtitle="Vanilla MCTS",
            ),
            self.add_logos(),
            self.add_seperator_line_top(),
            self.add_seperator_line_bottom()
        )

        # Create a simple JSP environment
        jsp = np.array([
            [
                [0, 1, 2],  # job 0
                [2, 0, 1],  # job 1
                [0, 2, 1]  # job 3
            ],
            [
                [1, 1, 5],  # task durations of job 0
                [5, 3, 3],  # task durations of job 1
                [3, 6, 3]  # task durations of job 1
            ]
        ])

        opt_makespan, _, df, _ = solve_jsp(jsp)
        x_range = int(opt_makespan)

        env = GJE.DisjunctiveGraphJspEnv(
            jps_instance=jsp,
            perform_left_shift_if_possible=False,
            normalize_observation_space=True,
            # see documentation of DisjunctiveGraphJspEnv::get_state for more information
            flat_observation_space=True,  # see documentation of DisjunctiveGraphJspEnv::get_state for more information
            action_mode='job',  # alternative 'job'
            dtype='float32'  # dtype of the observation space
        )

        color_map = {
            'Machine 0': TC.BLUE,
            'Machine 1': TC.ORANGE_DARK,
            'Machine 2': TC.GREEN,
            'Machine 3': TC.TEAL,
        }

        # vector-line, feature-search-outline, layers-search, diagram_project, megaport
        # type-hierarchy-sub

        phase_rect_with = 3.325
        phase_rect_height = 0.5
        phase_buff = TE.buff_normal

        rect_selection = TE.text_rectangle_with_icon(
            ["Selection"], icon="type-hierarchy-sub",
            width=phase_rect_with, height=phase_rect_height,
            icon_scale=TE.font_normalsize,
        )
        rect_selection.to_corner(m.UL, buff=0.5).shift(m.DOWN * 1.0)

        # plus-circle-multiple, shape-circle-plus
        #
        rect_expansion = TE.text_rectangle_with_icon(
            ["Expansion"], icon="plus-circle-multiple",
            # icon_rotate=180 * m.DEGREES,
            width=phase_rect_with, height=phase_rect_height,
            icon_scale=TE.font_normalsize,
        )
        rect_expansion.next_to(rect_selection, m.DOWN, buff=phase_buff)

        # chart-box-outline, chart-bar, file-chart, chart-multiple,
        # chart-bell-curve-cumulative
        # chart-box-outline
        rect_evaluation = TE.text_rectangle_with_icon(
            ["Evaluation"], icon="chart-multiple",
            width=phase_rect_with, height=phase_rect_height,
            icon_scale=TE.font_normalsize,
        )
        rect_evaluation.next_to(rect_expansion, m.DOWN, buff=phase_buff)

        rect_back_propagation = TE.text_rectangle_with_icon(
            ["Back-Propagation"], icon="debug-step-back",
            width=phase_rect_with, height=phase_rect_height,
            icon_scale=TE.font_normalsize,
        )
        rect_back_propagation.next_to(rect_evaluation, m.DOWN, buff=phase_buff)

        # gantt_box = TE.rounded_rectangle(
        #   width=phase_rect_with, height=phase_rect_with * 9/16,
        # )
        # gantt_box.next_to(rect_back_propagation, m.DOWN, buff=phase_buff)

        self.play(
            m.FadeIn(rect_selection),
            m.FadeIn(rect_expansion),
            m.FadeIn(rect_evaluation),
            m.FadeIn(rect_back_propagation),
        )

        total_width = 14.2222222222222222222222222222222

        # 0.5 buff on each side
        # 0.25 buff horizontal between phase rects ad mcts visualisation
        mcts_width = total_width - 2 * 0.5 - phase_rect_with - 0.25

        mcts_root_node = TE.math_circle(
            "s_0",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=RwthTheme.rwth_blau_75,
            radius=0.25,
        ).scale(0.75)

        mcts_root_node.move_to(np.array([
            rect_selection.get_right()[0] + 0.25 + mcts_width / 2,
            rect_selection.get_center()[1],
            0
        ]))

        mcts_root_node.shift(m.LEFT * 0.25)

        self.play(
            m.FadeIn(mcts_root_node),
        )


        mcts_h_buff = 0.2

        env.reset()
        mcts_root_gantt = PU.gantt_chart(env, color_map=color_map)
        mcts_root_gantt.scale_to_fit_height(mcts_root_node.height)
        # place to the left of the root node
        mcts_root_gantt.next_to(mcts_root_node, m.UP, buff=mcts_h_buff * 0.5)

        self.play(
            m.FadeIn(mcts_root_gantt),
        )


        # SELECTION 0

        attention_phase_rect = m.SurroundingRectangle(
            rect_selection,
            corner_radius=0.125, color=RwthTheme.rwth_magenta_75)

        self.play(
            m.Create(attention_phase_rect),
        )

        mcts_root_node.generate_target()
        mcts_root_node.target[0].set_stroke(color=RwthTheme.rwth_magenta_75)
        # '#mcts_root_node.target[1].set_color(TC.GREY_DARK)

        self.play(
            # m.Circumscribe(mcts_root_node, shape=m.Circle, color=TC.BLUE, fade_out=True),
            m.MoveToTarget(mcts_root_node),
        )


        # EXPANSION 0

        # root children
        mcts_width_per_child_level_1 = mcts_width / 3
        mcts_vertical_space = rect_selection.get_center()[1] - rect_evaluation.get_center()[1]
        mcts_vertical_space = mcts_vertical_space * 0.75

        mcts_s1 = TE.math_circle(
            "s_1",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=RwthTheme.rwth_blau_75,
            radius=0.25,
        ).scale(0.75)
        mcts_s1.move_to(np.array([
            mcts_root_node.get_center()[0] - mcts_width_per_child_level_1 - mcts_h_buff,
            mcts_root_node.get_center()[1] - mcts_vertical_space,
            0
        ]))
        env.reset()
        env.step(0)
        mcts_s1_gantt = PU.gantt_chart(env, color_map=color_map)
        mcts_s1_gantt.scale_to_fit_height(mcts_s1.height)
        mcts_s1_gantt.next_to(mcts_s1, m.LEFT, buff=mcts_h_buff)

        mcts_s2 = TE.math_circle(
            "s_2",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=RwthTheme.rwth_blau_75,
            radius=0.25,
        ).scale(0.75)
        mcts_s2.move_to(np.array([
            mcts_root_node.get_center()[0],
            mcts_root_node.get_center()[1] - mcts_vertical_space,
            0
        ]))
        env.reset()
        env.step(1)
        mcts_s2_gantt = PU.gantt_chart(env, color_map=color_map)
        mcts_s2_gantt.scale_to_fit_height(mcts_s2.height)
        mcts_s2_gantt.next_to(mcts_s2, m.LEFT, buff=mcts_h_buff)

        mcts_s3 = TE.math_circle(
            "s_3",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=RwthTheme.rwth_blau_75,
            radius=0.25,
        ).scale(0.75)

        mcts_s3.move_to(np.array([
            mcts_root_node.get_center()[0] + mcts_width_per_child_level_1 + mcts_h_buff,
            mcts_root_node.get_center()[1] - mcts_vertical_space,
            0
        ]))
        env.reset()
        env.step(2)
        mcts_s3_gantt = PU.gantt_chart(env, color_map=color_map)
        mcts_s3_gantt.scale_to_fit_height(mcts_s3.height)
        mcts_s3_gantt.next_to(mcts_s3, m.LEFT, buff=mcts_h_buff)

        mcts_arrow_color = TC.DARK_FONT

        # arrows from root to level 1 nodes
        mcts_arrow_s1 = TE.math_arrow(
            mcts_root_node.get_center(),
            mcts_s1.get_center(),
            color=mcts_arrow_color,
            buff=0.25,
        )
        mcts_arrow_s2 = TE.math_arrow(
            mcts_root_node.get_center(),
            mcts_s2.get_center(),
            color=mcts_arrow_color,
            buff=0.25,
        )

        mcts_arrow_s3 = TE.math_arrow(
            mcts_root_node.get_center(),
            mcts_s3.get_center(),
            color=mcts_arrow_color,
            buff=0.25,
        )

        self.play(
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_expansion, corner_radius=0.125, color=RwthTheme.rwth_magenta_75))
        )

        self.play(
            m.FadeIn(mcts_s1),
            m.FadeIn(mcts_s2),
            m.FadeIn(mcts_s3),

            m.FadeIn(mcts_s1_gantt),
            m.FadeIn(mcts_s2_gantt),
            m.FadeIn(mcts_s3_gantt),

            m.GrowArrow(mcts_arrow_s1),
            m.GrowArrow(mcts_arrow_s2),
            m.GrowArrow(mcts_arrow_s3),

        )

        # EVALUATION 0
        self.play(
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_evaluation, corner_radius=0.125, color=RwthTheme.rwth_magenta_75))
        )

        def mcts_score_group(mcts_node: m.Mobject) -> (
                m.VGroup, m.VMobject, m.VMobject, m.VMobject, m.VMobject, m.VMobject, m.VMobject):
            V = "V"
            U = "U"
            _buff = 0.05

            mcts_V_text = TE.text(f"{V}", font_color=RwthTheme.rwth_gruen_100).scale(TE.font_normalsize)
            # make last character different color
            mcts_U_text = TE.text(f"{U}", font_color=RwthTheme.rwth_lila_75).scale(TE.font_normalsize)

            mcts_V_seperator = TE.text(":", font_color=RwthTheme.rwth_schwarz_75).scale(TE.font_normalsize)
            mcts_U_seperator = TE.text(":", font_color=RwthTheme.rwth_schwarz_75).scale(TE.font_normalsize)

            mcts_V_value = TE.text("?", font_color=RwthTheme.rwth_schwarz_75).scale(TE.font_normalsize)
            mcts_U_value = TE.text("?", font_color=RwthTheme.rwth_schwarz_75).scale(TE.font_normalsize)

            mcts_V_seperator.next_to(mcts_V_text, m.RIGHT, buff=_buff)
            mcts_V_value.next_to(mcts_V_seperator, m.RIGHT, buff=_buff)

            mcts_U_text.next_to(mcts_V_text, m.DOWN, buff=_buff * 2.5)
            mcts_U_seperator.next_to(mcts_U_text, m.RIGHT, buff=_buff)
            mcts_U_value.next_to(mcts_U_seperator, m.RIGHT, buff=_buff)

            mcts_text_group = m.VGroup(
                mcts_V_text, mcts_U_text, mcts_V_seperator,
                mcts_U_seperator, mcts_V_value, mcts_U_value
            )
            mcts_text_group.scale_to_fit_height(mcts_node.height).scale(0.8)
            mcts_text_group.next_to(mcts_node, m.RIGHT, buff=mcts_h_buff)

            return mcts_text_group, mcts_V_value, mcts_U_value, mcts_V_text, mcts_U_text, mcts_V_seperator, mcts_U_seperator

        mcts_s1_score_group, s1_v, s1_u, *_ = mcts_score_group(mcts_s1)
        mcts_s2_score_group, s2_v, s2_u, *_ = mcts_score_group(mcts_s2)
        mcts_s3_score_group, s3_v, s3_u, *_ = mcts_score_group(mcts_s3)

        self.play(
            m.FadeIn(mcts_s1_score_group),
            m.FadeIn(mcts_s2_score_group),
            m.FadeIn(mcts_s3_score_group),
        )

        rollout_s1_line = PU.rollout_line()
        rollout_s1_line.next_to(mcts_s1.get_bottom(), m.DOWN, aligned_edge=m.UP, buff=0.125)
        rollout_s1_circle = TE.math_circle(
            "",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=TC.BLUE,
            radius=0.25,
            stroke_width=4,
        ).scale(0.5).next_to(rollout_s1_line, m.DOWN, buff=0.0)

        roulout_s1_actions = [0, 1, 2, 1, 1, 0, 0, 2, 2]  # makespan 26
        env.reset()
        for action in roulout_s1_actions:
            env.step(action)

        rollout_s1_gantt = PU.gantt_chart(env, color_map=color_map).scale_to_fit_height(mcts_root_node.height)
        rollout_s1_gantt.next_to(rollout_s1_circle, m.DOWN, buff=0.125)

        rollout_s1 = m.VGroup(rollout_s1_line, rollout_s1_circle, rollout_s1_gantt)

        rollout_s2_line = PU.rollout_line()
        rollout_s2_line.next_to(mcts_s2.get_bottom(), m.DOWN, aligned_edge=m.UP, buff=0.125)
        rollout_s2_circle = TE.math_circle(
            "",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=TC.BLUE,
            radius=0.25,
            stroke_width=4,
        ).scale(0.5).next_to(rollout_s2_line, m.DOWN, buff=0.0)

        roulout_s2_actions = [1, 0, 2, 2, 2, 1, 0, 1, 0]  # makespan 20
        env.reset()
        for action in roulout_s2_actions:
            env.step(action)

        rollout_s2_gantt = PU.gantt_chart(env, color_map=color_map).scale_to_fit_height(mcts_root_node.height)
        rollout_s2_gantt.next_to(rollout_s2_circle, m.DOWN, buff=0.125)

        rollout_s2 = m.VGroup(rollout_s2_line, rollout_s2_circle, rollout_s2_gantt)

        rollout_s3_line = PU.rollout_line()
        rollout_s3_line.next_to(mcts_s3.get_bottom(), m.DOWN, aligned_edge=m.UP, buff=0.125)

        rollout_s3_circle = TE.math_circle(
            "",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=TC.BLUE,
            radius=0.25,
            stroke_width=4,
        ).scale(0.5).next_to(rollout_s3_line, m.DOWN, buff=0.0)

        roulout_s3_actions = [2, 0, 1, 0, 1, 0, 2, 2, 1]  # makespan 22
        env.reset()
        for action in roulout_s3_actions:
            env.step(action)

        rollout_s3_gantt = PU.gantt_chart(env, color_map=color_map).scale_to_fit_height(mcts_root_node.height)
        rollout_s3_gantt.next_to(rollout_s3_circle, m.DOWN, buff=0.125)

        rollout_s3 = m.VGroup(rollout_s3_line, rollout_s3_circle, rollout_s3_gantt)

        self.play(
            m.FadeIn(rollout_s1),
            m.FadeIn(rollout_s2),
            m.FadeIn(rollout_s3),
        )



        s_1_v_value = TE.text("0.38").scale_to_fit_height(s1_v.height)
        s_1_v_value.next_to(s1_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_1_u_value = TE.text("0.20").scale_to_fit_height(s1_v.height)
        s_1_u_value.next_to(s1_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_2_v_value = TE.text("0.50").scale_to_fit_height(s2_v.height)
        s_2_v_value.next_to(s2_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_2_u_value = TE.text("0.42").scale_to_fit_height(s2_v.height)
        s_2_u_value.next_to(s2_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_3_v_value = TE.text("0.45").scale_to_fit_height(s3_v.height)
        s_3_v_value.next_to(s3_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_3_u_value = TE.text("0.39").scale_to_fit_height(s3_v.height)
        s_3_u_value.next_to(s3_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        self.play(
            *[m.FadeOut(elem) for elem in [s1_v, s1_u, s2_v, s2_u, s3_v, s3_u]],
            *[m.FadeOut(elem) for elem in [rollout_s1_line, rollout_s2_line, rollout_s3_line]],
            *[m.FadeOut(elem) for elem in [rollout_s1_circle, rollout_s2_circle, rollout_s3_circle]],
            m.TransformFromCopy(rollout_s1_gantt, s_1_u_value),
            m.TransformFromCopy(rollout_s2_gantt, s_2_u_value),
            m.TransformFromCopy(rollout_s3_gantt, s_3_u_value),
            m.ReplacementTransform(rollout_s1_gantt, s_1_v_value),
            m.ReplacementTransform(rollout_s2_gantt, s_2_v_value),
            m.ReplacementTransform(rollout_s3_gantt, s_3_v_value),
        )

        # BACK-PROPAGATION 0
        self.play(
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_back_propagation, corner_radius=0.125, color=RwthTheme.rwth_magenta_75))
        )

        self.play(
            m.Indicate(s_1_v_value, color=TC.PINK),
            m.Indicate(s_1_u_value, color=TC.PINK),
            m.Indicate(s_2_v_value, color=TC.PINK),
            m.Indicate(s_2_u_value, color=TC.PINK),
            m.Indicate(s_3_v_value, color=TC.PINK),
            m.Indicate(s_3_u_value, color=TC.PINK),
        )

        self.play(
            m.ShowPassingFlash(
                m.VGroup(mcts_arrow_s1, mcts_arrow_s2, mcts_arrow_s3)
                .copy().set_color(RwthTheme.rwth_magenta_75),
                time_width=1.0
            ),
            rate_func=lambda t: 1 - t
        )


        mcts_root_node.generate_target()
        mcts_root_node.target.set_stroke(color=RwthTheme.rwth_blau_75)
        # mcts_root_node.target[1].set_color(TC.DEFAULT_FONT)

        # selection 1
        self.play(
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_selection, corner_radius=0.125, color=RwthTheme.rwth_magenta_75)),
            m.MoveToTarget(mcts_root_node),
        )


        mcts_root_node.generate_target()
        mcts_root_node.target.set_stroke(color=RwthTheme.rwth_magenta_75)
        # '# mcts_root_node.target[1].set_color(TC.GREY_DARK)

        self.play(
            m.MoveToTarget(mcts_root_node),
        )

        self.play(
            m.Circumscribe(s_2_u_value, color=RwthTheme.rwth_magenta_75, fade_out=True),
        )



        mcts_root_node.generate_target()
        mcts_root_node.target.set_stroke(color=RwthTheme.rwth_blau_75)
        # mcts_root_node.target[1].set_color(TC.DEFAULT_FONT)

        mcts_s2.generate_target()
        mcts_s2.target.set_stroke(color=RwthTheme.rwth_magenta_75)
#         # mcts_s2.target[1].set_color(TC.GREY_DARK)

        self.play(
            m.ShowPassingFlash(mcts_arrow_s2.copy().set_color(RwthTheme.rwth_magenta_75), time_width=1.0),
            m.MoveToTarget(mcts_root_node),
            m.MoveToTarget(mcts_s2),
        )



        # expansion 1

        self.play(
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_expansion, corner_radius=0.125, color=RwthTheme.rwth_magenta_75))
        )

        mcts_width_per_child_level_2 = mcts_width_per_child_level_1 / 3.5

        mcts_s2_1 = TE.math_circle(
            "s_{3}",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=RwthTheme.rwth_blau_75,
            radius=0.25,
        ).scale(0.75)

        mcts_s2_1.move_to(np.array([
            mcts_s2.get_center()[0] - mcts_width_per_child_level_2 - mcts_h_buff,
            mcts_s2.get_center()[1] - mcts_vertical_space,
            0
        ]))

        env.reset()
        env.step(1)
        env.step(0)

        mcts_s2_1_gantt = PU.gantt_chart(env, color_map=color_map)
        mcts_s2_1_gantt.scale_to_fit_height(mcts_s2_1.height)
        mcts_s2_1_gantt.next_to(mcts_s2_1, m.DOWN, buff=mcts_h_buff * 0.5)

        mcts_s2_2 = TE.math_circle(
            "s_{4}",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=RwthTheme.rwth_blau_75,
            radius=0.25,
        ).scale(0.75)

        mcts_s2_2.move_to(np.array([
            mcts_s2.get_center()[0],
            mcts_s2.get_center()[1] - mcts_vertical_space,
            0
        ]))

        env.reset()
        env.step(1)
        env.step(1)

        mcts_s2_2_gantt = PU.gantt_chart(env, color_map=color_map)
        mcts_s2_2_gantt.scale_to_fit_height(mcts_s2_2.height)
        mcts_s2_2_gantt.next_to(mcts_s2_2, m.DOWN, buff=mcts_h_buff * 0.5)

        mcts_s2_3 = TE.math_circle(
            "s_{5}",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=RwthTheme.rwth_blau_75,
            radius=0.25,
        ).scale(0.75)

        mcts_s2_3.move_to(np.array([
            mcts_s2.get_center()[0] + mcts_width_per_child_level_2 + mcts_h_buff,
            mcts_s2.get_center()[1] - mcts_vertical_space,
            0
        ]))

        env.reset()
        env.step(1)
        env.step(2)

        mcts_s2_3_gantt = PU.gantt_chart(env, color_map=color_map)
        mcts_s2_3_gantt.scale_to_fit_height(mcts_s2_3.height)
        mcts_s2_3_gantt.next_to(mcts_s2_3, m.DOWN, buff=mcts_h_buff * 0.5)

        mcts_s2_arrow_1 = TE.math_arrow(
            mcts_s2.get_center(),
            mcts_s2_1.get_center(),
            color=mcts_arrow_color,
            buff=0.25,
        )

        mcts_s2_arrow_2 = TE.math_arrow(
            mcts_s2.get_center(),
            mcts_s2_2.get_center(),
            color=mcts_arrow_color,
            buff=0.25,
        )

        mcts_s2_arrow_3 = TE.math_arrow(
            mcts_s2.get_center(),
            mcts_s2_3.get_center(),
            color=mcts_arrow_color,
            buff=0.25,
        )

        self.play(
            m.FadeIn(mcts_s2_1),
            m.FadeIn(mcts_s2_2),
            m.FadeIn(mcts_s2_3),
            m.FadeIn(mcts_s2_1_gantt),
            m.FadeIn(mcts_s2_2_gantt),
            m.FadeIn(mcts_s2_3_gantt),
            m.GrowArrow(mcts_s2_arrow_1),
            m.GrowArrow(mcts_s2_arrow_2),
            m.GrowArrow(mcts_s2_arrow_3),
        )

        # EVALUATION 1

        mcts_s2_1_score_group, s2_1_v, s2_1_u, *_ = mcts_score_group(mcts_s2_1)
        mcts_s2_2_score_group, s2_2_v, s2_2_u, *_ = mcts_score_group(mcts_s2_2)
        mcts_s2_3_score_group, s2_3_v, s2_3_u, *_ = mcts_score_group(mcts_s2_3)

        # shift all to the left
        for elem in [mcts_s2_1_score_group, mcts_s2_2_score_group, mcts_s2_3_score_group]:
            elem.shift(m.LEFT * 0.1)

        self.play(
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_evaluation, corner_radius=0.125, color=RwthTheme.rwth_magenta_75)),
            m.FadeIn(mcts_s2_1_score_group),
            m.FadeIn(mcts_s2_2_score_group),
            m.FadeIn(mcts_s2_3_score_group),
        )

        rollout_s2_1_line = PU.rollout_line()
        rollout_s2_1_line.next_to(mcts_s2_1_gantt.get_bottom(), m.DOWN, aligned_edge=m.UP, buff=0.125)

        rollout_s2_1_circle = TE.math_circle(
            "",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=TC.BLUE,
            radius=0.25,
            stroke_width=4,
        ).scale(0.5).next_to(rollout_s2_1_line, m.DOWN, buff=0.0)

        # makespan: 16, actions: [1, 0, 2, 0, 1, 1, 2, 0, 2], m_utility: 0.625
        roulout_s2_1_actions = [1, 0, 2, 0, 1, 1, 2, 0, 2]
        env.reset()

        for action in roulout_s2_1_actions:
            env.step(action)

        rollout_s2_1_gantt = PU.gantt_chart(env, color_map=color_map).scale_to_fit_height(mcts_root_node.height)
        rollout_s2_1_gantt.next_to(rollout_s2_1_circle, m.DOWN, buff=0.125)

        rollout_s2_1 = m.VGroup(rollout_s2_1_line, rollout_s2_1_circle, rollout_s2_1_gantt)

        rollout_s2_2_line = PU.rollout_line()
        rollout_s2_2_line.next_to(mcts_s2_2_gantt.get_bottom(), m.DOWN, aligned_edge=m.UP, buff=0.125)

        rollout_s2_2_circle = TE.math_circle(
            "",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=TC.BLUE,
            radius=0.25,
            stroke_width=4,
        ).scale(0.5).next_to(rollout_s2_2_line, m.DOWN, buff=0.0)

        # makespan: 22, actions: [1, 1, 1, 2, 0, 2, 0, 0, 2], m_utility: 0.45454545454545453
        roulout_s2_2_actions = [1, 1, 1, 2, 0, 2, 0, 0, 2]
        env.reset()

        for action in roulout_s2_2_actions:
            env.step(action)

        rollout_s2_2_gantt = PU.gantt_chart(env, color_map=color_map).scale_to_fit_height(mcts_root_node.height)

        rollout_s2_2_gantt.next_to(rollout_s2_2_circle, m.DOWN, buff=0.125)

        rollout_s2_2 = m.VGroup(rollout_s2_2_line, rollout_s2_2_circle, rollout_s2_2_gantt)

        rollout_s2_3_line = PU.rollout_line()
        rollout_s2_3_line.next_to(mcts_s2_3_gantt.get_bottom(), m.DOWN, aligned_edge=m.UP, buff=0.125)

        rollout_s2_3_circle = TE.math_circle(
            "",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=TC.BLUE,
            radius=0.25,
            stroke_width=4,
        ).scale(0.5).next_to(rollout_s2_3_line, m.DOWN, buff=0.0)

        # makespan: 19, actions: [1, 2, 0, 0, 1, 0, 2, 1, 2], m_utility: 0.5263157894736842
        roulout_s2_3_actions = [1, 2, 0, 0, 1, 0, 2, 1, 2]
        env.reset()

        for action in roulout_s2_3_actions:
            env.step(action)

        rollout_s2_3_gantt = PU.gantt_chart(env, color_map=color_map).scale_to_fit_height(mcts_root_node.height)

        rollout_s2_3_gantt.next_to(rollout_s2_3_circle, m.DOWN, buff=0.125)

        rollout_s2_3 = m.VGroup(rollout_s2_3_line, rollout_s2_3_circle, rollout_s2_3_gantt)

        self.play(
            m.FadeIn(rollout_s2_1),
            m.FadeIn(rollout_s2_2),
            m.FadeIn(rollout_s2_3),
        )

        s_2_1_v_value = TE.text("0.63").scale_to_fit_height(s2_v.height)
        s_2_1_v_value.next_to(s2_1_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_2_1_u_value = TE.text("0.79").scale_to_fit_height(s2_v.height)
        s_2_1_u_value.next_to(s2_1_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_2_2_v_value = TE.text("0.45").scale_to_fit_height(s2_v.height)
        s_2_2_v_value.next_to(s2_2_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_2_2_u_value = TE.text("0.39").scale_to_fit_height(s2_v.height)
        s_2_2_u_value.next_to(s2_2_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_2_3_v_value = TE.text("0.52").scale_to_fit_height(s2_v.height)
        s_2_3_v_value.next_to(s2_3_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_2_3_u_value = TE.text("0.51").scale_to_fit_height(s2_v.height)
        s_2_3_u_value.next_to(s2_3_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        self.play(
            *[m.FadeOut(elem) for elem in [s2_1_v, s2_1_u, s2_2_v, s2_2_u, s2_3_v, s2_3_u]],
            *[m.FadeOut(elem) for elem in [rollout_s2_1_line, rollout_s2_2_line, rollout_s2_3_line]],
            *[m.FadeOut(elem) for elem in [rollout_s2_1_circle, rollout_s2_2_circle, rollout_s2_3_circle]],
            m.TransformFromCopy(rollout_s2_1_gantt, s_2_1_u_value),
            m.TransformFromCopy(rollout_s2_2_gantt, s_2_2_u_value),
            m.TransformFromCopy(rollout_s2_3_gantt, s_2_3_u_value),
            m.ReplacementTransform(rollout_s2_1_gantt, s_2_1_v_value),
            m.ReplacementTransform(rollout_s2_2_gantt, s_2_2_v_value),
            m.ReplacementTransform(rollout_s2_3_gantt, s_2_3_v_value),
        )

        # BACK-PROPAGATION 1
        self.play(
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_back_propagation, corner_radius=0.125, color=RwthTheme.rwth_magenta_75))
        )

        self.play(
            m.Indicate(s_2_1_v_value, color=TC.PINK),
            m.Indicate(s_2_1_u_value, color=TC.PINK),
            m.Indicate(s_2_2_v_value, color=TC.PINK),
            m.Indicate(s_2_2_u_value, color=TC.PINK),
            m.Indicate(s_2_3_v_value, color=TC.PINK),
            m.Indicate(s_2_3_u_value, color=TC.PINK),
        )

        self.play(
            m.ShowPassingFlash(
                m.VGroup(mcts_s2_arrow_1, mcts_s2_arrow_2, mcts_s2_arrow_3)
                .copy().set_color(RwthTheme.rwth_magenta_75),
                time_width=1.0
            ),
            rate_func=lambda t: 1 - t
        )

        # update V and U values for s_2
        s2_v_value_NEW = TE.text("0.53").scale_to_fit_height(s2_v.height)
        s2_v_value_NEW.next_to(s2_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s2_u_value_NEW = TE.text("0.35").scale_to_fit_height(s2_v.height)
        s2_u_value_NEW.next_to(s2_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        self.play(
            m.FadeOut(s2_v),
            m.FadeOut(s2_u),
            m.Transform(s_2_v_value, s2_v_value_NEW),
            m.Transform(s_2_u_value, s2_u_value_NEW),
            m.Circumscribe(m.VGroup(s2_v_value_NEW, s2_u_value_NEW, mcts_s2_score_group), color=TC.PINK, fade_out=True),
        )

        # propagate to root node

        self.play(
            m.ShowPassingFlash(
                m.VGroup(mcts_arrow_s2).copy().set_color(RwthTheme.rwth_magenta_75),
                time_width=1.0
            ),
            rate_func=lambda t: 1 - t
        )

        mcts_s2.generate_target()
        mcts_s2.target.set_stroke(color=RwthTheme.rwth_blau_75)
#         mcts_s2.target[1].set_color(TC.DEFAULT_FONT)

        self.play(
            m.MoveToTarget(mcts_s2),
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_selection, corner_radius=0.125, color=RwthTheme.rwth_magenta_75)),
        )

        # SELECTION 2
        mcts_root_node.generate_target()
        mcts_root_node.target.set_stroke(color=RwthTheme.rwth_magenta_75)
        # mcts_root_node.target[1].set_color(TC.GREY_DARK)

        self.play(
            m.MoveToTarget(mcts_root_node),
        )

        self.play(
            m.Circumscribe(s_3_u_value, color=RwthTheme.rwth_magenta_75, fade_out=True),
        )

        mcts_root_node.generate_target()
        mcts_root_node.target.set_stroke(color=RwthTheme.rwth_blau_75)
        # mcts_root_node.target[1].set_color(TC.DEFAULT_FONT)

        mcts_s3.generate_target()
        mcts_s3.target.set_stroke(color=RwthTheme.rwth_magenta_75)
#         mcts_s3.target[1].set_color(TC.GREY_DARK)

        self.play(
            m.ShowPassingFlash(mcts_arrow_s3.copy().set_color(RwthTheme.rwth_magenta_75), time_width=1.0),
            m.MoveToTarget(mcts_root_node),
            m.MoveToTarget(mcts_s3),
        )

        # EXPANSION 2

        self.play(
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_expansion, corner_radius=0.125, color=RwthTheme.rwth_magenta_75))
        )

        mcts_s3_1 = TE.math_circle(
            "s_{7}",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=RwthTheme.rwth_blau_75,
            radius=0.25,
        ).scale(0.75)

        mcts_s3_1.move_to(np.array([
            mcts_s3.get_center()[0] - mcts_width_per_child_level_2 - mcts_h_buff,
            mcts_s3.get_center()[1] - mcts_vertical_space,
            0
        ]))

        env.reset()
        env.step(2)
        env.step(0)

        mcts_s3_1_gantt = PU.gantt_chart(env, color_map=color_map)
        mcts_s3_1_gantt.scale_to_fit_height(mcts_s3_1.height)
        mcts_s3_1_gantt.next_to(mcts_s3_1, m.DOWN, buff=mcts_h_buff * 0.5)

        mcts_s3_2 = TE.math_circle(
            "s_{8}",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=RwthTheme.rwth_blau_75,
            radius=0.25,
        ).scale(0.75)

        mcts_s3_2.move_to(np.array([
            mcts_s3.get_center()[0],
            mcts_s3.get_center()[1] - mcts_vertical_space,
            0
        ]))

        env.reset()
        env.step(2)
        env.step(1)

        mcts_s3_2_gantt = PU.gantt_chart(env, color_map=color_map)
        mcts_s3_2_gantt.scale_to_fit_height(mcts_s3_2.height)
        mcts_s3_2_gantt.next_to(mcts_s3_2, m.DOWN, buff=mcts_h_buff * 0.5)

        mcts_s3_3 = TE.math_circle(
            "s_{9}",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=RwthTheme.rwth_blau_75,
            radius=0.25,
        ).scale(0.75)

        mcts_s3_3.move_to(np.array([
            mcts_s3.get_center()[0] + mcts_width_per_child_level_2 + mcts_h_buff,
            mcts_s3.get_center()[1] - mcts_vertical_space,
            0
        ]))

        env.reset()
        env.step(2)
        env.step(2)

        mcts_s3_3_gantt = PU.gantt_chart(env, color_map=color_map)
        mcts_s3_3_gantt.scale_to_fit_height(mcts_s3_3.height)
        mcts_s3_3_gantt.next_to(mcts_s3_3, m.DOWN, buff=mcts_h_buff * 0.5)

        mcts_s3_arrow_1 = TE.math_arrow(
            mcts_s3.get_center(),
            mcts_s3_1.get_center(),
            color=mcts_arrow_color,
            buff=0.25,
        )

        mcts_s3_arrow_2 = TE.math_arrow(
            mcts_s3.get_center(),
            mcts_s3_2.get_center(),
            color=mcts_arrow_color,
            buff=0.25,
        )

        mcts_s3_arrow_3 = TE.math_arrow(
            mcts_s3.get_center(),
            mcts_s3_3.get_center(),
            color=mcts_arrow_color,
            buff=0.25,
        )

        self.play(
            m.FadeIn(mcts_s3_1),
            m.FadeIn(mcts_s3_2),
            m.FadeIn(mcts_s3_3),
            m.FadeIn(mcts_s3_1_gantt),
            m.FadeIn(mcts_s3_2_gantt),
            m.FadeIn(mcts_s3_3_gantt),
            m.GrowArrow(mcts_s3_arrow_1),
            m.GrowArrow(mcts_s3_arrow_2),
            m.GrowArrow(mcts_s3_arrow_3),
        )

        # EVALUATION 2

        mcts_s3_1_score_group, s3_1_v, s3_1_u, *_ = mcts_score_group(mcts_s3_1)
        mcts_s3_2_score_group, s3_2_v, s3_2_u, *_ = mcts_score_group(mcts_s3_2)
        mcts_s3_3_score_group, s3_3_v, s3_3_u, *_ = mcts_score_group(mcts_s3_3)

        # shift all to the left
        for elem in [mcts_s3_1_score_group, mcts_s3_2_score_group, mcts_s3_3_score_group]:
            elem.shift(m.LEFT * 0.1)

        self.play(
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_evaluation, corner_radius=0.125, color=RwthTheme.rwth_magenta_75)),
            m.FadeIn(mcts_s3_1_score_group),
            m.FadeIn(mcts_s3_2_score_group),
            m.FadeIn(mcts_s3_3_score_group),
        )

        rollout_s3_1_line = PU.rollout_line()
        rollout_s3_1_line.next_to(mcts_s3_1_gantt.get_bottom(), m.DOWN, aligned_edge=m.UP, buff=0.125)

        rollout_s3_1_circle = TE.math_circle(
            "",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=TC.BLUE,
            radius=0.25,
            stroke_width=4,
        ).scale(0.5).next_to(rollout_s3_1_line, m.DOWN, buff=0.0)

        # makespan: 24, actions: [2, 0, 0, 0, 1, 2, 1, 1, 2], m_utility: 0.4166666666666667
        roulout_s3_1_actions = [2, 0, 0, 0, 1, 2, 1, 1, 2]
        env.reset()

        for action in roulout_s3_1_actions:
            env.step(action)

        rollout_s3_1_gantt = PU.gantt_chart(env, color_map=color_map).scale_to_fit_height(mcts_root_node.height)

        rollout_s3_1_gantt.next_to(rollout_s3_1_circle, m.DOWN, buff=0.125)

        rollout_s3_1 = m.VGroup(rollout_s3_1_line, rollout_s3_1_circle, rollout_s3_1_gantt)

        rollout_s3_2_line = PU.rollout_line()
        rollout_s3_2_line.next_to(mcts_s3_2_gantt.get_bottom(), m.DOWN, aligned_edge=m.UP, buff=0.125)

        rollout_s3_2_circle = TE.math_circle(
            "",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=TC.BLUE,
            radius=0.25,
            stroke_width=4,
        ).scale(0.5).next_to(rollout_s3_2_line, m.DOWN, buff=0.0)

        # makespan: 26, actions: [2, 1, 0, 1, 1, 0, 0, 2, 2], m_utility: 0.38461538461538464
        roulout_s3_2_actions = [2, 1, 0, 1, 1, 0, 0, 2, 2]

        env.reset()

        for action in roulout_s3_2_actions:
            env.step(action)

        rollout_s3_2_gantt = PU.gantt_chart(env, color_map=color_map).scale_to_fit_height(mcts_root_node.height)

        rollout_s3_2_gantt.next_to(rollout_s3_2_circle, m.DOWN, buff=0.125)

        rollout_s3_2 = m.VGroup(rollout_s3_2_line, rollout_s3_2_circle, rollout_s3_2_gantt)

        rollout_s3_3_line = PU.rollout_line()

        rollout_s3_3_line.next_to(mcts_s3_3_gantt.get_bottom(), m.DOWN, aligned_edge=m.UP, buff=0.125)

        rollout_s3_3_circle = TE.math_circle(
            "",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=TC.BLUE,
            radius=0.25,
            stroke_width=4,
        ).scale(0.5).next_to(rollout_s3_3_line, m.DOWN, buff=0.0)

        # makespan: 23, actions: [2, 1, 2, 1, 2, 0, 1, 0, 0], m_utility: 0.43478260869565216
        roulout_s3_3_actions = [2, 1, 2, 1, 2, 0, 1, 0, 0]

        env.reset()

        for action in roulout_s3_3_actions:
            env.step(action)

        rollout_s3_3_gantt = PU.gantt_chart(env, color_map=color_map).scale_to_fit_height(mcts_root_node.height)

        rollout_s3_3_gantt.next_to(rollout_s3_3_circle, m.DOWN, buff=0.125)

        rollout_s3_3 = m.VGroup(rollout_s3_3_line, rollout_s3_3_circle, rollout_s3_3_gantt)

        self.play(
            m.FadeIn(rollout_s3_1),
            m.FadeIn(rollout_s3_2),
            m.FadeIn(rollout_s3_3),
        )

        s_3_1_v_value = TE.text("0.41").scale_to_fit_height(s3_v.height)
        s_3_1_v_value.next_to(s3_1_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_3_1_u_value = TE.text("0.33").scale_to_fit_height(s3_v.height)
        s_3_1_u_value.next_to(s3_1_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_3_2_v_value = TE.text("0.38").scale_to_fit_height(s3_v.height)
        s_3_2_v_value.next_to(s3_2_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_3_2_u_value = TE.text("0.20").scale_to_fit_height(s3_v.height)
        s_3_2_u_value.next_to(s3_2_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_3_3_v_value = TE.text("0.43").scale_to_fit_height(s3_v.height)
        s_3_3_v_value.next_to(s3_3_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_3_3_u_value = TE.text("0.35").scale_to_fit_height(s3_v.height)
        s_3_3_u_value.next_to(s3_3_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        self.play(
            *[m.FadeOut(elem) for elem in [s3_1_v, s3_1_u, s3_2_v, s3_2_u, s3_3_v, s3_3_u]],
            *[m.FadeOut(elem) for elem in [rollout_s3_1_line, rollout_s3_2_line, rollout_s3_3_line]],
            *[m.FadeOut(elem) for elem in [rollout_s3_1_circle, rollout_s3_2_circle, rollout_s3_3_circle]],
            m.TransformFromCopy(rollout_s3_1_gantt, s_3_1_u_value),
            m.TransformFromCopy(rollout_s3_2_gantt, s_3_2_u_value),
            m.TransformFromCopy(rollout_s3_3_gantt, s_3_3_u_value),
            m.ReplacementTransform(rollout_s3_1_gantt, s_3_1_v_value),
            m.ReplacementTransform(rollout_s3_2_gantt, s_3_2_v_value),
            m.ReplacementTransform(rollout_s3_3_gantt, s_3_3_v_value),
        )

        # BACK-PROPAGATION 2

        self.play(
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_back_propagation, corner_radius=0.125, color=RwthTheme.rwth_magenta_75))
        )

        self.play(
            m.Indicate(s_3_1_v_value, color=TC.PINK),
            m.Indicate(s_3_1_u_value, color=TC.PINK),
            m.Indicate(s_3_2_v_value, color=TC.PINK),
            m.Indicate(s_3_2_u_value, color=TC.PINK),
            m.Indicate(s_3_3_v_value, color=TC.PINK),
            m.Indicate(s_3_3_u_value, color=TC.PINK),
        )

        self.play(
            m.ShowPassingFlash(
                m.VGroup(mcts_s3_arrow_1, mcts_s3_arrow_2, mcts_s3_arrow_3)
                .copy().set_color(RwthTheme.rwth_magenta_75),
                time_width=1.0
            ),
            rate_func=lambda t: 1 - t
        )

        # update V and U values for s_3
        s3_v_value_NEW = TE.text("0.42").scale_to_fit_height(s3_v.height)
        s3_v_value_NEW.next_to(s3_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s3_u_value_NEW = TE.text("0.31").scale_to_fit_height(s3_v.height)
        s3_u_value_NEW.next_to(s3_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        self.play(
            m.FadeOut(s3_v),
            m.FadeOut(s3_u),
            m.Transform(s_3_v_value, s3_v_value_NEW),
            m.Transform(s_3_u_value, s3_u_value_NEW),
            m.Circumscribe(m.VGroup(s3_v_value_NEW, s3_u_value_NEW, mcts_s3_score_group), color=TC.PINK, fade_out=True),
        )

        # propagate to root node
        self.play(
            m.ShowPassingFlash(
                m.VGroup(mcts_arrow_s3).copy().set_color(RwthTheme.rwth_magenta_75),
                time_width=1.0
            ),
            rate_func=lambda t: 1 - t
        )

        mcts_s3.generate_target()
        mcts_s3.target.set_stroke(color=RwthTheme.rwth_blau_75)
#         mcts_s3.target[1].set_color(TC.DEFAULT_FONT)

        self.play(
            m.MoveToTarget(mcts_s3),
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_selection, corner_radius=0.125, color=RwthTheme.rwth_magenta_75)),
        )

        # fade out all gantt charts
        self.play(
            *[m.FadeOut(elem) for elem in [
                mcts_root_gantt,
                mcts_s1_gantt, mcts_s2_gantt, mcts_s3_gantt,
                mcts_s2_1_gantt, mcts_s2_2_gantt, mcts_s2_3_gantt,
                mcts_s3_1_gantt, mcts_s3_2_gantt, mcts_s3_3_gantt,
            ]],
        )

        # SELECTION 3
        mcts_root_node.generate_target()
        mcts_root_node.target.set_stroke(color=RwthTheme.rwth_magenta_75)
        # mcts_root_node.target[1].set_color(TC.GREY_DARK)

        self.play(
            m.MoveToTarget(mcts_root_node),
        )

        # select s_2

        self.play(
            m.Circumscribe(s_2_u_value, color=RwthTheme.rwth_magenta_75, fade_out=True),
        )

        mcts_s2.generate_target()
        mcts_s2.target.set_stroke(color=RwthTheme.rwth_magenta_75)
#         mcts_s2.target[1].set_color(TC.GREY_DARK)

        mcts_root_node.generate_target()
        mcts_root_node.target.set_stroke(color=RwthTheme.rwth_blau_75)
        # mcts_root_node.target[1].set_color(TC.DEFAULT_FONT)

        self.play(
            m.MoveToTarget(mcts_s2),
            m.ShowPassingFlash(mcts_arrow_s2.copy().set_color(RwthTheme.rwth_magenta_75), time_width=1.0),
            m.MoveToTarget(mcts_root_node),
        )

        # select s_2_1
        self.play(
            m.Circumscribe(s_2_1_u_value, color=RwthTheme.rwth_magenta_75, fade_out=True),
        )

        mcts_s2_1.generate_target()
        mcts_s2_1.target.set_stroke(color=RwthTheme.rwth_magenta_75)
#         mcts_s2_1.target[1].set_color(TC.GREY_DARK)

        mcts_s2.generate_target()
        mcts_s2.target.set_stroke(color=RwthTheme.rwth_blau_75)
#         mcts_s2.target[1].set_color(TC.DEFAULT_FONT)

        self.play(
            m.MoveToTarget(mcts_s2_1),
            m.ShowPassingFlash(mcts_s2_arrow_1.copy().set_color(RwthTheme.rwth_magenta_75), time_width=1.0),
            m.MoveToTarget(mcts_s2),
        )

        # EXPANSION 3

        mcts_width_per_child_level_3 = mcts_width_per_child_level_2

        self.play(
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_expansion, corner_radius=0.125, color=RwthTheme.rwth_magenta_75))
        )

        mcts_s2_1_1 = TE.math_circle(
            "s_{10}",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=RwthTheme.rwth_blau_75,
            radius=0.25,
        ).scale(0.75)

        mcts_s2_1_1.move_to(np.array([
            mcts_s2_1.get_center()[0] - mcts_width_per_child_level_3 - mcts_h_buff,
            mcts_s2_1.get_center()[1] - mcts_vertical_space,
            0
        ]))

        mcts_s2_1_2 = TE.math_circle(
            "s_{11}",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=RwthTheme.rwth_blau_75,
            radius=0.25,
        ).scale(0.75)

        mcts_s2_1_2.move_to(np.array([
            mcts_s2_1.get_center()[0],
            mcts_s2_1.get_center()[1] - mcts_vertical_space,
            0
        ]))

        mcts_s2_1_3 = TE.math_circle(
            "s_{12}",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=RwthTheme.rwth_blau_75,
            radius=0.25,
        ).scale(0.75)

        mcts_s2_1_3.move_to(np.array([
            mcts_s2_1.get_center()[0] + mcts_width_per_child_level_3 + mcts_h_buff,
            mcts_s2_1.get_center()[1] - mcts_vertical_space,
            0
        ])
        )

        mcts_s2_1_arrow_1 = TE.math_arrow(
            mcts_s2_1.get_center(),
            mcts_s2_1_1.get_center(),
            color=mcts_arrow_color,
            buff=0.25,
        )

        mcts_s2_1_arrow_2 = TE.math_arrow(
            mcts_s2_1.get_center(),
            mcts_s2_1_2.get_center(),
            color=mcts_arrow_color,
            buff=0.25,
        )

        mcts_s2_1_arrow_3 = TE.math_arrow(
            mcts_s2_1.get_center(),
            mcts_s2_1_3.get_center(),
            color=mcts_arrow_color,
            buff=0.25,
        )

        self.play(
            m.FadeIn(mcts_s2_1_1),
            m.FadeIn(mcts_s2_1_2),
            m.FadeIn(mcts_s2_1_3),
            m.GrowArrow(mcts_s2_1_arrow_1),
            m.GrowArrow(mcts_s2_1_arrow_2),
            m.GrowArrow(mcts_s2_1_arrow_3),
        )

        # EVALUATION 3

        mcts_s2_1_1_score_group, s2_1_1_v, s2_1_1_u, *_ = mcts_score_group(mcts_s2_1_1)
        mcts_s2_1_2_score_group, s2_1_2_v, s2_1_2_u, *_ = mcts_score_group(mcts_s2_1_2)
        mcts_s2_1_3_score_group, s2_1_3_v, s2_1_3_u, *_ = mcts_score_group(mcts_s2_1_3)

        # shift all to the left
        for elem in [mcts_s2_1_1_score_group, mcts_s2_1_2_score_group, mcts_s2_1_3_score_group]:
            elem.shift(m.LEFT * 0.1)

        self.play(
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_evaluation, corner_radius=0.125, color=RwthTheme.rwth_magenta_75)),
            m.FadeIn(mcts_s2_1_1_score_group),
            m.FadeIn(mcts_s2_1_2_score_group),
            m.FadeIn(mcts_s2_1_3_score_group),
        )

        rollout_s2_1_1_line = PU.rollout_line(range=2)
        rollout_s2_1_1_line.next_to(mcts_s2_1_1.get_bottom(), m.DOWN, aligned_edge=m.UP, buff=0.125)

        rollout_s2_1_1_circle = TE.math_circle(
            "",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=TC.BLUE,
            radius=0.25,
            stroke_width=4,
        ).scale(0.5).next_to(rollout_s2_1_1_line, m.DOWN, buff=0.0)

        # makespan: 17, actions: [1, 0, 0, 2, 2, 1, 0, 2, 1], m_utility: 0.5882352941176471
        roulout_s2_1_1_actions = [1, 0, 0, 2, 2, 1, 0, 2, 1]
        env.reset()

        for action in roulout_s2_1_1_actions:
            env.step(action)

        rollout_s2_1_1_gantt = PU.gantt_chart(env, color_map=color_map).scale_to_fit_height(mcts_root_node.height)

        rollout_s2_1_1_gantt.next_to(rollout_s2_1_1_circle, m.DOWN, buff=0.125)

        rollout_s2_1_1 = m.VGroup(rollout_s2_1_1_line, rollout_s2_1_1_circle)

        rollout_s2_1_2_line = PU.rollout_line(range=2)

        rollout_s2_1_2_line.next_to(mcts_s2_1_2.get_bottom(), m.DOWN, aligned_edge=m.UP, buff=0.125)

        rollout_s2_1_2_circle = TE.math_circle(
            "",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=TC.BLUE,
            radius=0.25,
            stroke_width=4,
        ).scale(0.5).next_to(rollout_s2_1_2_line, m.DOWN, buff=0.0)

        # makespan: 20, actions: [1, 0, 1, 0, 2, 0, 2, 1, 2], m_utility: 0.5
        roulout_s2_1_2_actions = [1, 0, 1, 0, 2, 0, 2, 1, 2]

        env.reset()

        for action in roulout_s2_1_2_actions:
            env.step(action)

        rollout_s2_1_2_gantt = PU.gantt_chart(env, color_map=color_map).scale_to_fit_height(mcts_root_node.height)

        rollout_s2_1_2_gantt.next_to(rollout_s2_1_2_circle, m.DOWN, buff=0.125)

        rollout_s2_1_2 = m.VGroup(rollout_s2_1_2_line, rollout_s2_1_2_circle)

        rollout_s2_1_3_line = PU.rollout_line(range=2)

        rollout_s2_1_3_line.next_to(mcts_s2_1_3.get_bottom(), m.DOWN, aligned_edge=m.UP, buff=0.125)

        rollout_s2_1_3_circle = TE.math_circle(
            "",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=TC.BLUE,
            radius=0.25,
            stroke_width=4,
        ).scale(0.5).next_to(rollout_s2_1_3_line, m.DOWN, buff=0.0)

        # makespan: 16, actions: [1, 0, 2, 1, 0, 1, 2, 0, 2], m_utility: 0.625
        roulout_s2_1_3_actions = [1, 0, 2, 1, 0, 1, 2, 0, 2]

        env.reset()

        for action in roulout_s2_1_3_actions:
            env.step(action)

        rollout_s2_1_3_gantt = PU.gantt_chart(env, color_map=color_map).scale_to_fit_height(mcts_root_node.height)

        rollout_s2_1_3_gantt.next_to(rollout_s2_1_3_circle, m.DOWN, buff=0.125)

        rollout_s2_1_3 = m.VGroup(rollout_s2_1_3_line, rollout_s2_1_3_circle)

        self.play(
            m.FadeIn(rollout_s2_1_1),
            m.FadeIn(rollout_s2_1_2),
            m.FadeIn(rollout_s2_1_3),
        )

        s_2_1_1_v_value = TE.text("0.59").scale_to_fit_height(s2_v.height)
        s_2_1_1_v_value.next_to(s2_1_1_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_2_1_1_u_value = TE.text("0.61").scale_to_fit_height(s2_v.height)
        s_2_1_1_u_value.next_to(s2_1_1_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_2_1_2_v_value = TE.text("0.50").scale_to_fit_height(s2_v.height)
        s_2_1_2_v_value.next_to(s2_1_2_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_2_1_2_u_value = TE.text("0.42").scale_to_fit_height(s2_v.height)
        s_2_1_2_u_value.next_to(s2_1_2_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_2_1_3_v_value = TE.text("0.63").scale_to_fit_height(s2_v.height)
        s_2_1_3_v_value.next_to(s2_1_3_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_2_1_3_u_value = TE.text("0.79").scale_to_fit_height(s2_v.height)
        s_2_1_3_u_value.next_to(s2_1_3_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        self.play(
            *[m.FadeOut(elem) for elem in [s2_1_1_v, s2_1_1_u, s2_1_2_v, s2_1_2_u, s2_1_3_v, s2_1_3_u]],
            *[m.FadeOut(elem) for elem in [rollout_s2_1_1_line, rollout_s2_1_2_line, rollout_s2_1_3_line]],
            m.TransformFromCopy(rollout_s2_1_1_circle, s_2_1_1_u_value),
            m.TransformFromCopy(rollout_s2_1_2_circle, s_2_1_2_u_value),
            m.TransformFromCopy(rollout_s2_1_3_circle, s_2_1_3_u_value),
            m.ReplacementTransform(rollout_s2_1_1_circle, s_2_1_1_v_value),
            m.ReplacementTransform(rollout_s2_1_2_circle, s_2_1_2_v_value),
            m.ReplacementTransform(rollout_s2_1_3_circle, s_2_1_3_v_value),
        )

        # BACK-PROPAGATION 3

        self.play(
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_back_propagation, corner_radius=0.125, color=RwthTheme.rwth_magenta_75))
        )

        self.play(
            m.Indicate(s_2_1_1_v_value, color=TC.PINK),
            m.Indicate(s_2_1_1_u_value, color=TC.PINK),
            m.Indicate(s_2_1_2_v_value, color=TC.PINK),
            m.Indicate(s_2_1_2_u_value, color=TC.PINK),
            m.Indicate(s_2_1_3_v_value, color=TC.PINK),
            m.Indicate(s_2_1_3_u_value, color=TC.PINK),
        )

        self.play(
            m.ShowPassingFlash(
                m.VGroup(mcts_s2_1_arrow_1, mcts_s2_1_arrow_2, mcts_s2_1_arrow_3)
                .copy().set_color(RwthTheme.rwth_magenta_75),
                time_width=1.0
            ),
            rate_func=lambda t: 1 - t
        )

        # update V and U values for s_2_1
        s2_1_v_value_NEW = TE.text("0.59").scale_to_fit_height(s2_v.height)
        s2_1_v_value_NEW.next_to(s2_1_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s2_1_u_value_NEW = TE.text("0.50").scale_to_fit_height(s2_v.height)
        s2_1_u_value_NEW.next_to(s2_1_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        self.play(
            m.FadeOut(s2_1_v),
            m.FadeOut(s2_1_u),
            m.Transform(s_2_1_v_value, s2_1_v_value_NEW),
            m.Transform(s_2_1_u_value, s2_1_u_value_NEW),
            m.Circumscribe(m.VGroup(s2_1_v_value_NEW, s2_1_u_value_NEW, mcts_s2_1_score_group), color=TC.PINK,
                           fade_out=True),
        )

        # propagate to s_2_1
        self.play(
            m.ShowPassingFlash(
                m.VGroup(mcts_s2_arrow_1).copy().set_color(RwthTheme.rwth_magenta_75),
                time_width=1.0
            ),
            rate_func=lambda t: 1 - t
        )

        # update s_2 U and V values
        s2_v_value_NEW = TE.text("0.55").scale_to_fit_height(s2_v.height)
        s2_v_value_NEW.next_to(s2_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s2_u_value_NEW = TE.text("0.30").scale_to_fit_height(s2_v.height)
        s2_u_value_NEW.next_to(s2_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        self.play(
            m.FadeOut(s2_v),
            m.FadeOut(s2_u),
            m.Transform(s_2_v_value, s2_v_value_NEW),
            m.Transform(s_2_u_value, s2_u_value_NEW),
            m.Circumscribe(m.VGroup(s2_v_value_NEW, s2_u_value_NEW, mcts_s2_score_group), color=TC.PINK, fade_out=True),
        )

        # propagate to root node
        self.play(
            m.ShowPassingFlash(
                m.VGroup(mcts_arrow_s2).copy().set_color(RwthTheme.rwth_magenta_75),
                time_width=1.0
            ),
            rate_func=lambda t: 1 - t
        )

        mcts_s2_1.generate_target()
        mcts_s2_1.target.set_stroke(color=RwthTheme.rwth_blau_75)
#         mcts_s2_1.target[1].set_color(TC.DEFAULT_FONT)

        self.play(
            m.MoveToTarget(mcts_s2_1),
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_selection, corner_radius=0.125, color=RwthTheme.rwth_magenta_75)),
            m.Uncreate(attention_phase_rect)
        )

        mcts_root_node.generate_target()
        mcts_root_node.target.set_stroke(color=RwthTheme.rwth_gruen_75)
        # mcts_root_node.target[1].set_color(TC.GREY_DARK)

        self.play(
            m.MoveToTarget(mcts_root_node),
        )

        # Indicate s_1, s_2, s_3 V values
        self.play(
            m.Circumscribe(s_1_v_value, color=RwthTheme.rwth_gruen_75, fade_out=True),
            m.Circumscribe(s_2_v_value, color=RwthTheme.rwth_gruen_75, fade_out=True),
            m.Circumscribe(s_3_v_value, color=RwthTheme.rwth_gruen_75, fade_out=True),
        )

        # Indicate s_2 V value
        self.play(
            m.Circumscribe(s_2_v_value, color=RwthTheme.rwth_gruen_75, fade_out=True),
        )

        # move s_2 to root node
        mcts_s2.generate_target()
        mcts_s2.target.move_to(mcts_root_node.get_center())

        # fade out all other mcts elements
        mcts_fade_out_elems = [
            # nodes
            mcts_root_node,
            mcts_s1, mcts_s3,
            mcts_s2_1, mcts_s2_2, mcts_s2_3,
            mcts_s3_1, mcts_s3_2, mcts_s3_3,
            mcts_s2_1_1, mcts_s2_1_2, mcts_s2_1_3,
            # arrows
            mcts_arrow_s1, mcts_arrow_s2, mcts_arrow_s3,
            mcts_s2_arrow_1, mcts_s2_arrow_2, mcts_s2_arrow_3,
            mcts_s3_arrow_1, mcts_s3_arrow_2, mcts_s3_arrow_3,
            mcts_s2_1_arrow_1, mcts_s2_1_arrow_2, mcts_s2_1_arrow_3,
            # mcts value groups
            *mcts_s1_score_group, *mcts_s2_score_group, *mcts_s3_score_group,
            *mcts_s2_1_score_group, *mcts_s2_2_score_group, *mcts_s2_3_score_group,
            *mcts_s3_1_score_group, *mcts_s3_2_score_group, *mcts_s3_3_score_group,
            *mcts_s2_1_1_score_group, *mcts_s2_1_2_score_group, *mcts_s2_1_3_score_group,
            # mcts value texts
            s_1_v_value, s_1_u_value,
            s_2_v_value, s_2_u_value,
            s_3_v_value, s_3_u_value,
            s_2_1_v_value, s_2_1_u_value,
            s_2_2_v_value, s_2_2_u_value,
            s_2_3_v_value, s_2_3_u_value,
            s_3_1_v_value, s_3_1_u_value,
            s_3_2_v_value, s_3_2_u_value,
            s_3_3_v_value, s_3_3_u_value,
            s_2_1_1_v_value, s_2_1_1_u_value,
            s_2_1_2_v_value, s_2_1_2_u_value,
            s_2_1_3_v_value, s_2_1_3_u_value,
        ]

        # new mcts iteration

        neural_mcts_title = TE.title_text("Neural Monte Carlo Tree Search")


        self.play(
            self.change_subtitle("Neural Monte Carlo Tree Search"),
            m.MoveToTarget(mcts_s2),
            *[m.FadeOut(elem) for elem in mcts_fade_out_elems if self.is_in_scene(elem)],
        )


        # Selection 0
        attention_phase_rect = m.SurroundingRectangle(rect_selection, corner_radius=0.125, color=RwthTheme.rwth_magenta_75)

        mcts_root_node = mcts_s2
        mcts_root_node.generate_target()
        mcts_root_node.target.set_stroke(color=RwthTheme.rwth_blau_75)
        # mcts_root_node.target[1].set_color(TC.GREY_DARK)

        self.play(
            m.MoveToTarget(mcts_root_node),
            m.Create(attention_phase_rect),
        )

        # Expansion 0

        mcts_s2_1 = TE.math_circle(
            "s_{4}",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=RwthTheme.rwth_blau_75,
            radius=0.25,
        ).scale(0.75)

        mcts_s2_1.move_to(np.array([
            mcts_s2.get_center()[0] - mcts_width_per_child_level_1 - mcts_h_buff,
            mcts_s2.get_center()[1] - mcts_vertical_space,
            0
        ])
        )

        mcts_s2_2 = TE.math_circle(
            "s_{5}",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=RwthTheme.rwth_blau_75,
            radius=0.25,
        ).scale(0.75)

        mcts_s2_2.move_to(np.array([
            mcts_s2.get_center()[0],
            mcts_s2.get_center()[1] - mcts_vertical_space,
            0
        ])
        )

        mcts_s2_3 = TE.math_circle(
            "s_{6}",
            font_color=TC.DEFAULT_FONT,
            fill_color=TC.GREY_DARK_LIGHT,
            stroke_color=RwthTheme.rwth_blau_75,
            radius=0.25,
        ).scale(0.75)

        mcts_s2_3.move_to(np.array([
            mcts_s2.get_center()[0] + mcts_width_per_child_level_1 + mcts_h_buff,
            mcts_s2.get_center()[1] - mcts_vertical_space,
            0
        ])
        )

        mcts_s2_1_arrow = TE.math_arrow(
            mcts_s2.get_center(),
            mcts_s2_1.get_center(),
            color=mcts_arrow_color,
            buff=0.25,
        )

        mcts_s2_2_arrow = TE.math_arrow(
            mcts_s2.get_center(),
            mcts_s2_2.get_center(),
            color=mcts_arrow_color,
            buff=0.25,
        )

        mcts_s2_3_arrow = TE.math_arrow(
            mcts_s2.get_center(),
            mcts_s2_3.get_center(),
            color=mcts_arrow_color,
            buff=0.25,
        )

        self.play(
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_expansion, corner_radius=0.125, color=RwthTheme.rwth_magenta_75)),
            m.FadeIn(mcts_s2_1),
            m.FadeIn(mcts_s2_2),
            m.FadeIn(mcts_s2_3),
            m.GrowArrow(mcts_s2_1_arrow),
            m.GrowArrow(mcts_s2_2_arrow),
            m.GrowArrow(mcts_s2_3_arrow),
        )

        # Evaluation 0
        mcts_s2_1_score_group, s2_1_v, s2_1_u, *_ = mcts_score_group(mcts_s2_1)
        mcts_s2_2_score_group, s2_2_v, s2_2_u, *_ = mcts_score_group(mcts_s2_2)
        mcts_s2_3_score_group, s2_3_v, s2_3_u, *_ = mcts_score_group(mcts_s2_3)

        self.play(
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_evaluation, corner_radius=0.125, color=RwthTheme.rwth_magenta_75)),
            m.FadeIn(mcts_s2_1_score_group),
            m.FadeIn(mcts_s2_2_score_group),
            m.FadeIn(mcts_s2_3_score_group),
        )

        ai_rect = TE.rectangle_with_icon(
            icon='i_seti_illustrator',
            # icon_color=TC.PINK,
            icon_scale=TE.font_normalsize,
            width=total_width - 2 * 0.5,
            height=2.4
        )

        # align with rect_back_propagation on left side
        ai_rect.next_to(rect_back_propagation, m.DOWN, buff=phase_buff, aligned_edge=m.LEFT)

        v_nn = PU.simple_neural_network(
            neuron_circle_kwargs={'stroke_color': RwthTheme.rwth_gruen_75},
            output_layer_dim=1,
            input_layer_dim=5
        )
        v_nn.scale_to_fit_height(ai_rect.height - 0.5)

        p_nn = PU.simple_neural_network(
            neuron_circle_kwargs={'stroke_color': RwthTheme.rwth_magenta_75},
            output_layer_dim=1,
            input_layer_dim=5
        )
        p_nn.scale_to_fit_height(ai_rect.height - 0.5)

        p_nn.next_to(v_nn, m.RIGHT, buff=1.25)

        ai_rect_v_line = ai_rect[-1]

        ai_rect_h_offset = (ai_rect_v_line.get_center() - ai_rect.get_left())[1]

        nn_group = m.VGroup(v_nn, p_nn)
        nn_group.move_to(ai_rect.get_center() + m.RIGHT * ai_rect_h_offset)

        self.play(
            m.FadeIn(ai_rect),
            m.FadeIn(nn_group),
        )

        v_nn_input_layer_copy1 = v_nn[-1][0].copy()
        p_nn_input_layer_copy1 = p_nn[-1][0].copy()

        v_nn_input_layer_copy2 = v_nn[-1][0].copy()
        p_nn_input_layer_copy2 = p_nn[-1][0].copy()

        v_nn_input_layer_copy3 = v_nn[-1][0].copy()
        p_nn_input_layer_copy3 = p_nn[-1][0].copy()

        self.play_without_section(
            m.TransformFromCopy(mcts_s2_1, v_nn_input_layer_copy1),
            m.TransformFromCopy(mcts_s2_1, p_nn_input_layer_copy1),

            m.TransformFromCopy(mcts_s2_2, v_nn_input_layer_copy2),
            m.TransformFromCopy(mcts_s2_2, p_nn_input_layer_copy2),

            m.TransformFromCopy(mcts_s2_3, v_nn_input_layer_copy3),
            m.TransformFromCopy(mcts_s2_3, p_nn_input_layer_copy3),
        )
        self.remove(
            v_nn_input_layer_copy1, p_nn_input_layer_copy1,
            v_nn_input_layer_copy2, p_nn_input_layer_copy2,
            v_nn_input_layer_copy3, p_nn_input_layer_copy3,
        )

        self.play(
            PU.simple_neural_network_forward_animation(color=TC.PINK, nn=v_nn),
            PU.simple_neural_network_forward_animation(color=TC.PINK, nn=p_nn),
        )

        s_2_1_v_value = TE.text("0.39").scale_to_fit_height(s2_v.height)
        s_2_1_v_value.next_to(s2_1_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_2_1_u_value = TE.text("0.28").scale_to_fit_height(s2_v.height)
        s_2_1_u_value.next_to(s2_1_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_2_2_v_value = TE.text("0.56").scale_to_fit_height(s2_v.height)
        s_2_2_v_value.next_to(s2_2_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_2_2_u_value = TE.text("0.71").scale_to_fit_height(s2_v.height)
        s_2_2_u_value.next_to(s2_2_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_2_3_v_value = TE.text("0.45").scale_to_fit_height(s2_v.height)
        s_2_3_v_value.next_to(s2_3_v.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        s_2_3_u_value = TE.text("0.63").scale_to_fit_height(s2_v.height)
        s_2_3_u_value.next_to(s2_3_u.get_right(), m.RIGHT, aligned_edge=m.LEFT, buff=-0.05)

        self.play(
            *[m.FadeOut(elem) for elem in [s2_1_v, s2_1_u, s2_2_v, s2_2_u, s2_3_v, s2_3_u]],
            m.TransformFromCopy(p_nn[-1][-1], s_2_1_u_value),
            m.TransformFromCopy(p_nn[-1][-1], s_2_2_u_value),
            m.TransformFromCopy(p_nn[-1][-1], s_2_3_u_value),
            m.TransformFromCopy(v_nn[-1][-1], s_2_1_v_value),
            m.TransformFromCopy(v_nn[-1][-1], s_2_2_v_value),
            m.TransformFromCopy(v_nn[-1][-1], s_2_3_v_value),
        )

        # BACK-PROPAGATION 0

        self.play(
            m.Transform(attention_phase_rect,
                        m.SurroundingRectangle(rect_back_propagation, corner_radius=0.125, color=RwthTheme.rwth_magenta_75))
        )

        self.play(
            m.Indicate(s_2_1_v_value, color=TC.PINK),
            m.Indicate(s_2_1_u_value, color=TC.PINK),
            m.Indicate(s_2_2_v_value, color=TC.PINK),
            m.Indicate(s_2_2_u_value, color=TC.PINK),
            m.Indicate(s_2_3_v_value, color=TC.PINK),
            m.Indicate(s_2_3_u_value, color=TC.PINK),
        )

        self.play(
            m.ShowPassingFlash(
                m.VGroup(mcts_s2_1_arrow, mcts_s2_2_arrow, mcts_s2_3_arrow)
                .copy().set_color(RwthTheme.rwth_magenta_75),
                time_width=1.0
            ),
            rate_func=lambda t: 1 - t
        )

        neural_mcts_title = TE.title_text("Interim Summary")

        dark_grey_rect = TE.rectangle(
            fill_color=RwthTheme.background_color,
            stroke_color=RwthTheme.background_color,
            width=16,
            height=6.0
        ).shift(m.DOWN * 0.15)

        self.play(
            *[
                m.FadeOut(e) for e in [
                    ai_rect, nn_group,
                    mcts_root_node, mcts_s2_1, mcts_s2_2, mcts_s2_3,
                    mcts_s2_1_score_group, mcts_s2_2_score_group, mcts_s2_3_score_group,
                    s_2_1_v_value, s_2_1_u_value,
                    s_2_2_v_value, s_2_2_u_value,
                    s_2_3_v_value, s_2_3_u_value,
                    attention_phase_rect,
                    p_nn, v_nn,
                    *p_nn, *v_nn,
                    p_nn[-1][-1],
                    v_nn[-1][-1],
                    rect_selection, rect_expansion, rect_evaluation, rect_back_propagation,
                    v_nn_input_layer_copy1, p_nn_input_layer_copy1,
                    v_nn_input_layer_copy2, p_nn_input_layer_copy2,
                    v_nn_input_layer_copy3, p_nn_input_layer_copy3,
                    mcts_s2_1_arrow, mcts_s2_2_arrow, mcts_s2_3_arrow,

                    s2_1_v, s2_1_u, s2_2_v, s2_2_u, s2_3_v, s2_3_u,
                ] if self.is_in_scene(e)
            ],
            m.FadeIn(dark_grey_rect),
            self.set_title_row(
                title="Summary",
                seperator=None,
                subtitle=None,
            )
        )

        conclusion_buff = TE.buff_normal

        perso_production = TE.bullet_point_rectangle(
            width=self.content_width,
            icon="factory",
            title_rows=["Personalized production yields a high degree of flexibility in the production environment"],
            bullet_points=[
                ["Assigning tasks to machines"],
                ["Assingning personal to machines"],
                # ["Offline approach es are not feasible"],
            ]
        )
        perso_production.next_to(self._title_mobject, m.DOWN, buff=conclusion_buff+0.025, aligned_edge=m.LEFT)

        time_budget = TE.bullet_point_rectangle(
            width=self.content_width,
            icon="timer",
            title_rows=["The resulting optimization problem have a few minutes of time budget"],
            bullet_points=[
                ["MCTS is a anytime algorithm, that can make use of the time budget effectively"],
            ]
        )
        time_budget.next_to(perso_production, m.DOWN, buff=conclusion_buff, aligned_edge=m.LEFT)

        mcts_neural_guidance = TE.bullet_point_rectangle(
            width=self.content_width,
            icon="graph-outline",
            title_rows=["Monte Carlo Tree Search can be guided by a neural networks"],
            bullet_points=[
                ["For obtaining value V, and selection score U neural networks can be incorporated"],
            ]
        )
        mcts_neural_guidance.next_to(time_budget, m.DOWN, buff=conclusion_buff, aligned_edge=m.LEFT)

        self.play(
            m.FadeIn(perso_production),
            m.FadeIn(time_budget),
        )

        self.play(
            m.FadeIn(mcts_neural_guidance),
        )

        self.play(
            self.overlay_scene()
        )





if __name__ == '__main__':
    FIopMCTSVanilla.save_sections_without_cache()