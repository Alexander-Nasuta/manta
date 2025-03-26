import manim as m

from manta.color_theme.carolus.corolus_theme import CarolusTheme
from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from manta.slide_templates.minimal.minimal_intro_slide import MinimalIntroSlide

import manta.docbuild.image_path_utils as paths

class ExposeOutro(CarolusTheme, MinimalIntroSlide):

    font_name = "IosevkaTermSlab Nerd Font Mono"

    title = "Thank you for your attention!"

    # replace 'paths.get_coala_background_abs_path()' with a string path to a background image
    # this can be a relative path or an absolute path
    background_picture = "background_title.jpg"
    background_shift = m.UP * 0.75  + m.RIGHT * 3
    background_scale = 2.0  # make the background a bit bigger

    logo_paths = [
        "wzl.svg"
    ]

    def construct(self):
        self.play(
            self.fade_in_slide(
                title_kwargs={
                    "font_size": self.font_size_large
                },
                subtitle_kwargs={
                    "font_size": self.font_size_small
                }
            )
        )


if __name__ == '__main__':
    ExposeOutro.save_sections_without_cache()