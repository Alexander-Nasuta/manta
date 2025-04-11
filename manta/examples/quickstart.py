from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

from manta.components.neural_networks_utils import NeuralNetworkUtils
from manta.components.qr_code_utils import QrCodeUtils
from manta.components.uml_utils import UmlUtils
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate

import manim as m
import manta.docbuild.image_path_utils as path_utils

from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from manta.slide_templates.minimal.minimal_intro_slide import MinimalIntroSlide

import manta.docbuild.image_path_utils as paths
from manta.slide_templates.classic.classic_slide_template import ClassicSlideTemplate


class QuickstartIntroSlide(MinimalIntroSlide, VoiceoverScene):
    # replace 'paths.get_coala_background_abs_path()' with a string path to a background image
    # this can be a relative path or an absolute path
    background_picture = paths.get_coala_background_abs_path()
    background_shift = m.UP * 0.75  # shift the background a bit up
    background_scale = 1.05  # make the background a bit bigger

    logo_paths = [
        # feel free to replace these paths with your own logo paths
        # if your logos is called 'my_logo.svg' and is located in the same directory as this file, you can use
        # 'my_logo.svg' as the path
        paths.get_manta_logo_abs_path(),
        paths.get_rwth_logo_abs_path(),
    ]

    title = "Manta"
    subtitle = "A Framework for creating Presentation Slides \n with Manim and Python"
    subtitle_color = CatppuccinMochaTheme.rosewater

    def construct(self):
        self.set_speech_service(
            GTTSService(lang="en"),
        )

        self.play(self.fade_in_slide())
        voiceover_text = f"""

        Hello World! 

        This is a brief showcase of the Manta framework.
        Please note that you show have a basic understanding of Manim and the Manim Editor to follow along.
        For that please refer to the Manim documentation.
        """
        with self.voiceover(text=voiceover_text):
            self.wait(2)
        self.play(self.overlay_scene())
        self.remove_everything()  # remove everything, so that the overlay scene is not shown in the next slide




from manta.slide_templates.title_slide import TitleSlide


class QuickstartAgenda(TitleSlide, VoiceoverScene):

    def construct(self):
        self.set_speech_service(
            GTTSService(lang="en"),
        )

        voiceover_text = f"""

        Manta is a framework for creating animation and presentation slides with Manim and Python.
        
        """

        with self.voiceover(text=voiceover_text):
            self.play(
                self.set_title_row(
                    title="Agenda",
                    seperator=": ",
                    subtitle="Mantas Key Features"
                ),
            )

        agenda_point_a = self.icon_textbox(
            text="Slide Templates",
            icon='alpha-a-box-outline',
            width=self.content_width,
        )
        agenda_point_a.to_edge(m.UP, buff=1.0)

        agenda_point_b = self.icon_textbox(
            text="Icons",
            icon='alpha-b-box-outline',
            width=self.content_width,
        )
        agenda_point_b.next_to(agenda_point_a, m.DOWN, buff=self.med_large_buff)

        agenda_point_c = self.icon_textbox(
            text="Components",
            icon='alpha-c-box-outline',
            width=self.content_width,
        )
        agenda_point_c.next_to(agenda_point_b, m.DOWN, buff=self.med_large_buff)

        animation_group = m.AnimationGroup(
            *[m.FadeIn(elem) for elem in [agenda_point_a, agenda_point_b, agenda_point_c]],
            lag_ratio=0.15
        )

        voiceover_text = f"""

        This Presentation is a showcase a few of the key features of Manta.

        """
        with self.voiceover(text=voiceover_text):
            self.play(
                animation_group
            )



        # indicate the first a agenda point
        surrounding_rect = m.SurroundingRectangle(
            agenda_point_a,
            corner_radius=0.125, color=self.blue)

        voiceover_text = f"""

        Lets start with Mantas slide templates.

        """
        with self.voiceover(text=voiceover_text):
            self.play(
                m.Create(surrounding_rect)
            )


        self.play(
            m.FadeOut(surrounding_rect)
        )

        self.fade_out_scene()



