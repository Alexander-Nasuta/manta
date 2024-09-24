import manim as m
from manim_editor import PresentationSectionType

from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from manta.padding_style.manta_padding import MantaPadding
from manta.slide_templates.base.base_indexed_slide import BaseIndexedSlide


class BaseColorSlide(CatppuccinMochaTheme, MantaPadding, BaseIndexedSlide):

    def setup(self):
        super().setup()

        self.camera.background_color = self.background_color
        self.next_section(self.get_section_name(), PresentationSectionType.NORMAL)

    def overlay_scene(self, color: str = None, opacity: float = 1.0,
                      create_animation: m.Transform = m.FadeIn) -> m.Transform:
        overlay_color = self.camera.background_color if color is None else color
        overlay = m.Rectangle(width=self.scene_width, height=9, color=overlay_color, fill_color=overlay_color, fill_opacity=opacity)
        overlay.z_index = self.get_max_z_index() + 1
        return create_animation(overlay)
