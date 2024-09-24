import manim as m

from manta.elements.rectangle_utils import RectangleUtils
from manta.font_style.IosevkaTerm_base_24 import IosevkaTermSizing24
from manta.slide_templates.base.base_colored_slide import BaseColorSlide


class TitleSlide(IosevkaTermSizing24, RectangleUtils, BaseColorSlide):
    _title_mobject: m.Mobject | m.VGroup | None = None
    _title_seperator_mobject: m.Mobject | m.VGroup | None = None
    _subtitle_mobject: m.Mobject | m.VGroup | None = None
    title_row_font_size: float = None
    title_color: str = None
    subtitle_color: str = None
    title_seperator_color: str = None

    title_row_vertical_buff: float = None
    title_row_horizontal_buff: float = None

    default_title_seperator = ": "

    _last_title_value: str | None = None
    _last_seperator_value: str | None = None
    _last_subtitle_value: str | None = None

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

        # title, seperator, subtitle are have to single line strings
        if title is not None and len(title.split("\n")) > 1:
            raise ValueError("Title has to be a single line string")
        if seperator is not None and len(seperator.split("\n")) > 1:
            raise ValueError("Seperator has to be a single line string")
        if subtitle is not None and len(subtitle.split("\n")) > 1:
            raise ValueError("Subtitle has to be a single line string")

        # set last values
        self._last_title_value = title
        self._last_seperator_value = seperator
        self._last_subtitle_value = subtitle

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
        # hidden row = title+seperator+subtitle+hidden_char(█)
        # idea for aligning the title row:
        #   1. create a row with the whole title row (title+seperator+subtitle) and a hidden character at the end
        #   2. align the hidden row
        #   3. posisition the letters of the title, seperator, and subtitle at the same position as the hidden row
        #   4. don't add the hidden row to the scene, only the title, seperator, and subtitle

        # inbetween_buff = self.title_row_inbetween_buff if self.title_row_inbetween_buff is not None else self.small_buff
        # target_group.arrange(direction=m.RIGHT, buff=inbetween_buff)

        # position the title row in the top left corner
        # vertical_buff = self.title_row_vertical_buff if self.title_row_vertical_buff is not None else self.med_large_buff
        # horizontal_buff = self.title_row_horizontal_buff if self.title_row_horizontal_buff is not None else self.med_large_buff

        # target_group.to_edge(m.UP, buff=vertical_buff)
        # target_group.to_edge(m.LEFT, buff=horizontal_buff)

        target_strs = []
        for elem in [title, seperator, subtitle]:
            if elem is not None:
                target_strs.append(elem)
        target_strs.append(self._hidden_char)

        hidden_row = "".join(target_strs)
        hidden_row_mobj_vgroup = self.term_text(hidden_row, font_size=title_row_font_size)

        vertical_buff = self.title_row_vertical_buff if self.title_row_vertical_buff is not None else self.med_large_buff * 0.75
        horizontal_buff = self.title_row_horizontal_buff if self.title_row_horizontal_buff is not None else self.med_large_buff

        hidden_row_mobj_vgroup.to_edge(m.UP, buff=vertical_buff)
        hidden_row_mobj_vgroup.to_edge(m.LEFT, buff=horizontal_buff)

        target_letter_mobjects = []
        for target_elem in target_group:
            target_elem_text_mobject: m.Text = target_elem[0]
            target_letter_mobjects.extend(target_elem_text_mobject.submobjects)

        for target_letter_mobj, hidden_letter_mobj in zip(target_letter_mobjects,
                                                          hidden_row_mobj_vgroup[0].submobjects):
            target_letter_mobj.move_to(hidden_letter_mobj.get_center())

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

    def change_subtitle(self, new_subtitle: str | None = None, **kwargs) -> m.AnimationGroup:
        default_params = {
            "title": self._last_title_value,
            "seperator": self.default_title_seperator,
            "subtitle": new_subtitle
        }
        # if title is not None, new_subtitle is not None, and seperator is None -> use default seperator
        if (default_params["title"] is not None
                and default_params["subtitle"] is not None
                and default_params["seperator"] is None):
            default_params["seperator"] = self.default_title_seperator

        merged_params = {**default_params, **kwargs}

        return self.set_title_row(**merged_params)

    def remove_subtitle(self, **kwargs) -> m.AnimationGroup:
        return self.change_subtitle(new_subtitle=None, seperator=None, **kwargs)

    def change_title(self, new_title: str | None = None, **kwargs) -> m.AnimationGroup:
        default_params = {
            "title": new_title,
            "seperator": self.default_title_seperator,
            "subtitle": self._last_subtitle_value
        }
        # if title is not None, new_subtitle is not None, and seperator is None -> use default seperator
        if (default_params["title"] is not None
                and default_params["subtitle"] is not None
                and default_params["seperator"] is None):
            default_params["seperator"] = self.default_title_seperator

        merged_params = {**default_params, **kwargs}

        return self.set_title_row(**merged_params)

    def remove_title(self, **kwargs) -> m.AnimationGroup:
        return self.change_title(new_title=None, seperator=None, **kwargs)

    def change_title_seperator(self, new_seperator: str | None = None, update_default_seperator=True,
                               **kwargs) -> m.AnimationGroup:
        if update_default_seperator:
            self.default_title_seperator = new_seperator
        default_params = {
            "title": self._last_title_value,
            "seperator": new_seperator,
            "subtitle": self._last_subtitle_value
        }

        merged_params = {**default_params, **kwargs}

        return self.set_title_row(**merged_params)

    def remove_title_seperator(self, **kwargs) -> m.AnimationGroup:
        return self.change_title_seperator(new_seperator=None, **kwargs)

    def remove_title_row(self, **kwargs) -> m.AnimationGroup:
        return self.set_title_row(title=None, seperator=None, subtitle=None, **kwargs)


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
