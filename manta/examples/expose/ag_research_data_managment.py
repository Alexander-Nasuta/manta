import manim as m
import numpy as np
from pyrr.rectangle import height

from color_theme.carolus.corolus_theme import CarolusTheme
from components.axes_utils import AxesUtils
from components.gantt_utils import GanttUtils
from components.uml_utils import UmlUtils
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class ExposeResearchDataManagement(UmlUtils, CarolusTheme, AxesUtils, GanttUtils, MinimalSlideTemplate):
    index_prefix = "G"

    font_name = "IosevkaTermSlab Nerd Font Mono"

    subtitle_color = CarolusTheme.font_color_secondary
    title_seperator_color = CarolusTheme.blue_bright

    def step_polygon(
            self,
            text:str,
            polygon_color=None,
            polygon_kwargs=None,
            **kwargs,
    ):
        if polygon_kwargs is None:
            polygon_kwargs = {}
        x = 1.25
        x_plus = 0.5
        y = 0.325
        position_list = [
            [x,y,0],
            [x+x_plus,0,0],
            [x,-y,0],
            [-x,-y,0],
            [-x+x_plus,0,0],
            [-x,y,0],
        ]
        step_polygon = m.Polygon(
            *position_list,
            color=polygon_color,
            fill_color=polygon_color,
            fill_opacity=1.0,
            **polygon_kwargs)
        step_polygon.move_to(m.ORIGIN)


        # use hidden character to align text
        # the baseline of the text is not aligned with other text if one the text has characters like g or y and
        # the other not
        _hidden_character = "█"
        print_text = text.replace("\n", f"{_hidden_character}\n") + _hidden_character
        step_text = self.term_text(print_text, **kwargs)
        res_text = m.VGroup()
        for text_row in step_text:
            res_text.add(text_row[:-1])


        return m.VGroup(step_polygon, res_text)


    def rdm_element(
            self,
            text: str,
            color=None,
            width=None,
            body_text_group = m.VGroup | m.Text,
            height=None,
            **kwargs
    ):
        if color is None:
            color = self.blue

        if width is None:
            width = (self.content_width - 2 * self.med_large_buff) / 3

        if height is None:
            height = 2

        background_rect = m.Rectangle(
            width=width,
            height=height,
            color=self.outline_color,
            fill_color=self.background_color_bright,
            fill_opacity=1.0,
        )
        title_rect = m.Rectangle(
            width=width,
            height=self.term_text("█").scale(0.6).height +  self.small_buff,
            color=color,
            stroke_color=color,
            fill_color=color,
            fill_opacity=1.0,
        )
        title_rect.next_to(background_rect.get_top(), m.DOWN, buff=0, aligned_edge=m.UP)

        title_text = self.term_text(text, font_color=self.font_color)
        title_text.scale(0.6)

        title_text.next_to(background_rect.get_top(), m.DOWN, buff=self.small_buff)

        body_text_group.next_to(title_rect, m.DOWN, buff=self.small_buff, aligned_edge=m.LEFT)
        body_text_group.shift(m.RIGHT * self.med_small_buff)

        return m.VGroup(background_rect, title_rect, title_text, body_text_group)




    def construct(self):
        planning_step = self.step_polygon(
            text="Planning",
            polygon_color=self.blue,
        )
        production_step = self.step_polygon(
            text="Production",
            polygon_color=self.green,
        )
        analysis_step = self.step_polygon(
            text="Analysis",
            polygon_color=self.green_bright,
        )
        storage_step = self.step_polygon(
            text="Storage",
            polygon_color=self.yellow,
        )
        access_step = self.step_polygon(
            text="Access",
            polygon_color=self.red,
        )
        reuse_step = self.step_polygon(
            text="Re-Use",
            polygon_color=self.magenta,
        )



        steps_group = m.VGroup(
            planning_step,
            production_step,
            analysis_step,
            storage_step,
            access_step,
            reuse_step,
        )
        steps_group.arrange(m.RIGHT, buff=-0.3)

        steps_group.scale_to_fit_width(self.content_width)
        steps_group.to_edge(m.DOWN, buff=0.625)

        rect_width = (self.content_width - 2 * self.med_large_buff) / 3


        wzl_internal_text = self.term_text("WZL Internal").scale(0.75)
        wzl_internal_text.to_edge(m.UP, buff=0.85)
        wzl_internal_text.shift(m.LEFT * (rect_width + self.med_large_buff))

        rwth_internal_text = self.term_text("RWTH Internal").scale(0.75)
        rwth_internal_text.to_edge(m.UP, buff=0.85)

        external_text = self.term_text("External").scale(0.75)
        external_text.to_edge(m.UP, buff=0.85)
        external_text.shift(m.RIGHT * (rect_width + self.med_large_buff))

        scope_text_group = m.VGroup(
            wzl_internal_text,
            rwth_internal_text,
            external_text,
        )

        RWTH_publications_text_body = self.bullet_point_list(
            bulletpoints=[
                "Dissertation\ndocument",
            ],
            bullet_icon_color=self.red,
        ).scale(0.5)

        RWTH_publications = self.rdm_element(
            text="RWTH Publications (Open Access)",
            color=[self.red],
            body_text_group=RWTH_publications_text_body,
            height=0.9
        )

        rwth_publications_logo = m.ImageMobject("resources/ub.png").scale_to_fit_height(0.4)
        rwth_publications_logo.next_to(RWTH_publications_text_body, m.RIGHT, buff=self.small_buff)
        rwth_publications_logo.align_to(RWTH_publications[1], m.RIGHT).shift(m.LEFT * self.med_small_buff)

        RWTH_publications = m.Group(*RWTH_publications, rwth_publications_logo)

        institute_drive_text_body = self.titled_bulletpoints(
            titled_bulletpoints=[(
                "Folder with:",
                [
                    "Data Management Plans (DMPs) for each sub-activity",
                    "Dissertation document incl. source code",
                    "Associated publications\nincl. raw data, source code etc.",
                    "Other raw data, source code etc.",
                    "Documentation of the dissertation project",
                ]
            )
            ],
        ).scale(0.5)

        institute_drive = self.rdm_element(
            text="Institute Drive",
            color=self.yellow,
            body_text_group=institute_drive_text_body,
            height=2.25,
        )

        institute_drive.next_to(RWTH_publications, m.LEFT, buff=self.med_large_buff, aligned_edge=m.UP)



        zenodo_text_body = self.bullet_point_list(
            bulletpoints=[
                "Data Management Plans (DMPs)\n for each subactivity",
                "Dissertation document as PDF",
                "Selected raw data",
                "Selected source code",
            ],
            bullet_icon_color=self.red,
        ).scale(0.5)

        zenodo = self.rdm_element(
            text="Zenodo (Open Access)",
            color=[self.red, self.yellow],
            body_text_group=zenodo_text_body,
            height=2.25
        )

        zenodo_logo = m.SVGMobject("resources/zenodo2.svg", color=self.red).scale_to_fit_height(0.4)
        zenodo_logo.next_to(zenodo.get_bottom(), m.UP, buff=self.small_buff)
        zenodo_logo.set_color([self.red, self.yellow])

        zenodo.add(zenodo_logo)

        zenodo.next_to(RWTH_publications, m.RIGHT, buff=self.med_large_buff, aligned_edge=m.UP)


        coscine_text_body = self.bullet_point_list(
            bulletpoints=[
                "Data Management Plans (DMPs)",
                "Dissertation document incl. source code",
                "Associated publications incl. raw data,\nsource code etc.",
                "Other raw data, source code etc.",
                "Documentation of the dissertation project",
            ],
        ).scale(0.5)

        coscine = self.rdm_element(
            text="Coscine",
            color=self.yellow,
            body_text_group=coscine_text_body,
            height=2.0
        )

        coscine_logo = m.ImageMobject("resources/rwth_coscine_rgb.png", color=self.yellow)
        coscine_logo.scale_to_fit_height(coscine[1].height - 0.1)

        coscine_logo.next_to(coscine[1].get_right(), m.LEFT, buff=self.small_buff)

        coscine = m.Group(*coscine, coscine_logo)

        coscine.next_to(RWTH_publications, m.DOWN, buff=self.med_large_buff)



        RDMO_text_body = self.bullet_point_list(
            bulletpoints=[
                "Data Management Plans (DMPs) for each\nsubactivity",
            ],
            bullet_icon_color=self.blue,
        ).scale(0.5)

        RDMO = self.rdm_element(
            text="RDMO",
            color=self.blue,
            body_text_group=RDMO_text_body,
            height=0.9
        )

        RDMO_logo = m.ImageMobject("resources/rdmo-logo.png").scale_to_fit_height(0.4)
        RDMO_logo.next_to(RDMO_text_body, m.RIGHT, buff=self.small_buff)
        RDMO_logo.align_to(RDMO[1], m.RIGHT).shift(m.LEFT * self.med_small_buff)

        RDMO = m.Group(*RDMO, RDMO_logo)

        RDMO.next_to(RWTH_publications, m.UP, buff=self.med_large_buff)


        institute_gitlab_body = self.bullet_point_list(
            bulletpoints=[
                "Source code of demonstrators",
                "Source code for data processing",
            ],
            bullet_icon_color=self.green,
        ).scale(0.5)

        institute_gitlab = self.rdm_element(
            text="Institute GitLab",
            color=[self.yellow, self.green],
            body_text_group=institute_gitlab_body,
            height=1.0
        )


        institute_gitlab.next_to(institute_drive, m.DOWN, buff=self.large_buff)

        internal_gitlab_symbol = self.symbol("gitlab#1", color=self.green)
        internal_gitlab_symbol.set_color([self.yellow, self.green])
        internal_gitlab_symbol.next_to(institute_gitlab_body, m.RIGHT)
        internal_gitlab_symbol.align_to(institute_drive, m.RIGHT).shift(m.LEFT * self.med_small_buff)

        institute_gitlab = m.VGroup(*institute_gitlab, internal_gitlab_symbol)


        public_gitlab_body = self.bullet_point_list(
            bulletpoints=[
                "Selected source code",
            ],
            bullet_icon_color=self.red,
        ).scale(0.5)

        public_gitlab = self.rdm_element(
            text="Public GitLab (Open Access)",
            color=self.red,
            body_text_group=public_gitlab_body,
            height=1.0
        )

        public_gitlab.next_to(zenodo, m.DOWN, buff=self.large_buff)

        public_gitlab_symbol = self.symbol("gitlab#1", color=self.red)
        public_gitlab_symbol.next_to(internal_gitlab_symbol, m.RIGHT)
        public_gitlab_symbol.align_to(public_gitlab, m.RIGHT).shift(m.LEFT * self.med_small_buff)

        public_gitlab = m.VGroup(*public_gitlab, public_gitlab_symbol)



        readthedocs_text_body = self.bullet_point_list(
            bulletpoints=[
                "Documentation of selected code",
            ],
            bullet_icon_color=self.red,
        ).scale(0.5)

        readthedocs = self.rdm_element(
            text="Read the Docs (Open Access)",
            color=self.red,
            body_text_group=readthedocs_text_body,
            height=0.9
        )

        readtheDocs_logo = m.SVGMobject("resources/ReadtheDocs.svg").scale_to_fit_height(0.4)
        readtheDocs_logo.set_color(self.red)
        readtheDocs_logo.next_to(readthedocs.get_right(), m.LEFT, buff=self.med_small_buff)
        readtheDocs_logo.shift(m.DOWN * 0.175)

        readthedocs = m.VGroup(*readthedocs, readtheDocs_logo)

        readthedocs.next_to(zenodo, m.UP, buff=self.med_large_buff)


        rdm_elements = m.Group(
            RWTH_publications,
            institute_drive,
            zenodo,
            coscine,
            RDMO,
            institute_gitlab,
            public_gitlab,
            readthedocs,
        )

        rdm_elements.shift(m.UP * 1)


        animation_group = m.AnimationGroup(
            m.AnimationGroup(
                m.FadeIn(planning_step),
                m.FadeIn(RDMO)
            ),
            m.AnimationGroup(
                m.FadeIn(production_step),
                m.FadeIn(institute_gitlab)
            ),
            m.AnimationGroup(
                m.FadeIn(analysis_step),
            ),
            m.AnimationGroup(
                m.FadeIn(storage_step),
                m.FadeIn(institute_drive),
                m.FadeIn(coscine),
                m.FadeIn(zenodo)
            ),
            m.AnimationGroup(
                m.FadeIn(access_step),
                m.FadeIn(public_gitlab),
                m.FadeIn(readthedocs),
                m.FadeIn(RWTH_publications)
            ),
            m.AnimationGroup(
                m.FadeIn(reuse_step),
            ),
            lag_ratio=0.1
        )


        self.play(
            self.set_title_row(title="Research Data Management"),
        m.FadeIn(scope_text_group),
            animation_group,
        )

        self.wait(0.1)
        self.fade_out_scene()






if __name__ == '__main__':
    ExposeResearchDataManagement.save_sections_without_cache()