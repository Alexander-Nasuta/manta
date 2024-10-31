import manim as m
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyTermTextExamplesScene(MinimalSlideTemplate, VoiceoverScene):

    def construct(self):
        self.set_speech_service(
            GTTSService(lang="en"),
        )

        self.play(
            self.set_title_row(
                title="Text Utils",
                seperator=": ",
                subtitle="term_text"
            )
        )

        my_text= self.term_text("Hello World!", font_size=36)

        voiceover_text =f"""

        Hello World! 
        
        This is an A.I. generated voice.
        """
        with self.voiceover(text=voiceover_text):
            self.play(
                m.FadeIn(my_text),
            )



if __name__ == '__main__':
    MyTermTextExamplesScene.save_sections_without_cache()
