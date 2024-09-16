import manim as m

from manta.elements.shapes import ShapeUtils
from manta.padding_style.paddingABC import PaddingABC


class RectangleUtils(ShapeUtils, PaddingABC):

    def wrap_with_rectangle(self, mElement: m.Mobject | m.VGroup,
                            height=None, width=None,
                            include_element_in_group=True, rounded=True,
                            h_buff=None, v_buff=None,
                            **kwargs) \
            -> m.VGroup | m.Mobject:
        if h_buff is None:
            h_buff = self.med_large_buff
        if v_buff is None:
            v_buff = self.med_small_buff
        if height is None:
            height = mElement.height + v_buff * 2
        if width is None:
            width = mElement.width + h_buff * 2

        rectangle = self.rectangle(
            width=width,
            height=height,
            **kwargs
        ) if not rounded else self.rounded_rectangle(
            width=width,
            height=height,
            **kwargs
        )

        rectangle.move_to(mElement)
        if include_element_in_group:
            return m.VGroup(rectangle, mElement)
        else:
            return rectangle

    def wrap_with_icon_and_rectangle(self, mElement: m.Mobject | m.VGroup,
                                     icon: str | int = 'icons',
                                     icon_color: str = None,
                                     icon_kwargs=None,
                                     include_element_in_group=True,
                                     h_buff=None,
                                     v_buff=None,
                                     direction: str = 'left', **kwargs) -> m.VGroup | m.Mobject:

        if icon_kwargs is None:
            icon_kwargs = {}
        icon_default_params = {
            "font_size": self.font_size_normal,
            "symbol": icon
        }
        if icon_color is not None:
            icon_default_params["color"] = icon_color
        icon_params = {**icon_default_params, **icon_kwargs}

        icon = self.symbol(**icon_params)

        if direction not in ['left', 'right', 'up', 'down']:
            raise ValueError(f"Invalid direction: {direction}. Only 'left', 'right', 'up', 'down' are valid values.")

        if direction == 'left':
            np_direction = m.LEFT
        elif direction == 'right':
            np_direction = m.RIGHT
        elif direction == 'up':
            np_direction = m.UP
        else:
            np_direction = m.DOWN

        if h_buff is None:
            h_buff = self.med_large_buff
        if v_buff is None:
            v_buff = self.med_small_buff

        # use a hidden character to determine for positioning, because the icons might have slightly different sizes
        # and could cause to get inconsistent height and width values for the resulting VGroup for different icons
        hidden_char = self.term_text(self._hidden_char, font_size=icon_params["font_size"])

        hidden_char.next_to(mElement, np_direction, buff=1.5 * h_buff if direction in ['left', 'right'] else 1.5 * v_buff)
        icon.move_to(hidden_char.get_center())

        temp = m.VGroup(hidden_char, mElement)
        rect = self.wrap_with_rectangle(temp, include_element_in_group=False, h_buff=h_buff, v_buff=v_buff, **kwargs)

        if direction in ['left', 'right']:
            separation_line = m.Line(rect.get_top(), rect.get_bottom(), color=self.outline_color, stroke_width=1.0)
            separation_line.next_to(hidden_char, np_direction * -1, buff=h_buff)

            if direction == 'left':
                rect.next_to(hidden_char.get_left(), m.RIGHT, buff=-h_buff)
            else:
                rect.next_to(hidden_char.get_right(), m.LEFT, buff=-h_buff)

        else:  # case: up, down
            separation_line = m.Line(rect.get_left(), rect.get_right(), color=self.outline_color, stroke_width=1.0)
            separation_line.next_to(hidden_char, np_direction * -1, buff=v_buff)

        if include_element_in_group:
            return m.VGroup(rect, icon, separation_line, mElement).move_to(m.ORIGIN)
        else:
            return m.VGroup(rect, icon, separation_line).move_to(m.ORIGIN)

    def icon_textbox(self, text: str, icon: str | int = 'icons', direction='left',
                     t2c=None, t2b=None, t2c_strs: list[str] = None,
                     t2w_strs: list[str] = None, t2c_color=None, **kwargs) -> m.VGroup:
        t2c_strs = [] if t2c_strs is None else t2c_strs
        t2w_strs = [] if t2w_strs is None else t2w_strs

        if t2c_color is None:
            t2c_color = self.yellow
        if t2c is None:
            t2c = {s: t2c_color for s in t2c_strs}
        else:
            t2c = {**{s: t2c_color for s in t2c_strs}, **t2c}
        if t2b is None:
            t2b = {s: m.BOLD for s in t2w_strs}

        text_group = self.term_text(text)
        return self.wrap_with_icon_and_rectangle(text_group, icon=icon, direction=direction, **kwargs)

    def icon_bulletpoints_textbox(self, bullet_points: list[str], bullet_point_kwargs: dict = None,
                                  icon: str | int = 'icons',
                                  direction='left',
                                  t2c=None, t2w=None, t2c_strs: list[str] = None,
                                  t2w_strs: list[str] = None, t2c_color=None, **kwargs) -> m.VGroup:
        if bullet_point_kwargs is None:
            bullet_point_kwargs = {}
        t2c_strs = [] if t2c_strs is None else t2c_strs
        t2w_strs = [] if t2w_strs is None else t2w_strs

        if t2c_color is None:
            t2c_color = self.yellow
        if t2c is None:
            t2c = {s: t2c_color for s in t2c_strs}
        else:
            t2c = {**{s: t2c_color for s in t2c_strs}, **t2c}
        if t2w is None:
            t2w = {s: m.BOLD for s in t2w_strs}

        bullet_point_params = {
            "t2c": t2c,
            "t2w": t2w,
            **bullet_point_kwargs
        }

        bullet_points = self.bullet_point_list(bullet_points, **bullet_point_params)

        return self.wrap_with_icon_and_rectangle(bullet_points, icon=icon, direction=direction, **kwargs)

    def icon_title_bulletpoints_textbox(self, titled_bulletpoints: list[tuple[str, list[str]]],
                                        bullet_icon: str = 'circle-small',
                                        v_buff=0.25, h_buff=0.125,
                                        bullet_icon_kwargs: dict = None, title_kwargs: dict = None,
                                        icon: str | int = 'icons',
                                        direction='left',
                                        t2c=None, t2w=None, t2c_strs: list[str] = None,
                                        t2w_strs: list[str] = None, t2c_color=None, **kwargs) -> m.VGroup:
        if bullet_icon_kwargs is None:
            bullet_icon_kwargs = {}
        if title_kwargs is None:
            title_kwargs = {}
        t2c_strs = [] if t2c_strs is None else t2c_strs
        t2w_strs = [] if t2w_strs is None else t2w_strs

        if t2c_color is None:
            t2c_color = self.yellow
        if t2c is None:
            t2c = {s: t2c_color for s in t2c_strs}
        else:
            t2c = {**{s: t2c_color for s in t2c_strs}, **t2c}
        if t2w is None:
            t2w = {s: m.BOLD for s in t2w_strs}

        bullet_point_params = {
            "t2c": t2c,
            "t2w": t2w,
            **bullet_icon_kwargs
        }

        titled_bullet_points = self.titled_bulletpoints(titled_bulletpoints, bullet_icon=bullet_icon,
                                                        v_buff=v_buff, h_buff=h_buff,
                                                        bullet_icon_kwargs=bullet_point_params,
                                                        title_kwargs=title_kwargs)

        return self.wrap_with_icon_and_rectangle(titled_bullet_points, icon=icon, direction=direction, **kwargs)
