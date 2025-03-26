import manim as m
import numpy as np
from networkx.algorithms.bipartite.basic import color
from pyrr.rectangle import height

from color_theme.carolus.corolus_theme import CarolusTheme
from components.axes_utils import AxesUtils
from components.gantt_utils import GanttUtils
from components.uml_utils import UmlUtils
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class ExposeTimeline(UmlUtils, CarolusTheme, AxesUtils, GanttUtils, MinimalSlideTemplate):
    index_prefix = "H"

    font_name = "IosevkaTermSlab Nerd Font Mono"

    subtitle_color = CarolusTheme.font_color_secondary
    title_seperator_color = CarolusTheme.blue_bright


    text_scale = 0.4

    def construct(self):


        rect_width = (self.content_width - self.med_large_buff) / 2

        overlay_publications = self.rectangle(
            width=rect_width,
            height=6,
        )

        publications_title = self.term_text("Publications")
        publications_title.scale(0.75)

        title_rect_publications = self.rectangle(
            width=rect_width,
            height=self.term_text("█").scale(0.75).height + self.small_buff,
            color=self.blue,
            fill_opacity=1.0,
            fill_color=self.blue,
            stroke_color=self.blue,
        )

        title_rect_publications.next_to(overlay_publications.get_top(), m.DOWN, buff=0)

        publications_title.next_to(title_rect_publications.get_top(), m.DOWN, buff=self.small_buff)

        text_block_pub = """2025-Q1  Analysis of Optimization of
_________Gymnasium Environments using 
_________low-level Programming Languages
_________
2025-Q3  Systematic Literature Review of 
_________Size-Agnostic MCTS and RL 
_________Approaches
_________
2025-Q4  Meta-Heuristic Library for the 
_________Optimization of Gymnasium 
_________Environments
_________
2026-Q2  Framework for Size-Agnostic MCTS
"""
        t2c = {
            '2025-Q1': self.font_color_secondary,
            '2025-Q3': self.font_color_secondary,
            '2025-Q4': self.font_color_secondary,
            '2026-Q2': self.font_color_secondary,
            '_________': self.background_color_bright,
        }

        publications_text = self.term_text(
            t=text_block_pub,
            v_buff=self.small_buff * 1.25,
            font_size=48,
            t2c=t2c
        )
        publications_text.scale(self.text_scale)

        publications_text.next_to(title_rect_publications, m.DOWN, buff=self.med_small_buff, aligned_edge=m.LEFT)
        publications_text.shift(m.RIGHT * self.med_small_buff)


        publications_group = m.VGroup(
            overlay_publications,
            title_rect_publications,
            publications_title,
            publications_text
        )

        publications_group.to_edge(m.LEFT, buff=self.med_large_buff)



        overlay_dissertation_process = self.rectangle(
            width=rect_width,
            height=6,
        )

        dissertation_process_title = self.term_text("Dissertation Process")
        dissertation_process_title.scale(0.75)

        title_rect_dissertation_process = self.rectangle(
            width=rect_width,
            height=self.term_text("█").scale(0.75).height + self.small_buff,
            color=self.blue,
            fill_opacity=1.0,
            fill_color=self.blue,
            stroke_color=self.blue,
        )

        title_rect_dissertation_process.next_to(overlay_dissertation_process.get_top(), m.DOWN, buff=0)

        dissertation_process_title.next_to(title_rect_dissertation_process.get_top(), m.DOWN, buff=self.small_buff)

        text_block = """2024-Q2  Dissfahrt
_________
2024-Q2  1st Dissertation Presentation
_________
2024-Q4  Expose
_________
2025-Q4  2nd Dissertation Presentation
_________
2026-Q2  Disskolloquium
_________
2026-Q4  Dissertation Submission
_________
2027-Q2  Presentation and Examination"""

        t2c = {
            '2024-Q2': self.font_color_secondary,
            '2024-Q4': self.font_color_secondary,
            '2025-Q4': self.font_color_secondary,
            '2026-Q2': self.font_color_secondary,
            '2026-Q4': self.font_color_secondary,
            '2027-Q2': self.font_color_secondary,
            '_________': self.background_color_bright,
        }

        diss_process_text = self.term_text(
            t=text_block,
            v_buff=self.small_buff * 1.25,
            font_size=48,
            t2c=t2c
        )
        diss_process_text.scale(self.text_scale)

        diss_process_text.next_to(title_rect_dissertation_process, m.DOWN, buff=self.med_small_buff, aligned_edge=m.LEFT)
        diss_process_text.shift(m.RIGHT * self.med_small_buff)

        dissertation_process_group = m.VGroup(
            overlay_dissertation_process,
            title_rect_dissertation_process,
            dissertation_process_title,
            diss_process_text
        )

        dissertation_process_group.to_edge(m.RIGHT, buff=self.med_large_buff)



        self.play(
            self.set_title_row(title="Timeline"),
            m.FadeIn(dissertation_process_group),
            m.FadeIn(publications_group),
        )

        self.wait(0.1)
        self.fade_out_scene()



if __name__ == '__main__':
    ExposeTimeline.save_sections_without_cache()