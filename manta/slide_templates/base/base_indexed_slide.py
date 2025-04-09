import manim as m

from manta.manim_editor import PresentationSectionType

from manta.slide_templates.base.base_slide import BaseSlide


class BaseIndexedSlide(BaseSlide):
    index_prefix: str = ""
    index_counter: int = 0

    pdf_keyframe_suffix: str = "_pdf_kf"

    def get_section_name(self, is_keyframe: bool = False) -> str:
        if is_keyframe:
            return f"{self.index_prefix}{self.index_counter:02}{self.pdf_keyframe_suffix}"
        return f"{self.index_prefix}{self.index_counter:02}"

    def play(
            self,
            *args,
            subcaption=None,
            subcaption_duration=None,
            subcaption_offset=0,
            min_run_time=0,
            **kwargs,
    ):
        # not changing the parameterization of the play method
        # changing the signature of the play method might leds to issues in my experience
        # and especially when using the wait method
        section_type = kwargs.pop("presentation_section_type", None)
        if section_type is None:
            section_type = PresentationSectionType.NORMAL

        is_pdf_keyframes = kwargs.pop("is_pdf_keyframes", False)

        is_section = kwargs.pop("is_section", True)

        if is_section:
            self.next_section(f"{self.get_section_name(is_keyframe=is_pdf_keyframes)}", type=section_type)
            # self.next_slide(f"{self.get_section_name(is_keyframe=is_pdf_keyframes)}", type=section_type)

        animation_group = m.AnimationGroup(*args)
        group_runtime = animation_group.run_time

        # somehow the animation for the slide stops one frame before
        # the last frame animation
        # to solve this issue, I added a dummy animation with a hidden circle as a workaround
        hidden_circle = m.Circle().set_opacity(0).scale(0.00001)

        super().play(
            animation_group,
            m.FadeOut(hidden_circle, run_time=max(group_runtime+0.1, min_run_time)),
            **kwargs)

    def play_without_section(
            self,
            *args,
            **kwargs,
    ):
        super().play(*args, **kwargs)