class QuickstartMinimalSlideTemplate(MinimalSlideTemplate, VoiceoverScene):

    index_prefix = "A"



    def construct(self):
        # when creating standalone scenes you dont need to set the following parameters
        # this example does needs to reset the attributes from previous classes because the classes are
        # changed dynamically
        self._title_mobject = None
        self._title_seperator_mobject = None
        self._subtitle_mobject = None
        self.default_title_seperator = None
        self._last_subtitle_value = None
        self.index_counter = 0

        voiceover_text = f"""

        What you see now is Mantas minimal slide template.
        
        Manta extends the Manim Scene class by adding several extra functions to simplify the process of creating slides.
        Default values of the added functions are realised by class attributes.
        For details please have a look at the documentation.
        
        Lets get back to the minimal slide template.
    
        Slide templates feature a title in the top left corner and a slide index in the bottom left corner.
        
        The slide index is automatically increasing with each slide. 
        One slide corresponds to one animation and is triggered my Manims play function.
        In presentation mode, the Manim editor, the play animation will play and stop at the last frame of the animation  
        till you press the 'nextslide' button.

        """
        with self.voiceover(text=voiceover_text):
            self.play(
                self.change_title(title="Minimal Slide Template"),
                min_run_time=5 # set the min run time to 5 seconds, so there is enough time to read the text
            )

        voiceover_text = f"""
        
        You can change the title by calling the change_title function.
        Note how the slide index is automatically updated.
        """
        function_text = self.term_text('change_title("Changed Title")')
        with self.voiceover(text=voiceover_text):
            self.play(
                self.change_title("Changed Title"),
                m.FadeIn(function_text),
            )


        voiceover_text = f"""
        The Minimal Slide Template also supports subtitles.
        You can change the subtitle by calling the change_subtitle function.
        
        By default title and subtitle are separated by a colon.
        This can be changed by setting the default_title_seperator parameter.
        """
        with self.voiceover(text=voiceover_text):
            self.default_title_seperator = ": "
            self.play(
                self.change_subtitle("A Subtitle"),
                m.Transform(function_text, self.term_text('change_subtitle("A Subtitle")')),
            )
        voiceover_text = f"""
        
        you can also change the seperator by calling the change_title_seperator function.
        """
        with self.voiceover(text=voiceover_text):
            self.play(
                self.change_title_seperator("//"),
                m.Transform(function_text, self.term_text('change_title_seperator("//")')),
            )

        self.logo_paths = [path_utils.get_rwth_logo_abs_path()]
        voiceover_text = f"""

        you can add logos by setting the logo_paths parameter and calling the add_logos function.
        """

        with self.voiceover(text=voiceover_text):
            self.play(
                self.add_logos(),
                m.Transform(function_text, self.term_text('logo_paths = [<<path to logo>>]\nadd_logos()').move_to(m.ORIGIN)),
            )


        self.fade_out_scene()



class QuickstartClassicSlideTemplate(ClassicSlideTemplate, VoiceoverScene):
    index_prefix = "A"

    def construct(self):
        # when creating standalone scenes you dont need to set the following parameters
        # this example does needs to reset the attributes from previous classes because the classes are
        # changed dynamically
        self._title_mobject = None
        self._title_seperator_mobject = None
        self._subtitle_mobject = None
        self.default_title_seperator = None
        self._last_subtitle_value = None
        self.index_counter = 0

        self.logo_paths = [path_utils.get_rwth_logo_abs_path()]

        voiceover_text = f"""

        What you see now is Mantas classic slide template.
        It is supposed to look like a Powerpoint slide.
        
        It has all features of the minimal slide template.
        Additionally it has two seperator lines at the top and bottom of the slide.
        Moreover the default text size is smaller than in the minimal slide template.

        """
        with self.voiceover(text=voiceover_text):
            self.play(
                # set the title row set the title and subtitle and the seperator at once
                self.set_title_row(title="Class Slide Template", seperator=": ", subtitle="Powerpoint Style"),
                self.add_seperator_lines(),
                self.add_logos(),
                min_run_time=5  # set the min run time to 5 seconds, so there is enough time to read the text
            )

        self.fade_out_scene()


