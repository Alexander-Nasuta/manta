import manim as m

from color_theme.carolus.corolus_theme import CarolusTheme
from examples.kioptipack.KIOptipack_theme import OptiPackTheme
from manta.slide_templates.minimal.minimal_intro_slide import MinimalIntroSlide


class OpenHubDayIntro(CarolusTheme, MinimalIntroSlide):

    title = "Integration und Modellmanagement leicht gemacht"
    subtitle = "Der Weg zur datengetriebenen Kunststoffproduktion"
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
        wzl_logo = m.SVGMobject("resources/wzl.svg")
        wzl_logo.scale_to_fit_height(self.logo_height)
        wzl_logo.to_edge(m.DOWN, buff=self.med_small_buff)
        wzl_logo.to_edge(m.LEFT, buff=self.med_large_buff)
        wzl_logo.set_z_index(10)
        #wzl_logo.set_color(self.blue)

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
            m.AnimationGroup(
                m.FadeIn(wzl_logo),
                m.FadeIn(optipack_logo),
            ),
            lag_ratio=0.15
        )

        author_box = self.term_text("Alexander Nasuta & Sylwia Olbrych", font_size=self.font_size_normal, font_color=self.font_color_secondary)

        author_box.to_edge(m.LEFT, buff=self.med_large_buff)
        author_box.to_edge(m.DOWN, buff=1.2)
        author_box.set_z_index(20)

        self.play(
            animation_group,
            m.FadeIn(author_box)
        )

        self.play(self.overlay_scene())

        self.remove_everything()





if __name__ == '__main__':
    #OpenHubDayIntro.render_video_medium()
    OpenHubDayIntro.save_sections_without_cache()
