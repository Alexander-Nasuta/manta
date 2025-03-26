
import manim as m
import numpy as np
from docutils.nodes import description, subtitle
from pyrr.rectangle import height, width

from components.qr_code_utils import QrCodeUtils
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class OpenHubDaysDatenfluss(QrCodeUtils, MinimalSlideTemplate):

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

        preprocess_surrounding_rect = m.SurroundingRectangle(
            preprocessing_group,
            color=self.sapphire,
            corner_radius=0.125,
            stroke_width=5,
            buff=self.med_large_buff
        )

        database_surrounding_rect = m.SurroundingRectangle(
            database_group,
            color=self.sapphire,
            corner_radius=0.125,
            stroke_width=5,
            buff=self.med_large_buff
        )

        training_surrounding_rect = m.SurroundingRectangle(
            training_group,
            color=self.sapphire,
            corner_radius=0.125,
            stroke_width=5,
            buff=self.med_large_buff
        )

        serving_surrounding_rect = m.SurroundingRectangle(
            serving_group,
            color=self.sapphire,
            corner_radius=0.125,
            stroke_width=5,
            buff=self.med_large_buff
        )

        self.title_color = self.sapphire

        self.play(
            self.change_title("Blueprints"),
            m.FadeIn(preprocess_surrounding_rect),
            m.FadeIn(database_surrounding_rect),
            m.FadeIn(training_surrounding_rect),
            m.FadeIn(serving_surrounding_rect),
        )



        self.play(
            m.FadeOut(preprocess_surrounding_rect),
            m.FadeOut(database_surrounding_rect),
            m.FadeOut(training_surrounding_rect),
            m.FadeOut(serving_surrounding_rect),
            m.FadeOut(fastiot_services_group),
        )

        blueprint_text_box = self.icon_title_bulletpoints_textbox(
            [
                ("Blueprints", [
                    "Kopiervorlagen für FastIOT-Services zur Realisierung von ML-Applikationen",
                    "Zielgruppe: Entwickler und Data Scientists",
                    "Decken gängige ML-Libraries ab (Pytorch, LightGBM, Tensorflow, ...)",
                ]),
            ],
            icon='content-copy',
            # bullet_icon='user',
            icon_color=self.sapphire,
            bullet_icon_color=self.sapphire,
            # if with is not set, the width will be calculated automatically
            # same for height
            width=self.content_width,
            #height=4.0,
            t2w={
                "Blueprints": m.BOLD,
            },
            t2c={
                "Kopiervorlagen": self.sapphire,
                "Entwickler": self.sapphire,
                "Data Scientists": self.sapphire,
            },
            # this is an alternative to t2c
            # just type the words you want to colorize
            # and specify the color
            t2c_strs=["talk", "people"],
            t2c_color=self.green,
        )

        blueprint_text_box.next_to(self._title_mobject, m.DOWN, buff=self.med_large_buff, aligned_edge=m.LEFT)

        blueprint_example_screenshot = m.ImageMobject("resources/blueprint_preprocessing.png").scale_to_fit_height(3)
        blueprint_example_screenshot.next_to(blueprint_text_box, m.DOWN, buff=self.med_large_buff, aligned_edge=m.LEFT)

        blueprint_pytorch_screenshot = m.ImageMobject("resources/blueprint_pytorch.png").scale_to_fit_height(3)
        blueprint_pytorch_screenshot.next_to(blueprint_example_screenshot, m.RIGHT, buff=self.med_large_buff)

        blueprint_link = r"https://blueprint-dev-v2.readthedocs.io/en/latest/"

        qr_code = self.qr_code(
            blueprint_link,
            icon="content-copy",
            data_shape='circles',
            corner_color=self.sapphire,
            icon_color=self.sapphire,
        )
        qr_code.next_to(blueprint_pytorch_screenshot, m.RIGHT, buff=self.large_buff).scale_to_fit_height(2.4)
        qr_code.shift(m.UP * 0.05)


        self.play(
            m.FadeIn(blueprint_text_box),
            m.FadeIn(blueprint_example_screenshot),
            m.FadeIn(blueprint_pytorch_screenshot),
            m.FadeIn(qr_code),
        )










if __name__ == '__main__':
    OpenHubDaysDatenfluss.render_video_medium()