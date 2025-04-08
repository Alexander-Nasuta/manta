import manim as m

from color_theme.rwth.rwth_theme import RwthTheme
from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from manta.slide_templates.minimal.minimal_intro_slide import MinimalIntroSlide

import manta.docbuild.image_path_utils as paths

class GIopOutro(RwthTheme, MinimalIntroSlide):


    title = "Thank you for your attention!"
    title_color = RwthTheme.rwth_blau_100
    subtitle = "Alexander Nasuta & Calvin Kuhn"
    subtitle_color = RwthTheme.rwth_blau_75

    # font_name = "SauceCodePro Nerd Font Mono"

    # replace 'paths.get_coala_background_abs_path()' with a string path to a background image
    # this can be a relative path or an absolute path
    background_picture = "iop_background.jpeg"
    background_shift = m.UP * 0.75  # shift the background a bit up
    background_scale = 1.05  # make the background a bit bigger

    logo_paths = [
        "iop_logo.png"
    ]
    logo_height = 0.75

    def construct(self):
        self.play(
            self.fade_in_slide(
                title_kwargs={
                    "font_size": 24,
                },
                subtitle_kwargs={
                    "font_size": 22,
                }
            )
        )

        self.play(self.overlay_scene())

if __name__ == '__main__':
    GIopOutro.save_sections_without_cache()