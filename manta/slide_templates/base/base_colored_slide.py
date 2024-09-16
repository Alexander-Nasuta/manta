
from manim_editor import PresentationSectionType

from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from manta.padding_style.manta_padding import MantaPadding
from manta.slide_templates.base.base_indexed_slide import BaseIndexedSlide


class BaseColorSlide(CatppuccinMochaTheme, MantaPadding, BaseIndexedSlide):

    def setup(self):
        super().setup()

        self.camera.background_color = self.background_color
        self.next_section(self.get_section_name(), PresentationSectionType.NORMAL)