class QuickstartAgenda2(TitleSlide, VoiceoverScene):

    def construct(self):
        self._title_mobject = None
        self._title_seperator_mobject = None
        self._subtitle_mobject = None
        self.default_title_seperator = None
        self._last_subtitle_value = None
        self.index_counter = 0

        self.set_speech_service(
            GTTSService(lang="en"),
        )

        self.play(
            self.set_title_row(
                title="Agenda",
                seperator=": ",
                subtitle="Mantas Key Features"
            ),
        )


        agenda_point_a = self.icon_textbox(
            text="Slide Templates",
            icon='alpha-a-box-outline',
            width=self.content_width,
        )
        agenda_point_a.to_edge(m.UP, buff=1.0)

        agenda_point_b = self.icon_textbox(
            text="Icons",
            icon='alpha-b-box-outline',
            width=self.content_width,
        )
        agenda_point_b.next_to(agenda_point_a, m.DOWN, buff=self.med_large_buff)

        agenda_point_c = self.icon_textbox(
            text="Components",
            icon='alpha-c-box-outline',
            width=self.content_width,
        )
        agenda_point_c.next_to(agenda_point_b, m.DOWN, buff=self.med_large_buff)

        animation_group = m.AnimationGroup(
            *[m.FadeIn(elem) for elem in [agenda_point_a, agenda_point_b, agenda_point_c]],
            lag_ratio=0.15
        )


        self.play(
                animation_group
        )

        # indicate the first a agenda point
        surrounding_rect = m.SurroundingRectangle(
            agenda_point_b,
            corner_radius=0.125, color=self.blue)

        voiceover_text = f"""

        Lets move to Mantas Nerd Font Icons.

        """
        with self.voiceover(text=voiceover_text):
            self.play(
                m.Create(surrounding_rect)
            )

        self.play(
            m.FadeOut(surrounding_rect)
        )

        self.fade_out_scene()


class QuickstartIcons(MinimalSlideTemplate, VoiceoverScene):
    index_prefix = "B"

    def construct(self):
        # when creating standalone scenes you dont need to set the following parameters
        # this example does needs to reset the attributes from previous classes because the classes are
        # changed dynamically
        self._title_mobject = None
        self._title_seperator_mobject = None
        self._subtitle_mobject = None
        self.default_title_seperator = None
        self._last_subtitle_value = None
        self.index_counter = 0

        voiceover_text = f"""

        What you see now is Mantas Icon usage.
        In Manta you can use all available Nerd Font Icons.
        Nerd Fonts are monospace fonts that have been patched to include a large number of icons.
        These Fonts are typically used in text editors like NeoVim.
        Manta uses the Nerd Font Icons to offer a wide range of icons for your animations and slides.
        You can find the list of available icons when you jump to definition of the symbol function in your Code Editor.
        The Icons can be created passing the name of the icon to the symbol function or their unicode value.
        """

        cube_icon = self.symbol("cube")
        description  = self.term_text('symbol("cube")').next_to(cube_icon, m.DOWN, buff=self.small_buff)

        with self.voiceover(text=voiceover_text):
            self.play(
                m.FadeIn(cube_icon),
                m.FadeIn(description),
                self.set_title_row("Icons", seperator=": ", subtitle="Baisc Usage"),
                min_run_time=5  # set the min run time to 5 seconds, so there is enough time to read the text
            )

        voiceover_text = f"""
        
        Here are some more examples of icons with their names and unicode values.
        """

        no_rows = 6
        no_cols = 5
        item_per_page = no_rows * no_cols

        from manta.components.nerdfont_icons import SYMBOLS_UNICODE

        icon_key_list = list(SYMBOLS_UNICODE.keys())

        def icon_group(idx):
            icon_name = icon_key_list[idx]
            icon_unicode = SYMBOLS_UNICODE[icon_name]

            m_symbol = self.symbol(icon_unicode)
            m_name = self.term_text(icon_name, font_size=self.font_size_script)
            m_unicode = self.term_text(
                f"0x{icon_unicode:04X}",
                font_size=self.font_size_script,
                font_color=self.blue
            )

            m_name.move_to(m.DOWN * 0.35)
            m_unicode.move_to(m.DOWN * 0.6)

            return m.VGroup(m_symbol, m_name, m_unicode)

        offset = 7331
        table_content = [
            [
                icon_group(idx=i * no_cols + j + offset) for j in range(no_cols)
            ] for i in range(no_rows)
        ]
        table = m.MobjectTable(
            table_content,
            v_buff=0.1,
            h_buff=0.1,
            # don't show v adn h lines
            line_config={"stroke_width": 0},
        )

        self.play(
            m.FadeOut(cube_icon),
            m.FadeOut(description),
        )

        with self.voiceover(text=voiceover_text):
            self.play(
            self.set_title_row("Icons", seperator=": ", subtitle="a few examples"),
                m.FadeIn(table),
            )

        self.fade_out_scene()


