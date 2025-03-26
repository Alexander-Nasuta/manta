
import manim as m
import numpy as np
from docutils.nodes import description, subtitle, title
from pyrr.rectangle import height

import manta.color_theme.catppucin.catppuccin_frappe
from color_theme.carolus.corolus_theme import CarolusTheme
from color_theme.catppucin.catppuccin_latte import CatppuccinLatteTheme
from components.qr_code_utils import QrCodeUtils
from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class OpenHubDaysMLSlides(
    CatppuccinLatteTheme,
    CarolusTheme, QrCodeUtils, MinimalSlideTemplate):

    background_color = "#ffffff"

    index_prefix = "B"

    default_icon_color = MinimalSlideTemplate.mauve
    datenfluss_icon_stroke = CarolusTheme.blue

    subtitle_color = CarolusTheme.blue

    ml_lifecycle_text_rect_width = 2.25
    ml_lifecycle_text_rect_height = 0.75
    ml_lifecycle_text_size = MinimalSlideTemplate.font_size_tiny

    ml_lifecycle_stage_text_size = MinimalSlideTemplate.font_size_small

    ml_lifecycle_arrow_color = CarolusTheme.blue_bright


    icon_label_fontsize = MinimalSlideTemplate.font_size_small


    def construct(self):
        self.play(
            self.set_title_row(
                title="Machine Learning Lifecycle",
                seperator=" ",
                subtitle="(Schlegel et al.)"
            )
        )

        data_collection_text = self.term_text("Data Collection \n and Selection", font_size=self.ml_lifecycle_text_size)
        data_collection_rect = self.wrap_with_rectangle(
            data_collection_text,
            width=self.ml_lifecycle_text_rect_width,
            height=self.ml_lifecycle_text_rect_height
        )

        data_cleaning_text = self.term_text("Data Cleaning", font_size=self.ml_lifecycle_text_size)
        data_cleaning_rect = self.wrap_with_rectangle(
            data_cleaning_text,
            width=self.ml_lifecycle_text_rect_width,
            height=self.ml_lifecycle_text_rect_height
        )

        data_labeling_text = self.term_text("Data Labeling", font_size=self.ml_lifecycle_text_size)
        data_labeling_rect = self.wrap_with_rectangle(
            data_labeling_text,
            width=self.ml_lifecycle_text_rect_width,
            height=self.ml_lifecycle_text_rect_height
        )

        feature_engineering_text = self.term_text("Feature Engineering\n and selection", font_size=self.ml_lifecycle_text_size)
        feature_engineering_rect = self.wrap_with_rectangle(
            feature_engineering_text,
            width=self.ml_lifecycle_text_rect_width,
            height=self.ml_lifecycle_text_rect_height
        )

        data_cleaning_rect.next_to(data_collection_rect, m.RIGHT, buff=self.med_large_buff)
        data_labeling_rect.next_to(data_cleaning_rect, m.DOWN, buff=self.med_large_buff)
        feature_engineering_rect.next_to(data_labeling_rect, m.LEFT, buff=self.med_large_buff)

        data_oriented_stage_surrounding_rect = m.SurroundingRectangle(
            m.VGroup(data_collection_rect, data_cleaning_rect, data_labeling_rect, feature_engineering_rect),
            color=self.red,
            corner_radius=0.125,
            buff=self.med_small_buff
        )
        data_oriented_stage_text = self.term_text(
            "Data-oriented\nStage",
            font_size=self.ml_lifecycle_stage_text_size,
            font_color=self.red,
        ).rotate(90 * m.DEGREES)

        # data stage arrows
        data_arrow1 = self.math_arrow(
            data_collection_rect.get_right(),
            data_cleaning_rect.get_left() + m.LEFT * self.small_buff,
            color=self.ml_lifecycle_arrow_color,
        )
        data_arrow2 = self.math_arrow(
            data_cleaning_rect.get_bottom(),
            data_labeling_rect.get_top() + m.UP * self.small_buff,
            color=self.ml_lifecycle_arrow_color,
        )
        data_arrow3 = self.math_arrow(
            data_labeling_rect.get_left(),
            feature_engineering_rect.get_right() + m.RIGHT * self.small_buff,
            color=self.ml_lifecycle_arrow_color,
        )

        data_oriented_stage_arrows_group = m.VGroup(
            data_arrow1,
            data_arrow2,
            data_arrow3,
        )



        data_oriented_stage_group = m.VGroup(
            data_arrow1,
            data_arrow2,
            data_arrow3,

            data_collection_rect,
            data_cleaning_rect,
            data_labeling_rect,
            feature_engineering_rect,
            data_oriented_stage_surrounding_rect,
        )

        data_oriented_stage_group.move_to(np.array([0, 0, 0]))

        model_requirements_text = self.term_text("Model Requirements \n Analysis", font_size=self.ml_lifecycle_text_size)
        model_requirements_rect = self.wrap_with_rectangle(model_requirements_text)

        model_requirements_surrounding_rect = m.RoundedRectangle(
            corner_radius=0.125,
            height=1.15,
            width=data_oriented_stage_surrounding_rect.width,
            color=self.yellow,
        ).move_to(model_requirements_rect.get_center())

        model_requirements_stage_text = self.term_text(
            "Requirements\nStage",
            font_size=self.ml_lifecycle_stage_text_size,
            font_color=self.yellow,
        ).rotate(90 * m.DEGREES)
        model_requirements_stage_text.next_to(model_requirements_surrounding_rect, m.LEFT, buff=self.med_small_buff)

        model_requirements_stage_group = m.VGroup(
            model_requirements_rect,
            model_requirements_surrounding_rect,
        )

        model_requirements_stage_group.next_to(data_oriented_stage_group, m.UP, buff=self.med_large_buff)



        model_design_text = self.term_text("Model Design", font_size=self.ml_lifecycle_text_size)
        model_design_rect = self.wrap_with_rectangle(
            model_design_text,
            width=self.ml_lifecycle_text_rect_width,
            height=self.ml_lifecycle_text_rect_height
        )

        model_training_text = self.term_text("Model Training", font_size=self.ml_lifecycle_text_size)
        model_training_rect = self.wrap_with_rectangle(
            model_training_text,
            width=self.ml_lifecycle_text_rect_width,
            height=self.ml_lifecycle_text_rect_height
        )

        model_evaluation_text = self.term_text("Model Evaluation", font_size=self.ml_lifecycle_text_size)
        model_evaluation_rect = self.wrap_with_rectangle(
            model_evaluation_text,
            width=self.ml_lifecycle_text_rect_width,
            height=self.ml_lifecycle_text_rect_height
        )

        model_optimization_text = self.term_text("Model Optimization", font_size=self.ml_lifecycle_text_size)
        model_optimization_rect = self.wrap_with_rectangle(
            model_optimization_text,
            width=self.ml_lifecycle_text_rect_width,
            height=self.ml_lifecycle_text_rect_height
        )

        model_training_rect.next_to(model_design_rect, m.RIGHT, buff=self.med_large_buff)
        model_evaluation_rect.next_to(model_training_rect, m.DOWN, buff=self.med_large_buff)
        model_optimization_rect.next_to(model_evaluation_rect, m.LEFT, buff=self.med_large_buff)

        model_stage_surrounding_rect = m.SurroundingRectangle(
            m.VGroup(model_design_rect, model_training_rect, model_evaluation_rect, model_optimization_rect),
            color=self.blue,
            corner_radius=0.125,
            buff=self.med_small_buff
        )
        model_stage_text = self.term_text(
            "Model-oriented \nStage",
            font_size=self.ml_lifecycle_stage_text_size,
            font_color=self.blue,
        ).rotate(90 * m.DEGREES)

        model_stage_text.next_to(model_stage_surrounding_rect, m.LEFT, buff=self.med_small_buff)

        model_stage_arrow1 = self.math_arrow(
            model_design_rect.get_right(),
            model_training_rect.get_left() + m.LEFT * self.small_buff,
            color=self.ml_lifecycle_arrow_color,
        )
        model_stage_arrow2 = self.math_arrow(
            model_training_rect.get_bottom(),
            model_evaluation_rect.get_top() + m.UP * self.small_buff,
            color=self.ml_lifecycle_arrow_color,
        )
        model_stage_arrow3 = self.math_arrow(
            model_evaluation_rect.get_left(),
            model_optimization_rect.get_right() + m.RIGHT * self.small_buff,
            color=self.ml_lifecycle_arrow_color,
        )
        model_stage_arrow4 = self.math_arrow(
            model_optimization_rect.get_top(),
            model_design_rect.get_bottom() + m.DOWN * self.small_buff,
            color=self.ml_lifecycle_arrow_color,
        )

        model_stage_arrow_group = m.VGroup(
            model_stage_arrow1,
            model_stage_arrow2,
            model_stage_arrow3,
            model_stage_arrow4,
        )

        model_stage_group = m.VGroup(
            model_stage_arrow1,
            model_stage_arrow2,
            model_stage_arrow3,
            model_stage_arrow4,

            model_design_rect,
            model_training_rect,
            model_evaluation_rect,
            model_optimization_rect,
            model_stage_surrounding_rect,
        )


        m.VGroup(
            data_oriented_stage_group,
            model_stage_group,
        ).move_to(m.ORIGIN)


        model_deployment_text = self.term_text("Model Deployment", font_size=self.ml_lifecycle_text_size)
        model_deployment_rect = self.wrap_with_rectangle(
            model_deployment_text,
            width=self.ml_lifecycle_text_rect_width,
            height=self.ml_lifecycle_text_rect_height
        )

        model_monitoring_text = self.term_text("Model Monitoring", font_size=self.ml_lifecycle_text_size)
        model_monitoring_rect = self.wrap_with_rectangle(
            model_monitoring_text,
            width=self.ml_lifecycle_text_rect_width,
            height=self.ml_lifecycle_text_rect_height
        )

        model_monitoring_rect.next_to(model_deployment_rect, m.RIGHT, buff=self.med_large_buff)

        operation_arrow = self.math_arrow(
            model_deployment_rect.get_right(),
            model_monitoring_rect.get_left() + m.LEFT * self.small_buff,
            color=self.ml_lifecycle_arrow_color,
        )

        operations_stage_surrounding_rect = m.SurroundingRectangle(
            m.VGroup(model_deployment_rect, model_monitoring_rect),
            color=self.green,
            corner_radius=0.125,
            buff=self.med_small_buff
        )

        operations_stage_text = self.term_text(
            "Operations\nStage",
            font_size=self.ml_lifecycle_stage_text_size,
            font_color=self.green,
        ).rotate(90 * m.DEGREES)

        operations_stage_text.next_to(operations_stage_surrounding_rect, m.LEFT, buff=self.med_small_buff)

        operations_stage_group = m.VGroup(
            operation_arrow,
            model_deployment_rect,
            model_monitoring_rect,
            operations_stage_surrounding_rect,
        )


        model_requirements_stage_group.to_edge(m.LEFT, buff=1.25)
        model_requirements_stage_group.to_edge(m.UP, buff=2)


        data_oriented_stage_group.next_to(model_requirements_stage_group, m.DOWN, buff=self.large_buff)

        model_stage_group.to_edge(m.RIGHT, buff=self.med_large_buff)
        model_stage_group.to_edge(m.UP, buff=2)

        operations_stage_group.next_to(model_stage_group, m.DOWN, buff=self.large_buff)


        model_requirements_stage_text.next_to(model_requirements_stage_group, m.LEFT, buff=self.med_small_buff)
        data_oriented_stage_text.next_to(data_oriented_stage_surrounding_rect, m.LEFT, buff=self.med_small_buff)
        model_stage_text.next_to(model_stage_surrounding_rect, m.LEFT, buff=self.med_small_buff)
        operations_stage_text.next_to(operations_stage_surrounding_rect, m.LEFT, buff=self.med_small_buff)


        # arrows between boxes

        requirements_to_data_stage_arrow = self.math_arrow(
            model_requirements_stage_group.get_bottom(),
            data_oriented_stage_group.get_top() + m.UP * self.small_buff,
            color=self.ml_lifecycle_arrow_color,
        )

        data_to_model_stage_line1 = m.Line(
            data_oriented_stage_group.get_bottom(),
            data_oriented_stage_group.get_bottom() + m.DOWN * 0.75,
            stroke_width=3,
            color=self.ml_lifecycle_arrow_color,
            )
        data_to_model_stage_line2 = m.Line(
            data_oriented_stage_group.get_bottom() + m.DOWN * 0.75,
            np.array([
                0,
                data_oriented_stage_group.get_bottom()[1] - 0.75,
                0
            ]),
            stroke_width=3,
            color=self.ml_lifecycle_arrow_color,
        )

        data_to_model_stage_line3 = m.Line(
            np.array([
                0,
                data_oriented_stage_group.get_bottom()[1] - 0.75,
                0
            ]),
            np.array([
                0,
                model_requirements_stage_group.get_top()[1] + 0.75,
                0
            ]),
            stroke_width=3,
            color=self.ml_lifecycle_arrow_color,
        )

        data_to_model_stage_line4 = m.Line(
            np.array([
                0,
                model_stage_group.get_top()[1] + 0.75,
                0
            ]),
            model_stage_group.get_top() + m.UP * 0.75,
            stroke_width=3,
            color=self.ml_lifecycle_arrow_color,
        )

        data_to_model_stage_line5 = self.math_arrow(
            model_stage_group.get_top() + m.UP * 0.75,
            model_stage_group.get_top() + m.UP * self.small_buff,
            # buff=self.small_buff,
            color=self.ml_lifecycle_arrow_color,
        )

        model_stage_to_operations_stage_arrow = self.math_arrow(
            model_stage_group.get_bottom(),
            operations_stage_group.get_top() + m.UP * self.small_buff,
            color=self.ml_lifecycle_arrow_color,
        )

        self.play(
            m.FadeIn(model_requirements_stage_group),
            m.FadeIn(model_requirements_stage_text),
        )

        self.play(
            m.FadeIn(data_oriented_stage_group),
            m.Create(requirements_to_data_stage_arrow),
            m.FadeIn(data_oriented_stage_text),
        )


        runtime= 0.25
        self.play(
            m.AnimationGroup(
                m.Create(data_to_model_stage_line1, run_time=runtime),
                m.Create(data_to_model_stage_line2, run_time=runtime),
                m.Create(data_to_model_stage_line3, run_time=runtime),
                m.Create(data_to_model_stage_line4, run_time=runtime),
                m.Create(data_to_model_stage_line5, run_time=runtime),
                lag_ratio=0.85
            ),
            m.FadeIn(model_stage_group),
            m.FadeIn(model_stage_text),
        )

        self.play(
            m.Create(model_stage_to_operations_stage_arrow),
            m.FadeIn(operations_stage_group),
            m.FadeIn(operations_stage_text),
        )

        preprocessing_icon_group = self.icon_circle(
            "server-process",
            stroke_color=self.red,
        )
        preprocessing_label = self.term_text(
            "Daten-Aufarbeitungs\n Service",
            font_size=self.icon_label_fontsize,
            font_color=self.red
        ).next_to(preprocessing_icon_group, m.RIGHT, buff=self.med_large_buff)

        preprocessing_group_pre = m.VGroup(
            preprocessing_icon_group,
            preprocessing_label
        ).move_to(data_oriented_stage_group.get_center())

        training_icon_group = self.icon_circle(
            "chart-timeline-variant-shimmer",
            stroke_color=self.blue,
        )
        training_label = self.term_text(
            "Training\n Service",
            font_size=self.icon_label_fontsize,
            font_color=self.blue
        ).next_to(training_icon_group, m.RIGHT, buff=self.med_large_buff)

        training_group_pre = m.VGroup(
            training_icon_group,
            training_label
        ).move_to(model_stage_group.get_center())



        serving_icon_group = self.icon_circle(
            "server-network",
            stroke_color=self.green,
        )
        serving_label = self.term_text(
            "Model Serving\n Service",
            font_size=self.icon_label_fontsize,
            font_color=self.green
        ).next_to(serving_icon_group, m.RIGHT, buff=self.med_large_buff)

        serving_group_pre = m.VGroup(
            serving_icon_group,
            serving_label
        ).move_to(operations_stage_group.get_center())


        self.play(
            m.ReplacementTransform(
                m.VGroup(
                    data_collection_rect,
                    data_cleaning_rect,
                    data_labeling_rect,
                    feature_engineering_rect,
                ),
                preprocessing_group_pre),
            m.FadeOut(data_oriented_stage_arrows_group),

            m.ReplacementTransform(
                m.VGroup(
                    model_design_rect,
                    model_training_rect,
                    model_evaluation_rect,
                    model_optimization_rect,
                ),
                training_group_pre),
            m.FadeOut(model_stage_arrow_group),

            m.ReplacementTransform(
                m.VGroup(
                    model_deployment_rect,
                    model_monitoring_rect,
                ),
                serving_group_pre),
            m.FadeOut(operation_arrow),
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
        training_group= m.VGroup(training_icon_group, training_label)

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


        self.play(
            self.set_title_row(
                title="Machine Learning Lifecycle",
                seperator=": ",
                subtitle="Semantischer Datenraum",
            ),

            m.FadeIn(broker_icon_group),

            # create connections between icons
            m.Create(broker_preprocessing_line),
            m.Create(broker_serving_line),
            m.Create(broker_training_line),

            m.ReplacementTransform(training_group_pre,training_group),
            m.ReplacementTransform(preprocessing_group_pre,preprocessing_group),
            m.ReplacementTransform(serving_group_pre, serving_group),

            m.FadeOut(model_requirements_stage_group),
            m.FadeOut(model_requirements_stage_text),

            m.FadeOut(data_oriented_stage_surrounding_rect),
            m.FadeOut(data_oriented_stage_text),

            m.FadeOut(model_stage_surrounding_rect),
            m.FadeOut(model_stage_text),

            m.FadeOut(operations_stage_surrounding_rect),
            m.FadeOut(operations_stage_text),

            # fade out arrows between stages
            m.FadeOut(requirements_to_data_stage_arrow),
            m.FadeOut(data_to_model_stage_line1),
            m.FadeOut(data_to_model_stage_line2),
            m.FadeOut(data_to_model_stage_line3),
            m.FadeOut(data_to_model_stage_line4),
            m.FadeOut(data_to_model_stage_line5),

            m.FadeOut(model_stage_to_operations_stage_arrow),
        )

        self.play(
            # create connection lines
            m.Create(broker_others_line),
            m.Create(broker_db_line),
            m.Create(training_mlflow_line),
            m.Create(mlflow_serv_line),

            m.FadeIn(others_group),
            m.FadeIn(database_group),
            m.FadeIn(mlflow_group),
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

        fastiot_services_group.generate_target()
        fastiot_services_group.target.scale(0.5)
        fastiot_services_group.target.to_edge(m.RIGHT, buff=self.med_small_buff)
        fastiot_services_group.target.to_edge(m.UP, buff=1.6)

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
        t2c = {
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

        preprocessing_bullet_points.next_to(fastiot_services_group, m.DOWN, buff=self.med_large_buff,
                                            aligned_edge=m.RIGHT)
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

        training_text_content = self.bullet_point_list([
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
            # t2c={"extrovert": self.blue},
            # this is an alternative to t2c
            # just type the words you want to colorize
            # and specify the color
            # t2c_strs=["talk", "people"],
            # t2c_color=self.green,
        )
        serving_text_box.next_to(self._title_mobject, m.DOWN, buff=self.med_large_buff, aligned_edge=m.LEFT)

        self.play(
            m.FadeIn(serving_text_box),
        )

        fastiot_services_group.generate_target()
        fastiot_services_group.target.scale(2.0)
        fastiot_services_group.target.move_to(m.ORIGIN)

        self.play(
            m.FadeOut(focus_rect),
            m.FadeOut(serving_text_box),
            m.MoveToTarget(fastiot_services_group),
        )

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
            self.set_title_row(
                title="Blueprints",
                seperator=None,
                subtitle=None,
            ),
            m.FadeIn(preprocess_surrounding_rect),
            m.FadeIn(database_surrounding_rect),
            m.FadeIn(training_surrounding_rect),
            m.FadeIn(serving_surrounding_rect),
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
            # height=4.0,
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

            m.AnimationGroup(
                m.AnimationGroup(
                    m.FadeOut(fastiot_services_group),
                    m.FadeOut(preprocess_surrounding_rect),
                    m.FadeOut(database_surrounding_rect),
                    m.FadeOut(training_surrounding_rect),
                    m.FadeOut(serving_surrounding_rect),
                ),
                m.AnimationGroup(
                    m.FadeIn(blueprint_text_box),
                    m.FadeIn(blueprint_example_screenshot),
                    m.FadeIn(blueprint_pytorch_screenshot),
                    m.FadeIn(qr_code),
                ),
                lag_ratio=0.5
            )
        )

        self.wait(0.1)
        self.fade_out_scene()






if __name__ == '__main__':
    #OpenHubDaysMLSlides.render_video_medium()
    OpenHubDaysMLSlides.save_sections()