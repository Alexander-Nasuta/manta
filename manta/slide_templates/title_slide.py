import manim as m

from manta.elements.rectangle_utils import RectangleUtils
from manta.font_style.IosevkaTerm_base_24 import LatexFontSizing24
from manta.slide_templates.base.base_colored_slide import BaseColorSlide


class TitleSlide(LatexFontSizing24, RectangleUtils, BaseColorSlide):
    _title_mobject: m.Mobject | None = None
    _title_seperator_mobject: m.Mobject | None = None
    _subtitle_mobject: m.Mobject | None = None
    title_row_font_size: float = None
    title_color: str = None
    subtitle_color: str = None
    title_seperator_color: str = None
    title_row_inbetween_buff: float = None
    title_row_vertical_buff: float = None
    title_row_horizontal_buff: float = None

    def set_title_row(self, title: str | None = None, subtitle: str | None = None, seperator: str | None = None,
                      create_animation: m.Transform = None,
                      destroy_animation: m.Transform = None,
                      replace_animation: m.Transform = None,
                      **kwargs) -> m.AnimationGroup:
        # default values for transformations
        if create_animation is None:
            create_animation = m.FadeIn
        if destroy_animation is None:
            destroy_animation = m.FadeOut
        if replace_animation is None:
            replace_animation = m.Transform

        previous_title_is_present = self._title_seperator_mobject is not None or self.is_in_scene(self._title_mobject)
        previous_subtitle_is_present = self._subtitle_mobject is not None or self.is_in_scene(self._subtitle_mobject)
        previous_seperator_is_present = self._title_seperator_mobject is not None or self.is_in_scene(
            self._title_seperator_mobject)

        target_title_is_present = title is not None
        target_subtitle_is_present = subtitle is not None
        target_seperator_is_present = seperator is not None

        target_group = m.VGroup()

        title_row_font_size = self.title_row_font_size if self.title_row_font_size is not None else self.font_size_large

        if target_title_is_present:
            title_font_size = title_row_font_size
            title_font_color = self.title_color if self.title_color is not None else self.font_color
            target_title_mobj = self.term_text(title, font_color=title_font_color, font_size=title_font_size)
            target_group.add(target_title_mobj)

        if target_seperator_is_present:
            seperator_font_color = self.title_seperator_color if self.title_seperator_color is not None else self.font_color
            target_seperator_mobj = self.term_text(seperator, font_color=seperator_font_color,
                                                   font_size=title_row_font_size)
            target_group.add(target_seperator_mobj)

        if target_subtitle_is_present:
            subtitle_font_size = title_row_font_size
            subtitle_font_color = self.subtitle_color if self.subtitle_color is not None else self.font_color
            target_subtitle_mobj = self.term_text(subtitle, font_color=subtitle_font_color,
                                                  font_size=subtitle_font_size)
            target_group.add(target_subtitle_mobj)

        # alight the title row
        inbetween_buff = self.title_row_inbetween_buff if self.title_row_inbetween_buff is not None else self.small_buff
        target_group.arrange(direction=m.RIGHT, buff=inbetween_buff)

        # position the title row in the top left corner
        vertical_buff = self.title_row_vertical_buff if self.title_row_vertical_buff is not None else self.med_large_buff
        horizontal_buff = self.title_row_horizontal_buff if self.title_row_horizontal_buff is not None else self.med_large_buff

        target_group.to_edge(m.UP, buff=vertical_buff)
        target_group.to_edge(m.LEFT, buff=horizontal_buff)

        # build animation group
        animations_list = []

        # title animation
        if not previous_title_is_present and target_title_is_present:
            animations_list.append(create_animation(target_title_mobj))
            self._title_mobject = target_title_mobj
        elif previous_title_is_present and target_title_is_present:
            animations_list.append(replace_animation(self._title_mobject, target_title_mobj))
        elif previous_title_is_present and not target_title_is_present:
            animations_list.append(destroy_animation(self._title_mobject))
            self._title_mobject = None

        # seperator animation
        if not previous_seperator_is_present and target_seperator_is_present:
            animations_list.append(create_animation(target_seperator_mobj))
            self._title_seperator_mobject = target_seperator_mobj
        elif previous_seperator_is_present and target_seperator_is_present:
            animations_list.append(replace_animation(self._title_seperator_mobject, target_seperator_mobj))
        elif previous_seperator_is_present and not target_seperator_is_present:
            animations_list.append(destroy_animation(self._title_seperator_mobject))
            self._title_seperator_mobject = None

        # subtitle animation
        if not previous_subtitle_is_present and target_subtitle_is_present:
            animations_list.append(create_animation(target_subtitle_mobj))
            self._subtitle_mobject = target_subtitle_mobj
        elif previous_subtitle_is_present and target_subtitle_is_present:
            animations_list.append(replace_animation(self._subtitle_mobject, target_subtitle_mobj))
        elif previous_subtitle_is_present and not target_subtitle_is_present:
            animations_list.append(destroy_animation(self._subtitle_mobject))
            self._subtitle_mobject = None

        return m.AnimationGroup(*animations_list, **kwargs)


class TestTitleSlide(TitleSlide):

    def construct(self):
        self.play(
            self.set_title_row(
                title="Hallo"
            )
        )

        self.play(
            self.set_title_row(
                title="Hallo Welt",
                seperator=":",
                subtitle="Subtitle"
            )
        )

        self.play(
            self.set_title_row(
                title="Hallo Welt",
                seperator=":",
                subtitle="another subtitle"
            )
        )

        self.play(
            self.set_title_row(),
        )

        self.wait(0.1)


if __name__ == '__main__':
    TestTitleSlide.render_video_medium()
