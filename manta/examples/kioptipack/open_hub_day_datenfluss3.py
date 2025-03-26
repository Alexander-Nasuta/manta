
import manim as m
import numpy as np
from docutils.nodes import description
from pyrr.rectangle import height

from color_theme.carolus.corolus_theme import CarolusTheme
from examples.kioptipack.openhub_day_intro import OpenHubDayIntro
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class OpenHubDaysDatenfluss(CarolusTheme, MinimalSlideTemplate):

    index_prefix = "A"

    default_icon_color = CarolusTheme.red

    datenfluss_icon_stroke = CarolusTheme.blue

    highlight_color = m.RED

    def construct(self):
        self.play(
            self.set_title_row(
                title="Datenfluss im Datenraum",
            )
        )

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


        self.play(
            m.FadeIn(broker_icon_group)
        )

        description_box  = self.icon_title_bulletpoints_textbox(
            [
                ("Microservice Architektur", [
                    "Ein Message Broker (NATS) is das zentrale Element für den Infromationsfluss",
                    "Die Interation der Microservices erfolgt über das Framework FastIOT"
                ]),
            ],
            icon='information-outline',
            width=self.content_width,
            height=2.0,
            icon_color=self.yellow,
            font_size=self.font_size_small
        ).to_edge(m.DOWN, buff=0.625)


        self.play(
            m.FadeIn(description_box)
        )



        machine_icon_group = self.icon_circle(
            "robot-industrial",
            stroke_color=self.datenfluss_icon_stroke,
        ).move_to(np.array([-2, 1.5, 0]))

        description_target = self.icon_title_bulletpoints_textbox(
            [
                ("Integration einer Maschine", [
                    "Ein Datenproducer entspricht einem Microservice",
                ]),
            ],
            icon='robot-industrial',
            width=self.content_width,
            height=1.5,
            icon_color=self.yellow,
            font_size=self.font_size_small
        ).to_edge(m.DOWN, buff=0.625)

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


        self.play(
            m.Create(machine_broker_line),
            m.FadeIn(machine_icon_group),
            m.Transform(description_box, description_target)
        )




        database_icon_group = self.icon_circle(
            "database#3",
            stroke_color=self.datenfluss_icon_stroke,
        ).move_to(np.array([-2, -0.5, 0]))

        database_broker_line = m.Line(
            database_icon_group.get_center(),
            broker_icon_group.get_center(),
            **line_kwargs
        )

        description_target = self.icon_title_bulletpoints_textbox(
            [
                ("Speichern von Sensordaten", [
                    "Das Speichern von Sensordaten erfolgt über den Message Broker",
                    "Eine direkte Kommunikation zwischen den Microservices mit der Datenbank \n wird nicht benötigt",
                ]),
            ],
            icon='database#3',
            width=self.content_width,
            height=2.25,
            icon_color=self.yellow,
            font_size=self.font_size_small
        ).to_edge(m.DOWN, buff=0.625)


        self.play(
            m.Create(database_broker_line),
            m.FadeIn(database_icon_group),
            m.Transform(description_box, description_target)
        )

        datapoint = """{
    "timestamp": "2024-11-11T13:37:42",
    "temperature": 42.0,
    "pressure": 9000.01,
    ...
}"""

        example_datapoint = self.term_paragraph(
            datapoint,
            font_size=self.font_size_script,
            t2c={
                "timestamp": self.yellow,
                "temperature": self.yellow,
                "pressure": self.yellow,

                "9000.01": self.blue,
                "42.0": self.blue,

                "...": self.font_color_secondary,
            }
        )
        example_datapoint.next_to(machine_icon_group, m.RIGHT, buff=0.5)
        example_datapoint.to_edge(m.LEFT, buff=self.med_large_buff)

        self.play(
            m.FadeIn(example_datapoint)
        )


        surrounding_rect = m.SurroundingRectangle(
            example_datapoint,
           corner_radius=0.125, color=self.highlight_color
        )
        machine_circle, machine_icon = machine_icon_group
        machine_circle_highlighting = machine_circle.copy()
        machine_circle_highlighting.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)


        self.play(
            m.Create(surrounding_rect),
            m.FadeIn(machine_circle_highlighting),
        )

        broker_circle_highlighting = broker_icon_group[0].copy()
        broker_circle_highlighting.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        self.play(
            m.FadeOut(machine_circle_highlighting),
            m.FadeIn(broker_circle_highlighting),
            m.ShowPassingFlash(
                m.VGroup(machine_broker_line)
                .copy().set_color(self.highlight_color),
                time_width=1.0
            ),
            # rate_func=lambda t: 1 - t
        )

        database_circle_highlighting = database_icon_group[0].copy()
        database_circle_highlighting.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        self.play(
            m.FadeOut(broker_circle_highlighting),
            m.FadeIn(database_circle_highlighting),
            m.ShowPassingFlash(
                m.VGroup(database_broker_line)
                .copy().set_color(self.highlight_color),
                time_width=1.0,
                rate_func=lambda t: 1 - t
            ),
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

        description_target = self.icon_title_bulletpoints_textbox(
            [
                ("Abrufen von Daten", [
                    "Das Auslesen von Sensordaten erfolgt über den Message Broker",
                    "z.B. für die Anzeige auf einem Dashboard",
                ]),
            ],
            icon='desktop-mac-dashboard',
            width=self.content_width,
            height=1.75,
            icon_color=self.yellow,
            font_size=self.font_size_small
        ).to_edge(m.DOWN, buff=0.625)


        self.play(
            m.Create(dashboard_broker_line),
            m.FadeIn(dashboard_icon_group),
            m.Transform(description_box, description_target)
        )


        self.play(
            m.FadeOut(database_circle_highlighting),
            m.FadeIn(broker_circle_highlighting),
            m.ShowPassingFlash(
                m.VGroup(database_broker_line)
                .copy().set_color(self.highlight_color),
                time_width=1.0,
                #rate_func=lambda t: 1 - t
            ),
        )

        dashboard_circle_highlighting = dashboard_icon_group[0].copy()
        dashboard_circle_highlighting.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        self.play(
            m.FadeOut(broker_circle_highlighting),
            m.FadeIn(dashboard_circle_highlighting),
            m.ShowPassingFlash(
                m.VGroup(dashboard_broker_line)
                .copy().set_color(self.highlight_color),
                time_width=1.0,
                rate_func=lambda t: 1 - t
            ),
        )

        self.play(
            m.FadeOut(dashboard_circle_highlighting),
        )

        self.play(
            m.FadeOut(surrounding_rect),
            m.FadeOut(example_datapoint),
        )

        surrounding_rect = m.SurroundingRectangle(
            m.VGroup(machine_icon_group, broker_icon_group, database_icon_group, dashboard_icon_group),
            corner_radius=0.125, color=self.red,
            buff=0.325
        )

        motiv_text = self.term_text("Anlagenbetreiber")
        motiv_icon = self.symbol("industry")
        motiv_icon.next_to(motiv_text, m.LEFT, buff=self.med_small_buff).shift(m.UP * 0.075)

        motiv_group = m.VGroup(motiv_text, motiv_icon)
        motiv_group.next_to(surrounding_rect, m.UP, buff=self.med_large_buff)


        self.play(
            m.Create(surrounding_rect),
            m.FadeIn(motiv_group)
        )



        motiv_fastiot_group = m.VGroup(
            motiv_group,
            surrounding_rect,

            broker_icon_group,
            machine_icon_group,
            database_icon_group,
            dashboard_icon_group,

            machine_broker_line,
            database_broker_line,
            dashboard_broker_line,

        )

        motiv_fastiot_group.generate_target()
        motiv_fastiot_group.target.to_edge(m.LEFT, buff=self.med_large_buff)




        description_target = self.icon_bulletpoints_textbox(
            [
                "Innerhalb eines Unternehmens fließen Daten über den Message Broker",
                "Zwischen verschiedenen Unternehmen erfolgt der Datenaustausch über den \n Eclipse Dataspace Connector (EDC)",
            ],
            icon='send',
            width=self.content_width,
            height=1.75,
            icon_color=self.yellow,
            font_size=self.font_size_small
        ).to_edge(m.DOWN, buff=0.625)


        desc_rect, desc_icon, desc_seperator, desc_titled_bulletpoint_group = description_box

        desc_title, desc_bulletpoints  = desc_titled_bulletpoint_group[0]

        desc_target_rect, desc_target_icon, desc_target_seperator, desc_target_bulletpoint_group = description_target

        self.play(
            m.MoveToTarget(motiv_fastiot_group),
            m.Transform(desc_rect, desc_target_rect),
            m.Transform(desc_icon, desc_target_icon),
            m.Transform(desc_seperator, desc_target_seperator),
            m.Transform(desc_bulletpoints, desc_target_bulletpoint_group),
            m.FadeOut(desc_title),
            #m.Transform(m.VGroup(*desc_content), m.VGroup(*desc_target_content)),
        )

        dataspace_connector_icon_group = self.icon_circle(
            "send",
            stroke_color=self.datenfluss_icon_stroke,
        ).move_to(broker_icon_group.get_center() + np.array([2, 1.0, 0]))

        dataspace_connector_broker_line = m.Line(
            dataspace_connector_icon_group.get_center(),
            broker_icon_group.get_center(),
            **line_kwargs
        )


        self.play(
            m.FadeIn(dataspace_connector_icon_group),
            m.Create(dataspace_connector_broker_line),
        )


        motiv_fastiot_group.add(dataspace_connector_icon_group, dataspace_connector_broker_line)




        broker_icon_group2 = self.icon_circle_svg(
            "resources/nats_icon.svg",
            svg_color=self.default_icon_color,
            stroke_color=self.yellow,
            # radius=0.425
        )
        broker_icon_group2[-1].scale(1.1)

        broker_icon_group2.move_to(np.array([0, 0.5, 0]))


        dataspace_connector_icon_group2 = self.icon_circle(
            "send",
            stroke_color=self.datenfluss_icon_stroke,
        ).move_to(np.array([-2, 1.5, 0]))

        dataspace_connector_broker_line2 = m.Line(
            dataspace_connector_icon_group2.get_center(),
            broker_icon_group2.get_center(),
            **line_kwargs
        )


        database_icon_group2 = self.icon_circle(
            "database#3",
            stroke_color=self.datenfluss_icon_stroke,
        ).move_to(np.array([-2, -0.5, 0]))

        database_boker_line2 = m.Line(
            database_icon_group2.get_center(),
            broker_icon_group2.get_center(),
            **line_kwargs
        )


        more_icon_group2 = self.icon_circle(
            "dots-horizontal",
            stroke_color=self.datenfluss_icon_stroke,
        ).move_to(np.array([2, -0.5, 0]))

        dashboard_broker_line2 = m.Line(
            more_icon_group2.get_center(),
            broker_icon_group2.get_center(),
            **line_kwargs
        )


        fastiot_group2 = m.VGroup(
            broker_icon_group2,
            dataspace_connector_icon_group2,
            database_icon_group2,
            more_icon_group2,
            dataspace_connector_broker_line2,
            database_boker_line2,
            dashboard_broker_line2,
        )

        surrounding_rect2 = m.SurroundingRectangle(
            fastiot_group2,
            corner_radius=0.125, color=self.blue,
            buff=0.325
        )

        fastiot2_text = self.term_text("Externer Dienstleister")
        fastiot2_icon = self.symbol("users", color=self.blue)
        fastiot2_icon.next_to(fastiot2_text, m.LEFT, buff=self.med_small_buff).shift(m.UP * 0.0)

        fastiot2_group = m.VGroup(fastiot2_text, fastiot2_icon)

        fastiot2_group.next_to(surrounding_rect2, m.UP, buff=self.med_large_buff)

        external_company_group = m.VGroup(
            fastiot2_group,
            surrounding_rect2,
            broker_icon_group2,
            dataspace_connector_icon_group2,
            database_icon_group2,
            more_icon_group2,
            dataspace_connector_broker_line2,
            database_boker_line2,
            dashboard_broker_line2,
        )

        external_company_group.to_edge(m.RIGHT, buff=self.med_large_buff)

        self.play(
            m.FadeIn(external_company_group)
        )

        # dataspace to dataspace2 line
        dataspace_conn_line = m.Line(
            dataspace_connector_icon_group.get_center(),
            dataspace_connector_icon_group2.get_center(),
            **line_kwargs
        )

        self.play(
            m.Create(dataspace_conn_line)
        )


        dataspace_connector_icon_group2_highlighting = dataspace_connector_icon_group2[0].copy()
        dataspace_connector_icon_group2_highlighting.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        broker_icon_group2_highlighting = broker_icon_group2[0].copy()
        broker_icon_group2_highlighting.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        database_icon_group2_highlighting = database_icon_group2[0].copy()
        database_icon_group2_highlighting.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        more_icon_group2_highlighting = more_icon_group2[0].copy()
        more_icon_group2_highlighting.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)


        # dataspace negotiation

        self.play(
            m.ShowPassingFlash(
                m.VGroup(dataspace_conn_line)
                .copy().set_color(self.highlight_color),
                time_width=1.0
            ),
        )

        self.play(
            m.ShowPassingFlash(
                m.VGroup(dataspace_conn_line)
                .copy().set_color(self.highlight_color),
                time_width=1.0,
                rate_func=lambda t: 1 - t
            ),
        )


        # data transfer

        database_circle_highlighting.move_to(database_icon_group.get_center())
        broker_circle_highlighting.move_to(broker_icon_group.get_center())


        dataspace_connector_icon_group_highlighting = dataspace_connector_icon_group[0].copy()
        dataspace_connector_icon_group_highlighting.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)


        self.play(
            m.FadeIn(database_circle_highlighting)
        )


        self.play(
            m.ShowPassingFlash(
                m.VGroup(database_broker_line)
                .copy().set_color(self.highlight_color),
                time_width=1.0
            ),
            m.FadeIn(broker_circle_highlighting),
            m.FadeOut(database_circle_highlighting),
        )

        self.play(
            m.ShowPassingFlash(
                m.VGroup(dataspace_connector_broker_line)
                .copy().set_color(self.highlight_color),
                time_width=1.0,
                rate_func=lambda t: 1 - t
            ),
            m.FadeIn(dataspace_connector_icon_group_highlighting),
            m.FadeOut(broker_circle_highlighting),
        )

        self.play(
            m.ShowPassingFlash(
                m.VGroup(dataspace_conn_line)
                .copy().set_color(self.highlight_color),
                time_width=1.0
            ),
            m.FadeIn(dataspace_connector_icon_group2_highlighting),
            m.FadeOut(dataspace_connector_icon_group_highlighting),
        )

        self.play(
            m.ShowPassingFlash(
                m.VGroup(dataspace_connector_broker_line2)
                .copy().set_color(self.highlight_color),
                time_width=1.0,
                # rate_func=lambda t: 1 - t
            ),
            m.FadeOut(dataspace_connector_icon_group2_highlighting),
            m.FadeIn(broker_icon_group2_highlighting),
        )

        self.play(
            m.ShowPassingFlash(
                m.VGroup(database_boker_line2)
                .copy().set_color(self.highlight_color),
                time_width=1.0,
                rate_func=lambda t: 1 - t
            ),
            m.FadeOut(broker_icon_group2_highlighting),
            m.FadeIn(database_icon_group2_highlighting),
        )

        self.play(
            m.FadeOut(database_icon_group2_highlighting),
        )

        self.fade_out_scene()

if __name__ == '__main__':
    #OpenHubDaysDatenfluss.render_video_medium()
    #Datenfluss.render_video_4k()
    #OpenHubDaysDatenfluss.manim_slides_html_4k()
    OpenHubDaysDatenfluss.save_sections_without_cache()