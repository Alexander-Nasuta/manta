from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate
from manta.slide_templates.minimal.minimal_intro_slide import MinimalIntroSlide

import manim as m

from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from manta.slide_templates.minimal.minimal_intro_slide import MinimalIntroSlide

import manta.docbuild.image_path_utils as paths


class QuickstartIntroSlide(MinimalIntroSlide):
    # replace 'paths.get_coala_background_abs_path()' with a string path to a background image
    # this can be a relative path or an absolute path
    background_picture = paths.get_coala_background_abs_path()
    background_shift = m.UP * 0.75  # shift the background a bit up
    background_scale = 1.05  # make the background a bit bigger

    logo_paths = [
        # feel free to replace these paths with your own logo paths
        # if your logos is called 'my_logo.svg' and is located in the same directory as this file, you can use
        # 'my_logo.svg' as the path
        paths.get_manim_logo_abs_path(),
        paths.get_manta_logo_abs_path()
    ]

    title = "Manta"
    subtitle = "A Framework for creating Presentation Slides \n with Manim and Python"
    subtitle_color = CatppuccinMochaTheme.rosewater

    def construct(self):
        self.play(self.fade_in_slide())
        self.wait(2)
        self.play(self.overlay_scene())
        self.remove_everything()  # remove everything, so that the overlay scene is not shown in the next slide




from manta.slide_templates.title_slide import TitleSlide


class QuickstartAgenda(TitleSlide):

    def construct(self):
        self.play(
            self.set_title_row(
                title="Agenda",
                seperator=": ",
                subtitle="Mantas Key Features"
            ),
        )

        agenda_point_a = self.icon_textbox(
            text="Components",
            icon='alpha-a-box-outline',
            width=self.content_width,
        )
        agenda_point_a.to_edge(m.UP, buff=1.0)

        agenda_point_b = self.icon_textbox(
            text="Icons",
            icon='alpha-b-box-outline',
            width=self.content_width,
        )
        agenda_point_b.next_to(agenda_point_a, m.DOWN, buff=self.med_large_buff)

        agenda_point_c = self.icon_textbox(
            text="QR codes",
            icon='alpha-c-box-outline',
            width=self.content_width,
        )
        agenda_point_c.next_to(agenda_point_b, m.DOWN, buff=self.med_large_buff)

        animation_group = m.AnimationGroup(
            *[m.FadeIn(elem) for elem in [agenda_point_a, agenda_point_b, agenda_point_c]],
            lag_ratio=0.15
        )
        self.play(
            animation_group
        )

        # indicate the first a agenda point
        surrounding_rect = m.SurroundingRectangle(
            agenda_point_b,
            corner_radius=0.125, color=self.blue)
        self.play(
            m.Create(surrounding_rect)
        )

        self.wait(1)

        self.play(
            m.FadeOut(surrounding_rect)
        )

        self.fade_out_scene()



class QuickstartComponentsContent(MinimalSlideTemplate):

    def construct(self):
        self.play(
            self.set_title_row(title="Components",),
        )

        agenda_point_a = self.icon_textbox(
            text="Components",
            icon='alpha-a-box-outline',
            width=self.content_width,
        )



class QuickstartExample(MinimalSlideTemplate):

    def construct(self):

        ################################################################################################################
        #
        #   NOTE: this example changes classes dynamically to show different slides
        #         this is not recommended for production code. Use multiple classes instead and create a
        #         presentation using Manim Editor.
        #
        #         This code only changes classes dynamically to be able to show the output in the documentation as
        #         one single video.
        #
        ################################################################################################################

        # Intro Slides
        self.__class__ = QuickstartIntroSlide
        QuickstartIntroSlide.construct(self)

        # Agenda Slides
        self.__class__ = QuickstartComponentsContent
        QuickstartComponentsContent.construct(self)

        # Main Content
        self.__class__ = QuickstartExample


        self.play(
            self.set_title_row(
                title="Lucky Numbers",
            )
        )

        self.play(
            self.change_subtitle("Uncovering the Magic and Math Behind Good Fortune!"),
        )

        self.wait(2) # wait increases the index of the slide



if __name__ == '__main__':
    QuickstartExample.render_video_medium()
