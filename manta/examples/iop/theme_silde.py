import math

import manim as m

import numpy as np
import theme_colors as C
import theme_elements as T

from manim_editor import PresentationSectionType

from manim import config


class TEMPLATE_SILDES(m.MovingCameraScene):
    slide_prefix: str = "X"

    slide_title_text: str = "TITLE"
    slide_title_color: str = C.DEFAULT_FONT
    slide_title_scale: float = T.font_Large
    slide_title_mobj: m.Text = None

    slide_subtitle_separator: float = ":"
    slide_subtitle_separator_color: str = C.DARK_FONT
    slide_subtitle_separator_scale: float = T.font_Large
    slide_subtitle_separator_mobj: m.Text = None
    slide_subtitle_separator_buffer_left: float = 0.1
    slide_subtitle_separator_buffer_right: float = 0.1

    slide_subtitle_text: str = None
    slide_subtitle_color: str = C.DARK_FONT
    slide_subtitle_scale: float = T.font_Large
    slide_subtitle_mobj: m.Text = None

    _slide_index: int = 1
    _slide_font_color = C.DEFAULT_FONT
    slide_index_elem = None

    SCENE_WIDTH = 14.2222222222222222222222222
    CONTENT_WIDTH = SCENE_WIDTH - 2 * 0.5  # 0.5 is the default padding

    def slide_index_transform(self):
        if self.slide_index_elem is None:
            self.slide_index_elem = T.text(f"{self.slide_prefix}{self._slide_index:02}",
                                           color=self._slide_font_color) \
                .scale(0.5) \
                .to_corner(m.DL, buff=0.25)
            return m.FadeIn(self.slide_index_elem)
        self._slide_index += 1
        target = T.text(self.get_section_name(), color=self._slide_font_color) \
            .scale(0.5) \
            .to_corner(m.DL, buff=0.25)
        transform = m.Transform(
            self.slide_index_elem, target,
            replace_mobject_with_target_in_scene=True
        )
        self.slide_index_elem = target
        return transform

    def get_section_name(self) -> str:
        return f"{self.slide_prefix}{self._slide_index:02}"

    def setup(self):
        self.camera.background_color = C.GREY_DARK
        self.next_section(self.get_section_name(), PresentationSectionType.NORMAL)

        if self.slide_title_text:
            self.slide_title_mobj = T.title_text(
                self.slide_title_text,
                scale=self.slide_title_scale,
                color=self.slide_title_color
            )

        if self.slide_subtitle_text:
            self.slide_subtitle_separator_mobj = T.title_text(
                self.slide_subtitle_separator,
                scale=self.slide_subtitle_separator_scale,
                color=self.slide_subtitle_separator_color
            )
            self.slide_subtitle_mobj = T.title_text(
                self.slide_subtitle_text,
                scale=self.slide_subtitle_scale,
                color=self.slide_subtitle_color
            )

            # position the subtitle and separator
            self.slide_subtitle_separator_mobj.next_to(
                self.slide_title_mobj, m.RIGHT,
                buff=self.slide_subtitle_separator_buffer_left
            )
            self.slide_subtitle_mobj.next_to(
                self.slide_subtitle_separator_mobj, m.RIGHT,
                buff=self.slide_subtitle_separator_buffer_right
            )

    def play(
            self,
            *args,
            subcaption=None,
            subcaption_duration=None,
            subcaption_offset=0,
            **kwargs,
    ):
        self.next_section(f"{self.get_section_name()}", PresentationSectionType.NORMAL)
        super().play(*args, self.slide_index_transform(), **kwargs)

    def play_without_slide_index(
            self,
            *args,
            subcaption=None,
            subcaption_duration=None,
            subcaption_offset=0,
            **kwargs,
    ):
        self.next_section(f"{self.slide_prefix}00", PresentationSectionType.NORMAL)
        super().play(*args, **kwargs)

    def play_without_slide_index_and_section(
            self,
            *args,
            subcaption=None,
            subcaption_duration=None,
            subcaption_offset=0,
            **kwargs,
    ):
        super().play(*args, **kwargs)

    def play_wis(
            self,
            *args,
            subcaption=None,
            subcaption_duration=None,
            subcaption_offset=0,
            **kwargs,
    ):  # wis = without index and section
        super().play(*args, **kwargs)

    def construct(self):
        super().construct()
        self.wait(0.1)

    def new_subtitle(self, text: str):
        alignment_obj = self.slide_subtitle_separator_mobj
        if alignment_obj is None:
            if self.slide_title_mobj is not None:
                alignment_obj = self.slide_title_mobj
            else:
                raise ValueError(
                    "The is no title object to align the subtitle to. Either add a title object (self.slide_title_mobj) or "
                    "create a separator object (self.slide_subtitle_separator_mobj).")
        return T.title_text(
            text,
            scale=self.slide_subtitle_scale,
            color=self.slide_subtitle_color
        ).next_to(alignment_obj, m.RIGHT, buff=self.slide_subtitle_separator_buffer_right)

    def is_in_scene(self, mobj):
        return mobj in self.mobjects

    def animation_replace_subtitle(self, subtitle_text: str) -> list[m.Animation]:
        empy_string_values = [None, "", " "]
        self.slide_subtitle_text = subtitle_text

        # case 1: old subtitle is present and new subtitle is empty
        if self.slide_subtitle_text in empy_string_values:
            # Fade out the separator and subtitle if present
            fade_out = []
            if self.slide_subtitle_separator_mobj is not None:
                fade_out.append(m.FadeOut(self.slide_subtitle_separator_mobj))
            if self.slide_subtitle_mobj is not None:
                fade_out.append(m.FadeOut(self.slide_subtitle_mobj))
            return fade_out

        # case 2: old subtitle is empty and new subtitle is present
        if self.slide_subtitle_mobj is None or not self.is_in_scene(self.slide_subtitle_mobj):
            # Fade in the separator and subtitle
            fade_in = []
            if self.slide_subtitle_separator_mobj is not None or not self.is_in_scene(
                    self.slide_subtitle_separator_mobj):
                fade_in.append(m.FadeIn(self.slide_subtitle_separator_mobj))
            fade_in.append(m.FadeIn(self.new_subtitle(self.slide_subtitle_text)))
            return fade_in

        # case 3: old subtitle is present and new subtitle is present
        return m.Transform(self.slide_subtitle_mobj, self.new_subtitle(self.slide_subtitle_text)),

    def animation_fade_in_title_and_subtitle(self) -> list[m.Animation]:
        fade_in = []
        if self.slide_title_mobj is not None and not self.is_in_scene(self.slide_title_mobj):
            fade_in.append(m.FadeIn(self.slide_title_mobj))
        if self.slide_subtitle_separator_mobj is not None and not self.is_in_scene(self.slide_subtitle_separator_mobj):
            fade_in.append(m.FadeIn(self.slide_subtitle_separator_mobj))
        if self.slide_subtitle_mobj is not None and not self.is_in_scene(self.slide_subtitle_mobj):
            fade_in.append(m.FadeIn(self.slide_subtitle_mobj))
        return fade_in

    def animate_fade_out_title_and_subtitle(self) -> list[m.Animation]:
        fade_out = []
        if self.slide_title_mobj is not None and self.is_in_scene(self.slide_title_mobj):
            fade_out.append(m.FadeOut(self.slide_title_mobj))
        if self.slide_subtitle_separator_mobj is not None and self.is_in_scene(self.slide_subtitle_separator_mobj):
            fade_out.append(m.FadeOut(self.slide_subtitle_separator_mobj))
        if self.slide_subtitle_mobj is not None and self.is_in_scene(self.slide_subtitle_mobj):
            fade_out.append(m.FadeOut(self.slide_subtitle_mobj))
        return fade_out

    def animate_replace_title(self, title_text: str) -> m.AnimationGroup:

        empy_string_values = [None, "", " "]  # values that are considered empty
        self.slide_title_text = title_text

        # case 1: old title is present and new title is empty
        if self.slide_title_text in empy_string_values:
            return m.AnimationGroup(*self.animate_fade_out_title_and_subtitle())

        # case 2: old title is empty and new title is present
        if self.slide_title_mobj is None or not self.is_in_scene(self.slide_title_mobj):
            self.slide_title_mobj = T.title_text(
                title_text,
                scale=self.slide_title_scale,
                color=self.slide_title_color
            )
            return m.AnimationGroup(*self.animation_fade_in_title_and_subtitle())

        # case 3: old title is present and new title is present
        animations = []
        new_title = T.title_text(
            title_text,
            scale=self.slide_title_scale,
            color=self.slide_title_color
        )
        animations.append(m.Transform(self.slide_title_mobj, new_title))

        # adjust the subtitle separator position
        if self.slide_subtitle_separator_mobj is not None and self.is_in_scene(self.slide_subtitle_separator_mobj):
            new_separator = T.title_text(
                self.slide_subtitle_separator,
                scale=self.slide_subtitle_separator_scale,
                color=self.slide_subtitle_separator_color
            )
            new_separator.next_to(
                new_title, m.RIGHT,
                buff=self.slide_subtitle_separator_buffer_left
            )
            animations.append(m.Transform(self.slide_subtitle_separator_mobj, new_separator))

        if self.slide_subtitle_text is not None and self.is_in_scene(self.slide_subtitle_mobj):
            new_subtitle = T.title_text(
                self.slide_subtitle_text,
                scale=self.slide_subtitle_scale,
                color=self.slide_subtitle_color
            )
            new_subtitle.next_to(
                new_separator, m.RIGHT,
                buff=self.slide_subtitle_separator_buffer_right
            )
            animations.append(m.Transform(self.slide_subtitle_mobj, new_subtitle))

        return m.AnimationGroup(*animations)


class TEST(TEMPLATE_SILDES):

    def construct(self):
        self.play(
            m.FadeIn(self.slide_title_mobj),
            m.FadeIn(self.slide_subtitle_separator_mobj),
            m.FadeIn(self.slide_subtitle_mobj),
        )

        self.play(
            *self.animation_replace_subtitle("NEW SUBTITLE 1"),
        )

        self.play(
            *self.animation_replace_subtitle(""),
        )

        self.play(
            *self.animation_replace_subtitle("NEW SUBTITLE 2"),
        )

        self.wait(0.1)


if __name__ == '__main__':
    # Import manim library
    import os
    from pathlib import Path

    # FLAGS = "-s --disable_caching"
    FLAGS = "-pqm"
    SCENE = "TEST"

    # os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")
    file_path = Path(__file__).resolve()
    # script_name = file_path.stem

    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")
    # os.system(f"manim --disable_caching --save_sections -qk {file_path}")
