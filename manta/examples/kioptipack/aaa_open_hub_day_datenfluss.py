
import manim as m
import numpy as np
from docutils.nodes import description
from pyrr.rectangle import height, width

from color_theme.carolus.corolus_theme import CarolusTheme
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate
from slide_templates.title_slide import TitleSlide


class SemantischerDatenraum(CarolusTheme, TitleSlide):

    index_prefix = "A"

    default_icon_color = CarolusTheme.red

    datenfluss_icon_stroke = CarolusTheme.green

    highlight_color = m.RED


    description_scale = 0.75

    circumscribe_color = CarolusTheme.red
    circumscribe_buff = TitleSlide.med_large_buff

    def construct(self):

        broker_icon_group1 = self.icon_circle_svg(
            "resources/nats_icon.svg",
            svg_color=self.default_icon_color,
            stroke_color=self.blue_bright,
            #radius=0.425
        )
        broker_icon_group1[-1].scale(1.1)
        broker_icon_group1.move_to(np.array([0, 0.5, 0]))

        machine_icon_group1 = self.icon_circle(
            "robot-industrial",
            stroke_color=self.datenfluss_icon_stroke,
        ).move_to(np.array([-2, 1.5, 0]))


        line_kwargs = {
            "stroke_width": 3,
            "fill_color": self.font_color_secondary,
            "color": self.font_color_secondary,
            "buff": 0.325
        }

        machine_broker_line = m.Line(
            machine_icon_group1.get_center(),
            broker_icon_group1.get_center(),
            **line_kwargs
        )

        database_icon_group1 = self.icon_circle(
            "database#3",
            stroke_color=self.datenfluss_icon_stroke,
        ).move_to(np.array([-2, -0.5, 0]))


        database_broker_line = m.Line(
            database_icon_group1.get_center(),
            broker_icon_group1.get_center(),
            **line_kwargs
        )

        dashboard_icon_group1 = self.icon_circle(
            "desktop-mac-dashboard",
            stroke_color=self.datenfluss_icon_stroke,
        ).move_to(np.array([2, -0.5, 0]))


        dashboard_broker_line = m.Line(
            dashboard_icon_group1.get_center(),
            broker_icon_group1.get_center(),
            **line_kwargs
        )


        dashboard_circle_highlighting = dashboard_icon_group1[0].copy()
        dashboard_circle_highlighting.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)



        catalog_icon_group1 = self.icon_circle(
            "book-search-outline",
            stroke_color=self.datenfluss_icon_stroke,
        ).move_to(np.array([0, 2.0, 0]))


        policy_icon_group1 = self.icon_circle(
            "book-lock-outline",
            stroke_color=self.datenfluss_icon_stroke,
        ).move_to(np.array([2, 1.5, 0]))


        edc_icon_group1 = self.icon_circle_svg(
            "resources/GaiaX_icon.svg",
            stroke_color=self.datenfluss_icon_stroke,
            svg_color=self.default_icon_color,
        ).move_to(np.array([3.0, 1.5, 0]))


        circles_group1 = m.VGroup(
            machine_icon_group1,
            database_icon_group1,
            broker_icon_group1,
            dashboard_icon_group1,
            catalog_icon_group1,
            policy_icon_group1,
            edc_icon_group1,
        )

        broker_policy_line1 = m.Line(
            broker_icon_group1.get_center(),
            policy_icon_group1.get_center(),
            **line_kwargs
        )

        policy_edc_line1 = m.Line(
            policy_icon_group1.get_center(),
            edc_icon_group1.get_center(),
            **line_kwargs
        )

        broker_catalog_line = m.Line(
            broker_icon_group1.get_center(),
            catalog_icon_group1.get_center(),
            **line_kwargs
        )
        catalog_policy_line = m.Line(
            catalog_icon_group1.get_center(),
            policy_icon_group1.get_center(),
            **line_kwargs
        )


        line_group1 = m.VGroup(
            machine_broker_line,
            database_broker_line,
            dashboard_broker_line,
            broker_policy_line1,
            policy_edc_line1,
            broker_catalog_line,
            catalog_policy_line,
        )

        rounded_rect1 = m.RoundedRectangle(
            width=5.75,
            height=4.0,
            color=self.red,
            corner_radius=0.125
        )
        rounded_rect1.shift((0.25-0.125) * m.RIGHT + 0.75 * m.UP)

        services_group1 = m.VGroup(
            rounded_rect1,
            circles_group1,
            line_group1,
        )
        services_group1.shift(0.5 * m.DOWN)


        # mirror services 1 group vertically

        services_group2 = services_group1.copy()
        services_group2.apply_matrix(np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]))

        rounded_rect2, circles_group2, line_group2  = services_group2

        machine_icon_group2, database_icon_group2, broker_icon_group2, dashboard_icon_group2, catalog_icon_group2, policy_icon_group2, edc_icon_group2 = circles_group2

        machine_broker_line2, database_broker_line2, dashboard_broker_line2, broker_policy_line2, policy_edc_line2, broker_catalog_line2, catalog_policy_line2 = line_group2

        # asjust mirrored icon groups

        for e in [machine_icon_group2, policy_icon_group2, broker_icon_group2, dashboard_icon_group2, catalog_icon_group2]:
            temp = e.get_center()
            e.move_to(m.ORIGIN)
            e.apply_matrix(np.array([
                [-1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]
            ]))
            e.move_to(temp)





        services_group1.to_edge(m.LEFT, buff=self.med_large_buff)
        services_group2.to_edge(m.RIGHT, buff=self.med_large_buff)






        machine_label1 = self.term_text("Sensoren", font_size=self.font_size_script)
        machine_label1.next_to(machine_icon_group1, m.DOWN, buff=0.1)

        broker_label1 = self.term_text("Broker", font_size=self.font_size_script)
        broker_label1.next_to(broker_icon_group1, m.DOWN, buff=0.1)

        database_label1 = self.term_text("Datenbank", font_size=self.font_size_script)
        database_label1.next_to(database_icon_group1, m.DOWN, buff=0.1)

        edc_label1 = self.term_text("EDC", font_size=self.font_size_script)
        edc_label1.next_to(edc_icon_group1, m.DOWN, buff=0.1)
        edc_label1.shift(0.35 * m.RIGHT)

        policy_label1 = self.term_text("Policy", font_size=self.font_size_script)
        policy_label1.next_to(policy_icon_group1, m.DOWN, buff=0.1)

        catalog_label1 = self.term_text("Katalog", font_size=self.font_size_script)
        catalog_label1.next_to(catalog_icon_group1, m.UP, buff=0.1)

        dashboard_label1 = self.term_text("Dashboard", font_size=self.font_size_script)
        dashboard_label1.next_to(dashboard_icon_group1, m.DOWN, buff=0.1)

        label_group1 = m.VGroup(
            machine_label1,
            broker_label1,
            database_label1,
            edc_label1,
            policy_label1,
            catalog_label1,
            dashboard_label1,
        )



        machine_label2 = self.term_text("Sensoren", font_size=self.font_size_script)
        machine_label2.next_to(machine_icon_group2, m.DOWN, buff=0.1)

        broker_label2 = self.term_text("Broker", font_size=self.font_size_script)
        broker_label2.next_to(broker_icon_group2, m.DOWN, buff=0.1)

        database_icon_group2 = self.icon_circle(
            "dots-horizontal",
            stroke_color=self.datenfluss_icon_stroke,
        ).move_to(database_icon_group2.get_center())

        database_label2 = self.term_text("Services", font_size=self.font_size_script)
        database_label2.next_to(database_icon_group2, m.DOWN, buff=0.1)

        edc_label2 = self.term_text("EDC", font_size=self.font_size_script)
        edc_label2.next_to(edc_icon_group2, m.DOWN, buff=0.1)
        edc_label2.shift(0.35 * m.LEFT)

        policy_label2 = self.term_text("Policy", font_size=self.font_size_script)
        policy_label2.next_to(policy_icon_group2, m.DOWN, buff=0.1)

        catalog_label2 = self.term_text("Katalog", font_size=self.font_size_script)
        catalog_label2.next_to(catalog_icon_group2, m.UP, buff=0.1)

        dashboard_label2 = self.term_text("Dashboard", font_size=self.font_size_script)
        dashboard_label2.next_to(dashboard_icon_group2, m.DOWN, buff=0.1)

        label_group2 = m.VGroup(
            machine_label2,
            broker_label2,
            database_label2,
            edc_label2,
            policy_label2,
            catalog_label2,
            dashboard_label2,
        )

        services_group1_label = self.term_text("Anlagenbetreiber")
        services_group1_label_icon = self.symbol("industry", color=self.red)
        services_group1_label_icon.next_to(services_group1_label, m.LEFT, buff=self.small_buff)
        services_group1_label_icon.shift(0.075 * m.UP)

        services_group1_label_group = m.VGroup(
            services_group1_label,
            services_group1_label_icon,
        ).next_to(services_group1, m.UP, buff=self.med_small_buff)


        rounded_rect2.set_color(self.blue)
        services_group2_label = self.term_text("Externer Dienstleister")
        services_group2_label_icon = self.symbol("users", color=self.blue)
        services_group2_label_icon.next_to(services_group2_label, m.LEFT, buff=self.small_buff)

        services_group2_label_group = m.VGroup(
            services_group2_label,
            services_group2_label_icon,
        ).next_to(services_group2, m.UP, buff=self.med_small_buff).shift(0.05 * m.UP)



        ontologie_box = self.icon_textbox("Ontologie", icon='book_atlas', icon_color=self.yellow)
        ontologie_box.to_edge(m.UP, buff=0.4)

        catalog_ontologie_line1 = m.Line(
            catalog_icon_group1.get_center(),
            ontologie_box.get_center(),
            **line_kwargs
        )
        catalog_ontologie_line1.set_color(self.yellow)

        policy_ontology_line1 = m.Line(
            policy_icon_group1.get_center(),
            ontologie_box.get_center(),
            **line_kwargs
        )
        policy_ontology_line1.set_color(self.yellow)

        policy_ontology_line2 = m.Line(
            policy_icon_group2.get_center(),
            ontologie_box.get_center(),
            **line_kwargs
        )
        policy_ontology_line2.set_color(self.yellow)

        ontologie_lines_group = m.VGroup(
            catalog_ontologie_line1,
            policy_ontology_line1,
            policy_ontology_line2
        )


        edc1_edc2_line = m.Line(
            edc_icon_group1.get_center(),
            edc_icon_group2.get_center(),
            **line_kwargs
        )

        machine_circle1, machine_icon1 = machine_icon_group1
        machine_circle_highlighting1 = machine_circle1.copy()
        machine_circle_highlighting1.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        machine_circle2, machine_icon2 = machine_icon_group2
        machine_circle_highlighting2 = machine_circle2.copy()
        machine_circle_highlighting2.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        broker_circle1, broker_icon1 = broker_icon_group1
        broker_circle_highlighting1 = broker_circle1.copy()
        broker_circle_highlighting1.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        broker_circle2, broker_icon2 = broker_icon_group2
        broker_circle_highlighting2 = broker_circle2.copy()
        broker_circle_highlighting2.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        database_circle1, database_icon1 = database_icon_group1
        database_circle_highlighting1 = database_circle1.copy()
        database_circle_highlighting1.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        database_circle2, database_icon2 = database_icon_group2
        database_circle_highlighting2 = database_circle2.copy()
        database_circle_highlighting2.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        dashboard_circle1, dashboard_icon1 = dashboard_icon_group1
        dashboard_circle_highlighting1 = dashboard_circle1.copy()
        dashboard_circle_highlighting1.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        dashboard_circle2, dashboard_icon2 = dashboard_icon_group2
        dashboard_circle_highlighting2 = dashboard_circle2.copy()
        dashboard_circle_highlighting2.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        catalog_circle1, catalog_icon1 = catalog_icon_group1
        catalog_circle_highlighting1 = catalog_circle1.copy()
        catalog_circle_highlighting1.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        catalog_circle2, catalog_icon2 = catalog_icon_group2
        catalog_circle_highlighting2 = catalog_circle2.copy()
        catalog_circle_highlighting2.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        policy_circle1, policy_icon1 = policy_icon_group1
        policy_circle_highlighting1 = policy_circle1.copy()
        policy_circle_highlighting1.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        policy_circle2, policy_icon2 = policy_icon_group2
        policy_circle_highlighting2 = policy_circle2.copy()
        policy_circle_highlighting2.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        edc_circle1, edc_icon1 = edc_icon_group1
        edc_circle_highlighting1 = edc_circle1.copy()
        edc_circle_highlighting1.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        edc_circle2, edc_icon2 = edc_icon_group2
        edc_circle_highlighting2 = edc_circle2.copy()
        edc_circle_highlighting2.set_stroke(color=self.highlight_color).set_fill(opacity=0.0)

        circles_highlighting_group1 = m.VGroup(
            machine_circle_highlighting1,
            broker_circle_highlighting1,
            database_circle_highlighting1,
            dashboard_circle_highlighting1,
            catalog_circle_highlighting1,
            policy_circle_highlighting1,
            edc_circle_highlighting1,
        )

        circles_highlighting_group2 = m.VGroup(
            machine_circle_highlighting2,
            broker_circle_highlighting2,
            database_circle_highlighting2,
            dashboard_circle_highlighting2,
            catalog_circle_highlighting2,
            policy_circle_highlighting2,
            edc_circle_highlighting2,
        )


        desc_text = f"""Microservice Architektur
         Ein Message Broker (NATS) ist das zentrale Element für den Infromationsfluss
         Die Interation der Microservices erfolgt über das Framework FastIOT
        """

        description_box = self.wrap_with_icon_and_rectangle(
            mElement=self.term_text(desc_text,t2c=self.symbol_t2c(color=self.default_icon_color)).scale(self.description_scale),
            icon='█',
            icon_color=self.default_icon_color,
            width=self.content_width,
            height=1.75,
        ).to_edge(m.DOWN, buff=self.med_small_buff)

        rect, broker_icon_hidden, separation_line, desc_text = description_box

        broker_icon = m.SVGMobject("resources/nats_icon.svg").scale_to_fit_height(broker_icon_hidden.height)
        broker_icon.move_to(broker_icon_hidden.get_center()).set_color(self.red)
        description_box = m.VGroup(rect, broker_icon, separation_line, desc_text)

        self.play(
            m.FadeIn(broker_icon_group1),
            m.FadeIn(broker_label1),
            m.Circumscribe(broker_icon_group1, m.Circle, color=self.circumscribe_color, buff=self.circumscribe_buff),

            m.FadeIn(description_box),
        )

        desc_text = f"""Integration von Sensoren
         Ein Sensor wird über einen Service in das Gesamtsystem integriert  
         Die Kommunikation mit anderen Services, sowie der Datenbank erfolgt über den Broker
        """
        description_box_target = self.wrap_with_icon_and_rectangle(
            mElement=self.term_text(desc_text,t2c=self.symbol_t2c(color=self.default_icon_color)).scale(self.description_scale),
            icon='robot-industrial',
            icon_color=self.default_icon_color,
            width=self.content_width,
            height=1.75,
        ).to_edge(m.DOWN, buff=self.med_small_buff)

        self.play(
            m.FadeIn(machine_icon_group1),
            m.FadeIn(machine_label1),
            m.Create(machine_broker_line),

            m.Circumscribe(machine_icon_group1, m.Circle, color=self.circumscribe_color, buff=self.circumscribe_buff),

            m.Transform(description_box, description_box_target)
        )

        desc_text = f"""Integration von Datenbanken
                 Das Ablegen von Daten erfolgt über den Broker
                 FastIOT übernimmt die Kommunikation mit der Datenbank
                """
        description_box_target = self.wrap_with_icon_and_rectangle(
            mElement=self.term_text(desc_text, t2c=self.symbol_t2c(color=self.default_icon_color)).scale(
                self.description_scale),
            icon='database#3',
            icon_color=self.default_icon_color,
            width=self.content_width,
            height=1.75,
        ).to_edge(m.DOWN, buff=self.med_small_buff)


        self.play(
            m.FadeIn(database_icon_group1),
            m.FadeIn(database_label1),
            m.Create(database_broker_line),

            m.Circumscribe(database_icon_group1, m.Circle, color=self.circumscribe_color, buff=self.circumscribe_buff),

            m.Transform(description_box, description_box_target)
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

        surrounding_rect = m.SurroundingRectangle(
            example_datapoint,
            corner_radius=0.125, color=self.highlight_color
        )

        example_datapoint_group = m.VGroup(
            surrounding_rect,
            example_datapoint
        )

        desc_text = f"""Speicherung von Sensordaten
                         Anfallede Daten werden auf einem Broker Topic gepublished
                         FastIOT speichert alle Daten der entsprechenden Topics in der Datenbank
                        """
        description_box_target = self.wrap_with_icon_and_rectangle(
            mElement=self.term_text(desc_text, t2c=self.symbol_t2c(color=self.blue_bright)).scale(
                self.description_scale),
            icon='content-save-move-outline',
            icon_color=self.blue_bright,
            width=self.content_width,
            height=1.75,
        ).to_edge(m.DOWN, buff=self.med_small_buff)

        self.play(
            m.FadeIn(example_datapoint_group),

            m.Transform(description_box, description_box_target)
        )


        def animate_edge(edge):
            return m.ShowPassingFlash(
                m.VGroup(edge)
                .copy().set_color(self.highlight_color),
                time_width=1.0
            ),
        def animate_edge_revers(edge):
            return m.ShowPassingFlash(
                m.VGroup(edge)
                .copy().set_color(self.highlight_color),
                time_width=1.0,
                rate_func=lambda t: 1-t
            ),

        self.play(
            m.ReplacementTransform(example_datapoint_group, machine_circle_highlighting1),
        )
        self.play(
            m.FadeOut(machine_circle_highlighting1),
            animate_edge(machine_broker_line),
            m.FadeIn(broker_circle_highlighting1),
        )
        self.play(
            m.FadeOut(broker_circle_highlighting1),
            animate_edge_revers(database_broker_line),
            m.FadeIn(database_circle_highlighting1),
        )

        desc_text = f"""Auslesen von Daten
         Das Auslesen erfolgt über ein entsprechendes Reply Subject über den Broker
         FastIOT übernimmt die Datenabfrage und stellt sie dem anfragenden Service zur Verfügung
        """
        description_box_target = self.wrap_with_icon_and_rectangle(
            mElement=self.term_text(desc_text,t2c=self.symbol_t2c(color=self.blue_bright)).scale(self.description_scale),
            icon='desktop-mac-dashboard',
            icon_color=self.blue_bright,
            width=self.content_width,
            height=1.75,
        ).to_edge(m.DOWN, buff=self.med_small_buff)

        self.play(
            m.FadeIn(dashboard_icon_group1),
            m.FadeIn(dashboard_label1),
            m.Create(dashboard_broker_line),
            m.Transform(description_box, description_box_target),
            m.FadeOut(database_circle_highlighting1)
        )

        self.play(
            m.FadeIn(dashboard_circle_highlighting1)
        )

        self.play(
            m.FadeIn(broker_circle_highlighting1),
            animate_edge(dashboard_broker_line),
            m.FadeOut(dashboard_circle_highlighting1),
        )

        self.play(
            m.FadeIn(database_circle_highlighting1),
            animate_edge_revers(database_broker_line),
            m.FadeOut(broker_circle_highlighting1),
        )

        self.play(
            m.FadeOut(database_circle_highlighting1),
            animate_edge(database_broker_line),
            m.FadeIn(broker_circle_highlighting1),
        )

        self.play(
            m.FadeOut(broker_circle_highlighting1),
            animate_edge_revers(dashboard_broker_line),
            m.FadeIn(dashboard_circle_highlighting1),
        )

        self.play(
            m.FadeOut(dashboard_circle_highlighting1)
        )


        desc_text = f"""Semantischer Datenraum
                 Semantische Beschreibung der Daten über die Ontologie 
                 Selektive Freigabe von Daten über Policies
                 Transfer von Daten über den Eclipse Dataspace Connector
                """
        description_box_target = self.wrap_with_icon_and_rectangle(
            mElement=self.term_text(desc_text, t2c=self.symbol_t2c(color=self.blue_bright)).scale(
                self.description_scale),
            icon='users',
            icon_color=self.blue_bright,
            width=self.content_width,
            height=1.75,
        ).to_edge(m.DOWN, buff=self.med_small_buff)

        self.play(
            m.Create(rounded_rect1),
            m.FadeIn(services_group1_label_group),

            m.Create(rounded_rect2),
            m.FadeIn(services_group2_label_group),

            m.FadeIn(broker_icon_group2),
            m.FadeIn(broker_label2),

            m.FadeIn(database_icon_group2),
            m.FadeIn(database_label2),

            m.FadeIn(dashboard_icon_group2),
            m.FadeIn(dashboard_label2),

            m.Create(dashboard_broker_line2),
            m.Create(database_broker_line2),

            m.Transform(description_box, description_box_target)
        )

        self.play(
            m.FadeIn(catalog_icon_group1),
            m.FadeIn(catalog_label1),

            m.FadeIn(policy_icon_group1),
            m.FadeIn(policy_label1),

            m.FadeIn(edc_icon_group1),
            m.FadeIn(edc_label1),

            m.Create(broker_catalog_line),
            m.Create(catalog_policy_line),
            m.Create(broker_policy_line1),

            m.FadeIn(edc_icon_group2),
            m.FadeIn(edc_label2),

            m.FadeIn(policy_icon_group2),
            m.FadeIn(policy_label2),

            m.Create(broker_policy_line2),
            m.Create(policy_edc_line1),
            m.Create(policy_edc_line2),

            m.Create(edc1_edc2_line)
        )

        desc_text = f"""Ontologie
                         Gewährleistung eines einheitlichen Verständnisses der ausgetauschten Daten
                         Integration etablierter Standards sichert Interoperabilität
                         Komfortable Instanziierung über spezifisches User Interface
                        """
        description_box_target = self.wrap_with_icon_and_rectangle(
            mElement=self.term_text(desc_text, t2c=self.symbol_t2c(color=self.yellow)).scale(
                self.description_scale),
            icon='book_atlas',
            icon_color=self.yellow,
            width=self.content_width,
            height=1.75,
        ).to_edge(m.DOWN, buff=self.med_small_buff)


        self.play(
            m.FadeIn(ontologie_lines_group),
            m.FadeIn(ontologie_box),
            m.Circumscribe(ontologie_box, m.Rectangle, color=self.yellow, buff=self.circumscribe_buff),
            m.Transform(description_box, description_box_target)
        )

        desc_text = f"""Katalog
         Listet alle verfügbaren Daten im Datenraum
         Sichtbarkeiten können nach außen hin über Polices spezifiziert werden
        """
        description_box_target = self.wrap_with_icon_and_rectangle(
            mElement=self.term_text(desc_text, t2c=self.symbol_t2c(color=self.default_icon_color)).scale(
                self.description_scale),
            icon='book-search-outline',
            icon_color=self.default_icon_color,
            width=self.content_width,
            height=1.75,
        ).to_edge(m.DOWN, buff=self.med_small_buff)


        self.play(
            m.Circumscribe(catalog_icon_group1, m.Circle, color=self.circumscribe_color, buff=self.circumscribe_buff),
            m.Transform(description_box, description_box_target)
        )

        desc_text = f"""Policies
                 Defenieren welche Daten unternhemensübergreifend geteilt werden können 
                 Filtern sensible Daten aus
                """
        description_box_target = self.wrap_with_icon_and_rectangle(
            mElement=self.term_text(desc_text, t2c=self.symbol_t2c(color=self.default_icon_color)).scale(
                self.description_scale),
            icon='book-lock-outline',
            icon_color=self.default_icon_color,
            width=self.content_width,
            height=1.75,
        ).to_edge(m.DOWN, buff=self.med_small_buff)

        self.play(
            m.Circumscribe(policy_icon_group1, m.Circle, color=self.circumscribe_color, buff=self.circumscribe_buff),
            m.Circumscribe(policy_icon_group2, m.Circle, color=self.circumscribe_color, buff=self.circumscribe_buff),
            m.Transform(description_box, description_box_target)
        )

        desc_text = f"""Eclipse Dataspace Connector (EDC)
         Sicherer Datenaustausch basierend auf Gaia-X
         Zugriff und Kontrolle in unternehmensübergreifenden Netzwerken
         Datensouveränität ermöglicht sicheren Datenaustausch zwischen vertrauenswürdigen Partnern
        """
        description_box_target = self.wrap_with_icon_and_rectangle(
            mElement=self.term_text(desc_text, t2c=self.symbol_t2c(color=self.default_icon_color)).scale(
                self.description_scale),
            icon='█',
            icon_color=self.default_icon_color,
            width=self.content_width,
            height=1.75,
        ).to_edge(m.DOWN, buff=self.med_small_buff)
        rect, icon, line, desc_text = description_box_target
        gaia_icon = m.SVGMobject("resources/GaiaX_icon.svg").scale_to_fit_height(icon.height)
        gaia_icon.move_to(icon.get_center()).set_color(self.default_icon_color)
        description_box_target = m.VGroup(rect, gaia_icon, line, desc_text)

        self.play(
            m.Circumscribe(edc_icon_group1, m.Circle, color=self.circumscribe_color, buff=self.circumscribe_buff),
            m.Circumscribe(edc_icon_group2, m.Circle, color=self.circumscribe_color, buff=self.circumscribe_buff),
            m.Transform(description_box, description_box_target)
        )

        desc_text = f"""Katalogabfrage
         Die Katalogabfrage gibt Auskunft über verfügbare Daten und deren Nutzungrechte
        """
        description_box_target = self.wrap_with_icon_and_rectangle(
            mElement=self.term_text(desc_text, t2c=self.symbol_t2c(color=self.blue_bright)).scale(
                self.description_scale),
            icon='book-search-outline',
            icon_color=self.blue_bright,
            width=self.content_width,
            height=1.75,
        ).to_edge(m.DOWN, buff=self.med_small_buff)

        self.play(
            m.Transform(description_box, description_box_target),
            m.Circumscribe(dashboard_icon_group2, m.Circle, color=self.blue_bright, buff=self.circumscribe_buff),
            m.FadeIn(dashboard_circle_highlighting2),
        )

        self.play(
            m.FadeOut(dashboard_circle_highlighting2),
            animate_edge(dashboard_broker_line2),
            m.FadeIn(broker_circle_highlighting2),
        )

        self.play(
            m.FadeOut(broker_circle_highlighting2),
            animate_edge(broker_policy_line2),
            m.FadeIn(policy_circle_highlighting2),
        )

        self.play(
            m.FadeOut(policy_circle_highlighting2),
            animate_edge(policy_edc_line2),
            m.FadeIn(edc_circle_highlighting2),
        )

        self.play(
            m.FadeOut(edc_circle_highlighting2),
            animate_edge_revers(edc1_edc2_line),
            m.FadeIn(edc_circle_highlighting1),
        )

        self.play(
            m.FadeOut(edc_circle_highlighting1),
            animate_edge_revers(policy_edc_line1),
            m.FadeIn(policy_circle_highlighting1),
        )

        self.play(
            m.FadeOut(policy_circle_highlighting1),
            animate_edge_revers(catalog_policy_line),
            m.FadeIn(catalog_circle_highlighting1),
        )

        self.play(
            m.FadeOut(catalog_circle_highlighting1),
            animate_edge(catalog_policy_line),
            m.FadeIn(policy_circle_highlighting1),
        )

        self.play(
            m.FadeOut(policy_circle_highlighting1),
            animate_edge(policy_edc_line1),
            m.FadeIn(edc_circle_highlighting1),
        )

        self.play(
            m.FadeOut(edc_circle_highlighting1),
            animate_edge(edc1_edc2_line),
            m.FadeIn(edc_circle_highlighting2),
        )

        self.play(
            m.FadeOut(edc_circle_highlighting2),
            animate_edge_revers(policy_edc_line2),
            m.FadeIn(policy_circle_highlighting2),
        )

        self.play(
            m.FadeOut(policy_circle_highlighting2),
            animate_edge_revers(broker_policy_line2),
            m.FadeIn(broker_circle_highlighting2),
        )

        self.play(
            m.FadeOut(broker_circle_highlighting2),
            animate_edge_revers(dashboard_broker_line2),
            m.FadeIn(dashboard_circle_highlighting2),
        )



        desc_text = f"""Austausch von Daten
         Bei einer Anfrage nach Daten werden diese über den Broker und EDC bereitgestellt
         Es fließen nur Daten, die durch die Policies freigegeben wurden
        """
        description_box_target = self.wrap_with_icon_and_rectangle(
            mElement=self.term_text(desc_text, t2c=self.symbol_t2c(color=self.blue_bright)).scale(
                self.description_scale),
            icon='file-send-outline',
            icon_color=self.blue_bright,
            width=self.content_width,
            height=1.75,
        ).to_edge(m.DOWN, buff=self.med_small_buff)

        self.play(
            m.FadeOut(dashboard_circle_highlighting2),
            animate_edge(dashboard_broker_line2),
            m.FadeIn(broker_circle_highlighting2),
            m.Transform(description_box, description_box_target)
        )

        self.play(
            m.FadeOut(broker_circle_highlighting2),
            animate_edge(broker_policy_line2),
            m.FadeIn(policy_circle_highlighting2),
        )

        self.play(
            m.FadeOut(policy_circle_highlighting2),
            animate_edge(policy_edc_line2),
            m.FadeIn(edc_circle_highlighting2),
        )

        self.play(
            m.FadeOut(edc_circle_highlighting2),
            animate_edge_revers(edc1_edc2_line),
            m.FadeIn(edc_circle_highlighting1),
        )

        self.play(
            m.FadeOut(edc_circle_highlighting1),
            animate_edge_revers(policy_edc_line1),
            m.FadeIn(policy_circle_highlighting1),
        )

        self.play(
            m.FadeOut(policy_circle_highlighting1),
            animate_edge_revers(broker_policy_line1),
            m.FadeIn(broker_circle_highlighting1),
        )

        self.play(
            m.FadeOut(broker_circle_highlighting1),
            animate_edge_revers(database_broker_line),
            m.FadeIn(database_circle_highlighting1),
        )

        # back to dashboard2 in reverse order

        self.play(
            m.FadeOut(database_circle_highlighting1),
            animate_edge(database_broker_line),
            m.FadeIn(broker_circle_highlighting1),
        )


        self.play(
            m.FadeOut(broker_circle_highlighting1),
            animate_edge(broker_policy_line1),
            m.FadeIn(policy_circle_highlighting1),
        )

        self.play(
            m.FadeOut(policy_circle_highlighting1),
            animate_edge(policy_edc_line1),
            m.FadeIn(edc_circle_highlighting1),
        )

        self.play(
            m.FadeOut(edc_circle_highlighting1),
            animate_edge(edc1_edc2_line),
            m.FadeIn(edc_circle_highlighting2),
        )

        self.play(
            m.FadeOut(edc_circle_highlighting2),
            animate_edge_revers(policy_edc_line2),
            m.FadeIn(policy_circle_highlighting2),
        )

        self.play(
            m.FadeOut(policy_circle_highlighting2),
            animate_edge_revers(broker_policy_line2),
            m.FadeIn(broker_circle_highlighting2),
        )

        self.play(
            m.FadeOut(broker_circle_highlighting2),
            animate_edge_revers(dashboard_broker_line2),
            m.FadeIn(dashboard_circle_highlighting2),
        )

        self.wait(0.1)
        self.fade_out_scene()






if __name__ == '__main__':
    SemantischerDatenraum.render_video_medium()
    # Datenfluss.render_video_4k()
    # OpenHubDaysDatenfluss.manim_slides_html_4k()