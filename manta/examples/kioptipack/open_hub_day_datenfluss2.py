
import manim as m
import numpy as np
from docutils.nodes import description
from pyrr.rectangle import height

from color_theme.carolus.corolus_theme import CarolusTheme
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate
from slide_templates.title_slide import TitleSlide


class OpenHubDaysDatenflussOnto(CarolusTheme, TitleSlide):

    index_prefix = "A"

    default_icon_color = CarolusTheme.red

    datenfluss_icon_stroke = CarolusTheme.green

    highlight_color = m.RED

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

        database_label2 = self.term_text("Datenbank", font_size=self.font_size_script)
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


        edc_edc_line = m.Line(
            edc_icon_group1.get_center(),
            edc_icon_group2.get_center(),
            **line_kwargs
        )

        description = self.icon_bulletpoints_textbox(
            [
                "Innerhalb eines Unternehmens fließen Daten über den Message Broker",
                "Zwischen verschiedenen Unternehmen erfolgt der Datenaustausch über den \n Eclipse Dataspace Connector (EDC)",
            ],
            icon='robot-industrial',
            width=self.content_width,
            height=1.75,
            icon_color=self.yellow,
            font_size=self.font_size_small
        ).to_edge(m.DOWN, buff=self.med_small_buff)



        self.play(
            self.set_title_row(
                title="Datenfluss im Datenraum",
            ),

            m.FadeIn(services_group1),
            m.FadeIn(services_group1_label_group),

            m.FadeIn(services_group2),
            m.FadeIn(services_group2_label_group),

            m.FadeIn(label_group1),
            m.FadeIn(label_group2),

            m.FadeIn(edc_edc_line),

            m.FadeIn(ontologie_lines_group),
            m.FadeIn(ontologie_box),

            m.FadeIn(description),

        )

        self.play(
            m.Circumscribe(machine_icon_group1, m.Circle, color=self.yellow, time_width=2, )
        )

        self.play(
            m.Circumscribe(database_icon_group1, m.Circle, color=self.yellow, time_width=2, )
        )



if __name__ == '__main__':
    OpenHubDaysDatenflussOnto.save_sections_without_cache()
    # Datenfluss.render_video_4k()
    # OpenHubDaysDatenfluss.manim_slides_html_4k()