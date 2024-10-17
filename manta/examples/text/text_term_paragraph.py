






import manim as m

from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate

mono_sketch ="""
            Client                             Server                 
               ■                                  ■                 
               │      Establish TCP Connection      │                 
┌ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ─ ─ 
            SYN├───────────────────────────────────>░SYN             │
│              │                                    ░ACK              
            ACK│<───────────────────────────────────░                │
└ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ─ ─ 
               │                                    │                 
               │                                    │                 
               │         SSL/TLS Handshake          │                 
┌ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ─ ─ 
    ClientHello░───────────────────────────────────>░                │
│              ░                                    ░Server Hello     
    Certificate░<───────────────────────────────────░Certificate     │
│  verification░                                    ░                 
               ░                                    ░                │
│     ClientKey░<──────────────────────────────────>░ServerFinished   
       Exchange│                                    │                │
└ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ─ ─ 
               │                                    │                 
               │     Encrypted Application Data     │                 
┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ─ ─ 
          HTTP │<──────────────────────────────────>│HTTP            │
│          GET │                                    │Response         
 ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘
               │                                    │                 
               ■                                  ■                 
"""

class MyTermTextExamplesScene(MinimalSlideTemplate):

    def construct(self):

        mono_space_mobject = self.term_paragraph(
            mono_sketch,
        ).scale_to_fit_height(6)

        self.play(
            self.set_title_row(
                title="Text Utils",
                seperator=": ",
                subtitle="term_paragraph"
            ),
            m.FadeIn(mono_space_mobject),
        )


if __name__ == '__main__':
    MyTermTextExamplesScene.render_video_medium()