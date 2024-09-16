import manim as m

from manta.slide_templates.indexed_slide import IndexedSlide


class ExampleIndexedSlide(IndexedSlide):

    def construct(self):
        text_mobj = self.term_text("Hello, World!")
        self.play(
            m.FadeIn(text_mobj),
        )

        self.play_without_section(
            m.Transform(text_mobj, self.term_text("Hello, Manim! No Section Increment")),
        )

        self.play(
            m.Transform(text_mobj, self.term_text("Hello, Manim!")),
        )

        self.wait(0.1)


def test_indexed_slide():
    ExampleIndexedSlide.rendering_test()