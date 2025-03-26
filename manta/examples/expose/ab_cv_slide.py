import manim as m

from manta.color_theme.carolus.corolus_theme import CarolusTheme
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate
from slide_templates.title_slide import TitleSlide


class ExposeCV(CarolusTheme, TitleSlide):

    font_name = "IosevkaTermSlab Nerd Font Mono"

    def construct(self):
        self.play(
            self.set_title_row(
                title="Curriculum Vitae",
            )
        )

        general_info_col_width = 2.25

        n_cols = 3
        h_buff = self.med_large_buff
        v_buff = self.med_large_buff

        col_width = (self.content_width - (general_info_col_width + h_buff) - (n_cols - 1) * h_buff) / n_cols

        picture_rectangle = self.rectangle(
            width=general_info_col_width,
            height=6,
        )
        picture_rectangle.next_to(self._title_mobject, m.DOWN, buff=v_buff, aligned_edge=m.LEFT)

        experience_rectangle = self.rectangle(
            width=col_width,
            height=6,
        )
        experience_rectangle.next_to(picture_rectangle, m.RIGHT, buff=h_buff)

        projects_rectangle = self.rectangle(
            width=col_width,
            height=6,
        )
        projects_rectangle.next_to(experience_rectangle, m.RIGHT, buff=h_buff)

        rest_rectangle = self.rectangle(
            width=col_width,
            height=6,
        )
        rest_rectangle.next_to(projects_rectangle, m.RIGHT, buff=h_buff)

        rect_group = m.VGroup(
            picture_rectangle,
            experience_rectangle,
            projects_rectangle,
            rest_rectangle,
        )

        self.play(
            m.FadeIn(rect_group)
        )

        picture_circle = self.circle(
            radius=1,
            stroke_color=self.blue,
            stroke_width=5,
            fill_opacity=0.0,
        )
        picture_circle.scale_to_fit_width(general_info_col_width - 2 * 0.25)
        picture_circle.next_to(picture_rectangle.get_top(), m.DOWN, buff=h_buff)

        profile_pic_png = m.ImageMobject("profilbild.png")
        profile_pic_png.scale_to_fit_width(picture_circle.width).scale(1.125)
        profile_pic_png.move_to(picture_circle.get_center())

        name_text = self.term_text("Alexander Nasuta",
                                   color=self.blue,
                                   weight=m.BOLD,
                                   font_size=self.font_size_script
                                   )

        name_text.next_to(picture_circle, m.DOWN, buff=self.med_small_buff)

        position_text = self.term_text("Scientific Researcher", font_size=self.font_size_tiny)
        position_text.next_to(name_text, m.DOWN, buff=self.small_buff)

        genral_info_content = """Laboratory for Machine Tools
and Production Engineering

Intelligence in Quality Sensing

Department:
Data Intelligence

Research Group:
Machine Intelligence
Methodologies

Telephone:
+49 (0) 241 80 91158

E-Mail:
alexander.nasuta
@wzl-iqs.rwth-aachen.de
"""
        t2w = {
            'Laboratory for Machine Tools': m.BOLD,
            'and Production Engineering': m.BOLD,

            'Intelligence in Quality Sensing': m.BOLD,

            'Department:': m.BOLD,
            'Research Group:': m.BOLD,
            'Telephone:': m.BOLD,
            'E-Mail:': m.BOLD,
        }
        t2c = {
            'Department': self.yellow,
            'Research Group': self.yellow,
            'Telephone': self.yellow,
            'E-Mail': self.yellow,
        }
        general_info_block = self.term_text(
            genral_info_content,
            font_size=48,
            t2c=t2c,
            t2w=t2w,
        ).scale(0.18)

        general_info_block.next_to(picture_rectangle.get_corner(m.DL), m.UP, buff=self.small_buff, aligned_edge=m.LEFT)
        general_info_block.shift(m.RIGHT * self.small_buff)

        general_info_group = m.VGroup(
            # picture_circle,
            name_text,
            position_text,
            general_info_block,
        )

        def sub_group(icon: str | int, title: str, text_block: str, **kwargs) -> m.VGroup:
            SECTION_BACKGROUND_COLOR = self.blue
            SECTION_FONT_COLOR = self.yellow
            SECTION_TEXT_BUFF = self.small_buff
            SECTION_TEXT_SCALE =  0.275
            SECTION_HEIGHT = 0.5
            ICON_BACKGROUND_COLOR = self.blue

            TEXT_BODY_SCALE = 0.19125
            TEXT_BODY_COLOR = self.font_color
            TEXT_BODY_V_BUFF = self.small_buff * 1.25
            TEXT_BODY_H_BUFF = self.small_buff

            seperator_rect = self.rectangle(
                width=col_width,
                height=SECTION_HEIGHT,
                fill_color=SECTION_BACKGROUND_COLOR,
            )

            seperator_icon_rect = self.rectangle(
                width=SECTION_HEIGHT,
                height=SECTION_HEIGHT,
                fill_color=ICON_BACKGROUND_COLOR,
            )

            seperator_icon_rect.next_to(seperator_rect.get_left(), m.RIGHT, buff=0)

            seperator_icon = self.symbol(
                icon,
                color=SECTION_FONT_COLOR,
                font_size=48,
            ).scale(SECTION_TEXT_SCALE)
            seperator_icon.move_to(seperator_icon_rect)

            seperator_text = self.term_paragraph(
                title,
                #color=SECTION_FONT_COLOR,
                font_size=48,
            ).scale(SECTION_TEXT_SCALE)
            seperator_text.next_to(seperator_icon_rect, m.RIGHT, buff=SECTION_TEXT_BUFF)

            seperator_group = m.VGroup(
                seperator_rect,
                seperator_icon_rect,
                seperator_icon,
                seperator_text
            )

            text_block = self.term_text(
                text_block,
                v_buff=self.small_buff * 1.25,
                font_size=48,
                **kwargs
            ).scale(TEXT_BODY_SCALE).next_to(seperator_group, m.DOWN, buff=TEXT_BODY_V_BUFF, aligned_edge=m.LEFT).shift(
                m.RIGHT * TEXT_BODY_H_BUFF)

            return m.VGroup(
                seperator_group,
                text_block
            )

        v_buff_between_groups = self.med_small_buff

        professional_experience_group = sub_group(
            icon="briefcase-account-outline",
            title="Professional Experience",
            text_block="""Since  2022  Scientific Researcher  WZL-IQS
2019 - 2022  Student Research       IMA
_____________Assistant                        
2018 - 2019  Internship             Schaeffler
2017 - 2018  Student Research       IMA       
_____________Assistant                        
2016 - 2017  Student Research       AVT.BioVT 
_____________Assistant                        
2016         Student Research       IMA       
_____________Assistant""",
            t2c={
                '2016': self.font_color_secondary,
                '2017': self.font_color_secondary,
                '2018': self.font_color_secondary,
                '2019': self.font_color_secondary,
                '2022': self.font_color_secondary,
                'Since': self.font_color_secondary,
                'IMA': self.font_color_secondary,
                'WZL': self.font_color_secondary,
                'IQS': self.font_color_secondary,
                'Schaeffler': self.font_color_secondary,
                'AVT.BioVT': self.font_color_secondary,
                '-': self.font_color_secondary,
                '󰧟': self.font_color_secondary,
                '󰧞': self.font_color_secondary,
                "_____________": self.background_color_bright,
            }
        )
        professional_experience_group.next_to(experience_rectangle.get_top(), m.DOWN, buff=0)

        education_group = sub_group(
            icon="school-outline",
            title="Education",
            text_block="""Since  2022  PhD Student            RWTH Aachen
2020 - 2022  Automation Engineering RWTH Aachen
_____________M.Sc. ",
2014 - 2020  Mechanical Engineering RWTH Aachen
_____________B.Sc.""",
            t2c={
                '2014': self.font_color_secondary,
                '2020': self.font_color_secondary,
                '2022': self.font_color_secondary,
                'Since': self.font_color_secondary,

                'RWTH': self.font_color_secondary,
                'Aachen': self.font_color_secondary,

                '-': self.font_color_secondary,
                '󰧟': self.font_color_secondary,
                '󰧞': self.font_color_secondary,
                "_____________": self.background_color_bright,
            }
        )
        education_group.next_to(professional_experience_group, m.DOWN, buff=v_buff_between_groups)

        voluntary_group = sub_group(
            icon="hand-heart-outline",
            title="Voluntary Work",
            text_block="""Since  2015  Member                KHG-Chor
        Since  2017  Member                AEGEE-Aachen""",
            t2c={
                'Since': self.font_color_secondary,
                '2015': self.font_color_secondary,
                '2017': self.font_color_secondary,
                'KHG-Chor': self.font_color_secondary,
                'AEGEE-Aachen': self.font_color_secondary,
                '󰧟': self.font_color_secondary,
                '󰧞': self.font_color_secondary,
                "_____________": self.background_color_bright,
            }
        )
        voluntary_group.next_to(education_group, m.DOWN, buff=v_buff_between_groups)

        # projects rectangle content
        public_projects_group = sub_group(
            icon="building_columns",
            title="Publicly Funded Projects",
            text_block="""FAIRWork: Fair Production Planning using
                  _󰧟 Reinforcement Learning
                  _󰧟 Monte Carlo Tree Search
                  _󰧟 Constraint Programming
                
                KIOptiPack: Holistic AI-based optimization of 
                plastic packaging with recycled content
                  _󰧟 Packaging Processes
                  _󰧟 Production Planning
                
                OptiPro: AI-based optimization of production
                planning in the automotive industry
                _󰧟 Production Planning
                _󰧟 Machine Learning
                
                Internet of Production: Job Shop Production
                Planning  using
                _󰧟 Reinforcement Learning
                _󰧟 Monte Carlo Tree Search
                """,
            t2w={
                'FAIRWork': m.BOLD,
                'KIOptiPack': m.BOLD,
                'OptiPro': m.BOLD,
                'Internet of Production:': m.BOLD,
            },
            t2c={
                'FAIRWork': self.yellow,
                'KIOptiPack': self.yellow,
                'OptiPro': self.yellow,
                'Internet of Production:': self.yellow,
                '󰧟': self.yellow,
                '󰧞': self.yellow,
                '_': self.background_color_bright,
            }
        )
        public_projects_group.next_to(projects_rectangle.get_top(), m.DOWN, buff=0)

        industry_projects_group = sub_group(
            icon="factory",
            title="Industry Projects",
            text_block="""Siemens Kurzschlusslabor:
                  _󰧟 Development of a SQL Data Model for the
                  __Short Circuit Testing Facility
                  _󰧟 Migration of a Reference Dataset into a
                  __Reference Database""",
            t2w={
                'Siemens Kurzschlusslabor:': m.BOLD,
            },
            t2c={
                'Siemens Kurzschlusslabor:': self.yellow,
                '󰧟': self.yellow,
                '󰧞': self.yellow,
                '_': self.background_color_bright,
            }
        )
        industry_projects_group.next_to(public_projects_group, m.DOWN, buff=v_buff_between_groups)

        # rest rectangle content
        aquisitions_group = sub_group(
            icon="account-cash",
            title="Aquisitions",
            text_block="""Submitted Aquisitions
                  _󰧟 2024: AIXchemistry (DFG SPP 2331)""",
            t2w={
                'Submitted Aquisitions': m.BOLD,
            },
            t2c={
                'Submitted Aquisitions': self.yellow,
                '󰧟': self.yellow,
                '󰧞': self.yellow,
                '_': self.background_color_bright,
            }
        )
        aquisitions_group.next_to(rest_rectangle.get_top(), m.DOWN, buff=0)

        teaching_group = sub_group(
            icon="school",
            title="Teaching",
            text_block="""Advanced Software Engineering
                  _󰧟 Conducting exercises
                  _󰧟 Lecturing
                  _󰧟 Creating Exam Questions
                  _󰧟 Correcting Exams
                
                Informatik im Maschinenbau I
                  _󰧟 Tutoring
                  _󰧟 Correcting Exams
                
                Summer Schools
                  _󰧟 Lecturing
                  _󰧟 Content creation""",
            t2w={
                'Advanced Software Engineering': m.BOLD,
                'Informatik im Maschinenbau I': m.BOLD,
                'Summer Schools': m.BOLD,
            },
            t2c={
                'Advanced Software Engineering': self.yellow,
                'Informatik im Maschinenbau I': self.yellow,
                'Summer Schools': self.yellow,
                '󰧟': self.yellow,
                '󰧞': self.yellow,
                '_': self.background_color_bright,
            }
        )
        teaching_group.next_to(aquisitions_group, m.DOWN, buff=v_buff_between_groups)

        publications_group = sub_group(
            icon="book",
            title="Publications",
            text_block="""4 Publications
            _󰧟 2 of which as first author
            _󰧟 1 of which pending (submitted)""",
            t2w={
            },
            t2c={
                '󰧟': self.yellow,
                '󰧞': self.yellow,
                '_': self.background_color_bright,
                '_': self.background_color_bright,
            }
        )
        publications_group.next_to(teaching_group, m.DOWN, buff=v_buff_between_groups)

        self.play(
            m.FadeIn(profile_pic_png),
            m.FadeIn(picture_circle),
            m.FadeIn(general_info_group),
            m.FadeIn(professional_experience_group),
            m.FadeIn(education_group),
            m.FadeIn(voluntary_group),
            m.FadeIn(public_projects_group),
            m.FadeIn(industry_projects_group),
            m.FadeIn(aquisitions_group),
            m.FadeIn(teaching_group),
            m.FadeIn(publications_group),
        )

        self.wait(0.1)
        self.fade_out_scene()


if __name__ == '__main__':
    ExposeCV.save_sections_without_cache()