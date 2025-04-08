import math

import manim as m

import numpy as np
import theme_colors as TC
import theme_symbols as TS

from manim_editor import PresentationSectionType

from manim import config

from color_theme.rwth.rwth_theme import RwthTheme

WAIT_TIME = 0.325

# font sizes
# latex naming convention
font_tiny = 0.25
font_scriptsize = 0.275
font_footnotesize = 0.3
font_small = 0.3125
font_normalsize = 0.375
font_large = 0.5
font_Large = 0.625
font_LARGE = 0.75
font_huge = 0.875
font_Huge = 1.0

# buffs
buff_small = 0.125
buff_normal = 0.25
buff_large = 0.275
buff_Large = 0.3
buff_LARGE = 0.3125
buff_huge = 0.325
buff_Huge = 0.35


def text(t, **kwargs):
    color = kwargs.pop("font_color", None)  # for consistency with math_text
    default_params = {
        "font": "Iosevka Nerd Font",
        "color": RwthTheme.rwth_blau_75 if color is None else color,
    }
    params = {**default_params, **kwargs}
    return m.Text(t, **params)


def monospace_text_block(text_block: list[str], v_buff=buff_small, **kwargs):
    n_rows = len(text_block)
    n_cols = max([len(row) for row in text_block])
    # print(f"n_rows: {n_rows}, n_cols: {n_cols}")

    hidden_char = "█"
    hidden_row_content = hidden_char * n_cols

    block_group = m.VGroup()
    arrangement_group = m.VGroup()

    for i in range(n_rows):

        # print(f"hidden_row_content: {hidden_row_content}")
        hidden_row_text = text(hidden_row_content, **kwargs)

        row_text_encoded = str(text_block[i]).replace(" ", "█")
        # append "█" to row_text_encoded till is has n_cols characters
        row_text_encoded += hidden_char * (n_cols - len(row_text_encoded))

        mobj_row = text(row_text_encoded, **kwargs)

        row_str = text_block[i]

        non_empty_chars = m.VGroup()

        for orginal_char, elem in zip(row_str, mobj_row):
            if orginal_char != " ":
                non_empty_chars.add(elem)


        block_group.add(non_empty_chars)
        arrangement_group.add(mobj_row)

    arrangement_group.arrange(m.DOWN, buff=v_buff)
    return block_group




def title_text(title_text_str: str, buff=0.5, scale=font_Large, shift=np.array([0, 0, 0]), **kwargs):
    title_text = text(title_text_str, **kwargs).scale(
        scale).to_corner(m.UL, buff=buff).shift(shift)
    return title_text


def rounded_rectangle(width: float, height: float, **kwargs):
    return m.RoundedRectangle(
        corner_radius=0.125,
        height=height,
        width=width,
        fill_color=RwthTheme.background_color_bright,
        fill_opacity=1.0,
        stroke_color=RwthTheme.outline_color,
        stroke_width=1.0
    )


def rectangle(width: float, height: float, **kwargs):
    default_params = {
        "height": height,
        "width": width,
        "fill_color": TC.GREY_DARK_LIGHT,
        "fill_opacity": 1.0,
        "stroke_color": TC.GREY_OUTLINE,
        "stroke_width": 1.0,
        "corner_radius": 0.0,
    }
    merged_params = {**default_params, **kwargs}
    return m.RoundedRectangle(**merged_params)


def circle(radius: float, **kwargs):
    default_params = {
        "radius": radius,
        "fill_color": TC.GREY_DARK_LIGHT,
        "fill_opacity": 1.0,
        "stroke_color": TC.GREY_OUTLINE,
        "stroke_width": 1.0
    }
    merged_params = {**default_params, **kwargs}
    return m.Circle(**merged_params)


def rectangle_with_icon(icon: int | str, width: float, height: float,
                        icon_scale=0.5, icon_buff=0.25, icon_rotate=0.0,
                        icon_color: m.ManimColor = RwthTheme.rwth_blau_75) -> m.VGroup:
    rect = rounded_rectangle(width, height)
    icon_text = TS.symbol(icon, color=icon_color).scale(icon_scale)
    icon_text.next_to(rect.get_corner(m.LEFT), m.RIGHT, buff=icon_buff)
    icon_text.rotate(icon_rotate)
    icon_v_line = m.Line(rect.get_top(), rect.get_bottom(), color=TC.GREY_OUTLINE, stroke_width=1.0)
    icon_v_line.next_to(icon_text, m.RIGHT, buff=icon_buff)

    return m.VGroup(rect, icon_text, icon_v_line)


