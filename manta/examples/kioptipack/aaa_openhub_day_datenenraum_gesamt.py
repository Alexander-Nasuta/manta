import manim as m

from color_theme.carolus.corolus_theme import CarolusTheme
from examples.kioptipack.aaa_open_hub_day_datenfluss import SemantischerDatenraum
from examples.kioptipack.aaa_openhub_day_intro import OpenHubDayDatenraumIntro
from manta.slide_templates.minimal.minimal_intro_slide import MinimalIntroSlide


class OpenHubDayDatenraumGesamt(CarolusTheme, MinimalIntroSlide):


    def construct(self):
        # Intro Slides
        self.__class__ = OpenHubDayDatenraumIntro
        OpenHubDayDatenraumIntro.construct(self)

        # Agenda Slides
        self.__class__ = SemantischerDatenraum
        SemantischerDatenraum.construct(self)





if __name__ == '__main__':
    #OpenHubDayDatenraumGesamt.render_video_medium()
    OpenHubDayDatenraumGesamt.save_sections_without_cache()