class QuickstartAgenda3(TitleSlide, VoiceoverScene):

    def construct(self):
        self._title_mobject = None
        self._title_seperator_mobject = None
        self._subtitle_mobject = None
        self.default_title_seperator = None
        self._last_subtitle_value = None
        self.index_counter = 0

        self.set_speech_service(
            GTTSService(lang="en"),
        )

        self.play(
            self.set_title_row(
                title="Agenda",
                seperator=": ",
                subtitle="Mantas Key Features"
            ),
        )


        agenda_point_a = self.icon_textbox(
            text="Slide Templates",
            icon='alpha-a-box-outline',
            width=self.content_width,
        )
        agenda_point_a.to_edge(m.UP, buff=1.0)

        agenda_point_b = self.icon_textbox(
            text="Icons",
            icon='alpha-b-box-outline',
            width=self.content_width,
        )
        agenda_point_b.next_to(agenda_point_a, m.DOWN, buff=self.med_large_buff)

        agenda_point_c = self.icon_textbox(
            text="Components",
            icon='alpha-c-box-outline',
            width=self.content_width,
        )
        agenda_point_c.next_to(agenda_point_b, m.DOWN, buff=self.med_large_buff)

        animation_group = m.AnimationGroup(
            *[m.FadeIn(elem) for elem in [agenda_point_a, agenda_point_b, agenda_point_c]],
            lag_ratio=0.15
        )


        self.play(
                animation_group
        )

        # indicate the first a agenda point
        surrounding_rect = m.SurroundingRectangle(
            agenda_point_c,
            corner_radius=0.125, color=self.blue)

        voiceover_text = f"""

        Lets move to Mantas Components.

        """
        with self.voiceover(text=voiceover_text):
            self.play(
                m.Create(surrounding_rect)
            )

        self.play(
            m.FadeOut(surrounding_rect)
        )

        self.fade_out_scene()


ascii_art = r"""
================================================.
     .-.   .-.     .--.                         |
    | OO| | OO|   / _.-' .-.   .-.  .-.   .''.  |
    |   | |   |   \  '-. '-'   '-'  '-'   '..'  |
    '^^^' '^^^'    '--'                         |
===============.  .-.  .================.  .-.  |
               | |   | |                |  '-'  |
               | |   | |                |       |
               | ':-:' |                |  .-.  |
               |  '-'  |                |  '-'  |
==============='       '================'       |
"""

