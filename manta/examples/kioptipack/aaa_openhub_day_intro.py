import manim as m

from color_theme.carolus.corolus_theme import CarolusTheme
from examples.kioptipack.KIOptipack_theme import OptiPackTheme
from manta.slide_templates.minimal.minimal_intro_slide import MinimalIntroSlide


class OpenHubDayDatenraumIntro(CarolusTheme, MinimalIntroSlide):

    title = "Semantischer Datenraum"
    subtitle = "Intelligentes Netzwerk zur Verknüpfung und übergreifendenden\n Nutzung von Daten"
    subtitle_color = CarolusTheme.red

    # replace 'paths.get_coala_background_abs_path()' with a string path to a background image
    # this can be a relative path or an absolute path
    background_picture = "resources/Intro_background_carl.svg"
    background_shift = m.UP * 0.75  # shift the background a bit up
    background_scale = 1.05  # make the background a bit bigger

    logo_paths = [
        "resources/BMBF_Logo_carl.svg",
        "resources/BMBF_FONA_Logo_de_carl.svg",
    ]

    def construct(self):

        optipack_logo = m.SVGMobject("resources/logo-optipack_cat.svg")
        optipack_logo.scale_to_fit_height(self.logo_height*1.5)
        optipack_logo.to_edge(m.UP, buff=self.med_large_buff)
        optipack_logo.to_edge(m.LEFT, buff=self.med_large_buff)
        optipack_logo.set_z_index(10)
        optipack_logo.set_color(self.red)


        animation_group = m.AnimationGroup(
            self.fade_in_slide(
                title_kwargs={
                    "font_size": self.font_size_Large
                },
                subtitle_kwargs={
                    "font_size": self.font_size_large
                }
            ),

        )

        self.play(
            animation_group,
            m.FadeIn(optipack_logo),
            lag_ratio=0.15,
        )

        self.play(self.overlay_scene())

        self.remove_everything()





if __name__ == '__main__':
    #OpenHubDayDatenraumIntro.render_video_medium()
    OpenHubDayDatenraumIntro.save_sections_without_cache()