def text_rectangle_with_icon(text_rows: list[str], icon: int | str, width: float, height: float,
                             icon_scale=0.5, icon_buff=0.25, icon_rotate=0.0, text_scale=font_normalsize, text_buff=0.1,
                             **kwargs) -> m.VGroup:
    rect = rounded_rectangle(width, height)
    icon_text = TS.symbol(icon).scale(icon_scale)
    icon_text.next_to(rect.get_corner(m.LEFT), m.RIGHT, buff=icon_buff)
    icon_text.rotate(icon_rotate)
    icon_v_line = m.Line(rect.get_top(), rect.get_bottom(), color=TC.GREY_OUTLINE, stroke_width=1.0)
    icon_v_line.next_to(icon_text, m.RIGHT, buff=icon_buff)

    # use hidden text to align the rows
    hidden_text = text("Yy", opacity=0.0).scale(text_scale)
    hidden_rows = [hidden_text]

    # construct text rows
    first_row = text(text_rows[0]).scale(text_scale)
    rows = [first_row]

    # align left edge of frist_row with hidden_text
    first_row.align_to(hidden_text, m.LEFT)

    # rest of the rows
    for i in range(1, len(text_rows)):
        row = text(text_rows[i]).scale(text_scale)
        row.next_to(hidden_rows[i - 1], m.DOWN, buff=text_buff, aligned_edge=m.LEFT)
        rows.append(row)

        hidden_row = text("Yy", opacity=0.0).scale(text_scale)
        hidden_row.next_to(hidden_rows[i - 1], m.DOWN, buff=text_buff, aligned_edge=m.LEFT)
        hidden_rows.append(hidden_row)

    row_v_group = m.VGroup(*rows)
    row_v_group.next_to(icon_v_line, m.RIGHT, buff=icon_buff)

    return m.VGroup(rect, icon_text, icon_v_line, row_v_group)


def title_rectangle(title: str, width: float, height: float, title_size=font_large, buff=buff_normal, **kwargs):
    rect = rounded_rectangle(width, height)
    title_text = text(title).scale(title_size)
    title_text.next_to(rect.get_top(), m.DOWN, buff=buff)

    # invisible text to align horizontal line
    # letters as g, y, p ... then to mess up the alignment
    invisible_text = text("0", color=TC.PINK, opacity=0.0).scale(title_size)
    invisible_text.next_to(rect.get_top(), m.DOWN, buff=buff)

    title_h_line = m.Line(rect.get_left(), rect.get_right(), color=TC.GREY_OUTLINE, stroke_width=1.0)
    title_h_line.next_to(invisible_text, m.DOWN, buff=buff)

    return m.VGroup(rect, title_text, title_h_line)


def math_arrow(*args, color: m.ManimColor = TC.DEFAULT_FONT, **kwargs):
    class EngineerArrowTip(m.ArrowTip, m.Polygon):
        def __init__(self, length=0.35, **kwargs):
            # Define the vertices for a 30-degree arrow tip
            arrow_tip_angle = math.radians(15)
            vertices = [
                m.ORIGIN - m.RIGHT * length / 2,
                length * np.array([math.cos(arrow_tip_angle), math.sin(arrow_tip_angle), 0]) - m.RIGHT * length / 2,
                length * np.array([math.cos(arrow_tip_angle), -math.sin(arrow_tip_angle), 0]) - m.RIGHT * length / 2,
            ]
            m.Polygon.__init__(self, *vertices, **kwargs)
            m.Polygon.set_fill(self, color=color, opacity=1.0)

    arrow_default_kwargs = {
        "tip_shape": EngineerArrowTip,
        "tip_length": 0.1,
        "stroke_width": 3,
        "buff": 0,
        "fill_color": TC.DARK_FONT,
        "color": color
    }
    arrow_kwargs = {**arrow_default_kwargs, **kwargs}
    return m.Arrow(*args, **arrow_kwargs)


def math_circle(math_text: str, radius: 0.25, font_color=TC.GREY_DARK, text_scale=font_large,
                **kwargs) -> m.VGroup | m.Mobject:
    default_params = {
        "radius": radius,
        "stroke_width": 6,
        "stroke_color": TC.BLUE,
        "fill_color": TC.YELLOW,
        "fill_opacity": 1.0
    }
    params = {**default_params, **kwargs}
    circle = m.Circle(**params)

    text_none_values = [None, "", " "]
    if math_text in text_none_values:
        return circle

    circle_text = m.Tex(rf"$\mathsf{{{math_text}}}$", color=font_color).scale(text_scale)
    return m.VGroup(circle, circle_text)


def console_math_text(math_text: str, font_color=TC.DEFAULT_FONT, text_scale=font_normalsize, **kwargs):
    return m.Tex(rf"$\mathsf{{{math_text}}}$", color=font_color).scale(text_scale)


