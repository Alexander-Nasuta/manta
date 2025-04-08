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

class EIopRlLoop(RwthTheme, AxesUtils, GanttUtils, RwthSlideTemplate):

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
    index_prefix = "D "

    def construct(self):
        self.play(
            self.set_title_row(
                title="Job Shop Scheduling",
                seperator=": ",
                subtitle="Reinforcement Learning Approach"
            ),
            self.add_logos(),
            self.add_seperator_line_top(),
            self.add_seperator_line_bottom()
        )

        a_rect = m.RoundedRectangle(
            corner_radius=0.125,
            width=3,
            height=1,
            fill_color=self.background_color,
            fill_opacity=1.0,
            stroke_color=C.GREY_OUTLINE,
            stroke_width=1.0
        )
        a_text = styled_text("Agent", color=C.DEFAULT_FONT).scale(0.75)
        a_group = m.VGroup(a_rect, a_text)

        a_group.move_to([0, 2, 0])
        a_group.scale(0.75)


        self.play(
            m.DrawBorderThenFill(a_rect),
            m.Write(a_text)
        )

        axes = m.Axes(
            x_range=[0, 41, 1],
            y_range=[0, 4, 1],
            x_length=11,
            y_length=4,
            y_axis_config={"tick_size": 0},
            x_axis_config={"tick_size": 0},
            axis_config={"include_numbers": False, "tip_width": 0.125, "tip_height": 0.25}
        )

        axes.scale(0.35)
        axes.set_color(C.DEFAULT_FONT)

        axes.move_to([0, -2, 0])

        j1_t1 = m.Polygon(*[
            axes.c2p(5 + 11, 3),
            axes.c2p(5, 3),
            axes.c2p(5, 2),
            axes.c2p(16, 2),
        ], color=C.BLUE, fill_opacity=1, stroke_width=1)

        j1_t2 = m.Polygon(*[
            axes.c2p(16 + 3, 3),
            axes.c2p(16, 3),
            axes.c2p(16, 2),
            axes.c2p(19, 2),
        ], color=C.ORANGE_DARK, fill_opacity=1, stroke_width=1)

        j1_t3 = m.Polygon(*[
            axes.c2p(24, 3),
            axes.c2p(21, 3),
            axes.c2p(21, 2),
            axes.c2p(24, 2),
        ], color=C.GREEN, fill_opacity=1, stroke_width=1)

        j1_t4 = m.Polygon(*[
            axes.c2p(36, 3),
            axes.c2p(24, 3),
            axes.c2p(24, 2),
            axes.c2p(36, 2),
        ], color=C.TEAL, fill_opacity=1, stroke_width=1)

        j2_t1 = m.Polygon(*[
            axes.c2p(5, 2),
            axes.c2p(0, 2),
            axes.c2p(0, 1),
            axes.c2p(5, 1),
        ], color=C.BLUE, fill_opacity=1, stroke_width=1)

        j2_t2 = m.Polygon(*[
            axes.c2p(21, 2),
            axes.c2p(5, 2),
            axes.c2p(5, 1),
            axes.c2p(21, 1),
        ], color=C.GREEN, fill_opacity=1, stroke_width=1)

        j2_t3 = m.Polygon(*[
            axes.c2p(24, 2),
            axes.c2p(21, 2),
            axes.c2p(21, 1),
            axes.c2p(24, 1),
        ], color=C.ORANGE_DARK, fill_opacity=1, stroke_width=1)

        j2_t4 = m.Polygon(*[
            axes.c2p(40, 2),
            axes.c2p(36, 2),
            axes.c2p(36, 1),
            axes.c2p(40, 1),
        ], color=C.TEAL, fill_opacity=1, stroke_width=1)

        chart_rects = [
            j1_t1,
            j1_t2,
            j1_t3,
            j1_t4,

            j2_t1,
            j2_t2,
            j2_t3,
            j2_t4,
        ]
        gant_chart_full = m.VGroup(*chart_rects, axes)

        self.play(
            m.DrawBorderThenFill(gant_chart_full),
        )

        env_big_rect = m.RoundedRectangle(
            corner_radius=0.125,
            width=6,
            height=4.0,
            fill_color=self.background_color,
            fill_opacity=1.0,
            stroke_color=C.GREY_OUTLINE,
            stroke_width=1.0
        )
        a_big_rect = m.RoundedRectangle(
            corner_radius=0.125,
            width=3,
            height=1.5,
            fill_color=self.background_color,
            fill_opacity=1.0,
            stroke_color=C.GREY_OUTLINE,
            stroke_width=1.0
        )
        a_big_rect.set_opacity(0.0)
        env_big_rect.set_opacity(0.0)

        self.add(env_big_rect,a_big_rect)

        env_rect = m.RoundedRectangle(
            corner_radius=0.125,
            width=4,
            height=1,
            fill_color=self.background_color,
            fill_opacity=1.0,
            stroke_color=C.GREY_OUTLINE,
            stroke_width=1.0
        )
        env_text = styled_text("Environment", color=C.DEFAULT_FONT).scale(0.75)
        env_group = m.VGroup(env_rect, env_text)
        # env_group.z_index += 100

        env_group.move_to([0, -1.75, 0])


        #env_big_rect.z_index = env_group.z_index - 1
        env_big_rect.move_to([0, -1.75, 0])

        env_big_rect_title = styled_text("Environment", color=C.DEFAULT_FONT).scale(0.5)
        env_big_rect_title.move_to(env_big_rect.get_top())

        env_big_rect_title_rectangle = m.RoundedRectangle(
            corner_radius=0.125,
            height=3.0,
            width=11,
            fill_color=self.background_color,
            fill_opacity=1.0,
            stroke_color=C.GREY_OUTLINE,
            stroke_width=1.0
        ).scale_to_fit_height(env_big_rect_title.height + 0.5).move_to(env_big_rect_title.get_center())

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
        )

        small_axes = m.Axes(
            x_range=[0, 41, 1],
            y_range=[0, 4, 1],
            x_length=4.5,
            y_length=1.25,
            y_axis_config={"tick_size": 0},
            x_axis_config={"tick_size": 0},
            axis_config={"include_numbers": False, "tip_width": 0.0675, "tip_height": 0.125}
        )
        small_axes.set_color(C.DEFAULT_FONT)
        small_axes.move_to([0, -2.75, 0])

        temp_env_group = m.VGroup(
            env_group,
            env_big_rect,
            env_big_rect_title_rectangle,
            env_big_rect_title,
            graph,
            small_axes,
        ).scale(0.75)

        temp_env_group.shift(m.UP*0.25)


        self.play(
            m.Transform(gant_chart_full, env_group, replace_mobject_with_target_in_scene=True),
        )

        env_big_rect.generate_target()
        env_big_rect.target.set_opacity(1.0)
        self.play(
            m.MoveToTarget(env_big_rect),
            m.Transform(env_rect, env_big_rect_title_rectangle, replace_mobject_with_target_in_scene=True),
            m.Transform(env_text, env_big_rect_title, replace_mobject_with_target_in_scene=True),
            m.FadeIn(graph),
            m.FadeIn(small_axes),
        )


        a_big_rect.move_to([0, 2, 0])

        a_big_rect_title = styled_text("Agent", color=C.DEFAULT_FONT).scale(0.5)
        a_size_fitter = styled_text("Aeent", color=C.DEFAULT_FONT).scale(0.5)  # g shifts the text up a bit
        a_big_rect_title.move_to(a_big_rect.get_top())
        a_size_fitter.move_to(a_big_rect.get_top())

        a_big_rect_title_rectangle = m.RoundedRectangle(
            corner_radius=0.125,
            height=3.0,
            width=6,
            fill_color=self.background_color,
            fill_opacity=1.0,
            stroke_color=C.GREY_OUTLINE,
            stroke_width=1.0
        ).scale_to_fit_height(a_size_fitter.height + 0.5).move_to(a_size_fitter.get_center())

        neuron_circle_kwargs = {
            "radius": 0.1,
            "stroke_width": 2,
            "fill_color": C.GREY_DARK,
            "fill_opacity": 0.0
        }

        y_spacing = 0.325

        x_input_layer = -1
        x_hidden_layer = 0
        x_output_layer = 1

        neuron00 = m.Circle(stroke_color=C.DARK_FONT, **neuron_circle_kwargs)
        neuron00.move_to([x_input_layer, 1 * y_spacing, 0])

        neuron01 = m.Circle(stroke_color=C.DARK_FONT, **neuron_circle_kwargs)
        neuron01.move_to([x_input_layer, 0 * y_spacing, 0])

        neuron02 = m.Circle(stroke_color=C.DARK_FONT, **neuron_circle_kwargs)
        neuron02.move_to([x_input_layer, -1 * y_spacing, 0])

        # hidden layer
        neuron10 = m.Circle(stroke_color=C.DARK_FONT, **neuron_circle_kwargs)
        neuron10.move_to([x_hidden_layer, 0.5 * y_spacing, 0])

        neuron11 = m.Circle(stroke_color=C.DARK_FONT, **neuron_circle_kwargs)
        neuron11.move_to([x_hidden_layer, -0.5 * y_spacing, 0])

        # output layer
        neuron20 = m.Circle(stroke_color=C.DARK_FONT, **neuron_circle_kwargs)
        neuron20.move_to([x_output_layer, 0.5 * y_spacing, 0])

        neuron21 = m.Circle(stroke_color=C.DARK_FONT, **neuron_circle_kwargs)
        neuron21.move_to([x_output_layer, -0.5 * y_spacing, 0])

        # connections
        connection_kwargs = {
            "stroke_width": 3 * 0.5,
            "buff": neuron_circle_kwargs["radius"],
            "color": C.DARK_FONT
        }

        connection00_10 = m.Line(neuron00.get_center(), neuron10.get_center(), **connection_kwargs)
        connection01_10 = m.Line(neuron01.get_center(), neuron10.get_center(), **connection_kwargs)
        connection02_10 = m.Line(neuron02.get_center(), neuron10.get_center(), **connection_kwargs)

        connection00_11 = m.Line(neuron00.get_center(), neuron11.get_center(), **connection_kwargs)
        connection01_11 = m.Line(neuron01.get_center(), neuron11.get_center(), **connection_kwargs)
        connection02_11 = m.Line(neuron02.get_center(), neuron11.get_center(), **connection_kwargs)

        connection10_20 = m.Line(neuron10.get_center(), neuron20.get_center(), **connection_kwargs)
        connection11_20 = m.Line(neuron11.get_center(), neuron20.get_center(), **connection_kwargs)

        connection10_21 = m.Line(neuron10.get_center(), neuron21.get_center(), **connection_kwargs)
        connection11_21 = m.Line(neuron11.get_center(), neuron21.get_center(), **connection_kwargs)

        input_layer_group = m.VGroup(
            neuron00,
            neuron01,
            neuron02,
        )

        hidden_layer_group = m.VGroup(
            neuron10,
            neuron11,
        )

        output_layer_group = m.VGroup(
            neuron20,
            neuron21,
        )

        connection_input_hidden_group = m.VGroup(
            connection00_10,
            connection01_10,
            connection02_10,
            connection00_11,
            connection01_11,
            connection02_11,
        )

        connection_hidden_output_group = m.VGroup(
            connection10_20,
            connection11_20,
            connection10_21,
            connection11_21,
        )

        neural_network = m.VGroup(
            input_layer_group,
            hidden_layer_group,
            output_layer_group,
            connection_input_hidden_group,
            connection_hidden_output_group,
        )

        neural_network.move_to(a_big_rect.get_center())
        neural_network.shift(np.array([0, -0.125, 0]))

        temp_a_group = m.VGroup(
            a_big_rect,
            a_big_rect_title_rectangle,
            a_big_rect_title,
            neural_network
        ).scale(0.75)
        temp_a_group.add(a_group)

        a_big_rect.generate_target()
        a_big_rect.target.set_opacity(1.0)

        self.play(
            m.MoveToTarget(a_big_rect),
            m.Transform(a_rect, a_big_rect_title_rectangle, replace_mobject_with_target_in_scene=True),
            m.Transform(a_text, a_big_rect_title, replace_mobject_with_target_in_scene=True),
            m.FadeIn(neural_network),
        )

        signal_shift = 0.25

        signal_line_args = {
            "stroke_width": 3,
        }

        signal_arrow_args = {
            "tip_shape": m.ArrowTriangleFilledTip,
            "tip_length": 0.175 * 0.5,
            "stroke_width": 3,
            "buff": 0.0,
        }

        state_line0 = m.Line(
            env_big_rect.get_left() + m.DOWN * signal_shift,
            env_big_rect.get_left() + m.DOWN * signal_shift + m.LEFT * 2.5,
            color=C.DEFAULT_FONT,
            **signal_line_args
        )
        state_line1 = m.Line(
            state_line0.get_left(),
            np.array([state_line0.get_left()[0], (a_big_rect.get_left() + m.UP * signal_shift)[1], 0]),
            color=C.DEFAULT_FONT,
            **signal_line_args
        )
        state_line2 = m.Arrow(
            state_line1.get_top(),
            a_big_rect.get_left() + m.UP * signal_shift,
            color=C.DEFAULT_FONT,
            **signal_arrow_args
        )

        state_label = m.Tex(r"$\mathsf{s}$", color=C.DEFAULT_FONT).scale(0.75)
        state_label.next_to(state_line1, m.LEFT, buff=0.75)

        state_signal = m.VGroup(state_line0, state_line1, state_line2)

        self.play(
            m.FadeIn(state_signal),
            m.FadeIn(state_label)
        )

        s0_tex = styled_text("[1,0,...,1]").scale(0.3125)
        s0_tex.next_to(state_label, m.DOWN, buff=0.25)

        self.play(
            m.Transform(graph.copy(), s0_tex, replace_mobject_with_target_in_scene=True)
        )

        action_line0 = m.Line(
            a_big_rect.get_right(),
            a_big_rect.get_right() + m.RIGHT * 4.0,
            color=C.DEFAULT_FONT,
            **signal_line_args
        )

        action_line1 = m.Line(
            action_line0.get_right(),
            np.array([action_line0.get_right()[0], env_big_rect.get_right()[1], 0]),
            color=C.DEFAULT_FONT,
            **signal_line_args
        )

        action_line2 = m.Arrow(
            action_line1.get_bottom(),
            env_big_rect.get_right(),
            color=C.DEFAULT_FONT,
            **signal_arrow_args
        )

        action_label = m.Tex(r"$\mathsf{a}$", color=C.DEFAULT_FONT).scale(0.75)
        action_label.next_to(action_line1, m.RIGHT, buff=0.75)

        action_signal = m.VGroup(action_line0, action_line1, action_line2)

        self.play(
            m.FadeIn(action_signal),
            m.FadeIn(action_label)
        )

        j2_t1_small = m.Polygon(*[
            small_axes.c2p(5, 2),
            small_axes.c2p(0, 2),
            small_axes.c2p(0, 1),
            small_axes.c2p(5, 1),
        ], color=C.BLUE, fill_opacity=1, stroke_width=1)

        j2_t1_small_target = j2_t1_small.copy()

        j2_t1_small.next_to(action_label, m.DOWN, buff=0.25)
        #j2_t1_small_target.z_index = small_axes.z_index - 1

        nn_time_width = 0.85 * 2.0
        nn_runtime = 0.2 * 1.5

        self.play(
            m.Transform(s0_tex, input_layer_group)
        )

        self.remove(s0_tex)
        self.play_without_section(
            m.ShowPassingFlash(connection_input_hidden_group.copy().set_color(C.PINK), time_width=nn_time_width,
                               run_time=nn_runtime)
        )
        self.play_without_section(
            m.ShowPassingFlash(connection_hidden_output_group.copy().set_color(C.PINK), time_width=nn_time_width,
                               run_time=nn_runtime)
        )
        policy_output = output_layer_group.copy()
        self.play_without_section(
            m.Transform(policy_output, j2_t1_small, replace_mobject_with_target_in_scene=True)
        )

        t5_circle.generate_target()
        t5_circle.target.set_fill(C.GREEN_LIGHT)

        t5_circle_copy = t5_circle.copy()
        t5_circle_copy.set_fill(C.GREEN_LIGHT, opacity=0.0)

        tempt5 = t5_text.copy()
        tempt5.z_index = 300

        self.add(tempt5)

        self.play(
            m.MoveToTarget(t5_circle),
            m.Transform(j2_t1_small.copy(), t5_circle_copy, replace_mobject_with_target_in_scene=True),
            m.Transform(j2_t1_small, j2_t1_small_target, replace_mobject_with_target_in_scene=True)
        )

        reward_line0 = m.Line(
            env_big_rect.get_left() + m.UP * signal_shift,
            env_big_rect.get_left() + m.UP * signal_shift + m.LEFT * 2.0,
            color=C.DEFAULT_FONT,
            **signal_line_args
        )
        reward_line1 = m.Line(
            reward_line0.get_left(),
            np.array([reward_line0.get_left()[0], (a_big_rect.get_left() + m.DOWN * signal_shift)[1], 0]),
            color=C.DEFAULT_FONT,
            **signal_line_args
        )
        reward_line2 = m.Arrow(
            reward_line1.get_top(),
            a_big_rect.get_left() + m.DOWN * signal_shift,
            color=C.DEFAULT_FONT,
            **signal_arrow_args
        )

        reward_label = m.Tex(r"$\mathsf{r}$", color=C.DEFAULT_FONT).scale(0.75)
        reward_label.next_to(reward_line1, m.RIGHT, buff=0.25)

        reward_signal = m.VGroup(reward_line0, reward_line1, reward_line2)

        self.play(
            m.FadeIn(reward_signal),
            m.FadeIn(reward_label)
        )

        reward_text = styled_text("Reward: ", color=C.DEFAULT_FONT).scale(0.75).to_corner(m.UL, buff=0.25)
        reward_text.scale(0.75)
        reward_text.shift(m.DOWN * 0.75)

        # shift a_big_rect_text_group down

        y_shift = m.DOWN * 0.25

        a_big_group = m.VGroup(
            a_big_rect,
            a_big_rect_title_rectangle,
            a_big_rect_title,
            neural_network
        )

        a_big_group.generate_target()
        a_big_group.target.shift(y_shift)

        state_line0 = m.Line(
            env_big_rect.get_left() + m.DOWN * signal_shift,
            env_big_rect.get_left() + m.DOWN * signal_shift + m.LEFT * 2.5,
            color=C.DEFAULT_FONT,
            **signal_line_args
        )
        state_line1 = m.Line(
            state_line0.get_left(),
            np.array([state_line0.get_left()[0], (a_big_rect.get_left() + m.UP * signal_shift + y_shift)[1], 0]),
            color=C.DEFAULT_FONT,
            **signal_line_args
        )
        state_line2 = m.Arrow(
            state_line1.get_top(),
            a_big_rect.get_left() + m.UP * signal_shift + y_shift,
            color=C.DEFAULT_FONT,
            **signal_arrow_args
        )

        state_signal_new = m.VGroup(state_line0, state_line1, state_line2)

        # reward signal shift

        reward_line0 = m.Line(
            env_big_rect.get_left() + m.UP * signal_shift,
            env_big_rect.get_left() + m.UP * signal_shift + m.LEFT * 2.0,
            color=C.DEFAULT_FONT,
            **signal_line_args
        )
        reward_line1 = m.Line(
            reward_line0.get_left(),
            np.array([reward_line0.get_left()[0], (a_big_rect.get_left() + m.DOWN * signal_shift + y_shift)[1], 0]),
            color=C.DEFAULT_FONT,
            **signal_line_args
        )

        reward_line2 = m.Arrow(
            reward_line1.get_top(),
            a_big_rect.get_left() + m.DOWN * signal_shift + y_shift,
            color=C.DEFAULT_FONT,
            **signal_arrow_args
        )

        reward_signal_new = m.VGroup(reward_line0, reward_line1, reward_line2)

        # action signal shift

        action_line0 = m.Line(
            a_big_rect.get_right() + y_shift,
            a_big_rect.get_right() + m.RIGHT * 4.0 + y_shift,
            color=C.DEFAULT_FONT,
            **signal_line_args
        )

        action_line1 = m.Line(
            action_line0.get_right(),
            np.array([action_line0.get_right()[0], env_big_rect.get_right()[1], 0]),
            color=C.DEFAULT_FONT,
            **signal_line_args
        )

        action_line2 = m.Arrow(
            action_line1.get_bottom(),
            env_big_rect.get_right(),
            color=C.DEFAULT_FONT,
            **signal_arrow_args
        )

        action_signal_new = m.VGroup(action_line0, action_line1, action_line2)

        r_shift = m.DOWN * 0.09
        r_shift_komma = m.DOWN * 0.15

        r_buff = 0.25

        rewards_tex = m.Tex(r"$\mathsf{r_1}$", r"$\:,\,$",
                            r"$\mathsf{r_2}$", r"$\:,\,$",
                            r"$\mathsf{r_3}$", r"$\:,\,$",
                            r"$\mathsf{r_4}$", r"$\:,\,$",
                            r"$\mathsf{r_5}$", r"$\:,\,$",
                            r"$\mathsf{r_6}$", r"$\:,\,$",
                            r"$\mathsf{r_7}$", r"$\:,\,$",
                            r"$\mathsf{r_8}$",
                            color=C.DEFAULT_FONT).scale(0.75).next_to(reward_text, m.RIGHT, buff=0.25).shift(r_shift)

        # r_1 = m.MathTex("r_1", color=C.DEFAULT_FONT).next_to(reward_text, m.RIGHT, buff=0.25).shift(r_shift)
        # r_1_komma = m.MathTex(",", color=C.DEFAULT_FONT).next_to(r_1, m.RIGHT, buff=0.125).shift(r_shift_komma)

        # r_2 = m.MathTex("r_2", color=C.DEFAULT_FONT).next_to(r_1, m.RIGHT, buff=r_buff + r_1_komma.width)
        # r_2_komma = m.MathTex(",", color=C.DEFAULT_FONT).next_to(r_1_komma, m.RIGHT, buff=r_buff + r_1.width)

        # r_3 = m.MathTex("r_3", color=C.DEFAULT_FONT).next_to(r_2, m.RIGHT, buff=r_buff + r_2_komma.width)
        # r_3_komma = m.MathTex(",", color=C.DEFAULT_FONT).next_to(r_2_komma, m.RIGHT, buff=r_buff + r_2.width)

        # r_4 = m.MathTex("r_4", color=C.DEFAULT_FONT).next_to(r_3, m.RIGHT, buff=r_buff + r_3_komma.width)
        # r_4_komma = m.MathTex(",", color=C.DEFAULT_FONT).next_to(r_3_komma, m.RIGHT, buff=r_buff + r_3.width)

        # r_5 = m.MathTex("r_5", color=C.DEFAULT_FONT).next_to(r_4, m.RIGHT, buff=r_buff + r_4_komma.width)
        # r_5_komma = m.MathTex(",", color=C.DEFAULT_FONT).next_to(r_4_komma, m.RIGHT, buff=r_buff + r_4.width)

        # r_6 = m.MathTex("r_6", color=C.DEFAULT_FONT).next_to(r_5, m.RIGHT, buff=r_buff + r_5_komma.width)
        # r_6_komma = m.MathTex(",", color=C.DEFAULT_FONT).next_to(r_5_komma, m.RIGHT, buff=r_buff + r_5.width)

        # r_7 = m.MathTex("r_7", color=C.DEFAULT_FONT).next_to(r_6, m.RIGHT, buff=r_buff + r_6_komma.width)
        # r_7_komma = m.MathTex(",", color=C.DEFAULT_FONT).next_to(r_6_komma, m.RIGHT, buff=r_buff + r_6.width)

        # r_8 = m.MathTex("r_8", color=C.DEFAULT_FONT).next_to(r_7, m.RIGHT, buff=r_buff + r_7_komma.width)
        # r_8_komma = m.MathTex(",", color=C.DEFAULT_FONT).next_to(r_7_komma, m.RIGHT, buff=r_buff + r_7.width)

        s1_tex = styled_text("[0,0,...,0]").scale(0.3125).next_to(state_label, m.DOWN, buff=0.25)
        s2_tex = styled_text("[0,1,...,1]").scale(0.3125).next_to(state_label, m.DOWN, buff=0.25)
        s3_tex = styled_text("[1,0,...,0]").scale(0.3125).next_to(state_label, m.DOWN, buff=0.25)
        s4_tex = styled_text("[1,1,...,1]").scale(0.3125).next_to(state_label, m.DOWN, buff=0.25)
        s5_tex = styled_text("[0,0,...,1]").scale(0.3125).next_to(state_label, m.DOWN, buff=0.25)
        s6_tex = styled_text("[0,1,...,0]").scale(0.3125).next_to(state_label, m.DOWN, buff=0.25)
        s7_tex = styled_text("[1,0,...,1]").scale(0.3125).next_to(state_label, m.DOWN, buff=0.25)
        s8_tex = styled_text("[1,1,...,0]").scale(0.3125).next_to(state_label, m.DOWN, buff=0.25)

        r1_tex = m.Tex(r"$\mathsf{r_1}$", color=C.DEFAULT_FONT).scale(0.75).next_to(reward_label, m.DOWN, buff=0.25)
        r2_tex = m.Tex(r"$\mathsf{r_2}$", color=C.DEFAULT_FONT).scale(0.75).next_to(reward_label, m.DOWN, buff=0.25)
        r3_tex = m.Tex(r"$\mathsf{r_3}$", color=C.DEFAULT_FONT).scale(0.75).next_to(reward_label, m.DOWN, buff=0.25)
        r4_tex = m.Tex(r"$\mathsf{r_4}$", color=C.DEFAULT_FONT).scale(0.75).next_to(reward_label, m.DOWN, buff=0.25)
        r5_tex = m.Tex(r"$\mathsf{r_5}$", color=C.DEFAULT_FONT).scale(0.75).next_to(reward_label, m.DOWN, buff=0.25)
        r6_tex = m.Tex(r"$\mathsf{r_6}$", color=C.DEFAULT_FONT).scale(0.75).next_to(reward_label, m.DOWN, buff=0.25)
        r7_tex = m.Tex(r"$\mathsf{r_7}$", color=C.DEFAULT_FONT).scale(0.75).next_to(reward_label, m.DOWN, buff=0.25)
        r8_tex = m.Tex(r"$\mathsf{r_8}$", color=C.DEFAULT_FONT).scale(0.75).next_to(reward_label, m.DOWN, buff=0.25)

        j1_t1 = m.Polygon(*[
            small_axes.c2p(5 + 11, 3),
            small_axes.c2p(5, 3),
            small_axes.c2p(5, 2),
            small_axes.c2p(16, 2),
        ], color=C.BLUE, fill_opacity=1, stroke_width=1)

        j1_t2 = m.Polygon(*[
            small_axes.c2p(16 + 3, 3),
            small_axes.c2p(16, 3),
            small_axes.c2p(16, 2),
            small_axes.c2p(19, 2),
        ], color=C.ORANGE_DARK, fill_opacity=1, stroke_width=1)

        j1_t3 = m.Polygon(*[
            small_axes.c2p(24, 3),
            small_axes.c2p(21, 3),
            small_axes.c2p(21, 2),
            small_axes.c2p(24, 2),
        ], color=C.GREEN, fill_opacity=1, stroke_width=1)

        j1_t4 = m.Polygon(*[
            small_axes.c2p(36, 3),
            small_axes.c2p(24, 3),
            small_axes.c2p(24, 2),
            small_axes.c2p(36, 2),
        ], color=C.TEAL, fill_opacity=1, stroke_width=1)

        j2_t2 = m.Polygon(*[
            small_axes.c2p(21, 2),
            small_axes.c2p(5, 2),
            small_axes.c2p(5, 1),
            small_axes.c2p(21, 1),
        ], color=C.GREEN, fill_opacity=1, stroke_width=1)

        j2_t3 = m.Polygon(*[
            small_axes.c2p(28, 2),
            small_axes.c2p(21, 2),
            small_axes.c2p(21, 1),
            small_axes.c2p(28, 1),
        ], color=C.ORANGE_DARK, fill_opacity=1, stroke_width=1)

        j2_t4 = m.Polygon(*[
            small_axes.c2p(40, 2),
            small_axes.c2p(36, 2),
            small_axes.c2p(36, 1),
            small_axes.c2p(40, 1),
        ], color=C.TEAL, fill_opacity=1, stroke_width=1)

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

        self.play(
            m.Transform(graph.copy(), r1_tex, replace_mobject_with_target_in_scene=True),
            m.Transform(graph.copy(), s1_tex, replace_mobject_with_target_in_scene=True),
        )

        # initial shift and step 1
        scheduling_loop_runt_time = 0.25
        self.play(
            m.FadeIn(reward_text),
            m.MoveToTarget(a_big_group),
            m.Transform(state_signal, state_signal_new, replace_mobject_with_target_in_scene=True),
            m.Transform(reward_signal, reward_signal_new, replace_mobject_with_target_in_scene=True),
            m.Transform(action_signal, action_signal_new, replace_mobject_with_target_in_scene=True),
            m.Transform(r1_tex, rewards_tex[0], replace_mobject_with_target_in_scene=True),
        )
        self.play_without_section(
            m.Transform(s1_tex, input_layer_group, run_time=scheduling_loop_runt_time),
        )
        self.remove(s1_tex)
        self.play_without_section(
            m.ShowPassingFlash(connection_input_hidden_group.copy().set_color(C.PINK), time_width=nn_time_width,
                               run_time=nn_runtime)
        )
        self.play_without_section(
            m.ShowPassingFlash(connection_hidden_output_group.copy().set_color(C.PINK), time_width=nn_time_width,
                               run_time=nn_runtime)
        )

        policy_output = output_layer_group.copy()
        j1_t1_small_target = j1_t1.copy()
        j1_t1.next_to(action_label, m.DOWN, buff=0.25)

        self.play_without_section(
            m.Transform(policy_output, j1_t1, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
        )

        t1_circle.generate_target()
        t1_circle.target.set_fill(C.GREEN_LIGHT)

        t1_circle_copy = t1_circle.copy()
        t1_circle_copy.set_fill(C.GREEN_LIGHT, opacity=0.0)

        self.play_without_section(
            m.MoveToTarget(t1_circle, run_time=scheduling_loop_runt_time),
            m.Transform(j1_t1.copy(), t1_circle_copy, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(j1_t1, j1_t1_small_target, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Write(machine_edge_5_1, run_time=scheduling_loop_runt_time)
        )
        # add machine edge to graph
        graph.add(machine_edge_5_1)

        # step 2
        self.play_without_section(
            m.Transform(graph.copy(), r2_tex, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(graph.copy(), s2_tex, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
        )
        self.play_without_section(
            m.FadeIn(rewards_tex[1], run_time=scheduling_loop_runt_time),
            m.Transform(r2_tex, rewards_tex[2], replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(s2_tex, input_layer_group, run_time=scheduling_loop_runt_time),
        )
        self.remove(s2_tex)
        self.play_without_section(
            m.ShowPassingFlash(connection_input_hidden_group.copy().set_color(C.PINK), time_width=nn_time_width,
                               run_time=nn_runtime)
        )
        self.play_without_section(
            m.ShowPassingFlash(connection_hidden_output_group.copy().set_color(C.PINK), time_width=nn_time_width,
                               run_time=nn_runtime)
        )

        policy_output = output_layer_group.copy()
        j2_t2_small_target = j2_t2.copy()
        j2_t2.next_to(action_label, m.DOWN, buff=0.25).scale(0.8)

        self.play_without_section(
            m.Transform(policy_output, j2_t2, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
        )

        t6_circle.generate_target()
        t6_circle.target.set_fill(C.GREEN_LIGHT)

        t6_circle_copy = t6_circle.copy()
        t6_circle_copy.set_fill(C.GREEN_LIGHT, opacity=0.0)

        self.play_without_section(
            m.MoveToTarget(t6_circle, run_time=scheduling_loop_runt_time),
            m.Transform(j2_t2.copy(), t6_circle_copy, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(j2_t2, j2_t2_small_target, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
        )

        # step 3
        self.play_without_section(
            m.Transform(graph.copy(), r3_tex, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(graph.copy(), s3_tex, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
        )

        self.play_without_section(
            m.FadeIn(rewards_tex[3], run_time=scheduling_loop_runt_time),
            m.Transform(r3_tex, rewards_tex[4], replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(s3_tex, input_layer_group, run_time=scheduling_loop_runt_time),
        )
        self.remove(s3_tex)

        self.play_without_section(
            m.ShowPassingFlash(connection_input_hidden_group.copy().set_color(C.PINK), time_width=nn_time_width,
                               run_time=nn_runtime)
        )
        self.play_without_section(
            m.ShowPassingFlash(connection_hidden_output_group.copy().set_color(C.PINK), time_width=nn_time_width,
                               run_time=nn_runtime)
        )

        policy_output = output_layer_group.copy()
        j1_t2_small_target = j1_t2.copy()

        j1_t2.next_to(action_label, m.DOWN, buff=0.25)

        self.play_without_section(
            m.Transform(policy_output, j1_t2, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
        )

        t2_circle.generate_target()
        t2_circle.target.set_fill(C.GREEN_LIGHT)

        t2_circle_copy = t2_circle.copy()
        t2_circle_copy.set_fill(C.GREEN_LIGHT, opacity=0.0)

        self.play_without_section(
            m.MoveToTarget(t2_circle, run_time=scheduling_loop_runt_time),
            m.Transform(j1_t2.copy(), t2_circle_copy, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(j1_t2, j1_t2_small_target, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
        )

        # step 4
        self.play_without_section(
            m.Transform(graph.copy(), r4_tex, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(graph.copy(), s4_tex, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
        )

        self.play_without_section(
            m.FadeIn(rewards_tex[5], run_time=scheduling_loop_runt_time),
            m.Transform(r4_tex, rewards_tex[6], replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(s4_tex, input_layer_group, run_time=scheduling_loop_runt_time),
        )
        self.remove(s4_tex)

        self.play_without_section(
            m.ShowPassingFlash(connection_input_hidden_group.copy().set_color(C.PINK), time_width=nn_time_width,
                               run_time=nn_runtime)
        )
        self.play_without_section(
            m.ShowPassingFlash(connection_hidden_output_group.copy().set_color(C.PINK), time_width=nn_time_width,
                               run_time=nn_runtime)
        )

        policy_output = output_layer_group.copy()

        j1_t3_small_target = j1_t3.copy()
        j1_t3.next_to(action_label, m.DOWN, buff=0.25)

        self.play_without_section(
            m.Transform(policy_output, j1_t3, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
        )

        t3_circle.generate_target()
        t3_circle.target.set_fill(C.GREEN_LIGHT)

        t3_circle_copy = t3_circle.copy()
        t3_circle_copy.set_fill(C.GREEN_LIGHT, opacity=0.0)

        self.play_without_section(
            m.MoveToTarget(t3_circle, run_time=scheduling_loop_runt_time),
            m.Transform(j1_t3.copy(), t3_circle_copy, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(j1_t3, j1_t3_small_target, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Write(machine_edge_6_3, run_time=scheduling_loop_runt_time)
        )
        graph.add(machine_edge_6_3)

        # step 5
        self.play_without_section(
            m.Transform(graph.copy(), r5_tex, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(graph.copy(), s5_tex, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
        )

        self.play_without_section(
            m.FadeIn(rewards_tex[7], run_time=scheduling_loop_runt_time),
            m.Transform(r5_tex, rewards_tex[8], replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(s5_tex, input_layer_group, run_time=scheduling_loop_runt_time),
        )
        self.remove(s5_tex)

        self.play_without_section(
            m.ShowPassingFlash(connection_input_hidden_group.copy().set_color(C.PINK), time_width=nn_time_width,
                               run_time=nn_runtime)
        )
        self.play_without_section(
            m.ShowPassingFlash(connection_hidden_output_group.copy().set_color(C.PINK), time_width=nn_time_width,
                               run_time=nn_runtime)
        )

        policy_output = output_layer_group.copy()

        j2_t3_small_target = j2_t3.copy()
        j2_t3.next_to(action_label, m.DOWN, buff=0.25)

        self.play_without_section(
            m.Transform(policy_output, j2_t3, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
        )

        t7_circle.generate_target()
        t7_circle.target.set_fill(C.GREEN_LIGHT)

        t7_circle_copy = t7_circle.copy()
        t7_circle_copy.set_fill(C.GREEN_LIGHT, opacity=0.0)

        self.play_without_section(
            m.MoveToTarget(t7_circle, run_time=scheduling_loop_runt_time),
            m.Transform(j2_t3.copy(), t7_circle_copy, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(j2_t3, j2_t3_small_target, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Write(machine_edge_2_7, run_time=scheduling_loop_runt_time)
        )
        graph.add(machine_edge_2_7)

        # step 6
        self.play_without_section(
            m.Transform(graph.copy(), r6_tex, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(graph.copy(), s6_tex, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
        )

        self.play_without_section(
            m.FadeIn(rewards_tex[9], run_time=scheduling_loop_runt_time),
            m.Transform(r6_tex, rewards_tex[10], replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(s6_tex, input_layer_group, run_time=scheduling_loop_runt_time),
        )
        self.remove(s6_tex)

        self.play_without_section(
            m.ShowPassingFlash(connection_input_hidden_group.copy().set_color(C.PINK), time_width=nn_time_width,
                               run_time=nn_runtime)
        )
        self.play_without_section(
            m.ShowPassingFlash(connection_hidden_output_group.copy().set_color(C.PINK), time_width=nn_time_width,
                               run_time=nn_runtime)
        )

        policy_output = output_layer_group.copy()

        j1_t4_small_target = j1_t4.copy()
        j1_t4.next_to(action_label, m.DOWN, buff=0.25)

        self.play_without_section(
            m.Transform(policy_output, j1_t4, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
        )

        t4_circle.generate_target()
        t4_circle.target.set_fill(C.GREEN_LIGHT)

        t4_circle_copy = t4_circle.copy()
        t4_circle_copy.set_fill(C.GREEN_LIGHT, opacity=0.0)

        self.play_without_section(
            m.MoveToTarget(t4_circle, run_time=scheduling_loop_runt_time),
            m.Transform(j1_t4.copy(), t4_circle_copy, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(j1_t4, j1_t4_small_target, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
        )

        # step 7
        self.play_without_section(
            m.Transform(graph.copy(), r7_tex, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(graph.copy(), s7_tex, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
        )

        self.play_without_section(
            m.FadeIn(rewards_tex[11], run_time=scheduling_loop_runt_time),
            m.Transform(r7_tex, rewards_tex[12], replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(s7_tex, input_layer_group, run_time=scheduling_loop_runt_time),
        )
        self.remove(s7_tex)

        self.play_without_section(
            m.ShowPassingFlash(connection_input_hidden_group.copy().set_color(C.PINK), time_width=nn_time_width,
                               run_time=nn_runtime)
        )
        self.play_without_section(
            m.ShowPassingFlash(connection_hidden_output_group.copy().set_color(C.PINK), time_width=nn_time_width,
                               run_time=nn_runtime)
        )

        policy_output = output_layer_group.copy()

        j2_t4_small_target = j2_t4.copy()
        j2_t4.next_to(action_label, m.DOWN, buff=0.25)

        self.play_without_section(
            m.Transform(policy_output, j2_t4, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
        )

        t8_circle.generate_target()
        t8_circle.target.set_fill(C.GREEN_LIGHT)

        t8_circle_copy = t8_circle.copy()
        t8_circle_copy.set_fill(C.GREEN_LIGHT, opacity=0.0)

        self.play_without_section(
            m.MoveToTarget(t8_circle, run_time=scheduling_loop_runt_time),
            m.Transform(j2_t4.copy(), t8_circle_copy, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(j2_t4, j2_t4_small_target, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Write(machine_edge_4_8, run_time=scheduling_loop_runt_time)
        )
        graph.add(machine_edge_4_8)

        # step 8
        self.play_without_section(
            m.Transform(graph.copy(), r8_tex, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.Transform(graph.copy(), s8_tex, replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
        )

        self.play_without_section(
            m.FadeIn(rewards_tex[13], run_time=scheduling_loop_runt_time),
            m.Transform(r8_tex, rewards_tex[14], replace_mobject_with_target_in_scene=True,
                        run_time=scheduling_loop_runt_time),
            m.FadeOut(s8_tex),
        )

        # highlight rewards
        reward_group = [
            rewards_tex[0],
            rewards_tex[2],
            rewards_tex[4],
            rewards_tex[6],
            rewards_tex[8],
            rewards_tex[10],
            rewards_tex[12],
            rewards_tex[14]
        ]

        self.play(
            *[m.Indicate(r, color=C.YELLOW, scale_factor=1.05) for r in reward_group],
        )

        self.play(
            m.Indicate(state_signal, color=C.YELLOW, scale_factor=1.00),
            m.Indicate(state_label, color=C.YELLOW, scale_factor=1.2),
        )

        self.play(
            m.Indicate(action_signal, color=C.YELLOW, scale_factor=1.00),
            m.Indicate(action_label, color=C.YELLOW, scale_factor=1.2),
        )

        self.play(
            m.Indicate(reward_signal, color=C.YELLOW, scale_factor=1.00),
            m.Indicate(reward_label, color=C.YELLOW, scale_factor=1.2),
        )

        self.play(
            self.overlay_scene()
        )






if __name__ == '__main__':
    EIopRlLoop.save_sections_without_cache()