import types
from types import MappingProxyType as mappingproxy
from typing import get_type_hints
from collections import namedtuple

import manim as m
import inspect

from rich.cells import cell_len
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from elements.rectangle_utils import RectangleUtils
from manta.logger import log

from manta.elements.shapes import ShapeUtils

MethodMeta = namedtuple('MethodMeta', ['name', 'parameters_with_types', 'return_type'])


class UmlUtils(RectangleUtils):

    @staticmethod
    def _extract_type_str(type_str: str) -> str:
        if type_str.startswith("<class '") and type_str.endswith("'>"):
            # return the type string without the "<class '" and "'>"
            return type_str[8:-2]
        else:
            return type_str

    @staticmethod
    def _extract_parameters_with_types(parameters: mappingproxy) -> list[tuple[str, str]]:
        result = []
        for name, param in parameters.items():
            if name == "self":
                continue
            param_type = param.annotation if param.annotation != param.empty else 'Unknown'
            result.append((name, UmlUtils._extract_type_str(str(param_type))))
        return result

    @staticmethod
    def _print_uml_class(attributes_with_types: dict[str, str], methods: list[MethodMeta], class_name: str) -> None:
        # Create a Console object
        console = Console()

        class_attributes_rich_text = Text()

        for e in attributes_with_types:
            visibility = "+"

            if e.startswith("_"):
                visibility = "~"
            if e.startswith("__"):
                visibility = "-"

            class_attributes_rich_text.append(f"{visibility} ", style="bold cyan")
            class_attributes_rich_text.append(f"{e}", style="bold green")
            class_attributes_rich_text.append(f":  ", style="bold cyan")
            class_attributes_rich_text.append(f"{attributes_with_types[e]}", style="bold yellow")
            class_attributes_rich_text.append("\n")

        class_methods_rich_text = Text()
        for e in methods:
            visibility = "+"

            if e.name.startswith("_"):
                visibility = "#"
            if e.name.startswith("__"):
                visibility = "-"

            class_methods_rich_text.append(f"{visibility} ", style="bold cyan")
            class_methods_rich_text.append(f"{e.name}", style="bold green")
            class_methods_rich_text.append("(", style="bold cyan")
            for i, (param_name, param_type) in enumerate(e.parameters_with_types):
                class_methods_rich_text.append(f"{param_name}", style="bold magenta")
                class_methods_rich_text.append(": ", style="bold cyan")
                class_methods_rich_text.append(f"{param_type}", style="bold yellow")
                if i < len(e.parameters_with_types) - 1:
                    class_methods_rich_text.append(", ", style="bold cyan")
            class_methods_rich_text.append("): ", style="bold cyan")
            class_methods_rich_text.append(f"{e.return_type}", style="bold yellow")
            class_methods_rich_text.append("\n")

        # Split the text into lines and find the width of the widest line
        attr_lines = class_attributes_rich_text.split("\n")
        method_lines = class_methods_rich_text.split("\n")

        max_width_attr = max(cell_len(line.plain) for line in attr_lines)
        max_width_method = max(cell_len(line.plain) for line in method_lines)
        max_width = max(max_width_attr, max_width_method)

        rich_seperator = Text("─" * max_width + "\n", style="blue")

        # Create a Panel with some content
        panel = Panel(
            class_attributes_rich_text + rich_seperator + class_methods_rich_text,
            title=Text(f"{class_name}", style="bold orange"),
            expand=False,
            border_style="blue",
            # width=1000  # Set a very large width
        )
        # Print the Panel to the console
        console.print(panel)

    @staticmethod
    def _get_attributes_with_types(klass: type) -> dict[str, str]:
        return {
            attr: UmlUtils._extract_type_str(str(typ))
            for attr, typ
            in klass.__annotations__.items()
        }

    @staticmethod
    def _get_methods_with_types(klass: type, unknown_return_type: str = 'Any') -> list[MethodMeta]:
        # Get all methods of the class
        methods_raw = [func for func in dir(klass) if
                       callable(getattr(klass, func)) and not func.startswith("__")]

        methods = [
            MethodMeta(
                name=str(func_),
                parameters_with_types=UmlUtils._extract_parameters_with_types(
                    inspect.signature(getattr(klass, func_)).parameters
                ),
                return_type=UmlUtils._extract_type_str(
                    str(get_type_hints(getattr(klass, func_)).get('return', unknown_return_type))
                )
            ) for func_ in methods_raw
        ]
        return methods

    def uml_class_diagram(self,
                          klass: type,
                          class_name: str = None,
                          print_class_in_console: bool = True,
                          color_python_keyword: bool = True,
                          type_t2c=None,
                          visibility_color=None,
                          fields_color=None,
                          colon_separator_color=None,
                          type_color=None,
                          type_color_keywords=None,
                          type_special_characters_color=None,
                          parameters_color=None,
                          ) -> m.VGroup:
        if type_t2c is None:
            type_t2c = {}
        if class_name is None:
            class_name = klass.__name__

        # set default colors
        if visibility_color is None:
            visibility_color = self.green
        if fields_color is None:
            fields_color = self.font_color
        if colon_separator_color is None:
            colon_separator_color = self.blue
        if type_color is None:
            type_color = self.cyan
        if type_color_keywords is None:
            type_color_keywords = self.yellow
        if type_special_characters_color is None:
            type_special_characters_color = self.font_color_secondary
        if parameters_color is None:
            parameters_color = self.red

        # will be passed as t2c when creating the text for the class diagram
        pyhon_keyword_color_map = {
            # "None": m.RED,
            # "True": self.red,
            # "False": self.red,

            "str": type_color_keywords,
            "int": type_color_keywords,
            "float": type_color_keywords,
            "bool": type_color_keywords,
            "list": type_color_keywords,
            "dict": type_color_keywords,
            "tuple": type_color_keywords,
            "set": type_color_keywords,
            # "frozenset": self.yellow,
            "complex": type_color_keywords,
            "bytes": type_color_keywords,
            # "bytearray": self.yellow,
            "memoryview": type_color_keywords,
            "range": type_color_keywords,
            "slice": type_color_keywords,

            "|": type_special_characters_color,
            ",": type_special_characters_color,
            "[": type_special_characters_color,
            "]": type_special_characters_color,
            "(": type_special_characters_color,
            ")": type_special_characters_color,
            "->": type_special_characters_color,
            "~": type_special_characters_color,
        }

        if color_python_keyword:
            merged_t2c = {**pyhon_keyword_color_map, **type_t2c}
        else:
            merged_t2c = type_t2c

        attributes_with_types = self._get_attributes_with_types(klass)
        methods_with_types = self._get_methods_with_types(klass)

        if print_class_in_console:
            self._print_uml_class(
                attributes_with_types=attributes_with_types,
                methods=methods_with_types,
                class_name=class_name
            )

        # attributes group
        # the attributes consists of sub vGroups, that consists of term_texts
        # the subgroup has the following structure:
        # - visibility term_text
        # - attribute term_text
        # - colon_separator term_text
        # - type term_text
        attributes_group = m.VGroup()
        for attr, typ in attributes_with_types.items():
            visibility = "+ "
            if attr.startswith("_"):
                visibility = "~ "
            if attr.startswith("__"):
                visibility = "- "

            visibility_text, attribute_text, colon_separator_text, type_text = self.text_line(
                visibility,
                attr,
                ": ",
                typ,
                text_segment_kwargs=[
                    {},  # visibility
                    {},  # attr
                    {},  # :
                    {  # typ
                        "font_color": type_color,
                        "t2c": merged_t2c
                    }
                ]
            )

            visibility_text.set_color(visibility_color)
            attribute_text.set_color(fields_color)
            colon_separator_text.set_color(colon_separator_color)
            # type_text.set_color(self.magenta).set_color_by_t2c(merged_t2c)

            attribute_group = m.VGroup(visibility_text, attribute_text, colon_separator_text, type_text)
            attributes_group.add(attribute_group)

        attributes_group.arrange(m.DOWN, buff=0.1, aligned_edge=m.LEFT)

        # methods group
        # the methods consists of sub vGroups, that consists of term_texts
        # the subgroup has the following structure:
        # - visibility term_text
        # - method term_text
        # - open_parentheses term_text
        # - parameters term_text
        # - close_parentheses term_text
        # - colon_separator term_text
        # - return_type term_text
        methods_group = m.VGroup()
        for method in methods_with_types:
            visibility = "+ "
            if method.name.startswith("_"):
                visibility = "~ "
            if method.name.startswith("__"):
                visibility = "- "

            method_parameter = []
            method_parameter_types = []
            method_text_segments = []
            for param_name, param_type in method.parameters_with_types:
                method_parameter.append(param_name)
                method_parameter_types.append(param_type)

                method_text_segments.append(param_name)
                method_text_segments.append(": ")
                method_text_segments.append(param_type)
                method_text_segments.append(", ")

            # delete the last comma
            if len(method_text_segments):
                method_text_segments.pop()

            text_segments_args = [
                visibility,
                method.name,
                "(",
                *method_text_segments,
                ")",
                ": ",
                str(method.return_type),
            ]

            text_segments_args_kwargs = [
                {  # visibility
                    "font_color": visibility_color
                },
                {  # method
                    "font_color": fields_color
                },
                {  # (
                    "font_color": fields_color
                },
            ]

            for i, (param_name, param_type) in enumerate(zip(method_parameter, method_parameter_types)):
                text_segments_args_kwargs.append({  # param_name
                    "font_color": parameters_color,
                })
                text_segments_args_kwargs.append({  # :
                    "font_color": fields_color
                })
                text_segments_args_kwargs.append({  # param_type
                    "font_color": type_color,
                    "t2c": merged_t2c
                })
                if i < len(method_parameter) - 1:
                    text_segments_args_kwargs.append({})  # ,

            text_segments_args_kwargs.extend([
                {  # )
                    "font_color": fields_color
                },
                {  # :
                    "font_color": colon_separator_color
                },
                {  # return_type
                    "font_color": type_color,
                    "t2c": merged_t2c
                }
            ])

            text_segments = self.text_line(
                *text_segments_args,
                text_segment_kwargs=text_segments_args_kwargs
            )

            # Note: the following code was used before the text_line_kwargs was implemented.
            # It will eventually be removed

            # visibility_text = text_segments[0]
            # method_text = text_segments[1]
            # open_parentheses_text = text_segments[2]

            # parameter_segments = text_segments[3:-3]

            # close_parentheses_text = text_segments[-3]
            # return_colon_separator_text = text_segments[-2]
            # return_text = text_segments[-1]

            # parameters_name_segments = parameter_segments[::4]
            # parameters_colon_segments = parameter_segments[1::4]
            # parameters_type_segments = parameter_segments[2::4]

            # set colors
            # visibility_text.set_color(visibility_color)
            # method_text.set_color(fields_color)
            # open_parentheses_text.set_color(fields_color)
            # close_parentheses_text.set_color(fields_color)
            # return_colon_separator_text.set_color(colon_separator_color)
            # return_text.set_color(self.magenta).set_color_by_t2c(merged_t2c)

            # for i, (param_name, param_type) in enumerate(zip(parameters_name_segments, parameters_type_segments)):
            #   param_name.set_color(parameters_color)
            #   param_type.set_color(type_color)
            #   if i < len(parameters_name_segments) - 1:
            #       parameters_colon_segments[i].set_color(self.cyan)

            method_group = m.VGroup(
                *text_segments
            )
            methods_group.add(method_group)

        methods_group.arrange(m.DOWN, buff=0.1, aligned_edge=m.LEFT)

        group_max_width = max(attributes_group.width, methods_group.width)

        separator_line = m.Line(
            m.LEFT * 0.5 * group_max_width,
            m.RIGHT * 0.5 * group_max_width,
            color=self.outline_color
        )

        uml_class_group = m.VGroup(
            attributes_group,
            separator_line,
            methods_group
        )
        uml_class_group.arrange(m.DOWN, buff=self.med_small_buff, aligned_edge=m.LEFT)

        uml_rectangle = self.wrap_with_icon_and_rectangle(
            mElement=uml_class_group,
            icon_color=self.font_color,
            icon=class_name,
            direction='up',
            include_element_in_group=False,
            v_buff=self.med_small_buff
        )

        separation_line_top = uml_rectangle[-1]

        uml_class_group.next_to(separation_line_top, m.DOWN, buff=self.med_small_buff)

        separation_line_mid = separation_line_top.copy()
        separation_line_mid.move_to(separator_line.get_center())

        return m.VGroup(
            uml_rectangle,
            attributes_group,
            separation_line_mid,
            methods_group
        )
