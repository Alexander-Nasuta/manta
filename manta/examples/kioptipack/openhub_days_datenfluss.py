
import manim as m
import numpy as np
from docutils.nodes import description
from pyrr.rectangle import height

from color_theme.carolus.corolus_theme import CarolusTheme
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class OpenHubDaysDatenfluss(CarolusTheme, MinimalSlideTemplate):

    index_prefix = "A"

    default_icon_color = CarolusTheme.red

    datenfluss_icon_stroke = CarolusTheme.blue

    def construct(self):
        self.play(
            self.set_title_row(
                title="Datenfluss im Datenraum",
            )
        )

        machine_icon_group = self.icon_circle(
            "robot-industrial",
            stroke_color=self.datenfluss_icon_stroke,
        ).move_to(np.array([-2, 1.5, 0]))



        broker_icon_group = self.icon_circle_svg(
            "resources/nats_icon.svg",
            svg_color=self.default_icon_color,
            stroke_color=self.yellow,
            #radius=0.425
        )
        broker_icon_group[-1].scale(1.1)

        broker_icon_group.move_to(np.array([0, 0.5, 0]))


        line_kwargs = {
            "stroke_width": 3,
            "fill_color": self.font_color_secondary,
            "color": self.font_color_secondary,
            "buff": 0.325
        }

        machine_broker_line = m.Line(
            machine_icon_group.get_center(),
            broker_icon_group.get_center(),
            **line_kwargs
        )



        database_icon_group = self.icon_circle(
            "database#3",
            stroke_color=self.datenfluss_icon_stroke,
        ).move_to(np.array([-2, -0.5, 0]))

        database_boker_line = m.Line(
            database_icon_group.get_center(),
            broker_icon_group.get_center(),
            **line_kwargs
        )



        dataspace_connector_icon_group = self.icon_circle(
            "send",
            stroke_color=self.datenfluss_icon_stroke,
        ).move_to(np.array([2, 1.5, 0]))

        dataspace_connector_broker_line = m.Line(
            dataspace_connector_icon_group.get_center(),
            broker_icon_group.get_center(),
            **line_kwargs
        )


        dashboard_icon_group = self.icon_circle(
            "desktop-mac-dashboard",
            stroke_color=self.datenfluss_icon_stroke,
        ).move_to(np.array([2, -0.5, 0]))

        dashboard_broker_line = m.Line(
            dashboard_icon_group.get_center(),
            broker_icon_group.get_center(),
            **line_kwargs
        )



        more_icon_group = self.icon_circle(
            "dots-horizontal",
            stroke_color=self.datenfluss_icon_stroke,
        ).shift(m.RIGHT * 4).move_to(np.array([0, 2.5, 0]))

        more_broker_line = m.Line(
            more_icon_group.get_center(),
            broker_icon_group.get_center(),
            **line_kwargs
        )


        description_box = self.icon_textbox(
            "Datenfluss im Datenraum",
            icon='information-outline',
            width=self.content_width,
            height=1.5
        ).to_edge(m.DOWN, buff=0.625)


        self.play(

            m.FadeIn(machine_icon_group),
            m.FadeIn(broker_icon_group),
            m.FadeIn(database_icon_group),
            m.FadeIn(dataspace_connector_icon_group),
            m.FadeIn(dashboard_icon_group),
            m.FadeIn(more_icon_group),
            m.FadeIn(description_box),

            m.FadeIn(machine_broker_line),
            m.FadeIn(database_boker_line),
            m.FadeIn(dataspace_connector_broker_line),
            m.FadeIn(dashboard_broker_line),
            m.FadeIn(more_broker_line),
        )



if __name__ == '__main__':
    OpenHubDaysDatenfluss.render_video_medium()