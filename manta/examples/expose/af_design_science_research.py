import manim as m
import numpy as np

from color_theme.carolus.corolus_theme import CarolusTheme
from components.axes_utils import AxesUtils
from components.gantt_utils import GanttUtils
from components.uml_utils import UmlUtils
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class ExposeDesignScienceResearch(UmlUtils, CarolusTheme, AxesUtils, GanttUtils, MinimalSlideTemplate):
    index_prefix = "F"

    font_name = "IosevkaTermSlab Nerd Font Mono"

    subtitle_color = CarolusTheme.font_color_secondary
    title_seperator_color = CarolusTheme.blue_bright

    def construct(self):
        self.play(
            self.set_title_row(
                title="Design Science Research",
            )
        )

        circle_width = 1.5

        rect_width = (self.content_width - (2 * circle_width) - (4 * self.med_small_buff)) / 3


        environment_rect = self.title_rectangle(
            width=rect_width,
            height=6,
            title="Environment",
            title_scale=0.75,

        )

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
            width=4, height=2, data=gantt_data, n_machines=4, resource_naming="Machine"
        ).scale_to_fit_width(environment_rect.width * 0.6)

        assignment_circle_radius = 0.25
        worker_color = self.blue
        task_color = self.red

        worker_circle_0 = self.math_circle("w_0", radius=assignment_circle_radius, fill_color=self.yellow,
                                           stroke_color=worker_color, font_color=self.black, stroke_width=3)
        worker_circle_1 = self.math_circle("w_1", radius=assignment_circle_radius, fill_color=self.yellow,
                                           stroke_color=worker_color, font_color=self.black, stroke_width=3)
        worker_circle_2 = self.math_circle("w_2", radius=assignment_circle_radius, fill_color=self.yellow,
                                           stroke_color=worker_color, font_color=self.black, stroke_width=3)
        worker_circle_3 = self.math_circle("w_3", radius=assignment_circle_radius, fill_color=self.yellow,
                                           stroke_color=worker_color, font_color=self.black, stroke_width=3)

        task_circle_0 = self.math_circle("t_0", radius=assignment_circle_radius, stroke_color=task_color,
                                         fill_color=self.yellow, font_color=self.black, stroke_width=3)
        task_circle_1 = self.math_circle("t_1", radius=assignment_circle_radius, stroke_color=task_color,
                                         fill_color=self.yellow, font_color=self.black, stroke_width=3)
        task_circle_2 = self.math_circle("t_2", radius=assignment_circle_radius, stroke_color=task_color,
                                         fill_color=self.yellow, font_color=self.black, stroke_width=3)
        task_circle_3 = self.math_circle("t_3", radius=assignment_circle_radius, stroke_color=task_color,
                                         fill_color=self.yellow, font_color=self.black, stroke_width=3)

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

        assignment_group.scale_to_fit_height(gantt_chart.height)


        assignment_group.next_to(gantt_chart, m.RIGHT, buff=self.small_buff)


        example_group = m.VGroup(
            gantt_chart,
            assignment_group,
        )

        example_group.next_to(environment_rect.get_top(), m.DOWN, buff=1)

        knowledge_base_text = self.titled_bulletpoints(
            titled_bulletpoints=[(
                "Motivation",
                [
                    "Personalized production yields\n a high degree of flexibility \nin the production environment",
                    "Interconnected optimization\n problems require a performant\n approach",
                    "The resulting optimization \nproblem have a few minutes of\n time budget",
                ]
            )]
        )
        knowledge_base_text.scale(0.6)

        knowledge_base_text.shift(m.DOWN * 0.8)



        environment_group = m.VGroup(
            environment_rect,
            example_group,
            knowledge_base_text
        )

        environment_group.to_edge(m.LEFT, buff=self.med_large_buff)

        relevance_cycle = m.Circle(
            radius=circle_width / 2,
            fill_color=self.blue,
            fill_opacity=0.2,
            stroke_width=2,
            stroke_color=self.outline_color,
        )
        relevance_cycle_label = self.term_text("Relevance\nCycle")
        relevance_cycle_label.scale(0.75)
        relevance_cycle_label.move_to(m.ORIGIN)

        relevance_cycle_top_curved_arrow1 = m.CurvedArrow(
            start_point=relevance_cycle.point_at_angle(180 * m.DEGREES),
            end_point=relevance_cycle.point_at_angle(70 * m.DEGREES),
            radius=-0.5 * circle_width,
            color=self.yellow,
            tip_length=0.075,
        )

        relevance_cycle_top_curved_arrow2 = m.CurvedArrow(
            start_point=relevance_cycle.point_at_angle(60 * m.DEGREES),
            end_point=relevance_cycle.point_at_angle(-50 * m.DEGREES),
            radius=-0.5 * circle_width,
            color=self.yellow,
            tip_length=0.075,
        )

        relevance_cycle_top_curved_arrow3 = m.CurvedArrow(
            start_point=relevance_cycle.point_at_angle(-60 * m.DEGREES),
            end_point=relevance_cycle.point_at_angle(-170 * m.DEGREES),
            radius=-0.5 * circle_width,
            color=self.yellow,
            tip_length=0.075,
        )

        relevance_cycle_top_label = self.term_text("Problem\nSolving")
        relevance_cycle_top_label.scale(0.625)
        relevance_cycle_top_label.next_to(relevance_cycle, m.UP, buff=self.med_small_buff)

        relevance_cycle_bot_label = self.term_text("Problem\nDefinition")
        relevance_cycle_bot_label.scale(0.625)
        relevance_cycle_bot_label.next_to(relevance_cycle, m.DOWN, buff=self.med_small_buff)

        relevance_cycle_top_text = self.term_text(
            "Problem identification\nin practice"
        )
        relevance_cycle_top_text.scale(0.4)

        relevance_cycle_top_text_rect = self.rectangle(
            width=circle_width,
            height=0.75,
            fill_color=self.blue,
            fill_opacity=0.2,
        )

        relevance_cycle_top_text.move_to(m.UP * 2)
        relevance_cycle_top_text_rect.move_to(m.UP * 2)

        relevance_cycle_bot_text = self.term_text(
            "Implementation in\nresearch/industrial\nprojects"
        )
        relevance_cycle_bot_text.scale(0.4)
        relevance_cycle_bot_text.move_to(m.DOWN * 2)

        relevance_cycle_bot_text_rect = self.rectangle(
            width=circle_width,
            height=0.75,
            fill_color=self.blue,
            fill_opacity=0.2,
        )
        relevance_cycle_bot_text_rect.move_to(m.DOWN * 2)

        relevance_cycle_group = m.VGroup(
            relevance_cycle,
            relevance_cycle_label,
            relevance_cycle_top_curved_arrow1,
            relevance_cycle_top_curved_arrow2,
            relevance_cycle_top_curved_arrow3,
            relevance_cycle_top_label,
            relevance_cycle_bot_label,
            relevance_cycle_top_text,
            relevance_cycle_top_text_rect,
            relevance_cycle_bot_text,
            relevance_cycle_bot_text_rect,
        )

        relevance_cycle_group.shift(
            m.LEFT * (rect_width/2 + self.med_small_buff + circle_width/2),
        )


        design_research_rect = self.title_rectangle(
            width=rect_width,
            height=6,
            title="Design Research",
            title_scale=0.75,
        )

        import gymnasium as gym

        gym_class_uml_diagram = self.uml_class_diagram(gym.Env, class_name="NeuralMCTS.Env")
        gym_class_uml_diagram.scale_to_fit_height(0.625)

        gym_class_uml_diagram.next_to(design_research_rect[-1], m.DOWN, buff=self.med_small_buff)

        design_cycle = m.Circle(
            radius=circle_width / 2,
            fill_color=self.blue,
            fill_opacity=0.2,
            stroke_width=2,
            stroke_color=self.outline_color,
        )
        design_cycle_label = self.term_text("Design\nCycle")
        design_cycle_label.scale(0.75)
        design_cycle_label.move_to(m.ORIGIN)

        design_cycle_top_curved_arrow1 = m.CurvedArrow(
            start_point=design_cycle.point_at_angle(180 * m.DEGREES),
            end_point=design_cycle.point_at_angle(70 * m.DEGREES),
            radius=-0.5 * circle_width,
            color=self.red,
            tip_length=0.075,
        )

        design_cycle_top_curved_arrow2 = m.CurvedArrow(
            start_point=design_cycle.point_at_angle(60 * m.DEGREES),
            end_point=design_cycle.point_at_angle(-50 * m.DEGREES),
            radius=-0.5 * circle_width,
            color=self.red,
            tip_length=0.075,
        )

        design_cycle_top_curved_arrow3 = m.CurvedArrow(
            start_point=design_cycle.point_at_angle(-60 * m.DEGREES),
            end_point=design_cycle.point_at_angle(-170 * m.DEGREES),
            radius=-0.5 * circle_width,
            color=self.red,
            tip_length=0.075,
        )

        design_cycle_top_label = self.term_text("Framework\nDevelopment")
        design_cycle_top_label.scale(0.625)
        design_cycle_top_label.next_to(design_cycle, m.UP, buff=self.med_small_buff)

        design_cycle_bot_label = self.term_text("Framework\nEvaluation")
        design_cycle_bot_label.scale(0.625)
        design_cycle_bot_label.next_to(design_cycle, m.DOWN, buff=self.med_small_buff)


        design_cycle_group = m.VGroup(
            design_cycle,
            design_cycle_label,
            design_cycle_top_curved_arrow1,
            design_cycle_top_curved_arrow2,
            design_cycle_top_curved_arrow3,
            design_cycle_top_label,
            design_cycle_bot_label,
        )





        design_research_group = m.VGroup(
            design_research_rect,
            gym_class_uml_diagram,
            design_cycle_group
        )



        rigor_cycle = m.Circle(
            radius=circle_width / 2,
            fill_color=self.blue,
            fill_opacity=0.2,
            stroke_width=2,
            stroke_color=self.outline_color,
        )
        rigor_cycle_label = self.term_text("Rigor\nCycle")
        rigor_cycle_label.scale(0.75)
        rigor_cycle_label.move_to(m.ORIGIN)

        rigor_cycle_top_curved_arrow1 = m.CurvedArrow(
            start_point=rigor_cycle.point_at_angle(180 * m.DEGREES),
            end_point=rigor_cycle.point_at_angle(70 * m.DEGREES),
            radius=-0.5 * circle_width,
            color=self.yellow,
            tip_length=0.075,
        )

        rigor_cycle_top_curved_arrow2 = m.CurvedArrow(
            start_point=rigor_cycle.point_at_angle(60 * m.DEGREES),
            end_point=rigor_cycle.point_at_angle(-50 * m.DEGREES),
            radius=-0.5 * circle_width,
            color=self.yellow,
            tip_length=0.075,
        )

        rigor_cycle_top_curved_arrow3 = m.CurvedArrow(
            start_point=rigor_cycle.point_at_angle(-60 * m.DEGREES),
            end_point=rigor_cycle.point_at_angle(-170 * m.DEGREES),
            radius=-0.5 * circle_width,
            color=self.yellow,
            tip_length=0.075,
        )

        rigor_cycle_top_label = self.term_text("Additions to\nKnowledge Base")
        rigor_cycle_top_label.scale(0.625)
        rigor_cycle_top_label.next_to(rigor_cycle, m.UP, buff=self.med_small_buff)


        rigor_cycle_bot_label = self.term_text("Applicable\nKnowledge")
        rigor_cycle_bot_label.scale(0.625)
        rigor_cycle_bot_label.next_to(rigor_cycle, m.DOWN, buff=self.med_small_buff)

        rigor_cycle_top_text = self.term_text(
            "Results dissemination\nat conferences and in\npublications"
        )
        rigor_cycle_top_text.scale(0.4)
        rigor_cycle_top_text.move_to(m.UP * 2)

        rigor_cycle_top_text_rect = self.rectangle(
            width=circle_width,
            height=0.75,
            fill_color=self.blue,
            fill_opacity=0.2,
        )
        rigor_cycle_top_text_rect.move_to(m.UP * 2)

        rigor_cycle_bot_text = self.term_text(
            "Implementation of\nfoundations and\nmethodologies"
        )
        rigor_cycle_bot_text.scale(0.4)
        rigor_cycle_bot_text.move_to(m.DOWN * 2)

        rigor_cycle_bot_text_rect = self.rectangle(
            width=circle_width,
            height=0.75,
            fill_color=self.blue,
            fill_opacity=0.2,
        )

        rigor_cycle_bot_text_rect.move_to(m.DOWN * 2)






        rigor_cycle_group = m.VGroup(
            rigor_cycle,
            rigor_cycle_label,

            rigor_cycle_top_curved_arrow1,
            rigor_cycle_top_curved_arrow2,
            rigor_cycle_top_curved_arrow3,

            rigor_cycle_top_label,
            rigor_cycle_bot_label,

            rigor_cycle_top_text,
            rigor_cycle_top_text_rect,

            rigor_cycle_bot_text,
            rigor_cycle_bot_text_rect,
        )


        rigor_cycle_group.shift(
            m.RIGHT * (rect_width/2 + self.med_small_buff + circle_width/2),
        )


        knowledge_base_rect = self.title_rectangle(
            width=rect_width,
            height=6,
            title="Knowledge Base",
            title_scale=0.75,

        )


        learning_to_dispatch_screenshot = m.ImageMobject("screenshots/2020_l2d.png")

        learn_small_play_large_screenshot = m.ImageMobject("screenshots/2021_train_small.png")
        learn_small_play_large_screenshot.scale_to_fit_height(learning_to_dispatch_screenshot.height)
        learn_small_play_large_screenshot.next_to(learning_to_dispatch_screenshot, m.RIGHT, buff=self.med_large_buff)

        paper_group = m.Group(
            learning_to_dispatch_screenshot,
            learn_small_play_large_screenshot
        )
        paper_group.scale_to_fit_width(rect_width - 2*self.med_small_buff)
        paper_group.next_to(knowledge_base_rect[-1], m.DOWN, buff=self.med_small_buff)

        knowledge_base_text = self.titled_bulletpoints(
            titled_bulletpoints=[(
                "Foundations and Methodologies",
                [
                    "Operations Research",
                    "Job Shop Scheduling",
                    "Algorithms and Data Structures",
                    "Reinforcement Learning",
                    "Monte Carlo Tree Search",
                    "Meta-Heuristics",
                    "..."
                ]
            )]
        )
        knowledge_base_text.scale(0.6)

        knowledge_base_text.next_to(paper_group, m.DOWN, buff=self.med_small_buff)

        knowledge_base_group = m.Group(
            knowledge_base_rect,
            paper_group,
            knowledge_base_text
        )
        knowledge_base_group.to_edge(m.RIGHT, buff=self.med_large_buff)



        self.play(
            m.FadeIn(environment_group),

            m.FadeIn(design_research_group),


            m.FadeIn(knowledge_base_group),

            m.FadeIn(relevance_cycle_group),
            m.FadeIn(rigor_cycle_group),
        )

        self.wait(0.1)
        self.fade_out_scene()


if __name__ == '__main__':
    ExposeDesignScienceResearch.save_sections_without_cache()