class QuickstartComponents(QrCodeUtils, UmlUtils, NeuralNetworkUtils, MinimalSlideTemplate, VoiceoverScene):
    index_prefix = "C"

    def construct(self):
        # when creating standalone scenes you dont need to set the following parameters
        # this example does needs to reset the attributes from previous classes because the classes are
        # changed dynamically
        self._title_mobject = None
        self._title_seperator_mobject = None
        self._subtitle_mobject = None
        self.default_title_seperator = None
        self._last_subtitle_value = None
        self.index_counter = 0

        self.set_speech_service(
            GTTSService(lang="en"),
        )

        voiceover_text = f"""
        
        For providing useful animationobjects, such as Charts and Diagrams, Manta uses an object oriented approach.
        
        """

        with self.voiceover(text=voiceover_text):
            self.play(
                self.set_title_row(title="Components"),
            )

        example_class = self.term_text(
            'class MyMantaScene(<<ComponentClass>>, MinimalSlideTemplate):',
            t2c={
                "class": self.blue,
                "ComponentClass": self.yellow,
                "<<": self.font_color_secondary,
                ">>": self.font_color_secondary,
            }
        )

        example_class.move_to(m.ORIGIN)

        voiceover_text = f"""
        The utility class can be used by extending the class using pythons multiple inheritance feature.
        Thereby all the configuration a like color theming and font sizes will be applied to the utilityclass functions.
        """
        with self.voiceover(text=voiceover_text):
            self.play(
                m.FadeIn(example_class),
            )

        self.play_without_section(
            m.FadeOut(example_class)
        )

        some_text = self.term_paragraph(ascii_art)
        wrapped_ascii_art = self.wrap_with_rectangle(some_text).shift(m.UP)

        code_text = self.term_text(
            f"some_text = self.term_paragraph(ascii_art)\nwrapped_ascii_art = self.wrap_with_rectangle(some_text)",
            t2c={
                "self": self.blue,
                "wrap_with_rectangle": self.yellow,
            }
        )

        code_text.next_to(wrapped_ascii_art, m.DOWN, buff=self.med_small_buff)

        voiceover_text = f"""
        Here you see an example of the RectangleUtils class.
        The wrap_with_rectangle function allows to wrap a Manim Object with a rectangle, wich is useful for creating slides.
        
        """
        with self.voiceover(text=voiceover_text):
            self.play(
                self.set_title_row("Component", seperator=": ", subtitle="RectangleUtils (included by default)"),
            m.FadeIn(wrapped_ascii_art),
                m.FadeIn(code_text),
            )

        icon_text_box1 = self.icon_title_bulletpoints_textbox(
            [
                ("Extrovert", ["Im an extrovert.", "I love to talk to people."]),
                ("Introvert", ["Im an introvert.", "It's exhausting for me to talk to people."]),
            ],
            icon="users", # can be any nerd font icon
        )

        code_text2 = self.term_paragraph(
            """
            icon_text_box = self.icon_title_bulletpoints_textbox(
                [
                    ("Extrovert", ["Im an extrovert.", "I love to talk to people."]),
                    ("Introvert", ["Im an introvert.", "It's exhausting for me to talk to people."]),
                ],
                icon="users", # can be any nerd font icon
            )
            """,
            t2c={
                '"Extrovert"': self.green,
                '"Im an extrovert."': self.green,
                '"I love to talk to people."': self.green,
                '"Introvert"': self.green,
                '"Im an introvert."': self.green,
                '"It\'s exhausting for me to talk to people."': self.green,
                '"users"': self.green,
                "self": self.blue,
                "wrap_with_rectangle": self.yellow,
                '# can be any nerd font icon': self.font_color_secondary,
            }
        )

        icon_text_box1.shift(m.UP * 1.5)
        code_text2.next_to(icon_text_box1, m.DOWN, buff=self.med_small_buff)

        voiceover_text = f"""
        Another function of the RectangleUtils class is the icon_title_bulletpoints_textbox function.
        It allows to create a bulletpointlist.
        
        Manta features a lot of utilities around bulletpointslists.
        """
        with self.voiceover(text=voiceover_text):
            self.play(
                m.ReplacementTransform(wrapped_ascii_art, icon_text_box1),
                m.ReplacementTransform(code_text, code_text2)
            )

        class PersonClass:
            name: str
            _age: int | float | None

            def say_hello(self) -> str:
                return f"Hello, my name is {self.name}."

        person_uml_class_diagram = self.uml_class_diagram(PersonClass).scale(0.5)

        code_text3 = self.term_text(
            "uml_class_diagram = self.uml_class_diagram(PersonClass)",
            t2c={
                "self": self.blue,
                "uml_class_diagram": self.yellow,
                "PersonClass": self.font_color_secondary,
            }
        )

        person_uml_class_diagram.shift(m.UP * 1)
        code_text3.next_to(person_uml_class_diagram, m.DOWN, buff=self.med_small_buff)

        voiceover_text = f"""
        
        Here are some more examples:
        
        The UML-Utils Component allows the creation of UML class diagrams for a given Python class.
        
        """
        with self.voiceover(text=voiceover_text):
            self.play(
                self.set_title_row("Component", seperator=": ", subtitle="UmlUtils"),
                m.ReplacementTransform(icon_text_box1, person_uml_class_diagram),
                m.ReplacementTransform(code_text2, code_text3)
            )


        nn = self.simple_neural_network()
        nn.scale(2.0)  # make the network a bit bigger

        code_text4 = self.term_text(
            "nn = self.simple_neural_network()",
            t2c={
                "self": self.blue,
                "simple_neural_network": self.yellow,
            }
        )

        code_text4.next_to(nn, m.DOWN, buff=self.med_small_buff)
        voiceover_text = f"""
        The NeuralNetworkUtils Component allows the creation of neural networks.
        """
        with self.voiceover(text=voiceover_text):
            self.play(
                self.set_title_row(title="Component", seperator=": ", subtitle="NeuralNetworkUtils"),
                m.ReplacementTransform(person_uml_class_diagram, nn),
                m.ReplacementTransform(code_text3, code_text4)
            )

        python_qr_code = self.qr_code("https://www.python.org/",
                                      icon="language-python",
                                      data_shape='circles',
                                      corner_color=self.blue,
                                      icon_color=self.yellow,
                                      icon_size=4,  # make the icon 5 qr code pixels wide
                                      )

        code_text5 = self.term_text(
            "python_qr_code = self.qr_code('https://www.python.org/', icon='language-python')",
            t2c={
                "self": self.blue,
                "'https://www.python.org/'": self.green,
                "'language-python'": self.green,
            }
        )

        python_qr_code.shift(m.UP * 1)
        code_text5.next_to(python_qr_code, m.DOWN, buff=self.med_small_buff)

        voiceover_text = f"""
        The QR Code Component allows the creation of QR codes.
        """
        with self.voiceover(text=voiceover_text):
            self.play(
                self.set_title_row("Component", seperator=": ", subtitle="QrCodeUtils"),
                m.ReplacementTransform(nn, python_qr_code),
                m.ReplacementTransform(code_text4, code_text5)
            )

        self.fade_out_scene()


