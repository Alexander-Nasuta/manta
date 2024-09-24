import manim as m

from color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from slide_templates.minimal.minimal_intro_slide import MinimalIntroSlide

import manta.docbuild.image_path_utils as paths


class ExampleIntroSlideWithImages(MinimalIntroSlide):
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

    title = "Coalas"
    subtitle = "Tree-Hugging Heroes and Their Amazing Eucalyptus World!"
    subtitle_color = CatppuccinMochaTheme.rosewater

    def construct(self):
        self.play(
            self.fade_in_slide()
        )

        self.wait(2)

        # an alternative to self.fade_out_scene()
        # instead of fading out the scene, we can just play the overlay scene with a rectangle with a fill_color that
        # matches the background color of the scene
        self.play(self.overlay_scene())


if __name__ == '__main__':
    ExampleIntroSlideWithImages.render_video_medium()
