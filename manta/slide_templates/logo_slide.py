import manim as m

from manta.elements.rectangle_utils import RectangleUtils
from manta.slide_templates.base.base_colored_slide import BaseColorSlide


class LogoSlide(RectangleUtils, BaseColorSlide):
    logos: m.Group | None = m.Group()
    logo_paths: list[str] = []
    logo_height: float = None
    logo_inbetween_buff: float = None
    logo_vertical_buff: float = None
    logo_horizontal_buff: float = None
    logo_position: str = 'right'  # 'left' , 'right' are the only valid values for TermSlide

    def add_logos(self, transformation: m.Transform | None = None, **kwargs) -> m.AnimationGroup | m.Transform:
        if transformation is None:
            transformation = m.FadeIn

        logo_height = self.med_large_buff if self.logo_height is None else self.logo_height
        logo_vertical_buff = self.med_small_buff if self.logo_vertical_buff is None else self.logo_vertical_buff
        logo_horizontal_buff = self.med_large_buff if self.logo_horizontal_buff is None else self.logo_horizontal_buff
        logo_inbetween_buff = self.med_small_buff if self.logo_inbetween_buff is None else self.logo_inbetween_buff
        logo_position = 'right' if self.logo_position is None else self.logo_position

        if logo_position not in ['left', 'right']:
            raise ValueError("logo_position should be either 'left' or 'right'")

        if self.logo_paths:
            # delete old logos if exist
            for logo in self.logos:
                self.remove(logo)

            self.logos = m.Group()

            for logo_path in self.logo_paths:
                # .svg -> SVGMobject, .png, jpeg etc -> ImageMobject
                logo = m.SVGMobject(logo_path) if logo_path.endswith(".svg") else m.ImageMobject(logo_path)
                logo.scale_to_fit_height(logo_height)

                self.logos.add(logo)

            # arrange logos inside the group
            self.logos.arrange(direction=m.RIGHT, buff=logo_inbetween_buff)

            # move the group to corner
            self.logos.to_edge(m.DOWN, buff=logo_vertical_buff)
            self.logos.to_edge(
                m.RIGHT if logo_position == 'right' else m.LEFT,
                buff=logo_horizontal_buff
            )

            return transformation(self.logos, **kwargs)

        else:
            return m.AnimationGroup()


class TestLogoSlide(LogoSlide):
    logo_paths = ["../../resources/logos/Manim_icon.svg", "../../resources/logos/logo.png"]

    def construct(self):
        self.play(
            self.add_logos()
        )

        self.wait(2)

        self.play(
            m.FadeOut(self.logos)
        )


if __name__ == '__main__':
    TestLogoSlide().render_video_medium()
