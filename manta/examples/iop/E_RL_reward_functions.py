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

class EIopRlRewardFunctions(RwthTheme, AxesUtils, GanttUtils, RwthSlideTemplate):

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
    index_prefix = "H "

    def construct(self):
        self.play(
            self.set_title_row(
                title="RL Approach",
                seperator=": ",
                subtitle="Reward Functions"
            ),
            self.add_logos(),
            self.add_seperator_line_top(),
            self.add_seperator_line_bottom()
        )


        terminal_case_1 = m.MathTex(r"\mathtt{C}", r"\over", r"\mathtt{C_{LB}}", color=C.DEFAULT_FONT).scale(
            0.75).move_to(m.UP * 0.5)
        terminal_case_0 = m.MathTex(r"-", color=C.DEFAULT_FONT).scale(0.75).next_to(terminal_case_1, m.LEFT, buff=0.25)
        terminal_case_desc = m.MathTex("\mathtt{terminal}", color=C.DEFAULT_FONT).scale(0.75)
        terminal_case_desc.next_to(np.array([1.5, 0.5, 0]), m.RIGHT, buff=0)

        else_case = styled_text(r" 0 ", color=C.DEFAULT_FONT).scale(0.625).move_to(m.DOWN * 0.5)
        else_case_desc = m.MathTex("\mathtt{else}", color=C.DEFAULT_FONT).scale(0.75).next_to(else_case, m.RIGHT,
                                                                                              buff=0.25)
        else_case_desc.next_to(np.array([1.5, -0.5, 0]), m.RIGHT, buff=0)

        # brace
        brace = m.BraceBetweenPoints(np.array([-1, 1, 0]), np.array([-1, -0.75, 0]), direction=m.LEFT)

        rew_function_tex = (m.MathTex(r"\mathtt{r(s_t) }", "\:\mathtt{= }", color=C.DEFAULT_FONT)
                            .scale(0.75).next_to(brace, m.LEFT, buff=0.25))

        trivial_rew_function_group = m.VGroup(
            terminal_case_0,
            terminal_case_1,
            terminal_case_desc,
            else_case,
            else_case_desc,
            brace,
            rew_function_tex,
        )

        trivial_rew_function_group.shift(m.UP * 1.5)
        trivial_rew_function_group.shift(m.LEFT * 3.25)

        self.play(
            self.change_subtitle("Trivial Reward Function"),
            m.FadeIn(trivial_rew_function_group),
        )


        sur_rect_1 = m.SurroundingRectangle(terminal_case_1[0], buff=.1, color=C.PINK)
        sur_rect_description_1 = styled_text("Makespan", color=C.PINK).scale(0.625)
        sur_rect_description_1.move_to(np.array([5, sur_rect_1.get_center()[1], 0]))

        self.play(
            m.Create(sur_rect_1),
            m.FadeIn(sur_rect_description_1)
        )


        sur_rect_2 = m.SurroundingRectangle(terminal_case_1[2], buff=.1, color=RwthTheme.rwth_orange_75)
        sur_rect_description_2 = styled_text("Lower Bound", color=RwthTheme.rwth_orange_75).scale(0.625)
        sur_rect_description_2.move_to(np.array([5, sur_rect_2.get_center()[1], 0]))

        self.play(
            m.Create(sur_rect_2),
            m.FadeIn(sur_rect_description_2)
        )



        class MyText(m.Text):
            def __init__(self, *tex_strings, **kwargs):
                super().__init__(*tex_strings, font="Iosevka Nerd Font", **kwargs)

        axes = m.Axes(
            x_range=[0, 41, 1],
            y_range=[0, 4, 1],
            x_length=10.5,
            y_length=1.75,
            y_axis_config={"tick_size": 0},
            x_axis_config={
                "tick_size": 0.0425,
                "numbers_to_include": [0, 5, 10, 15, 20, 25, 30, 35, 40],
                "numbers_with_elongated_ticks": [0, 5, 10, 15, 20, 25, 30, 35, 40],
                "font_size": 20,
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

        axes.move_to([0.5, -1.75, 0])
        axes.set_color(C.DEFAULT_FONT)
        labels = axes.get_axis_labels(x_label=styled_text("time").scale(0.5), y_label='')
        labels.set_color(C.DEFAULT_FONT)

        labels.shift(0.5 * m.DOWN)

        job0_title = styled_text("Job 0", color=C.DEFAULT_FONT).scale(0.5)
        job0_title.move_to(axes.c2p(-4, 2.5))

        job1_title = styled_text("Job 1", color=C.DEFAULT_FONT).scale(0.5)
        job1_title.move_to(axes.c2p(-4, 1.5))

        reward_text = styled_text("Reward: ", color=C.DEFAULT_FONT).scale(0.5).to_corner(m.UL, buff=0.5)
        reward_text.next_to(np.array([rew_function_tex.get_left()[0], 0, 0]), m.RIGHT, buff=0.0)

        # rewards_tex = m.MathTex(r"0", r"\:,", r"0", r"\:,", r"0", r"\:,", r"0", r"\:,", r"0", r"\:,", r"0", r"\:,",
        #                       r"0", r"\:,", r"-1",
        #                       color=C.DEFAULT_FONT).scale(0.625).next_to(reward_text, m.RIGHT, buff=0.0)
        calc_obj_0 = styled_text("0", color=C.DEFAULT_FONT).scale(0.5)
        calc_obj_comma = styled_text(",", color=C.DEFAULT_FONT).scale(0.5)
        comma_shift = calc_obj_0.height - calc_obj_comma.height
        rewards_tex = m.Group(
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5),
            styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("-1", color=C.DEFAULT_FONT).scale(0.5),
        ).arrange(m.RIGHT, buff=0.125)
        rewards_tex.next_to(reward_text.get_right(), m.RIGHT, buff=0.25)
        for i in range(1, len(rewards_tex), 2):
            rewards_tex[i].shift(comma_shift * m.DOWN)
        # rewards_tex.shift(m.DOWN * 0.05)

        self.play(
            m.FadeIn(reward_text),
            m.Uncreate(sur_rect_1),
            m.Uncreate(sur_rect_2),
            m.FadeOut(sur_rect_description_1),
            m.FadeOut(sur_rect_description_2),
            m.FadeIn(axes),
            m.FadeIn(labels),
            m.FadeIn(job0_title),
            m.FadeIn(job1_title),
        )

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
        # j1_t1.z_index = axes.z_index - 1

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

        self.play(
            m.FadeIn(j1_t1),
            m.TransformFromCopy(else_case, rewards_tex[0]),
        )
        #

        self.play(
            m.FadeIn(j0_t1),
            m.FadeIn(rewards_tex[1]),
            m.TransformFromCopy(else_case, rewards_tex[2]),
        )

        #
        run_time = 0.35

        self.play(
            m.FadeIn(j0_t2,
                     #
                     ),
            m.FadeIn(rewards_tex[3],
                     #
                     ),
            m.TransformFromCopy(else_case, rewards_tex[4],
                                #
                                ),
        )
        #

        self.play(
            m.FadeIn(j1_t2,
                     #
                     ),
            m.FadeIn(rewards_tex[5],
                     #
                     ),
            m.TransformFromCopy(else_case, rewards_tex[6],
                                #
                                ),
        )
        # self.wait(WAIT_TIME * 0.5)

        self.play(
            m.FadeIn(j0_t3,
                     #
                     ),
            m.FadeIn(rewards_tex[7],
                     #
                     ),
            m.TransformFromCopy(else_case, rewards_tex[8],
                                #
                                ),
        )
        # self.wait(WAIT_TIME * 0.5)

        self.play(
            m.FadeIn(j1_t3,
                     #
                     ),
            m.FadeIn(rewards_tex[9],
                     #
                     ),
            m.TransformFromCopy(else_case, rewards_tex[10],
                                #
                                ),
        )
        # self.wait(WAIT_TIME * 0.5)

        self.play(
            m.FadeIn(j0_t4,
                     #
                     ),
            m.FadeIn(rewards_tex[11],
                     #
                     ),
            m.TransformFromCopy(else_case, rewards_tex[12],
                                #
                                ),
        )
        terminal_case_group = m.VGroup(terminal_case_0, terminal_case_1)

        self.play(
            m.FadeIn(j1_t4,
                     #
                     ),
        )
        # self.wait(WAIT_TIME * 0.5)

        makespan_brace = m.BraceBetweenPoints(axes.c2p(0, 2.75), axes.c2p(40, 2.75), direction=m.UP)
        makespan_brace.set_color(C.PINK)

        makespan_text = styled_text("Makespan", color=C.PINK).scale(0.5)
        makespan_text.move_to(makespan_brace.get_center() + m.UP * 0.5)

        lower_bound_text = styled_text("Lower Bound = 40", color=RwthTheme.rwth_orange_75).scale(0.5)
        lower_bound_text.next_to(makespan_text.get_top() + m.RIGHT * 1.5, m.DR, buff=0.0)

        self.play(
            m.Write(makespan_brace),
            m.FadeIn(makespan_text),
            m.FadeIn(lower_bound_text),
        )


        self.play(
            m.FadeOut(makespan_brace),
            m.Transform(makespan_text, terminal_case_1[0]),
            m.Transform(lower_bound_text, terminal_case_1[2]),
        )

        self.remove(makespan_text, lower_bound_text)
        self.play(
            m.FadeIn(rewards_tex[13]),
            m.TransformFromCopy(terminal_case_group, rewards_tex[14]),
        )


        # Samsonov

        terminal_case_1_samsonov = m.MathTex(r"\mathtt{\gamma}",
                                             r"^{\mathtt{C_{opt}}}",
                                             r"\over",
                                             r"\mathtt{\gamma}",
                                             r"^{\mathtt{C}}",
                                             color=C.DEFAULT_FONT).scale(0.75).move_to(m.UP * 0.5 + m.RIGHT * 0.5)
        terminal_case_0_samsonov = styled_text("1000", color=C.DEFAULT_FONT).scale(0.625).next_to(
            terminal_case_1_samsonov, m.LEFT, buff=0.25)

        else_case_samsonov = styled_text(" 0 ", color=C.DEFAULT_FONT).scale(0.625).move_to(m.DOWN * 0.5 + m.RIGHT * 0.5)

        samsonov_rew_function_group = m.VGroup(
            terminal_case_1_samsonov,
            terminal_case_0_samsonov,
            else_case_samsonov
        )
        samsonov_rew_function_group.shift(m.UP * 1.5)
        samsonov_rew_function_group.shift(m.LEFT * 3.25)

        job_polygons = [j0_t1, j0_t2, j0_t3, j0_t4, j1_t1, j1_t2, j1_t3, j1_t4]

        self.play(
            self.change_subtitle("Samsonov et al."),
            #m.Transform(reward_function_trivial, reward_function_samsonov, replace_mobject_with_target_in_scene=True),
            m.Transform(terminal_case_1, terminal_case_1_samsonov, replace_mobject_with_target_in_scene=True),
            m.Transform(terminal_case_0, terminal_case_0_samsonov, replace_mobject_with_target_in_scene=True),
            m.Transform(else_case, else_case_samsonov, replace_mobject_with_target_in_scene=True),
            m.FadeOut(rewards_tex),
            *[m.FadeOut(p) for p in job_polygons],
        )


        spacing = 0.75
        padding = 0.75
        param_C = m.MathTex(r"\mathtt{C}", color=C.DEFAULT_FONT).scale(0.625)
        param_C.next_to(m.UP * spacing, m.DR, buff=0.0)
        param_C_opt = m.MathTex(r"\mathtt{C_{opt}}", color=C.DEFAULT_FONT).scale(0.625)
        param_C_opt.next_to(m.ORIGIN * spacing, m.DR, buff=0.0)
        param_gamma = m.MathTex(r"\mathtt{\gamma}", color=C.DEFAULT_FONT).scale(0.625)
        param_gamma.next_to(m.DOWN * spacing, m.DR, buff=0.0)

        param_C_desc = styled_text("Makespan", color=C.DEFAULT_FONT).scale(0.45)
        param_C_desc.next_to(m.UP * spacing + m.RIGHT * padding, m.DR, buff=0.0)
        param_C_opt_desc = styled_text("Optimal Makespan", color=C.DEFAULT_FONT).scale(0.45)
        param_C_opt_desc.next_to(m.ORIGIN * spacing + m.RIGHT * padding, m.DR, buff=0.0)
        param_gamma_desc = styled_text("parameter", color=C.DEFAULT_FONT).scale(0.45)
        param_gamma_desc.next_to(m.DOWN * spacing + m.RIGHT * padding, m.DR, buff=0.0)

        param_group = m.VGroup(
            param_C,
            param_C_opt,
            param_gamma,
            param_C_desc,
            param_C_opt_desc,
            param_gamma_desc
        )

        param_group.move_to(np.array([3, rew_function_tex.get_center()[1], 0]))

        self.play(
            m.FadeIn(param_group)
        )


        rewards_tex = m.Group(
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.625),
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5),
            styled_text(",", color=C.DEFAULT_FONT).scale(0.5),

            styled_text("0", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("1000", color=C.DEFAULT_FONT).scale(0.5),
        ).arrange(m.RIGHT, buff=0.125)
        rewards_tex.next_to(reward_text.get_right(), m.RIGHT, buff=0.25)
        for i in range(1, len(rewards_tex), 2):
            rewards_tex[i].shift(comma_shift * m.DOWN)

        self.play(
            m.FadeIn(j1_t1),
            m.TransformFromCopy(else_case_samsonov, rewards_tex[0]),
        )

        self.play(
            m.FadeIn(j0_t1),
            m.FadeIn(rewards_tex[1]),
            m.TransformFromCopy(else_case_samsonov, rewards_tex[2]),
        )
        run_time = 0.35
        self.play_without_section(
            m.FadeIn(j0_t2, ),
            m.FadeIn(rewards_tex[3], ),
            m.TransformFromCopy(else_case_samsonov, rewards_tex[4], ),
        )

        self.play_without_section(
            m.FadeIn(j1_t2, ),
            m.FadeIn(rewards_tex[5], ),
            m.TransformFromCopy(else_case_samsonov, rewards_tex[6], ),
        )

        self.play_without_section(
            m.FadeIn(j0_t3, ),
            m.FadeIn(rewards_tex[7], ),
            m.TransformFromCopy(else_case_samsonov, rewards_tex[8], ),
        )

        self.play_without_section(
            m.FadeIn(j1_t3, ),
            m.FadeIn(rewards_tex[9], ),
            m.TransformFromCopy(else_case_samsonov, rewards_tex[10], ),
        )

        self.play_without_section(
            m.FadeIn(j0_t4, ),
            m.FadeIn(rewards_tex[11], ),
            m.TransformFromCopy(else_case_samsonov, rewards_tex[12], ),
        )

        makespan_brace = m.BraceBetweenPoints(axes.c2p(0, 2.75), axes.c2p(40, 2.75), direction=m.UP)
        makespan_brace.set_color(C.PINK)

        makespan_text = styled_text("Makespan", color=C.PINK).scale(0.5)
        makespan_text.move_to(makespan_brace.get_center() + m.UP * 0.5)

        opt_makespan_text = m.MathTex("\mathtt{C_{opt}}", "\:\mathtt{=}\:", "40", color=RwthTheme.rwth_orange_75).scale(0.65)
        opt_makespan_text = m.Group(
            opt_makespan_text[0],
            opt_makespan_text[1],
            styled_text("40", color=RwthTheme.rwth_orange_75)
            .scale_to_fit_height(opt_makespan_text[2].height)
            .move_to(opt_makespan_text[2].get_center() + m.RIGHT * 0.125)
        )
        opt_makespan_text.next_to(makespan_text.get_top() + m.RIGHT * 1.25, m.DR, buff=0.0)

        gamma_text = m.MathTex(r"\mathtt{\gamma}", "\:\mathtt{=}\:", "1.025", color=C.ORANGE_DARK).scale(0.65)
        gamma_text = m.Group(
            gamma_text[0],
            gamma_text[1],
            styled_text("1.025", color=C.ORANGE_DARK)
            .scale_to_fit_height(gamma_text[2].height).move_to(gamma_text[2].get_center() + m.RIGHT * 0.125)
        )
        gamma_text.next_to(opt_makespan_text.get_top() + m.RIGHT * 1.325, m.DR, buff=0.0)

        self.play_without_section(
            m.FadeIn(j1_t4),
            m.Write(makespan_brace),
            m.FadeIn(makespan_text),
            m.FadeIn(opt_makespan_text),
            m.FadeIn(gamma_text),
        )
        gamma_text_copy = gamma_text.copy()

        self.play(
            m.FadeOut(makespan_brace),
            m.Transform(makespan_text, terminal_case_1_samsonov[4]),
            m.Transform(opt_makespan_text[2], terminal_case_1_samsonov[4]),
            m.FadeOut(opt_makespan_text[:2]),
            m.Transform(gamma_text_copy[2], terminal_case_1_samsonov[0]),
            m.Transform(gamma_text[2], terminal_case_1_samsonov[3]),
            m.FadeOut(gamma_text[:2]),
        )
        self.remove(makespan_text, opt_makespan_text, gamma_text, gamma_text_copy, opt_makespan_text[2],
                    gamma_text_copy[2], gamma_text[2])

        terminal_case_samsonov_group = m.VGroup(terminal_case_0_samsonov, terminal_case_1_samsonov)

        self.play(
            m.FadeIn(rewards_tex[13]),
            m.TransformFromCopy(terminal_case_samsonov_group, rewards_tex[14]),
        )

        samsonov_group = m.VGroup(
            terminal_case_0_samsonov,
            terminal_case_1_samsonov,
            else_case_samsonov,
            # brace,
            # terminal_case_desc,
            # else_case_desc,
        )

        # graph-tassel

        graph_tassel_function_tex = m.MathTex(
            r"\sum\limits_{"
            r"\substack{\mathtt{\alpha} \\ \exists \hat{\mathtt{s}}_{\mathtt{\alpha}}}"
            r"} \mathtt{p}_{\mathtt{\alpha}}",
            r"\over",
            r"|\mathcal{M}| \ \mathtt{\max\limits_{\substack{"
            r"\mathtt{\alpha} \\ \exists \hat{\mathtt{s}}_{\mathtt{\alpha}}}"
            r"} \hat{\mathtt{s}}_{\mathtt{\alpha}} + \mathtt{p}_{\mathtt{\alpha}}}",
            color=C.DEFAULT_FONT
        ).scale(0.75)

        graph_tassel_function_tex.shift(m.UP * 1.682)
        graph_tassel_function_tex.shift(m.LEFT * 3.25)

        rew_func_eq_sign_copy = rew_function_tex[1].copy()
        rew_func_eq_sign_copy.shift(m.RIGHT * 3.675)

        rew_func_prop_sign_copy = m.MathTex("\mathtt{\propto}", color=C.DEFAULT_FONT)
        rew_func_prop_sign_copy.move_to(rew_func_eq_sign_copy.get_center())

        graph_tassel_function_tex2 = m.MathTex(
            r"\sum\limits_{"
            r"\substack{\mathtt{\alpha} \\ \exists \hat{\mathtt{s}}_{\mathtt{\alpha}}}"
            r"} \mathtt{p}_{\mathtt{\alpha}}",
            r"\over",
            r"|\mathcal{J}| \ \mathtt{\max\limits_{\substack{"
            r"\mathtt{\alpha} \\ \exists \hat{\mathtt{s}}_{\mathtt{\alpha}}}"
            r"} \hat{\mathtt{s}}_{\mathtt{\alpha}} + \mathtt{p}_{\mathtt{\alpha}}}",
            color=C.DEFAULT_FONT
        ).scale(0.75)

        graph_tassel_function_tex2.shift(m.UP * 1.682)
        graph_tassel_function_tex2.shift(m.RIGHT * 0.35)

        graph_tassel_function_group = m.VGroup(
            graph_tassel_function_tex,
            graph_tassel_function_tex2,
            rew_func_prop_sign_copy,
        )

        self.play(
            self.change_subtitle("Tassel et al."),
            #m.Transform(reward_function_samsonov, reward_function_graph_tassel,
            #           replace_mobject_with_target_in_scene=True),
            m.FadeOut(param_group),
            m.FadeOut(rewards_tex),
            m.FadeOut(brace),
            m.FadeOut(terminal_case_desc),
            m.FadeOut(else_case_desc),
            *[m.FadeOut(p) for p in job_polygons],
            m.Transform(samsonov_group, graph_tassel_function_group, replace_mobject_with_target_in_scene=True),
        )



        rew_func_eq_sign_copy = rew_function_tex[1].copy()
        rew_func_eq_sign_copy.shift(m.RIGHT * 7.125)

        tassel_frac_line = m.Line(
            rew_func_eq_sign_copy.get_right(),
            rew_func_eq_sign_copy.get_right() + m.RIGHT * 3.5,
            buff=0.25,
            stroke_width=1.5,
            color=C.DEFAULT_FONT
        )

        tassel_scheduled_area_text = styled_text("Scheduled Area").scale(0.55)
        tassel_scheduled_area_text.next_to(tassel_frac_line.get_center(), m.UP, buff=0.25)

        tassel_total_area_text = styled_text("Total Area").scale(0.55)
        tassel_total_area_text.next_to(tassel_frac_line.get_center(), m.DOWN, buff=0.25)

        tassel_frac_group = m.VGroup(
            tassel_scheduled_area_text,
            tassel_frac_line,
            tassel_total_area_text,
        )

        self.play(
            m.FadeIn(rew_func_eq_sign_copy),
            m.FadeIn(tassel_frac_group)
        )


        rewards_tex = m.MathTex(r"0.5", r"\:,", r"0.5", r"\:,", r"0.5", r"\:,", r"0.83", r"\:,", r"0.79", r"\:,",
                                r"0.8",
                                r"\:,", r"0.79", r"\:,", r"0.76",
                                color=C.DEFAULT_FONT).scale(0.625).next_to(reward_text, m.RIGHT, buff=0.0)
        rewards_tex = m.Group(
            styled_text("0.5", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.625),
            styled_text("0.5", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0.5", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0.83", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0.79", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0.8", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0.79", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0.76", color=C.DEFAULT_FONT).scale(0.5),
        ).arrange(m.RIGHT, buff=0.125)
        rewards_tex.next_to(reward_text.get_right(), m.RIGHT, buff=0.25)
        for i in range(1, len(rewards_tex), 2):
            rewards_tex[i].shift(comma_shift * m.DOWN)

        total_area1 = m.Polygon(*[
            axes.c2p(5, 3),
            axes.c2p(0, 3),
            axes.c2p(0, 1),
            axes.c2p(5, 1),
        ], color=C.PINK, fill_opacity=0.0, stroke_width=3)
        # total_area1.z_index = axes.z_index - 1

        self.play(
            m.Write(j1_t1),
            m.FadeIn(total_area1)
        )
        scheduled_area = j1_t1.copy()
        self.play(
            m.Transform(total_area1, tassel_total_area_text),
            m.Transform(scheduled_area, tassel_scheduled_area_text)
        )
        self.remove(scheduled_area, total_area1)
        self.play_without_section(
            m.Transform(tassel_frac_group.copy(), rewards_tex[0], replace_mobject_with_target_in_scene=True),
        )
        # step 2
        total_area2 = m.Polygon(*[
            axes.c2p(16, 3),
            axes.c2p(0, 3),
            axes.c2p(0, 1),
            axes.c2p(16, 1),
        ], color=C.PINK, fill_opacity=0.0, stroke_width=3)
        self.play(
            m.FadeIn(j0_t1),
            m.FadeIn(total_area2)
        )
        scheduled_area = m.VGroup(j0_t1.copy(), j1_t1.copy())
        self.play_without_section(
            m.Transform(total_area2, tassel_total_area_text),
            m.Transform(scheduled_area, tassel_scheduled_area_text),
        )
        self.remove(scheduled_area, total_area2)
        self.play_without_section(
            m.FadeIn(rewards_tex[1]),
            m.Transform(tassel_frac_group.copy(), rewards_tex[2], replace_mobject_with_target_in_scene=True),
        )

        # step 3
        total_area3 = m.Polygon(*[
            axes.c2p(19, 3),
            axes.c2p(0, 3),
            axes.c2p(0, 1),
            axes.c2p(19, 1),
        ], color=C.PINK, fill_opacity=0.0, stroke_width=3)
        self.play_without_section(
            m.FadeIn(j0_t2),
            m.FadeIn(total_area2),
        )
        scheduled_area = m.VGroup(j0_t1.copy(), j1_t1.copy(), j0_t2.copy())
        self.play_without_section(
            m.Transform(total_area3, tassel_total_area_text),
            m.Transform(scheduled_area, tassel_scheduled_area_text),
        )
        self.remove(scheduled_area, total_area3)
        self.play_without_section(
            m.FadeIn(rewards_tex[3]),
            m.Transform(tassel_frac_group.copy(), rewards_tex[4], replace_mobject_with_target_in_scene=True),
        )

        # step 4
        total_area3 = m.Polygon(*[
            axes.c2p(21, 3),
            axes.c2p(0, 3),
            axes.c2p(0, 1),
            axes.c2p(21, 1),
        ], color=C.PINK, fill_opacity=0.0, stroke_width=3)
        self.play_without_section(
            m.FadeIn(j1_t2),
            m.FadeIn(total_area2),

        )
        scheduled_area = m.VGroup(j0_t1.copy(), j1_t1.copy(), j0_t2.copy(), j1_t2.copy())
        self.play_without_section(
            m.Transform(total_area3, tassel_total_area_text),
            m.Transform(scheduled_area, tassel_scheduled_area_text),

        )
        self.remove(scheduled_area, total_area3)
        self.play_without_section(
            m.FadeIn(rewards_tex[5]),
            m.Transform(tassel_frac_group.copy(), rewards_tex[6], replace_mobject_with_target_in_scene=True),

        )

        # step 5
        total_area3 = m.Polygon(*[
            axes.c2p(24, 3),
            axes.c2p(0, 3),
            axes.c2p(0, 1),
            axes.c2p(24, 1),
        ], color=C.PINK, fill_opacity=0.0, stroke_width=3)
        self.play_without_section(
            m.FadeIn(j0_t3),
            m.FadeIn(total_area2),

        )
        scheduled_area = m.VGroup(j0_t1.copy(), j1_t1.copy(), j0_t2.copy(), j1_t2.copy(), j0_t3.copy())
        self.play_without_section(
            m.Transform(total_area3, tassel_total_area_text),
            m.Transform(scheduled_area, tassel_scheduled_area_text),

        )
        self.remove(scheduled_area, total_area3)
        self.play_without_section(
            m.FadeIn(rewards_tex[7]),
            m.Transform(tassel_frac_group.copy(), rewards_tex[8], replace_mobject_with_target_in_scene=True),

        )

        # step 6
        total_area3 = m.Polygon(*[
            axes.c2p(28, 3),
            axes.c2p(0, 3),
            axes.c2p(0, 1),
            axes.c2p(28, 1),
        ], color=C.PINK, fill_opacity=0.0, stroke_width=3)
        self.play_without_section(
            m.FadeIn(j1_t3),
            m.FadeIn(total_area2),

        )
        scheduled_area = m.VGroup(j0_t1.copy(), j1_t1.copy(), j0_t2.copy(), j1_t2.copy(), j0_t3.copy(), j1_t3.copy())
        self.play_without_section(
            m.Transform(total_area3, tassel_total_area_text),
            m.Transform(scheduled_area, tassel_scheduled_area_text),

        )
        self.remove(scheduled_area, total_area3)
        self.play_without_section(
            m.FadeIn(rewards_tex[9]),
            m.Transform(tassel_frac_group.copy(), rewards_tex[10], replace_mobject_with_target_in_scene=True),

        )

        # step 7
        total_area3 = m.Polygon(*[
            axes.c2p(36, 3),
            axes.c2p(0, 3),
            axes.c2p(0, 1),
            axes.c2p(36, 1),
        ], color=C.PINK, fill_opacity=0.0, stroke_width=3)
        self.play_without_section(
            m.FadeIn(j0_t4),
            m.FadeIn(total_area2),

        )
        scheduled_area = m.VGroup(j0_t1.copy(), j1_t1.copy(), j0_t2.copy(), j1_t2.copy(), j0_t3.copy(), j1_t3.copy(),
                                  j0_t4.copy())
        self.play_without_section(
            m.Transform(total_area3, tassel_total_area_text),
            m.Transform(scheduled_area, tassel_scheduled_area_text),

        )
        self.remove(scheduled_area, total_area3)
        self.play_without_section(
            m.FadeIn(rewards_tex[11]),
            m.Transform(tassel_frac_group.copy(), rewards_tex[12], replace_mobject_with_target_in_scene=True),

        )

        # step 8
        total_area3 = m.Polygon(*[
            axes.c2p(40, 3),
            axes.c2p(0, 3),
            axes.c2p(0, 1),
            axes.c2p(40, 1),
        ], color=C.PINK, fill_opacity=0.0, stroke_width=3)
        self.play_without_section(
            m.FadeIn(j1_t4),
            m.FadeIn(total_area2)
        )
        scheduled_area = m.VGroup(j0_t1.copy(), j1_t1.copy(), j0_t2.copy(), j1_t2.copy(), j0_t3.copy(), j1_t3.copy(),
                                  j0_t4.copy(), j1_t4.copy())
        self.play_without_section(
            m.Transform(total_area3, tassel_total_area_text),
            m.Transform(scheduled_area, tassel_scheduled_area_text),

        )
        self.remove(scheduled_area, total_area3)
        self.play_without_section(
            m.FadeIn(rewards_tex[13]),
            m.Transform(tassel_frac_group.copy(), rewards_tex[14], replace_mobject_with_target_in_scene=True),
        )

        self.remove(total_area3, total_area1, total_area2)

        # zhang

        zhang_function_tex = m.MathTex(
            r"H(s_{t-1})",
            r"-",
            r"H(s_{t})",
            color=C.DEFAULT_FONT,
        ).scale(0.75)

        zhang_function_tex.shift(m.UP * 1.625)
        zhang_function_tex.shift(m.LEFT * 3.5)

        task_circle_kwargs = {
            "radius": 0.25,
            "stroke_width": 6,
            "fill_color": RwthTheme.rwth_orange_75,
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
        t1_text = m.MathTex("\mathtt{t_1}", color=C.GREY_DARK).scale(0.5)
        t1_group = m.VGroup(t1_circle, t1_text)
        t1_group.move_to(np.array([-3, row1_y, 0]))

        t2_circle = m.Circle(stroke_color=C.ORANGE_DARK, **task_circle_kwargs)
        t2_text = m.MathTex("\mathtt{t_2}", color=C.GREY_DARK).scale(0.5)
        t2_group = m.VGroup(t2_circle, t2_text)
        t2_group.move_to(np.array([-1, row1_y, 0]))

        t3_circle = m.Circle(stroke_color=C.GREEN, **task_circle_kwargs)
        t3_text = m.MathTex("\mathtt{t_3}", color=C.GREY_DARK).scale(0.5)
        t3_group = m.VGroup(t3_circle, t3_text)
        t3_group.move_to(np.array([1, row1_y, 0]))

        t4_circle = m.Circle(stroke_color=C.TEAL, **task_circle_kwargs)
        t4_text = m.MathTex("\mathtt{t_4}", color=C.GREY_DARK).scale(0.5)
        t4_group = m.VGroup(t4_circle, t4_text)
        t4_group.move_to(np.array([3, row1_y, 0]))

        t5_circle = m.Circle(stroke_color=C.BLUE, **task_circle_kwargs)
        t5_text = m.MathTex("\mathtt{t_5}", color=C.GREY_DARK).scale(0.5)
        t5_group = m.VGroup(t5_circle, t5_text)
        t5_group.move_to(np.array([-3, row2_y, 0]))

        t6_circle = m.Circle(stroke_color=C.GREEN, **task_circle_kwargs)
        t6_text = m.MathTex("\mathtt{t_6}", color=C.GREY_DARK).scale(0.5)
        t6_group = m.VGroup(t6_circle, t6_text)
        t6_group.move_to(np.array([-1, row2_y, 0]))

        t7_circle = m.Circle(stroke_color=C.ORANGE_DARK, **task_circle_kwargs)
        t7_text = m.MathTex("\mathtt{t_7}", color=C.GREY_DARK).scale(0.5)
        t7_group = m.VGroup(t7_circle, t7_text)
        t7_group.move_to(np.array([1, row2_y, 0]))

        t8_circle = m.Circle(stroke_color=C.TEAL, **task_circle_kwargs)
        t8_text = m.MathTex("\mathtt{t_9}", color=C.GREY_DARK).scale(0.5)
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
        t0_text = m.MathTex("\mathtt{t_0}", color=C.GREY_DARK).scale(0.5)
        t0_group = m.VGroup(t0_circle, t0_text)
        t0_group.move_to(np.array([-4.5, (row1_y + row2_y) * 0.5, 0]))

        t9_circle = m.Circle(stroke_color=C.DARK_FONT, **fictive_task_circle_kwargs)
        t9_text = m.MathTex("\mathtt{t_*}", color=C.GREY_DARK).scale(0.5)
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

        full_gantt_group = m.VGroup(*job_polygons, axes)

        graph.scale(0.8)
        graph.shift(m.UP * 0.125)

        self.play(
            self.change_subtitle("Zhang et al."),
            # m.Transform(reward_function_graph_tassel, reward_function_zhang, replace_mobject_with_target_in_scene=True),
            m.Transform(graph_tassel_function_group, zhang_function_tex),
            m.FadeOut(rewards_tex),
            # *[m.FadeOut(p) for p in job_polygons],
            # m.FadeOut(axes),
            m.FadeOut(tassel_frac_group),
            m.FadeOut(rew_func_eq_sign_copy),
            m.FadeOut(job0_title),
            m.FadeOut(job1_title),
            m.Transform(full_gantt_group, graph, replace_mobject_with_target_in_scene=True),
            m.FadeOut(labels),
        )


        rew_func_eq_sign_copy = rew_function_tex[1].copy()
        rew_func_eq_sign_copy.shift(m.RIGHT * 3.25)

        zhang_text = styled_text("- Increase in Critical Path").scale(0.55)

        zhang_text.move_to(tassel_frac_line.get_center() + m.LEFT * 2.5)
        zhang_text.shift(m.RIGHT * 0.125 + m.UP * 0.04)

        self.play(
            m.FadeIn(rew_func_eq_sign_copy),
            m.FadeIn(zhang_text)
        )


        longest_path_lines_kwargs = {
            "stroke_width": 10,
            "buff": -3,
            "color": C.PINK,
            "stroke_opacity": 0.75,
        }

        longest_path_prev_lines_kwargs = {
            "stroke_width": 20,
            "buff": -3,
            "color": C.TEAL_DARK,
            "stroke_opacity": 0.75,
        }

        line_0_5 = m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_5_6 = m.Line(start=t5_circle, end=t6_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_6_7 = m.Line(start=t6_circle, end=t7_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_7_8 = m.Line(start=t7_circle, end=t8_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)
        line_8_9 = m.Line(start=t8_circle, end=t9_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs)

        line_0_5_prev = m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1,
                               **longest_path_prev_lines_kwargs)
        line_5_6_prev = m.Line(start=t5_circle, end=t6_circle, z_index=t1_circle.z_index - 1,
                               **longest_path_prev_lines_kwargs)
        line_6_7_prev = m.Line(start=t6_circle, end=t7_circle, z_index=t1_circle.z_index - 1,
                               **longest_path_prev_lines_kwargs)
        line_7_8_prev = m.Line(start=t7_circle, end=t8_circle, z_index=t1_circle.z_index - 1,
                               **longest_path_prev_lines_kwargs)
        line_8_9_prev = m.Line(start=t8_circle, end=t9_circle, z_index=t1_circle.z_index - 1,
                               **longest_path_prev_lines_kwargs)

        longest_path_prev = m.VGroup(
            line_0_5_prev,
            line_5_6_prev,
            line_6_7_prev,
            line_7_8_prev,
            line_8_9_prev
        )

        h_prev = zhang_function_tex[0]

        h_prev.generate_target()
        h_prev.target.set_color(C.TEAL)

        temp_text_copy_group = m.VGroup(
            t0_text.copy(),
            t1_text.copy(),
            t2_text.copy(),
            t3_text.copy(),
            t4_text.copy(),
            t5_text.copy(),
            t6_text.copy(),
            t7_text.copy(),
            t8_text.copy(),
            t9_text.copy(),
        )

        temp_text_copy_group.z_index = 600
        self.add(temp_text_copy_group)

        self.play(
            m.Write(longest_path_prev),
            m.MoveToTarget(h_prev),
        )

        h_now = zhang_function_tex[2]
        h_now.generate_target()
        h_now.target.set_color(C.PINK)

        longest_path = m.VGroup(
            line_0_5,
            line_5_6,
            line_6_7,
            line_7_8,
            line_8_9,
        )

        t5_circle.generate_target()
        t5_circle.target.set_fill(C.GREEN_LIGHT)

        self.play(
            m.Write(longest_path),
            m.MoveToTarget(h_now),
            m.MoveToTarget(t5_circle)
        )

        rewards_tex = m.MathTex(r"0", r"\:,", r"-2", r"\:,", r"0", r"\:,", r"0", r"\:,", r"-2", r"\:,", r"0",
                                r"\:,", r"0", r"\:,", r"-4",
                                color=C.DEFAULT_FONT).scale(0.625).next_to(reward_text, m.RIGHT, buff=0.0)
        rewards_tex = m.Group(
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.625),
            styled_text("-2", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("-2", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("0", color=C.DEFAULT_FONT).scale(0.5), styled_text(",", color=C.DEFAULT_FONT).scale(0.5),
            styled_text("-4", color=C.DEFAULT_FONT).scale(0.5),
        ).arrange(m.RIGHT, buff=0.125)
        rewards_tex.next_to(reward_text.get_right(), m.RIGHT, buff=0.25)
        for i in range(1, len(rewards_tex), 2):
            rewards_tex[i].shift(comma_shift * m.DOWN)

        longest_path_prev_copy = longest_path_prev.copy()
        longest_path_copy = longest_path.copy()
        self.play(
            m.Transform(longest_path_prev_copy, h_prev),
            m.Transform(longest_path_copy, h_now),
            m.Transform(longest_path, longest_path_prev, replace_mobject_with_target_in_scene=True)
        )
        self.remove(longest_path_prev_copy, longest_path_copy)
        self.play_without_section(
            m.TransformFromCopy(zhang_function_tex, rewards_tex[0]),
        )

        # step 2

        machine_arrow_kwargs = {
            "tip_shape": m.ArrowTriangleFilledTip,
            "tip_length": 0.175,
            "stroke_width": 3,
            "buff": 0,
        }

        t1_circle.generate_target()
        t1_circle.target.set_fill(C.GREEN_LIGHT)

        machine_edge_5_1 = m.Arrow(start=t5_circle, end=t1_circle, color=C.BLUE, **machine_arrow_kwargs)
        machine_edge_5_1_label = styled_text("5", color=C.BLUE).scale(0.425).move_to(
            machine_edge_5_1.get_center() + m.RIGHT * 0.25)

        longest_path = m.VGroup(
            m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t5_circle, end=t1_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t1_circle, end=t2_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t2_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t3_circle, end=t4_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t4_circle, end=t9_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
        )

        longest_path_prev_copy = longest_path_prev.copy()
        longest_path_copy = longest_path.copy()
        self.play(
            m.MoveToTarget(t1_circle),
            m.Write(machine_edge_5_1),
            m.FadeIn(machine_edge_5_1_label),
            m.Write(longest_path),
        )
        self.play(
            m.Transform(longest_path_prev_copy, h_prev),
            m.Transform(longest_path_copy, h_now),
        )
        longest_path_prev_target = m.VGroup(
            m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t5_circle, end=t1_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t1_circle, end=t2_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t2_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t3_circle, end=t4_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t4_circle, end=t9_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
        )
        self.remove(longest_path_prev_copy, longest_path_copy)
        self.play_without_section(
            m.FadeOut(longest_path_prev),
            m.Transform(longest_path, longest_path_prev_target),
            m.FadeIn(rewards_tex[1]),
            m.TransformFromCopy(zhang_function_tex, rewards_tex[2]),
        )
        self.remove(longest_path_prev_target)
        longest_path_prev = longest_path

        # step 3
        t2_circle.generate_target()
        t2_circle.target.set_fill(C.GREEN_LIGHT)

        longest_path = m.VGroup(
            m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t5_circle, end=t1_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t1_circle, end=t2_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t2_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t3_circle, end=t4_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t4_circle, end=t9_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
        )

        longest_path_prev_copy = longest_path_prev.copy()
        longest_path_copy = longest_path.copy()
        self.play(
            m.MoveToTarget(t2_circle),
            m.Write(longest_path),

        )
        self.play_without_section(
            m.Transform(longest_path_prev_copy, h_prev),
            m.Transform(longest_path_copy, h_now),

        )
        longest_path_prev_target = m.VGroup(
            m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t5_circle, end=t1_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t1_circle, end=t2_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t2_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t3_circle, end=t4_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t4_circle, end=t9_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
        )
        self.remove(longest_path_prev_copy, longest_path_copy)
        self.play_without_section(
            m.FadeOut(longest_path_prev),
            m.Transform(longest_path, longest_path_prev_target),
            m.FadeIn(rewards_tex[3]),
            m.TransformFromCopy(zhang_function_tex, rewards_tex[4]),

        )
        self.remove(longest_path_prev_target)
        longest_path_prev = longest_path

        # step 4
        t6_circle.generate_target()
        t6_circle.target.set_fill(C.GREEN_LIGHT)

        longest_path = m.VGroup(
            m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t5_circle, end=t1_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t1_circle, end=t2_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t2_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t3_circle, end=t4_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t4_circle, end=t9_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
        )

        longest_path_prev_copy = longest_path_prev.copy()
        longest_path_copy = longest_path.copy()
        self.play_without_section(
            m.MoveToTarget(t6_circle),
            m.Write(longest_path),

        )
        self.play_without_section(
            m.Transform(longest_path_prev_copy, h_prev),
            m.Transform(longest_path_copy, h_now),

        )
        longest_path_prev_target = m.VGroup(
            m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t5_circle, end=t1_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t1_circle, end=t2_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t2_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t3_circle, end=t4_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t4_circle, end=t9_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
        )
        self.remove(longest_path_prev_copy, longest_path_copy)
        self.play_without_section(
            m.FadeOut(longest_path_prev),
            m.Transform(longest_path, longest_path_prev_target),
            m.FadeIn(rewards_tex[5]),
            m.TransformFromCopy(zhang_function_tex, rewards_tex[6]),

        )
        self.remove(longest_path_prev_target)
        longest_path_prev = longest_path

        # step 5
        t3_circle.generate_target()
        t3_circle.target.set_fill(C.GREEN_LIGHT)

        machine_edge_6_3 = m.Arrow(start=t6_circle, end=t3_circle, color=C.GREEN, **machine_arrow_kwargs)
        machine_edge_6_3_label = styled_text("16", color=C.GREEN).scale(0.425).move_to(
            machine_edge_6_3.get_center() + np.array([-0.25, -0.6, 0]))

        longest_path = m.VGroup(
            m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t5_circle, end=t6_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t6_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t3_circle, end=t4_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t4_circle, end=t9_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
        )

        longest_path_prev_copy = longest_path_prev.copy()
        longest_path_copy = longest_path.copy()
        self.play(
            m.Write(machine_edge_6_3),
            m.FadeIn(machine_edge_6_3_label),
            m.MoveToTarget(t3_circle),
            m.Write(longest_path),

        )
        self.play_without_section(
            m.Transform(longest_path_prev_copy, h_prev),
            m.Transform(longest_path_copy, h_now),

        )
        longest_path_prev_target = m.VGroup(
            m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t5_circle, end=t6_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t6_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t3_circle, end=t4_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t4_circle, end=t9_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
        )
        self.remove(longest_path_prev_copy, longest_path_copy)
        self.play_without_section(
            m.FadeOut(longest_path_prev),
            m.Transform(longest_path, longest_path_prev_target),
            m.FadeIn(rewards_tex[7]),
            m.TransformFromCopy(zhang_function_tex, rewards_tex[8]),

        )
        self.remove(longest_path_prev_target)
        longest_path_prev = longest_path

        # step 6
        t7_circle.generate_target()
        t7_circle.target.set_fill(C.GREEN_LIGHT)

        machine_edge_2_7 = m.Arrow(start=t2_circle, end=t7_circle, color=C.ORANGE_DARK, **machine_arrow_kwargs)
        machine_edge_2_7_label = styled_text("3", color=C.ORANGE_DARK).scale(0.425).move_to(
            machine_edge_2_7.get_center() + np.array([-0.25, 0.6, 0]))

        longest_path = m.VGroup(
            m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t5_circle, end=t6_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t6_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t3_circle, end=t4_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t4_circle, end=t9_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
        )

        longest_path_prev_copy = longest_path_prev.copy()
        longest_path_copy = longest_path.copy()
        self.play_without_section(
            m.Write(machine_edge_2_7),
            m.FadeIn(machine_edge_2_7_label),
            m.MoveToTarget(t7_circle),
            m.Write(longest_path),

        )
        self.play(
            m.Transform(longest_path_prev_copy, h_prev),
            m.Transform(longest_path_copy, h_now),

        )
        longest_path_prev_target = m.VGroup(
            m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t5_circle, end=t6_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t6_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t3_circle, end=t4_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t4_circle, end=t9_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
        )
        self.remove(longest_path_prev_copy, longest_path_copy)
        self.play_without_section(
            m.FadeOut(longest_path_prev),
            m.Transform(longest_path, longest_path_prev_target),
            m.FadeIn(rewards_tex[9]),
            m.TransformFromCopy(zhang_function_tex, rewards_tex[10]),

        )
        self.remove(longest_path_prev_target)
        longest_path_prev = longest_path

        # step 7
        t4_circle.generate_target()
        t4_circle.target.set_fill(C.GREEN_LIGHT)

        longest_path = m.VGroup(
            m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t5_circle, end=t6_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t6_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t3_circle, end=t4_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t4_circle, end=t9_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
        )

        longest_path_prev_copy = longest_path_prev.copy()
        longest_path_copy = longest_path.copy()
        self.play_without_section(
            m.MoveToTarget(t4_circle),
            m.Write(longest_path),

        )
        self.play(
            m.Transform(longest_path_prev_copy, h_prev),
            m.Transform(longest_path_copy, h_now),

        )
        longest_path_prev_target = m.VGroup(
            m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t5_circle, end=t6_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t6_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t3_circle, end=t4_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
            m.Line(start=t4_circle, end=t9_circle, z_index=t1_circle.z_index - 1, **longest_path_prev_lines_kwargs),
        )
        self.remove(longest_path_prev_copy, longest_path_copy)
        self.play_without_section(
            m.FadeOut(longest_path_prev),
            m.Transform(longest_path, longest_path_prev_target),
            m.FadeIn(rewards_tex[11]),
            m.TransformFromCopy(zhang_function_tex, rewards_tex[12]),

        )
        self.remove(longest_path_prev_target)
        longest_path_prev = longest_path

        # step 7
        t8_circle.generate_target()
        t8_circle.target.set_fill(C.GREEN_LIGHT)

        machine_edge_4_8 = m.Arrow(start=t4_circle, end=t8_circle, color=C.TEAL, **machine_arrow_kwargs)
        machine_edge_4_8_label = styled_text("12", color=C.TEAL).scale(0.425).move_to(
            machine_edge_4_8.get_center() + m.LEFT * 0.25)

        longest_path = m.VGroup(
            m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t5_circle, end=t6_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t6_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t3_circle, end=t4_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t4_circle, end=t8_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t8_circle, end=t9_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
        )

        longest_path_prev_copy = longest_path_prev.copy()
        longest_path_copy = longest_path.copy()
        self.play(
            m.Write(machine_edge_4_8),
            m.FadeIn(machine_edge_4_8_label),
            m.MoveToTarget(t8_circle),
            m.Write(longest_path),

        )
        self.play_without_section(
            m.Transform(longest_path_prev_copy, h_prev),
            m.Transform(longest_path_copy, h_now),

        )
        longest_path_prev_target = m.VGroup(
            m.Line(start=t0_circle, end=t5_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t5_circle, end=t6_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t6_circle, end=t3_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t3_circle, end=t4_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t4_circle, end=t8_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
            m.Line(start=t8_circle, end=t9_circle, z_index=t1_circle.z_index - 1, **longest_path_lines_kwargs),
        )
        self.remove(longest_path_prev_copy, longest_path_copy)
        self.play_without_section(
            m.FadeOut(longest_path_prev),
            m.Transform(longest_path, longest_path_prev_target),
            m.FadeIn(rewards_tex[13]),
            m.TransformFromCopy(zhang_function_tex, rewards_tex[14]),

        )

        self.remove(longest_path_prev_target)
        longest_path_prev = longest_path

        self.play(
            self.overlay_scene()
        )





if __name__ == '__main__':
    EIopRlRewardFunctions.save_sections_without_cache()