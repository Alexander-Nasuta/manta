import manim as m
import numpy as np

from manta.font_style.IosevkaTerm_base_24 import LatexFontSizing24
from manta.slide_templates.logo_slide import LogoSlide


class ClassicIntroSlide(LatexFontSizing24, LogoSlide):
    background_picture = None
    background_scale: float = 1.0
    background_shift: np.ndarray = np.array([0, 0, 0])

    overlay_height = 2.75
    overlay_color = None

    logo_paths = []
    logo_height = 0.5

    title = ""
    title_v_buff: float = None
    title_h_buff: float = None
    title_shift: np.ndarray = np.array([0, 0, 0])

    subtitle = ""
    subtitle_v_buff: float = None
    subtitle_h_buff: float = None
    subtitle_shift: np.ndarray = np.array([0, 0, 0])

    def fade_in_slide(self, lag_ratio=0.15, lag_ratio_background_img = 0.6) -> m.AnimationGroup:
        if self.background_picture is None:
            background_image = self.rectangle(width=self.scene_width, height=9, color=self.blue, fill_opacity=0.5)
        elif self.background_picture.endswith(".svg") or self.background_picture.endswith(".SVG"): # case: .svg format
            background_image = m.SVGMobject(self.background_picture)
        else:
            background_image = m.ImageMobject(self.background_picture)

        background_image.scale_to_fit_width(self.scene_width)
        background_image.to_edge(m.UP, buff=0)
        background_image.scale(self.background_scale)
        background_image.shift(self.background_shift)

        overlay_rect = m.Rectangle(
            width=self.scene_width,
            height=self.overlay_height,
            color=self.background_color_bright if self.overlay_color is None else self.overlay_color,
            fill_opacity=1
        )
        overlay_rect.to_edge(m.DOWN, buff=0.0)

        title_v_buff = self.med_small_buff if self.title_v_buff is None else self.title_v_buff
        title_h_buff = self.med_large_buff if self.title_h_buff is None else self.title_h_buff

        title_mobject = self.term_text(self.title, font_size=self.font_size_LARGE)
        title_mobject.next_to(overlay_rect.get_top(), m.DOWN, buff=title_v_buff)
        title_mobject.to_edge(m.LEFT, buff=title_h_buff)
        title_mobject.shift(self.title_shift)

        subtitle_v_buff = self.med_small_buff if self.subtitle_v_buff is None else self.subtitle_v_buff
        subtitle_h_buff = self.med_large_buff if self.subtitle_h_buff is None else self.subtitle_h_buff

        subtitle_mobject = self.term_text(self.subtitle, font_size=self.font_size_large)
        subtitle_mobject.next_to(title_mobject, m.DOWN, buff=subtitle_v_buff)
        subtitle_mobject.to_edge(m.LEFT, buff=subtitle_h_buff)
        subtitle_mobject.shift(self.subtitle_shift)

        background_image.set_z_index(0)
        overlay_rect.set_z_index(1)
        title_mobject.set_z_index(2)
        subtitle_mobject.set_z_index(3)

        add_logo_animation = self.add_logos(),
        self.logos.set_z_index(4)

        overlay_group = m.AnimationGroup(
            m.FadeIn(overlay_rect, ),
            m.FadeIn(title_mobject),
            m.FadeIn(subtitle_mobject),
            add_logo_animation,
            lag_ratio=lag_ratio
        ) if self.logo_paths else m.AnimationGroup(
            m.FadeIn(overlay_rect),
            m.FadeIn(title_mobject),
            m.FadeIn(subtitle_mobject),
            lag_ratio=lag_ratio
        )

        complete_group = m.AnimationGroup(
            overlay_group,
            m.FadeIn(background_image),
            lag_ratio=lag_ratio_background_img
        )

        return complete_group

    def construct(self):
        pass


class TestIntroSlide(ClassicIntroSlide):
    title = "Title 1337"
    subtitle = "Subtitle row 1 \n Subtitle row 2"

    def construct(self):
        self.play(
            self.fade_in_slide()
        )


class TestIntroSlideWithPictures(ClassicIntroSlide):
    # https://commons.wikimedia.org/wiki/File:Coala_background.svg
    background_picture = "../../../resources/background/Coala_background.svg"
    logo_paths = ["../../../resources/logos/Manim_icon.svg", "../../../resources/logos/logo.png"]
    background_shift = np.array([0, 1, 0]) # shift the background image 1 unit up

    title = "Coalas are Cool"
    subtitle = ("The koala is an arboreal herbivorous marsupial native to Australia. \n"
                "https://commons.wikimedia.org/wiki/File:Coala_background.svg")

    def construct(self):
        self.play(
            self.fade_in_slide()
        )


if __name__ == '__main__':
    TestIntroSlideWithPictures.render_video_medium()
