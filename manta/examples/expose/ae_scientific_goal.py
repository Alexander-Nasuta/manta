import manim as m
import numpy as np

from color_theme.carolus.corolus_theme import CarolusTheme
from components.axes_utils import AxesUtils
from components.gantt_utils import GanttUtils
from components.uml_utils import UmlUtils
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class ExposeDesignScientificGoal(UmlUtils, CarolusTheme, AxesUtils, GanttUtils, MinimalSlideTemplate):
    index_prefix = "D"

    font_name = "IosevkaTermSlab Nerd Font Mono"

    subtitle_color = CarolusTheme.font_color_secondary
    title_seperator_color = CarolusTheme.blue_bright

    def construct(self):
        self.play(
            self.set_title_row(title="Research Questions"),
        )

        overall_research_question = self.icon_textbox(
            text="How should a size-agnostic neural MCIS be designed to utilizethe available time\n budget and leverage learning from small problem instances to larger ones?",
            font_size=self.font_size_small,
            # icon='alpha-a-box-outline',
            icon="goal",
            width=self.content_width,
        )
        overall_research_question.to_edge(m.UP, buff=1.0)

        research_queston1 = self.icon_textbox(
            text="What approaches to realize size-invariance can be identified in existing neural\n MCTS and RL application?",
            font_size=self.font_size_small,
            # icon='alpha-b-box-outline',
            icon="numeric-1-circle-outline",
            width=self.content_width,
        )
        research_queston1.next_to(overall_research_question, m.DOWN, buff=self.med_large_buff)

        research_question2 = self.icon_textbox(
            text="How can the size-agnostic neural MCTS be designed to be adaptable to different\n optimization problems in manufacturing?",
            font_size=self.font_size_small,
            # icon='alpha-c-box-outline',
            icon="numeric-2-circle-outline",
            width=self.content_width,
        )
        research_question2.next_to(research_queston1, m.DOWN, buff=self.med_large_buff)

        research_question3 = self.icon_textbox(
            text="To what extent can size-agnostic neural MCTS leverage learning from small problem\n instances to solve larger problem instances in manufacturing?",
            font_size=self.font_size_small,
            # icon='alpha-c-box-outline',
            icon="numeric-3-circle-outline",
            width=self.content_width,
        )
        research_question3.next_to(research_question2, m.DOWN, buff=self.med_large_buff)

        animation_group = m.AnimationGroup(
            *[m.FadeIn(elem) for elem in [overall_research_question, research_queston1, research_question2, research_question3]],
            lag_ratio=0.15
        )

        self.play(
            self.set_title_row(title="Research Questions", seperator=": ", subtitle="Scientific Goal"),
            m.FadeIn(overall_research_question),
        )

        self.play(
            self.set_title_row(title="Research Question 1", seperator=": ", subtitle="Literature Review"),
            m.FadeIn(research_queston1),
        )

        self.play(
            m.FadeOut(overall_research_question),
            m.FadeOut(research_queston1),
        )


        text_scale = 0.6

        t2c = {
            'Reinforcement Learning': self.blue,
            'Monte Carlo Tree Search': self.blue,
            'Neural': self.blue,
            'MCTS': self.blue,
            'AlphaGo': self.blue,
            'AlphaZero': self.blue,
            'MuZero': self.blue,
            'AND': self.font_color_secondary,
            'OR': self.font_color_secondary,
            '(': self.font_color_secondary,
            ')': self.font_color_secondary,

            'generalizable': self.green,
            'transferable': self.green,
            'dynamic size': self.green,
            'size-invariant': self.green,
            'size-agnostic': self.green,
            'board size': self.green

        }

        methods_text = """(Reinforcement Learning 
        AND Monte Carlo Tree Search) OR
        Neural Monte Carlo Tree Search OR 
        Neural MCTS OR
        AlphaGo OR 
        AlphaZero OR 
        MuZero"""

        methods_text_pre = self.term_text(
            "Reinforcement Learning",
            t2c=t2c
        )
        methods_text_pre.scale(text_scale)

        methods_text = self.term_text(
            methods_text,
            t2c=t2c
        )
        methods_text.scale(text_scale)

        and_text = self.term_text(
            "AND",
            font_color=self.font_color_secondary,
        )
        and_text.scale(text_scale)
        and_text.next_to(methods_text, m.RIGHT, buff=0.2)

        additions_text = "generalizable OR\ntransferable OR\ndynamic size OR\nsize-invariant OR\nsize-agnostic OR\nboard size"

        additions_text = self.term_text(
            additions_text,
            t2c=t2c
        )
        additions_text.scale(text_scale)

        additions_text.next_to(and_text, m.RIGHT, buff=0.2)

        query = m.VGroup(
            methods_text,
            and_text,
            additions_text,
        )


        query.move_to(m.ORIGIN)




        methods_text_pre.next_to(and_text, m.LEFT, buff=0.2)
        query_pre = m.VGroup(
            methods_text_pre,
            and_text,
            additions_text,
        )

        initial_query_box = self.wrap_with_icon_and_rectangle(
            query_pre,
            icon='card-search-outline',
            icon_color=self.blue,
            width=self.content_width,
            height=2.25
        )
        initial_query_box.to_edge(m.UP, buff=1.0)


        bullet_points_pre = self.bullet_point_list(
            [
                "Web of Science: 426",
                "Scopus: 630",
                "IEEExplore: 301",
                "PubMed: 50",
            ],
            t2c={
                '1': self.blue,
                '2': self.blue,
                '3': self.blue,
                '4': self.blue,
                '5': self.blue,
                '6': self.blue,
                '7': self.blue,
                '8': self.blue,
                '9': self.blue,
                '0': self.blue,
            },
            bullet_icon_color=self.blue,
        ).scale(0.625)

        initial_results_box = self.wrap_with_icon_and_rectangle(
            bullet_points_pre,
            icon='database-search',
            icon_color=self.blue,
            width=self.content_width,
            height=2.0
        )
        initial_results_box.next_to(initial_query_box, m.DOWN, buff=self.med_large_buff)

        self.play(
            self.set_title_row(title="Initial Literature Search", seperator=": ", subtitle="size-agnostic RL"),
            m.FadeIn(initial_query_box),
        )

        self.play(
            m.FadeIn(initial_results_box),
        )

        and_text_copy = and_text.copy()
        additions_text_copy = additions_text.copy()

        methods_text.move_to(m.ORIGIN)
        and_text_copy.next_to(methods_text, m.RIGHT, buff=0.2)
        additions_text_copy.next_to(and_text_copy, m.RIGHT, buff=0.2)

        query = m.VGroup(
            methods_text,
            and_text_copy,
            additions_text_copy,
        )


        query_box = self.wrap_with_icon_and_rectangle(
            query,
            icon='card-search-outline',
            icon_color=self.blue,
            width=self.content_width,
            height=2.25
        )

        query_box.to_edge(m.UP, buff=1.0)

        bullet_points = self.bullet_point_list(
            [
                "Web of Science: 34",
                "Scopus: 49",
                "IEEExplore: 58",
                "PubMed: 4",
            ],
            t2c={
                '3': self.blue,
                '9': self.blue,
                '58': self.blue,
                '4': self.blue,
            },
            bullet_icon_color=self.blue,
        ).scale(0.625)

        results_box = self.wrap_with_icon_and_rectangle(
            bullet_points,
            icon='database-search',
            icon_color=self.blue,
            width=self.content_width,
            height=2.0
        )
        results_box.next_to(query_box, m.DOWN, buff=self.med_large_buff)

        self.play(
            self.set_title_row(title="Initial Literature Search", seperator=": ", subtitle="size-agnostic neural MCTS"),
            m.ReplacementTransform(initial_query_box, query_box),
            m.ReplacementTransform(initial_results_box, results_box),
        )


        text_block="""
                             ╻      ╻                     ╻            ╻                ╻                  
          authors            ┃ year ┃ domain              ┃ method     ┃ size-agonistic ┃ size-agonistic   
                             ┃      ┃                     ┃            ┃ value-function ┃ policy           
        ━━━━━━━━━━━━━━━━━━━━━╋━━━━━━╋━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━
          Zhang et al.       ┃ 2020 ┃ optimization        ┃ RL         ┃       󰫈        ┃        󰫆         
        ━━━━━━━━━━━━━━━━━━━━━╋━━━━━━╋━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━
          Oren et al.        ┃ 2021 ┃ optimization        ┃ RL + NMCTS ┃       󰫇        ┃        󰫇         
        ━━━━━━━━━━━━━━━━━━━━━╋━━━━━━╋━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━
          Ben-Assayag et al. ┃ 2021 ┃ games               ┃ NMCTS      ┃       󰫈        ┃        󰫈         
        ━━━━━━━━━━━━━━━━━━━━━╋━━━━━━╋━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━
          Thacker et al.     ┃ 2022 ┃ redundancy analysis ┃ NMCTS      ┃       󰫈        ┃        󰫅         
        ━━━━━━━━━━━━━━━━━━━━━╋━━━━━━╋━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━
          Pirnay et al.      ┃ 2023 ┃ optimization        ┃ NMCTS      ┃       󰋙        ┃        󰋙         
        ━━━━━━━━━━━━━━━━━━━━━╋━━━━━━╋━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━
          Yang et al.        ┃ 2024 ┃ games               ┃ NMCTS      ┃       󰫈        ┃        󰫈         
                             ╹      ╹                     ╹            ╹                ╹                  """

        table = self.term_paragraph(
            text_block,
        t2c = {
            '╋': self.outline_color,
            '┃': self.outline_color,
            '━': self.outline_color,
            '╻': self.outline_color,
            '╹': self.outline_color,
            '󰫈': self.yellow,
            '󰫇': self.yellow,
            '󰫆': self.yellow,
            '󰫅': self.yellow,
            '󰋙': self.yellow,
        }, t2w = {
            'authors': m.BOLD,
            'year': m.BOLD,
            'domain': m.BOLD,
            'method': m.BOLD,
            'size-agonistic': m.BOLD,
            'value-function': m.BOLD,
            'policy': m.BOLD,
        })

        table.scale_to_fit_width(self.content_width)

        table_box = self.wrap_with_rectangle(
            table,
            width=self.content_width,
            height=table.height,
        )

        self.play(
            self.set_title_row(title="Initial Literature Search", seperator=": ", subtitle="most relevant papers"),
            m.AnimationGroup(
                m.AnimationGroup(
                    m.FadeOut(query_box),
                    m.FadeOut(results_box),
                ),
                m.AnimationGroup(
                    m.FadeIn(table_box),
                ),
                lag_ratio=0.5
            )
        )

        animation_group = m.AnimationGroup(
            *[m.FadeIn(elem) for elem in
              [overall_research_question, research_queston1, research_question2]],
            lag_ratio=0.15
        )


        self.play(
            m.FadeOut(table_box),
        )

        self.play(
            self.set_title_row(title="Research Question 2", seperator=": ", subtitle="Designing a Framework"),
            animation_group,
        )

        self.play(
            self.set_title_row(title="Research Question 3", seperator=": ", subtitle="Evaluating the Framework"),
            m.FadeIn(research_question3),
        )

        self.wait(0.1)
        self.fade_out_scene()







if __name__ == '__main__':
    ExposeDesignScientificGoal.save_sections_without_cache()