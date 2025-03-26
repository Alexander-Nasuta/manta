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

class IopRlResults(RwthTheme, AxesUtils, GanttUtils, RwthSlideTemplate):

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

        buffi = 0.75
        extra_info_buff = 6.75
        extra_extra_info_buff = 7.75
        desc_scale = 0.375

        opti_gap = styled_text("Optimality Gap").scale(0.5)
        opti_f_tex = m.VGroup(
            m.MathTex(
                r" \mathtt{C} ",
                r"\over ",
                r"\mathtt{ ",
                r"C",
                r"_{opt} }").scale(0.6),
            styled_text("- 1").scale(0.5)
        ).arrange(m.RIGHT, buff=0.225)

        opti_gap.to_edge(m.LEFT, buff=buffi).shift(m.UP * 1.0)
        opti_f_tex.to_edge(m.LEFT, buff=5).shift(m.UP * 1.0)

        opti_legend_c = (m.MathTex(r" \mathtt{C} ", color=C.DARK_FONT)
                         .scale(0.6)
                         .to_edge(m.LEFT, buff=extra_info_buff)
                         )
        opti_legend_c.move_to(np.array([
            opti_legend_c.get_center()[0],
            opti_f_tex[0][0].get_center()[1],
            opti_f_tex[0][0].get_center()[2]
        ]))

        opti_legend_c_description = (styled_text("Makespan of the Solution", color=C.DARK_FONT)
                                     .scale(desc_scale)
                                     .to_edge(m.LEFT, buff=extra_extra_info_buff))
        opti_legend_c_description.move_to(np.array([
            opti_legend_c_description.get_center()[0],
            opti_f_tex[0][0].get_center()[1],
            opti_f_tex[0][0].get_center()[2]
        ]))

        opti_legend_c_opt = (m.MathTex(r" \mathtt{C_{opt}} ", color=C.DARK_FONT)
                             .scale(0.6)
                             .to_edge(m.LEFT, buff=extra_info_buff)
                             )
        opti_legend_c_opt.move_to(np.array([
            opti_legend_c_opt.get_center()[0],
            opti_f_tex[0][3].get_center()[1],
            opti_f_tex[0][3].get_center()[2]
        ]))

        opti_legend_c_opt_description = (styled_text("Optimal Makespan", color=C.DARK_FONT)
                                         .scale(desc_scale)
                                         .to_edge(m.LEFT, buff=extra_extra_info_buff))
        opti_legend_c_opt_description.move_to(np.array([
            opti_legend_c_opt_description.get_center()[0],
            opti_f_tex[0][3].get_center()[1],
            opti_f_tex[0][3].get_center()[2]
        ]))

        left_shifts = styled_text("Left Shifts").scale(0.5)
        left_shifts_f_tex = m.MathTex(
            r"\mathtt{ \# t_{LS} }",
            r" \over ",
            r"\mathtt{t}}"
        ).scale(0.6)

        left_shifts.to_edge(m.LEFT, buff=buffi).shift(m.DOWN * 0.0)

        left_shifts_f_tex.to_edge(m.LEFT, buff=5).shift(m.DOWN * 0.0)

        left_shifts_num_LS = (m.MathTex(r"\mathtt{ \# t_{LS} }", color=C.DARK_FONT)
                              .scale(0.6)
                              .to_edge(m.LEFT, buff=extra_info_buff)
                              )
        left_shifts_num_LS.move_to(np.array([
            left_shifts_num_LS.get_center()[0],
            left_shifts_f_tex[0].get_center()[1],
            left_shifts_f_tex[0].get_center()[2]
        ]))

        left_shifts_num_LS_description = (styled_text("Total Number of Left Shifts", color=C.DARK_FONT)
                                          .scale(desc_scale)
                                          .to_edge(m.LEFT, buff=extra_extra_info_buff))
        left_shifts_num_LS_description.move_to(np.array([
            left_shifts_num_LS_description.get_center()[0],
            left_shifts_f_tex[0].get_center()[1],
            left_shifts_f_tex[0].get_center()[2]
        ]))

        left_shifts_t = (m.MathTex(r"\mathtt{t}", color=C.DARK_FONT)
                         .scale(0.6)
                         .to_edge(m.LEFT, buff=extra_info_buff)
                         )
        left_shifts_t.move_to(np.array([
            left_shifts_t.get_center()[0],
            left_shifts_f_tex[2].get_center()[1],
            left_shifts_f_tex[2].get_center()[2]
        ]))

        left_shifts_t_description = (styled_text("Current Timestep", color=C.DARK_FONT)
                                     .scale(desc_scale)
                                     .to_edge(m.LEFT, buff=extra_extra_info_buff))
        left_shifts_t_description.move_to(np.array([
            left_shifts_t_description.get_center()[0],
            left_shifts_f_tex[2].get_center()[1],
            left_shifts_f_tex[2].get_center()[2]
        ]))

        reward = styled_text("Reward").scale(0.5)
        reward.to_edge(m.LEFT, buff=buffi)
        reward.shift(m.DOWN * 1.0)

        reward_tex = m.MathTex(r"\mathtt{r(s_t)}").scale(0.6)
        reward_tex.to_edge(m.LEFT, buff=5)
        reward_tex.shift(m.DOWN * 1.0)

        reward_tex_extra_info = styled_text("(smoothed)", color=C.DARK_FONT).scale(0.5)
        reward_tex_extra_info.to_edge(m.LEFT, buff=extra_info_buff)
        reward_tex_extra_info.shift(m.DOWN * 1.0)

        instance_text = styled_text("Instance").scale(0.5)
        instance_text.to_edge(m.LEFT, buff=buffi)
        instance_text.shift(m.UP * 2.0)

        instance_name = styled_text("orb04").scale(0.5)
        instance_name.to_edge(m.LEFT, buff=5.0)
        instance_name.shift(m.UP * 2.0)

        instance_name_extra_info = styled_text("(Applegate and Cook, 1991)", color=C.DARK_FONT).scale(0.5)
        instance_name_extra_info.to_edge(m.LEFT, buff=extra_info_buff)
        instance_name_extra_info.shift(m.UP * 2.0)

        self.play(

            m.FadeIn(instance_text),
            m.FadeIn(instance_name),
            m.FadeIn(instance_name_extra_info),

            m.FadeIn(opti_gap),
            m.FadeIn(opti_f_tex),
            m.FadeIn(opti_legend_c),
            m.FadeIn(opti_legend_c_opt),
            m.FadeIn(opti_legend_c_description),
            m.FadeIn(opti_legend_c_opt_description),

            m.FadeIn(left_shifts),
            m.FadeIn(left_shifts_f_tex),
            m.FadeIn(left_shifts_num_LS),
            m.FadeIn(left_shifts_t),
            m.FadeIn(left_shifts_num_LS_description),
            m.FadeIn(left_shifts_t_description),

            m.FadeIn(reward),
            m.FadeIn(reward_tex),
            m.FadeIn(reward_tex_extra_info),
        )

        class MyText(m.Text):
            def __init__(self, *tex_strings, **kwargs):
                super().__init__(*tex_strings, font="Larabiefont", **kwargs)

        opti_axes = m.Axes(
            x_range=[0.0, 2.5, 0.1],
            y_range=[0.0, 2.0, 0.5],
            x_length=11,
            y_length=2.5,
            y_axis_config={
                "tick_size": 0.0425,
                "numbers_to_include": [0.0, 0.5, 1.0, 1.5, 2.0],
                "numbers_with_elongated_ticks": [0.0, 0.5, 1.0, 1.5, 2.0],
                "font_size": 13,
                "exclude_origin_tick": False,
                "numbers_to_exclude": [],
                "label_constructor": MyText,
            },
            x_axis_config={
                "tick_size": 0.0425,
                "numbers_to_include": [0.0, 0.5, 1.0, 1.5, 2.0, 2.5],
                "numbers_with_elongated_ticks": [0.0, 0.5, 1.0, 1.5, 2.0, 2.5],
                "exclude_origin_tick": False,
                "numbers_to_exclude": [],
                "font_size": 13,
                "label_constructor": MyText,
            },
            axis_config={"include_numbers": False},
            tips=False,
        )
        opti_axes.shift(m.UP * 1.75 + m.RIGHT * 0.25)

        x_shift = 3.25
        y_shift = -1.75

        rew_axes = m.Axes(
            x_range=[0, 2.5, 0.1],
            y_range=[-2, 1, 0.2],
            x_length=4.5,
            y_length=2.0,
            y_axis_config={
                "tick_size": 0.0425,
                "numbers_to_include": [-2, -1, 0, 1],
                "numbers_with_elongated_ticks": [-2, -1, 0, 1],
                "font_size": 13,
                "exclude_origin_tick": False,
                "numbers_to_exclude": [],
                "label_constructor": MyText,
            },
            x_axis_config={
                "tick_size": 0.0425,
                "numbers_to_include": [0.0, 0.5, 1.0, 1.5, 2.0, 2.5],
                "numbers_with_elongated_ticks": [0.0, 0.5, 1.0, 1.5, 2.0, 2.5],
                "font_size": 13,
                "exclude_origin_tick": False,
                "numbers_to_exclude": [0.0],
                "label_constructor": MyText,
            },
            axis_config={"include_numbers": False},
            tips=False,
        )
        rew_axes.move_to(np.array([-x_shift, y_shift + 0.15, 0]))

        border_kwargs = {
            "color": C.DEFAULT_FONT,
            "stroke_width": 1.75,
        }

        # Create top and right borders
        rew_top_border = m.Line(rew_axes.c2p(0, 1), rew_axes.c2p(2.5, 1), **border_kwargs)
        rew_bot_border = m.Line(rew_axes.c2p(2.5, 1), rew_axes.c2p(2.5, -2), **border_kwargs)
        rew_right_border = m.Line(rew_axes.c2p(0, -2), rew_axes.c2p(2.5, -2), **border_kwargs)
        rew_borders = m.VGroup(rew_top_border, rew_bot_border, rew_right_border)

        opti_top_border = m.Line(opti_axes.c2p(0, 0.8), opti_axes.c2p(2.5, 0.8), **border_kwargs)
        opti_right_border = m.Line(opti_axes.c2p(2.5, 0.8), opti_axes.c2p(2.5, 0), **border_kwargs)

        opti_borders = m.VGroup(opti_top_border, opti_right_border)

        ls_axes = m.Axes(
            x_range=[0, 2.5, 0.1],
            y_range=[0, 40, 5],
            x_length=4.5,
            y_length=2.0,
            y_axis_config={
                "tick_size": 0.0425,
                "numbers_to_include": [0, 10, 20, 30, 40],
                "numbers_with_elongated_ticks": [0, 10, 20, 30, 40],
                "font_size": 13,
                "exclude_origin_tick": False,
                "numbers_to_exclude": [],
                "label_constructor": MyText,
            },
            x_axis_config={
                "tick_size": 0.0425,
                "numbers_to_include": [0.0, 0.5, 1.0, 1.5, 2.0, 2.5],
                "numbers_with_elongated_ticks": [0.0, 0.5, 1.0, 1.5, 2.0, 2.5],
                "font_size": 13,
                "exclude_origin_tick": False,
                "numbers_to_exclude": [],
                "label_constructor": MyText,
            },
            axis_config={"include_numbers": False},
            tips=False,
        )
        ls_axes.move_to(np.array([x_shift, y_shift, 0]))

        opti_gap.generate_target()
        opti_gap.target.rotate(90 * m.DEGREES).scale(0.625)
        opti_gap.target.move_to(opti_axes.c2p(-0.25, 1.0))

        left_shifts.generate_target()
        left_shifts.target.rotate(90 * m.DEGREES).scale(0.625)
        left_shifts.target.move_to(ls_axes.c2p(-0.5, 20))

        reward.generate_target()
        reward.target.rotate(90 * m.DEGREES).scale(0.625)
        reward.target.move_to(rew_axes.c2p(-0.5, -1.0))

        timesteps_opti_text = styled_text("Timesteps").scale(0.5).scale(0.625)
        timesteps_opti_text.move_to(opti_axes.c2p(2.5 * 0.5, -0.5))

        timesteps_opti_text_unit = m.MathTex("[\,", "10", "^{\,6}", "\,]").scale(0.625).scale(0.625)
        timesteps_opti_text_unit.next_to(timesteps_opti_text, m.RIGHT, buff=0.1)

        timestep_unit_10 = styled_text("10").scale_to_fit_height(timesteps_opti_text_unit[1].height).move_to(
            timesteps_opti_text_unit[1].get_center())
        timestep_unit_power = styled_text("6").scale_to_fit_height(timesteps_opti_text_unit[2].height).move_to(
            timesteps_opti_text_unit[2].get_center())
        timestep_unit_bracket_open = styled_text("[").scale_to_fit_height(timesteps_opti_text_unit[0].height).move_to(
            timesteps_opti_text_unit[0].get_center())
        timestep_unit_bracket_close = styled_text("]").scale_to_fit_height(timesteps_opti_text_unit[3].height).move_to(
            timesteps_opti_text_unit[3].get_center())

        timesteps_opti_text_unit = m.VGroup(timestep_unit_bracket_open, timestep_unit_10, timestep_unit_power,
                                            timestep_unit_bracket_close)

        timesteps_ls_text = styled_text("Timesteps").scale(0.5).scale(0.625)
        timesteps_ls_unit = timesteps_opti_text_unit.copy()
        timesteps_ls_text.move_to(np.array([x_shift, y_shift - 1.5, 0]))
        timesteps_ls_unit.next_to(timesteps_ls_text, m.RIGHT, buff=0.1)

        timesteps_rew_text = styled_text("Timesteps").scale(0.5).scale(0.625)
        timesteps_rew_text_unit = timesteps_opti_text_unit.copy()
        timesteps_rew_text.move_to(np.array([-x_shift, y_shift - 1.5, 0]))
        timesteps_rew_text_unit.next_to(timesteps_rew_text, m.RIGHT, buff=0.1)

        left_shifts_unit = m.MathTex("[", "\%", "]").scale(0.625).scale(0.75)
        left_shifts_unit.rotate(90 * m.DEGREES)
        left_shifts_unit.next_to(left_shifts.target, m.UP, buff=0.125)

        left_shifts_unit_1 = styled_text("%").rotate(90 * m.DEGREES).scale_to_fit_width(
            left_shifts_unit[1].width).move_to(left_shifts_unit[1].get_center())
        left_shifts_unit_bracket_open = styled_text("[").rotate(90 * m.DEGREES).scale_to_fit_width(
            left_shifts_unit[0].width).move_to(left_shifts_unit[0].get_center())
        left_shifts_unit_bracket_close = styled_text("]").rotate(90 * m.DEGREES).scale_to_fit_width(
            left_shifts_unit[2].width).move_to(left_shifts_unit[2].get_center())

        left_shifts_unit = m.VGroup(left_shifts_unit_bracket_open, left_shifts_unit_1, left_shifts_unit_bracket_close)

        opti_gap_unit = m.MathTex("[", "1", "\,]").scale(0.625).scale(0.75)
        opti_gap_unit.rotate(90 * m.DEGREES)
        opti_gap_unit.next_to(opti_gap.target, m.UP, buff=0.125)

        opti_gap_unit_1 = styled_text("1").rotate(90 * m.DEGREES).scale_to_fit_width(opti_gap_unit[1].width).move_to(
            opti_gap_unit[1].get_center())
        opti_gap_unit_bracket_open = styled_text("[").rotate(90 * m.DEGREES).scale_to_fit_width(
            opti_gap_unit[0].width).move_to(opti_gap_unit[0].get_center())
        opti_gap_unit_bracket_close = styled_text("]").rotate(90 * m.DEGREES).scale_to_fit_width(
            opti_gap_unit[2].width).move_to(opti_gap_unit[2].get_center())

        opti_gap_unit = m.VGroup(opti_gap_unit_bracket_open, opti_gap_unit_1, opti_gap_unit_bracket_close)

        reward_unit = m.MathTex("[", "1", "\,]").scale(0.625).scale(0.75)
        reward_unit.rotate(90 * m.DEGREES)
        reward_unit.next_to(reward.target, m.UP, buff=0.125)

        reward_unit_1 = styled_text("1", color=C.DEFAULT_FONT).rotate(90 * m.DEGREES).scale_to_fit_width(
            reward_unit[1].width).move_to(reward_unit[1].get_center())
        reward_unit_bracket_open = styled_text("[").rotate(90 * m.DEGREES).scale_to_fit_width(
            reward_unit[0].width).move_to(reward_unit[0].get_center())
        reward_unit_bracket_close = styled_text("]").rotate(90 * m.DEGREES).scale_to_fit_width(
            reward_unit[2].width).move_to(reward_unit[2].get_center())

        reward_unit = m.VGroup(reward_unit_bracket_open, reward_unit_1, reward_unit_bracket_close)

        self.play(
            m.FadeIn(opti_axes),
            m.FadeIn(rew_axes),
            m.FadeIn(ls_axes),
            m.FadeOut(opti_f_tex),
            m.FadeOut(left_shifts_f_tex),
            # m.FadeOut(opti_eq_tex),
            # m.FadeOut(left_shits_eq_tex),
            m.MoveToTarget(opti_gap),
            m.MoveToTarget(left_shifts),
            m.MoveToTarget(reward),
            m.FadeIn(timesteps_opti_text),
            m.FadeIn(timesteps_opti_text_unit),
            m.FadeIn(timesteps_ls_text),
            m.FadeIn(timesteps_rew_text),
            m.FadeIn(timesteps_ls_unit),
            m.FadeIn(timesteps_rew_text_unit),
            m.FadeIn(opti_gap_unit),
            m.FadeIn(left_shifts_unit),
            m.FadeIn(reward_unit),
            # m.FadeIn(rew_borders),
            # m.FadeIn(opti_borders)
            *[m.FadeOut(obj) for obj in [
                instance_name,
                instance_text,
                opti_legend_c,
                opti_legend_c_opt,
                opti_legend_c_description,
                opti_legend_c_opt_description,
                left_shifts_num_LS,
                left_shifts_t,
                left_shifts_num_LS_description,
                left_shifts_t_description,
                reward_tex,
                reward_tex_extra_info,
                instance_name_extra_info,
                timesteps_opti_text,
                timesteps_opti_text_unit,
                timesteps_ls_text,
                timesteps_rew_text,
                timesteps_ls_unit,
                timesteps_rew_text_unit,
            ]]
        )

        import pandas as pd

        tassel_ls = pd.read_csv('orb04_graph-tassel_ls.csv')
        nasuta_ls = pd.read_csv('orb04_nasuta_ls.csv')
        zhang_ls = pd.read_csv('orb04_zhang_ls.csv')
        samsonov_ls = pd.read_csv('orb04_samsonov_ls.csv')

        reward_unit_samsonov = m.MathTex("[", "10", "^{-3}", "\,]", color=C.BLUE).scale(0.625).scale(0.75)
        reward_unit_samsonov.rotate(90 * m.DEGREES)
        reward_unit_samsonov.next_to(reward_unit, m.UP, buff=0.125)

        reward_unit_samsonov_10 = styled_text("10", color=C.BLUE).rotate(90 * m.DEGREES).scale_to_fit_width(
            reward_unit_samsonov[1].width).move_to(reward_unit_samsonov[1].get_center())
        reward_unit_samsonov_power = styled_text("-3", color=C.BLUE).rotate(90 * m.DEGREES).scale_to_fit_width(
            reward_unit_samsonov[2].width).move_to(reward_unit_samsonov[2].get_center())

        reward_unit_samsonov_bracket_open = (styled_text("[").rotate(90 * m.DEGREES)
        .scale_to_fit_width(reward_unit_samsonov[0].width)
        .move_to(np.array([
            reward_unit[0].get_center()[0],
            reward_unit_samsonov[0].get_center()[1],
            reward_unit_samsonov[0].get_center()[2],
        ])))

        reward_unit_samsonov_bracket_close = (styled_text("]").rotate(90 * m.DEGREES)
        .scale_to_fit_width(reward_unit_samsonov[3].width)
        .move_to(np.array([
            reward_unit[0].get_center()[0],
            reward_unit_samsonov[3].get_center()[1],
            reward_unit_samsonov[3].get_center()[2],
        ])))

        reward_unit_samsonov = m.VGroup(reward_unit_samsonov_bracket_open, reward_unit_samsonov_10,
                                        reward_unit_samsonov_power, reward_unit_samsonov_bracket_close)

        plots = m.VGroup()
        for rew, color in zip(
                [tassel_ls, nasuta_ls, zhang_ls, samsonov_ls],
                [C.ORANGE_DARK, RwthTheme.rwth_lila_75, C.GREEN, C.BLUE]):
            opti_plot = opti_axes.plot_line_graph(
                rew["num_timesteps"].to_numpy(),
                rew["optimality_gap"].to_numpy(),
                add_vertex_dots=False,
                line_color=color,
                stroke_width=1,
            )
            plots.add(opti_plot)

            rew_plot = rew_axes.plot_line_graph(
                rew["num_timesteps"].to_numpy(),
                rew["reward_mean"].to_numpy(),
                add_vertex_dots=False,
                line_color=color,
                stroke_width=2,
            )
            plots.add(rew_plot)

            ls_plot = ls_axes.plot_line_graph(
                rew["num_timesteps"].to_numpy(),
                rew["left_shift_pct"].to_numpy(),
                add_vertex_dots=False,
                line_color=color,
                stroke_width=1,
            )
            plots.add(ls_plot)

        tassel_no_ls = pd.read_csv('orb04_graph-tassel_no-ls.csv')
        nasuta_no_ls = pd.read_csv('orb04_nasuta_no-ls.csv')
        zhang_no_ls = pd.read_csv('orb04_zhang_no-ls.csv')
        samsonov_no_ls = pd.read_csv('orb04_samsonov_no-ls.csv')

        for rew, color in zip(
                [tassel_no_ls, nasuta_no_ls, zhang_no_ls, samsonov_no_ls],
                [C.YELLOW, RwthTheme.rwth_lila_50, C.GREEN_LIGHT, C.BLUE_LIGHT]):
            opti_plot = opti_axes.plot_line_graph(
                rew["num_timesteps"].to_numpy(),
                rew["optimality_gap"].to_numpy(),
                add_vertex_dots=False,
                line_color=color,
                stroke_width=1,
            )
            plots.add(opti_plot)

            rew_plot = rew_axes.plot_line_graph(
                rew["num_timesteps"].to_numpy(),
                rew["reward_mean"].to_numpy(),
                add_vertex_dots=False,
                line_color=color,
                stroke_width=2,
            )
            plots.add(rew_plot)

        y1 = 2.5
        y2 = 2.25
        legend = m.VGroup()

        tassel_ls_rect = m.Rectangle(
            width=0.325,
            height=0.125 * 0.25,
            color=C.ORANGE_DARK,
            fill_opacity=1,
        )
        tassel_ls_rect_text = styled_text("Machine Utilization LS", color=C.DEFAULT_FONT).scale(0.25)
        tassel_ls_rect.move_to(opti_axes.c2p(0.0375, y1))
        tassel_ls_rect_text.next_to(tassel_ls_rect, m.RIGHT, buff=0.1)
        legend.add(tassel_ls_rect)
        legend.add(tassel_ls_rect_text)

        tassel_no_ls_rect = m.Rectangle(
            width=0.325,
            height=0.125 * 0.25,
            color=C.YELLOW,
            fill_opacity=1,
        )
        tassel_no_ls_rect_text = styled_text("Machine Utilization", color=C.DEFAULT_FONT).scale(0.25)
        tassel_no_ls_rect.move_to(opti_axes.c2p(0.0375, y2))
        tassel_no_ls_rect_text.next_to(tassel_no_ls_rect, m.RIGHT, buff=0.1)
        legend.add(tassel_no_ls_rect)
        legend.add(tassel_no_ls_rect_text)

        nasuta_ls_rect = m.Rectangle(
            width=0.325,
            height=0.125 * 0.25,
            color=RwthTheme.rwth_lila_75,
            fill_opacity=1,
        )
        nasuta_ls_rect_text = styled_text("Trivial LS", color=C.DEFAULT_FONT).scale(0.25)
        nasuta_ls_rect.move_to(opti_axes.c2p(0.0375 + 0.65, y1))
        nasuta_ls_rect_text.next_to(nasuta_ls_rect, m.RIGHT, buff=0.1)
        legend.add(nasuta_ls_rect)
        legend.add(nasuta_ls_rect_text)

        nasuta_no_ls_rect = m.Rectangle(
            width=0.325,
            height=0.125 * 0.25,
            color=RwthTheme.rwth_lila_50,
            fill_opacity=1,
        )
        nasuta_no_ls_rect_text = styled_text("Trivial", color=C.DEFAULT_FONT).scale(0.25)
        nasuta_no_ls_rect.move_to(opti_axes.c2p(0.0375 + 0.65, y2))
        nasuta_no_ls_rect_text.next_to(nasuta_no_ls_rect, m.RIGHT, buff=0.1)
        legend.add(nasuta_no_ls_rect)
        legend.add(nasuta_no_ls_rect_text)

        zhang_ls_rect = m.Rectangle(
            width=0.325,
            height=0.125 * 0.25,
            color=C.GREEN,
            fill_opacity=1,
        )
        zhang_ls_rect_text = styled_text("Zhang LS", color=C.DEFAULT_FONT).scale(0.25)
        zhang_ls_rect.move_to(opti_axes.c2p(0.0375 + 1.03125, y1))
        zhang_ls_rect_text.next_to(zhang_ls_rect, m.RIGHT, buff=0.1)
        legend.add(zhang_ls_rect)
        legend.add(zhang_ls_rect_text)

        zhang_no_ls_rect = m.Rectangle(
            width=0.325,
            height=0.125 * 0.25,
            color=C.GREEN_LIGHT,
            fill_opacity=1,
        )
        zhang_no_ls_rect_text = styled_text("Zhang", color=C.DEFAULT_FONT).scale(0.25)
        zhang_no_ls_rect.move_to(opti_axes.c2p(0.0375 + 1.03125, y2))
        zhang_no_ls_rect_text.next_to(zhang_no_ls_rect, m.RIGHT, buff=0.1)
        legend.add(zhang_no_ls_rect)
        legend.add(zhang_no_ls_rect_text)

        samsonov_ls_rect = m.Rectangle(
            width=0.325,
            height=0.125 * 0.25,
            color=C.BLUE,
            fill_opacity=1,
        )
        samsonov_ls_rect_text = styled_text("Samsonov LS", color=C.DEFAULT_FONT).scale(0.25)
        samsonov_ls_rect.move_to(opti_axes.c2p(0.0375 + 1.365, y1))
        samsonov_ls_rect_text.next_to(samsonov_ls_rect, m.RIGHT, buff=0.1)
        legend.add(samsonov_ls_rect)
        legend.add(samsonov_ls_rect_text)

        samsonov_no_ls_rect = m.Rectangle(
            width=0.325,
            height=0.125 * 0.25,
            color=C.BLUE_LIGHT,
            fill_opacity=1,
        )
        samsonov_no_ls_rect_text = styled_text("Samsonov", color=C.DEFAULT_FONT).scale(0.25)
        samsonov_no_ls_rect.move_to(opti_axes.c2p(0.0375 + 1.365, y2))
        samsonov_no_ls_rect_text.next_to(samsonov_no_ls_rect, m.RIGHT, buff=0.1)
        legend.add(samsonov_no_ls_rect)
        legend.add(samsonov_no_ls_rect_text)

        self.play(
            m.FadeIn(plots),
            m.FadeIn(legend),
            m.FadeIn(reward_unit_samsonov),
        )

        tassel_plots = m.VGroup()
        for rew, color in zip(
                [tassel_ls],
                [C.ORANGE_DARK]):
            opti_plot = opti_axes.plot_line_graph(
                rew["num_timesteps"].to_numpy(),
                rew["optimality_gap"].to_numpy(),
                add_vertex_dots=False,
                line_color=color,
                stroke_width=1,
            )
            tassel_plots.add(opti_plot)

            rew_plot = rew_axes.plot_line_graph(
                rew["num_timesteps"].to_numpy(),
                rew["reward_mean"].to_numpy(),
                add_vertex_dots=False,
                line_color=color,
                stroke_width=2,
            )
            tassel_plots.add(rew_plot)

            ls_plot = ls_axes.plot_line_graph(
                rew["num_timesteps"].to_numpy(),
                rew["left_shift_pct"].to_numpy(),
                add_vertex_dots=False,
                line_color=color,
                stroke_width=1,
            )
            tassel_plots.add(ls_plot)
        self.add(tassel_plots)

        self.play(
            m.FadeOut(plots),
            m.FadeOut(legend[2:]),
            m.FadeOut(reward_unit_samsonov),
        )



if __name__ == '__main__':
    IopRlResults.render_video_low()