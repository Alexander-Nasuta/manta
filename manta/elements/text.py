import manim as m

from manta.color_theme.color_theme_ABC import ColorThemeABC
from manta.elements.nerdfont_icons import NerdfontIconUtils
from manta.font_style.fontABC import FontABC


class TextUtils(NerdfontIconUtils, ColorThemeABC, FontABC):
    _hidden_char = "█"

    def term_text(self, t: str, v_buff=0.05, **kwargs) -> m.VGroup:
        color = kwargs.pop("font_color", None)  # for consistency with math_text
        default_params = {
            "font": self.font_name,
            "color": self.font_color if color is None else color,
            "font_size": self.font_size_normal,
        }
        params = {**default_params, **kwargs}

        lines = t.split("\n")
        if len(lines) == 1:
            return m.VGroup(m.Text(t, **params))
        else:
            hidden_text = m.Text(self._hidden_char, **params)
            hidden_rows = [hidden_text]

            first_row = m.Text(lines[0], **params)
            rows = [first_row]

            first_row.align_to(hidden_text, m.LEFT)

            # rest of the rows
            for i in range(1, len(lines)):
                row = m.Text(lines[i], **params)
                row.next_to(hidden_rows[i - 1], m.DOWN, buff=v_buff, aligned_edge=m.LEFT)
                rows.append(row)

                hidden_row = m.Text(self._hidden_char, **params)
                hidden_row.next_to(hidden_rows[i - 1], m.DOWN, buff=v_buff, aligned_edge=m.LEFT)
                hidden_rows.append(hidden_row)

            # only return the row and not the hidden elements
            return m.VGroup(*rows)

    def title_text(self, t: str, **kwargs) -> m.Mobject:
        return self.term_text(t, font_size=self.font_size_large, **kwargs)

    def text_mono(self, t: str, v_buff=0.1, t2c=None, t2b=None, t2c_strs: list[str] = None,
                  t2w_strs: list[str] = None, t2c_color=None, color_icons=True, **kwargs) -> m.VGroup:
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

        # replace all spaces with _hidden_char for every key of t2c, t2b
        temp = {}
        for key in t2c.keys():
            new_key = key.replace(" ", self._hidden_char)
            temp[new_key] = t2c[key]
        t2c = temp

        if color_icons:
            t2c = {
                **self.symbol_t2c(color=t2c_color),
                **t2c,
            }

        # split multiple line text into an array of lines
        lines = t.split("\n")

        n_rows = len(lines)
        n_cols = max([len(row) for row in lines])

        block_group = m.VGroup()
        arrangement_group = m.VGroup()

        hidden_row_content = self._hidden_char * n_cols

        for i in range(n_rows):

            # print(f"hidden_row_content: {hidden_row_content}")
            hidden_row_text = self.term_text(hidden_row_content, **kwargs)

            row_text_encoded = str(lines[i]).replace(" ", "█")
            # append "█" to row_text_encoded till it has n_cols characters
            row_text_encoded += self._hidden_char * (n_cols - len(row_text_encoded))

            mobj_row = self.term_text(row_text_encoded, t2c=t2c, **kwargs)

            row_str = lines[i]

            non_empty_chars = m.VGroup()

            for orginal_char, elem in zip(row_str, mobj_row):
                if orginal_char != " ":
                    non_empty_chars.add(elem)

            block_group.add(non_empty_chars)
            arrangement_group.add(mobj_row)

        arrangement_group.arrange(m.DOWN, buff=v_buff)
        return block_group

    def mono_block(self, t: str, **kwargs) -> m.VGroup:
        return self.text_mono(t, v_buff=0, **kwargs)

    def term_math_text(self, math_text: str, color=None, font_color=None, **kwargs) -> m.Mobject:
        if font_color is None:
            font_color = self.font_color
        if color is None:
            color = font_color
        default_params = {
            "color": color,
            "font_size": self.font_size_normal,
        }
        params = {**default_params, **kwargs}
        return m.Tex(rf"$\mathsf{{{math_text}}}$", **params)

    def bullet_point_list(self, bulletpoints: list[str], bullet_icon: str | int = 'circle-small', v_buff=0.25,
                          h_buff=0.125,
                          bullet_icon_kwargs=None,
                          **kwargs) -> m.VGroup:
        if bullet_icon_kwargs is None:
            bullet_icon_kwargs = {}

        bullet_point_groups = []
        for bp in bulletpoints:
            bullet_point_text = self.term_text(bp, **kwargs)

            bp_icon = self.symbol(symbol=bullet_icon, **bullet_icon_kwargs)
            bp_icon.next_to(bullet_point_text[0], m.LEFT, buff=h_buff)

            bullet_point_group = m.VGroup(bp_icon, bullet_point_text)
            bullet_point_groups.append(bullet_point_group)

        return m.VGroup(*bullet_point_groups).arrange(m.DOWN, buff=v_buff, aligned_edge=m.LEFT)

    def titled_bulletpoints(self, titled_bulletpoints: list[tuple[str, list[str]]], bullet_icon: str = 'circle-small',
                            v_buff=0.25, h_buff=0.125,
                            bullet_icon_kwargs: dict = None, title_kwargs: dict = None, **kwargs) -> m.VGroup:
        if bullet_icon_kwargs is None:
            bullet_icon_kwargs = {}
        if title_kwargs is None:
            title_kwargs = {}

        titled_bullet_point_groups = []
        for title, bulletpoints in titled_bulletpoints:

            title_text = self.term_text(title, **title_kwargs)

            bullet_point_group = self.bullet_point_list(bulletpoints, bullet_icon=bullet_icon, v_buff=v_buff,
                                                        h_buff=h_buff, bullet_icon_kwargs=bullet_icon_kwargs, **kwargs)

            bullet_point_group.next_to(title_text, m.DOWN, buff=v_buff, aligned_edge=m.LEFT).shift(h_buff * m.RIGHT)

            titled_bullet_point_group = m.VGroup(title_text, bullet_point_group)
            titled_bullet_point_groups.append(titled_bullet_point_group)

        return m.VGroup(*titled_bullet_point_groups).arrange(m.DOWN, buff=v_buff, aligned_edge=m.LEFT)
