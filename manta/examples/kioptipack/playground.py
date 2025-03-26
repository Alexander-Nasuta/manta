
import manim as m
import numpy as np
from docutils.nodes import description, subtitle
from pyrr.rectangle import height, width

from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class OpenHubDaysDatenfluss(MinimalSlideTemplate):

    index_prefix = "B"

    default_icon_color = MinimalSlideTemplate.mauve
    datenfluss_icon_stroke = MinimalSlideTemplate.blue

    subtitle_color = MinimalSlideTemplate.blue

    ml_lifecycle_text_rect_width = 2.25
    ml_lifecycle_text_rect_height = 0.75
    ml_lifecycle_text_size = MinimalSlideTemplate.font_size_tiny

    ml_lifecycle_stage_text_size = MinimalSlideTemplate.font_size_small

    ml_lifecycle_arrow_color = MinimalSlideTemplate.sapphire

    icon_label_fontsize = MinimalSlideTemplate.font_size_small

    def construct(self):
        self.play(
            self.set_title_row(
                title="Machine Learning Lifecycle",
                seperator=": ",
                subtitle="Semantischer Datenraum",
            )
        )

        poly = m.RegularPolygon(n=6, start_angle=0 * m.DEGREES).scale_to_fit_width(4)

        # self.play(m.FadeIn(poly))

        broker_icon_group = self.icon_circle_svg(
            "resources/nats_icon.svg",
            svg_color=self.default_icon_color,
            stroke_color=self.yellow,
            # radius=0.425
        )
        broker_icon_group[-1].scale(1.1)
        broker_icon_group.move_to(poly.get_center())

        others_icon_group = self.icon_circle(
            "dots-horizontal",
            stroke_color=self.datenfluss_icon_stroke,
        ).move_to(poly.get_vertices()[2])
        others_label = self.term_text(
            "Andere FastIOT-\n Services",
            font_size=self.icon_label_fontsize,
            font_color=self.datenfluss_icon_stroke
        ).next_to(others_icon_group, m.LEFT, buff=self.med_large_buff)
        others_group = m.VGroup(others_icon_group, others_label)

        preprocessing_icon_group = self.icon_circle(
            "server-process",
            stroke_color=self.red,
        ).move_to(poly.get_vertices()[1])
        preprocessing_label = self.term_text(
            "Daten-Aufarbeitungs\n Service",
            font_size=self.icon_label_fontsize,
            font_color=self.red
        ).next_to(preprocessing_icon_group, m.RIGHT, buff=self.med_large_buff)
        preprocessing_group = m.VGroup(preprocessing_icon_group, preprocessing_label)

        database_icon_group = self.icon_circle(
            "database#3",
            stroke_color=self.red,
        ).move_to(poly.get_vertices()[0])
        database_label = self.term_text(
            "Datenbank\n Service",
            font_size=self.icon_label_fontsize,
            font_color=self.red
        ).next_to(database_icon_group, m.RIGHT, buff=self.med_large_buff)
        database_group = m.VGroup(database_icon_group, database_label)

        # chart-bell-curve-cumulative
        # chart-timeline-variant-shimmer

        training_icon_group = self.icon_circle(
            "chart-timeline-variant-shimmer",
            stroke_color=self.blue,
        ).move_to(poly.get_vertices()[-1])
        training_label = self.term_text(
            "Training\n Service",
            font_size=self.icon_label_fontsize,
            font_color=self.blue
        ).next_to(training_icon_group, m.RIGHT, buff=self.med_large_buff)
        training_group = m.VGroup(training_icon_group, training_label)

        mlflow_icon_group = self.icon_circle_npg(
            "resources/mlflow_icon.png",
            svg_color=self.default_icon_color,
            stroke_color=[self.blue, self.green],
            # radius=0.425
        ).move_to(poly.get_vertices()[-2])
        mlflow_icon_group = self.icon_circle(
            "sync#2",
            stroke_color=self.blue,
        ).move_to(poly.get_vertices()[-2])
        mlflow_label = self.term_text(
            "MLflow\n Tracking",
            font_size=self.icon_label_fontsize,
            font_color=self.green,
        ).next_to(mlflow_icon_group, m.LEFT, buff=self.med_large_buff)
        mlflow_group = m.VGroup(mlflow_icon_group, mlflow_label)

        serving_icon_group = self.icon_circle(
            "server-network",
            stroke_color=self.green,
        ).move_to(poly.get_vertices()[-3])
        serving_label = self.term_text(
            "Model Serving\n Service",
            font_size=self.icon_label_fontsize,
            font_color=self.green
        ).next_to(serving_icon_group, m.LEFT, buff=self.med_large_buff)
        serving_group = m.VGroup(serving_icon_group, serving_label)

        # lines between icons
        line_kwargs = {
            "stroke_width": 3,
            "fill_color": self.font_color_secondary,
            "color": self.font_color_secondary,
            "buff": 0.325
        }

        broker_others_line = m.Line(
            broker_icon_group.get_center(),
            others_icon_group.get_center(),
            **line_kwargs
        )

        broker_preprocessing_line = m.Line(
            broker_icon_group.get_center(),
            preprocessing_icon_group.get_center(),
            **line_kwargs
        )
        broker_db_line = m.Line(
            broker_icon_group.get_center(),
            database_icon_group.get_center(),
            **line_kwargs
        )
        broker_training_line = m.Line(
            broker_icon_group.get_center(),
            training_icon_group.get_center(),
            **line_kwargs
        )
        broker_serving_line = m.Line(
            broker_icon_group.get_center(),
            serving_icon_group.get_center(),
            **line_kwargs
        )

        training_mlflow_line = m.Line(
            training_icon_group.get_center(),
            mlflow_icon_group.get_center(),
            **line_kwargs
        )

        mlflow_serv_line = m.Line(
            mlflow_icon_group.get_center(),
            serving_icon_group.get_center(),
            **line_kwargs
        )


        fastiot_services_group = m.Group(
            broker_icon_group,
            training_group,
            preprocessing_group,
            database_group,
            mlflow_group,
            serving_group,
            others_group,

            # lines
            broker_others_line,
            broker_db_line,
            broker_training_line,
            broker_preprocessing_line,
            broker_serving_line,
            training_mlflow_line,
            mlflow_serv_line,
        )

        self.add(fastiot_services_group)

        fastiot_services_group.generate_target()
        fastiot_services_group.target.scale(0.5)
        fastiot_services_group.target.to_edge(m.RIGHT, buff=self.med_large_buff)
        fastiot_services_group.target.to_edge(m.UP, buff=self.large_buff + self.med_small_buff)

        self.play(
            m.MoveToTarget(fastiot_services_group),
        )


        focus_rect = m.SurroundingRectangle(
            preprocessing_group,
            color=self.red,
            corner_radius=0.125,
            stroke_width=2
        )

        self.subtitle_color = self.red

        self.play(
            m.Create(focus_rect),
            self.change_subtitle("Daten-Aufarbeitungs Service")
        )


        datapoint_json = r"""[
████{
████████"ListeKomponenten": ["K000055"],
████████"Emodul": 923.5297844703941,
████████"MaximaleZugspannung": 35.17817424546557,
████████...
████████"Temp": 300,
████████"Zeit": 8,
████████"Druck": 1,
████},
████{
████"ListeKomponenten": ["K000141", "K000055"],
████████"Emodul": 758.2831428949372,
████████"MaximaleZugspannung": 31.672337664835965,
████████...
████████"Temp": 420,
████████"Zeit": 16,
████████"Druck": 2.67,
████},
████...
]"""

        datapoint_processed_json = r"""[
████{
████████"K000034": 0,
████████"K000035": 0,
████████"K000055": 1,
████████"K000141": 0,
████████...
████████"Emodul": 1.0,
████████"MaximaleZugspannung": 0.896,
████████...
████████"Temp": 0.6,
████████"Zeit": 0.2,
████████"Druck": 0.166,
████},
████{
████████"K000034": 0,
████████"K000035": 0,
████████"K000055": 1,
████████"K000141": 1,
████████...
████████"Emodul": 0.821,
████████"MaximaleZugspannung": 0.80,
████████...
████████"Temp": 0.84,
████████"Zeit": 0.4,
████████"Druck": 0.445,
████},
████...
]"""
        t2c={
            "████": self.background_color_bright,
            r'"ListeKomponenten"': self.yellow,
            r'"K000034"': self.yellow,
            r'"K000035"': self.yellow,
            r'"K000055"': self.yellow,
            r'"K000141"': self.yellow,
            r'"Emodul"': self.yellow,
            r'"MaximaleZugspannung"': self.yellow,
            r'"Temp"': self.yellow,
            r'"Zeit"': self.yellow,
            r'"Druck"': self.yellow,
        }

        json_scale = 0.5

        datapoint_block = self.term_text(
            datapoint_json,
            v_buff=0,
            t2c=t2c
        ).scale(json_scale)


        datapoint_block_processed = self.term_text(
            datapoint_processed_json,
            v_buff=0,
            t2c=t2c
        ).scale(json_scale)


        wrapped_datapoint_block_processed = self.wrap_with_rectangle(
            datapoint_block_processed,
            v_buff=self.small_buff,
            h_buff=self.small_buff,
        )

        wrapped_datapoint_block = self.wrap_with_rectangle(
            datapoint_block,
            height=wrapped_datapoint_block_processed.height,
            v_buff=self.small_buff,
            h_buff=self.small_buff,
        )

        wrapped_datapoint_block_processed.next_to(wrapped_datapoint_block, m.RIGHT, buff=self.large_buff)


        data_example_group = m.VGroup(
            wrapped_datapoint_block,
            wrapped_datapoint_block_processed,
        )
        data_example_group.next_to(self._title_mobject, m.DOWN, buff=self.med_large_buff, aligned_edge=m.LEFT)

        # arrow between datapoint blocks
        preprocessing_service_arrow = m.Arrow(
            wrapped_datapoint_block.get_right(),
            wrapped_datapoint_block_processed.get_left(),
            color=self.font_color_secondary,
        )

        self.play(
            m.FadeIn(wrapped_datapoint_block)
        )

        self.play(
            m.FadeIn(wrapped_datapoint_block_processed),
            m.Create(preprocessing_service_arrow),
        )


        preprocessing_bullet_content = self.bullet_point_list([
                "Definiert eine Processing Pipleline",
                "Data Cleaning",
                "Data Transformation",
                "Basiert auf Scikit-Learn Pipeline",
                "Speichert verarbeitete Daten in Datenbank",
            ])
        preprocessing_bullet_content.scale(0.5)

        preprocessing_bullet_points = self.wrap_with_icon_and_rectangle(
            preprocessing_bullet_content,
            icon='server-process',
            icon_color=self.red,
        )

        preprocessing_bullet_points.next_to(fastiot_services_group, m.DOWN, buff=self.med_large_buff, aligned_edge=m.RIGHT)
        # preprocessing_bullet_points.to_edge(m.RIGHT, buff=self.med_large_buff)

        self.play(
            m.FadeIn(preprocessing_bullet_points),
        )

        self.subtitle_color = self.blue

        self.play(
            self.change_subtitle("Training Service"),
            m.Transform(focus_rect, m.SurroundingRectangle(training_group, color=self.blue, corner_radius=0.125)),
            m.FadeOut(preprocessing_bullet_points),
            m.FadeOut(wrapped_datapoint_block),
            m.FadeOut(wrapped_datapoint_block_processed),
            m.FadeOut(preprocessing_service_arrow),
        )

        training_screenshot = m.ImageMobject("resources/training_screenshot.png")

        training_screenshot.scale_to_fit_height(5)

        training_screenshot.next_to(self._title_mobject, m.DOWN, buff=self.med_large_buff, aligned_edge=m.LEFT)

        training_text_content= self.bullet_point_list([
            "Trainiert ein ML Modell",
            "Lädt Daten sequentiell",
            "Speichert Trainings Metriken",
            "Speichert Modell in MLflow Registry",
        ])
        training_text_content.scale(0.5)

        training_text_box = self.wrap_with_icon_and_rectangle(
            training_text_content,
            icon='server-process',
            icon_color=self.red,
            width=fastiot_services_group.width,
        )

        training_text_box.next_to(fastiot_services_group, m.DOWN, buff=self.med_large_buff,
                                            aligned_edge=m.RIGHT)

        self.play(
            m.FadeIn(training_screenshot),
            m.FadeIn(training_text_box),
        )

        self.subtitle_color = self.green

        self.play(
            self.change_subtitle("MLflow Tracking"),
            m.FadeOut(training_screenshot),
            m.FadeOut(training_text_box),
            m.Transform(focus_rect, m.SurroundingRectangle(mlflow_group, color=self.green, corner_radius=0.125)),
        )

        mlflow_screenshot = m.ImageMobject("resources/ml_flow_screenshot.png")
        mlflow_screenshot.scale_to_fit_height(5)

        mlflow_screenshot.next_to(self._title_mobject, m.DOWN, buff=self.med_large_buff, aligned_edge=m.LEFT)

        mlflow_text_content = self.bullet_point_list([
            "Speichert Modell Metriken",
            "Speichert Modell Artefakte",
            "Verwaltet Modell Versionen",
        ])
        mlflow_text_content.scale(0.5)

        mlflow_text_box = self.wrap_with_icon_and_rectangle(
            mlflow_text_content,
            icon='sync#2',
            icon_color=self.green,
            width=fastiot_services_group.width,
        )

        mlflow_text_box.next_to(fastiot_services_group, m.DOWN, buff=self.med_large_buff,
                                            aligned_edge=m.RIGHT)

        self.play(
            m.FadeIn(mlflow_screenshot),
            m.FadeIn(mlflow_text_box),
        )

        self.play(
            self.change_subtitle("Model Serving Service"),
            m.FadeOut(mlflow_screenshot),
            m.FadeOut(mlflow_text_box),
            m.Transform(focus_rect, m.SurroundingRectangle(serving_group, color=self.green, corner_radius=0.125)),
        )

        serving_text_box = self.icon_bulletpoints_textbox(
            [
                "Lädt ein Modell aus der MLflow Registry.",
                "Stellt anderen Services die Möglichkeit\n zur Verfügung Prediktionen des Modells\n zu erhalten.",
                "Greift auf den Preprocessing Service zu,\n um Daten für die Prediktion aufzubereiten.",
            ],
            icon='server-network',
            icon_color=self.green,
            # if with is not set, the width will be calculated automatically
            # same for height
            width=8.25,
            # height=2.5,
            #t2c={"extrovert": self.blue},
            # this is an alternative to t2c
            # just type the words you want to colorize
            # and specify the color
            #t2c_strs=["talk", "people"],
            #t2c_color=self.green,
        )
        serving_text_box.next_to(self._title_mobject, m.DOWN, buff=self.med_large_buff, aligned_edge=m.LEFT)

        self.play(
            m.FadeIn(serving_text_box),
        )

        fastiot_services_group.generate_target()
        fastiot_services_group.target.scale(2.0)
        fastiot_services_group.target.move_to(m.ORIGIN)

        self.play(
            self.set_title_row(
                title="Machine Learning Lifecycle",
                seperator=None,
                subtitle=None,
            ),
            m.FadeOut(focus_rect),
            m.FadeOut(serving_text_box),
            m.MoveToTarget(fastiot_services_group),
        )












if __name__ == '__main__':
    OpenHubDaysDatenfluss.render_video_medium()