class QuickstartOutro(MinimalIntroSlide, VoiceoverScene):
    # replace 'paths.get_coala_background_abs_path()' with a string path to a background image
    # this can be a relative path or an absolute path
    background_picture = paths.get_coala_background_abs_path()
    background_shift = m.UP * 0.75  # shift the background a bit up
    background_scale = 1.05  # make the background a bit bigger

    logo_paths = [
        # feel free to replace these paths with your own logo paths
        # if your logos is called 'my_logo.svg' and is located in the same directory as this file, you can use
        # 'my_logo.svg' as the path
        paths.get_manim_logo_abs_path(),
        paths.get_manta_logo_abs_path()
    ]

    title = "Manta"
    subtitle = "Thanks for watching!"
    subtitle_color = CatppuccinMochaTheme.rosewater

    def construct(self):
        self.set_speech_service(
            GTTSService(lang="en"),
        )

        self.play(self.fade_in_slide())
        voiceover_text = f"""

        That's it for the quickstart.
        If you want to learn more about Manta, please have a look at the documentation and the example gallery.
        There you will find a lot of examples and alongside the code to recreate the examples.
        
        Thanks for watching!
        """
        with self.voiceover(text=voiceover_text):
            self.wait(2)

        self.play(self.overlay_scene())
        self.remove_everything()  # remove everything, so that the overlay scene is not shown in the next slide








class QuickstartExample(MinimalSlideTemplate):

    def construct(self):

        ################################################################################################################
        #
        #   NOTE: this example changes classes dynamically to show different slides
        #         this is not recommended for production code. Use multiple classes instead and create a
        #         presentation using Manim Editor.
        #
        #         This code only changes classes dynamically to be able to show the output in the documentation as
        #         one single video.
        #
        ################################################################################################################

        # Intro Slides
        self.__class__ = QuickstartIntroSlide
        QuickstartIntroSlide.construct(self)

        # Agenda Slides
        self.__class__ = QuickstartAgenda
        QuickstartAgenda.construct(self)

        # Minimal Slide Template
        self.__class__ = QuickstartMinimalSlideTemplate
        QuickstartMinimalSlideTemplate.construct(self)

        # Classic Slide Template
        self.__class__ = QuickstartClassicSlideTemplate
        QuickstartClassicSlideTemplate.construct(self)

        # Agenda Slides
        self.__class__ = QuickstartAgenda2
        QuickstartAgenda2.construct(self)

        # Icons
        self.__class__ = QuickstartIcons
        QuickstartIcons.construct(self)

        # Agenda
        self.__class__ = QuickstartAgenda2
        QuickstartAgenda2.construct(self)

        # Components
        self.__class__ = QuickstartComponents
        QuickstartComponents.construct(self)

        self.__class__ = QuickstartOutro
        QuickstartOutro.construct(self)




if __name__ == '__main__':
    QuickstartExample.render_video_medium()