def bullet_point_rectangle(
        title_rows: list[str],
        bullet_points: list[list[str]] = None,
        width: float = None,
        height: float = None,
        icon: int | str = 'information-outline',
        icon_scale=0.5,
        icon_buff=buff_normal,
        icon_color=RwthTheme.rwth_orange_75,
        title_font_size=font_normalsize,
        title_buff=0.1,
        bullet_icon: int | str = 'circle-small',
        bullet_icon_scale=font_normalsize,
        bullet_text_size=font_normalsize,
        bullet_icon_color=RwthTheme.rwth_orange_75,
        bullet_h_buff=None,
        bullet_v_buff=0.1,
        between_bullet_buff=0.125,
):
    if bullet_points is None:
        bullet_points = []

    # use hidden text to align the rows
    hidden_text = text("Yy", opacity=0.0).scale(title_font_size)
    hidden_rows = [hidden_text]

    # construct text bullet point title rows
    first_row = text(title_rows[0]).scale(title_font_size)
    title_rows = [first_row]
    # align left edge of frist_row with hidden_text
    first_row.align_to(hidden_text, m.LEFT)

    # rest of the title rows
    for i in range(1, len(title_rows)):
        row = text(title_rows[i]).scale(title_font_size)
        row.next_to(hidden_rows[i - 1], m.DOWN, buff=title_buff, aligned_edge=m.LEFT)

        title_rows.append(row)
        hidden_row = text("Yy", opacity=0.0).scale(title_font_size)
        hidden_row.next_to(hidden_rows[i - 1], m.DOWN, buff=title_buff, aligned_edge=m.LEFT)
        hidden_rows.append(hidden_row)

    bullet_title_group = m.VGroup(*title_rows)
    hidden_rows_group = m.VGroup(*hidden_rows)

    bullet_groups = []

    for bullet_rows in bullet_points:
        bullet_icon_obj = TS.symbol(bullet_icon, color=bullet_icon_color).scale(bullet_icon_scale)

        if bullet_h_buff is None:
            bullet_h_buff = text("0123456789", opacity=0.0).scale(bullet_text_size).width / 10
            # print(f"bullet_h_buff: {bullet_h_buff}")
            # print(f"bullet_icon_obj width: {bullet_icon_obj.width}")

        hidden_text = text("Yy", opacity=0.0).scale(bullet_text_size)
        hidden_rows = [hidden_text]

        hidden_text.next_to(bullet_icon_obj, m.RIGHT, buff=bullet_h_buff)

        bullet_point_first_row = text(bullet_rows[0]).scale(bullet_text_size)
        bullet_rows_group = [bullet_point_first_row]

        bullet_point_first_row.align_to(hidden_text, m.LEFT)

        for i in range(1, len(bullet_rows)):
            row = text(bullet_rows[i]).scale(bullet_text_size)
            row.next_to(hidden_rows[i - 1], m.DOWN, buff=bullet_v_buff, aligned_edge=m.LEFT)

            bullet_rows_group.append(row)
            hidden_row = text("Yy", opacity=0.0).scale(bullet_text_size)
            hidden_row.next_to(hidden_rows[i - 1], m.DOWN, buff=bullet_v_buff, aligned_edge=m.LEFT)
            hidden_rows.append(hidden_row)

        bullet_rows_group = m.VGroup(*bullet_rows_group)
        bullet_groups.append(m.VGroup(bullet_icon_obj, bullet_rows_group))

    rect_icon = TS.symbol(icon, color=icon_color).scale(icon_scale)

    if height is None:
        # add height of elements
        bullet_total_group_height = sum([bullet_group.height for bullet_group in bullet_groups])
        bullet_total_group_height += bullet_title_group.height
        # add the space between the bullet groups
        # title group
        bullet_total_group_height += 0.25 * 2  # very top and very bottom a 0.25 buff
        # bullet groups
        bullet_total_group_height += len(bullet_groups) * between_bullet_buff  # between bullet groups
        height = bullet_total_group_height

    if width is None:
        # get the width of the longest bullet point33
        temp = TS.symbol(bullet_icon, color=bullet_icon_color).scale(bullet_icon_scale)
        width = max(
            bullet_title_group.width,
            m.VGroup(*bullet_groups).width + bullet_h_buff * 2 + temp.width
        ) + rect_icon.width + 3 * icon_buff

    rect = rounded_rectangle(width=width, height=height)

    # place ret_icon to the left of the rect
    rect_icon.next_to(rect.get_corner(m.LEFT), m.RIGHT, buff=icon_buff)

    # vertical line next to the icon
    rect_v_line = m.Line(rect.get_top(), rect.get_bottom(), color=TC.GREY_OUTLINE, stroke_width=1.0)
    rect_v_line.next_to(rect_icon, m.RIGHT, buff=icon_buff)

    # position the title rows to top right of the vertical line top end
    bullet_title_group.next_to(rect_v_line, m.RIGHT, aligned_edge=m.UP, buff=icon_buff).shift(m.DOWN * 0.25)

    # position bullet_groups elemets below the title rows

    # first bullet group
    if len(bullet_groups):
        bullet_groups[0].next_to(bullet_title_group, m.DOWN, buff=between_bullet_buff, aligned_edge=m.LEFT)

    # rest of the bullet groups
    for i in range(1, len(bullet_groups)):
        bullet_groups[i].next_to(bullet_groups[i - 1], m.DOWN, buff=between_bullet_buff, aligned_edge=m.LEFT)

    # shift all bullet group to the right by bullet_h_buff
    for bullet_group in bullet_groups:
        bullet_group.shift(m.RIGHT * bullet_h_buff)

    return m.VGroup(
        rect,
        *title_rows,
        *bullet_groups,
        rect_v_line,
        rect_icon
    )
