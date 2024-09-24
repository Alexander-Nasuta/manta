
import manim as m
import numpy as np

from color_theme.carolus.corolus_theme import CarolusTheme
from elements.rectangle_utils import RectangleUtils


class IQS_Utils(CarolusTheme, RectangleUtils):

    def igs_hexagon(self) -> m.VGroup:
        poly_2 = m.RegularPolygon(n=6, start_angle=30 * m.DEGREES, color=self.font_color)
        # self.add(poly_2)

        # circles at the corners
        # color_small_circle = TC.CHART_TEAL_LIGHT
        color_I = self.cyan
        color_Q = self.green
        color_S = self.blue

        radius_big_circle = 0.075

        radius_small_circle = 0.045

        edge_stroke_width = 1.5

        # I-Bereich
        coords_I = poly_2.get_vertices()[1]
        circle_up = m.Circle(radius=radius_big_circle, color=color_I, fill_opacity=1).move_to(coords_I)
        circle_up_text = self.term_text("I", color=self.font_color, font_size=10).move_to(coords_I)
        circle_up.move_to(coords_I)
        circle_up_group = m.VGroup(circle_up, circle_up_text)

        I_text_line1 = self.term_text("Information", color=self.font_color, font_size=6)
        # change color of the first character
        I_text_line1[0].set_color(color_I)
        # make first character bold
        I_text_line1[0].weight = "bold"

        I_text_line2 = self.term_text("Management", color=self.font_color, font_size=6)

        I_text_line1.move_to(m.ORIGIN)
        I_text_line2.move_to(np.array([0, -0.1, 0]))

        I_text_group = m.VGroup(I_text_line1, I_text_line2)
        I_text_group.move_to(coords_I + np.array([0, 0.25, 0]))

        # Q-Bereich
        coords_Q = poly_2.get_vertices()[3]
        circle_left_down = m.Circle(radius=radius_big_circle, color=color_Q, fill_opacity=1).move_to(coords_Q)
        circle_left_down_text = self.term_text("Q", color=self.font_color, font_size=10).move_to(coords_Q)
        circle_left_down.move_to(coords_Q)
        circle_left_down_group = m.VGroup(circle_left_down, circle_left_down_text)

        Q_text_line1 = self.term_text("Sustainable", color=self.font_color, font_size=6)
        # change color of the first character
        Q_text_line2 = self.term_text("Quality", color=self.font_color, font_size=6)
        Q_text_line2[0].set_color(color_Q)

        Q_text_line1.move_to(m.ORIGIN)
        Q_text_line2.move_to(m.ORIGIN + np.array([0, -0.1, 0]))

        Q_text_group = m.VGroup(Q_text_line1, Q_text_line2)
        Q_text_group.move_to(coords_I + np.array([0.0, 0.35, 0]))

        Q_text_group.rotate(120 * m.DEGREES, about_point=m.ORIGIN).rotate(-120 * m.DEGREES)

        # S-Bereich
        coords_S = poly_2.get_vertices()[5]
        circle_down_right = m.Circle(radius=radius_big_circle, color=color_S, fill_opacity=1).move_to(coords_S)
        circle_down_right_text = self.term_text("S", color=self.font_color, font_size=10).move_to(coords_S)
        circle_down_right.move_to(coords_S)
        circle_down_right_group = m.VGroup(circle_down_right, circle_down_right_text)

        S_text_line1 = self.term_text("Sensing &", color=self.font_color, font_size=6)
        # change color of the first character
        S_text_line1[0].set_color(color_S)
        S_text_line2 = self.term_text("Robotics", color=self.font_color, font_size=6)

        S_text_line1.move_to(m.ORIGIN)
        S_text_line2.move_to(m.ORIGIN + np.array([0, -0.1, 0]))

        S_text_group = m.VGroup(S_text_line1, S_text_line2)
        S_text_group.move_to(coords_I + np.array([0.0, 0.35, 0]))
        S_text_group.rotate(-120 * m.DEGREES, about_point=m.ORIGIN).rotate(120 * m.DEGREES)

        text_group = m.VGroup(I_text_group, Q_text_group, S_text_group)

        # small circles

        # I - S - connection
        coords_IS = poly_2.get_vertices()[0]
        circle_right_up = m.Circle(radius=radius_small_circle, color=color_I, fill_opacity=1, stroke_color=self.blue,
                                   stroke_width=edge_stroke_width).move_to(coords_IS)

        # I - Q - connection
        coords_IQ = poly_2.get_vertices()[2]
        circle_left_up = m.Circle(radius=radius_small_circle, color=color_Q, fill_opacity=1, stroke_color=color_I,
                                  stroke_width=edge_stroke_width).move_to(coords_IQ)

        # Q - S - connection
        coords_QS = poly_2.get_vertices()[4]
        circle_down = m.Circle(radius=radius_small_circle, color=color_S, fill_opacity=1, stroke_color=color_Q,
                               stroke_width=edge_stroke_width).move_to(coords_QS)

        small_cricle_group = m.VGroup(circle_right_up, circle_left_up, circle_down)

        # edge I - IQ
        edge_I_IQ = m.Line(start=coords_I, end=coords_IQ, color=color_I, stroke_width=edge_stroke_width)
        # edge I - IS
        edge_I_IS = m.Line(start=coords_I, end=coords_IS, color=color_I, stroke_width=edge_stroke_width)
        # edge Q - IQ
        edge_Q_IQ = m.Line(start=coords_Q, end=coords_IQ, color=color_Q, stroke_width=edge_stroke_width)
        # edge Q - QS
        edge_Q_QS = m.Line(start=coords_Q, end=coords_QS, color=color_Q, stroke_width=edge_stroke_width)
        # edge S - IS
        edge_S_IS = m.Line(start=coords_S, end=coords_IS, color=color_S, stroke_width=edge_stroke_width)
        # edge S - QS
        edge_S_QS = m.Line(start=coords_S, end=coords_QS, color=color_S, stroke_width=edge_stroke_width)

        geo_group = m.VGroup(
            edge_I_IQ,
            edge_I_IS,
            circle_up_group,

            edge_Q_IQ,
            edge_Q_QS,
            circle_left_down_group,

            edge_S_IS,
            edge_S_QS,
            circle_down_right_group,

            small_cricle_group
        )

        width = 0.75
        width_shift_corners = 0.15
        height = 0.25

        box_text_y_shift = 0.11
        box_text_scale = 0.5

        position_list = [
            [width, height, 0],  # middle right
            [width + width_shift_corners, 0, 0],  # bottom right
            [width, -height, 0],  # bottom left
            [-width, -height, 0],  # top left
            [-width - width_shift_corners, 0, 0],  # middle
            [-width, height, 0],  # top right
        ]

        # I - IQ - box

        I_IQ_box = m.Polygon(*position_list, color=color_I, fill_color=self.background_color, fill_opacity=1, stroke_width=2)

        I_IQ_text_up = self.term_text("Socio-Technical", color=self.font_color).scale(box_text_scale).move_to(
            [0, box_text_y_shift, 0])
        I_IQ_text_down = self.term_text("Systems", color=self.font_color).scale(box_text_scale).move_to(
            [0, -box_text_y_shift, 0])

        I_IQ_box.move_to(m.ORIGIN)

        # group text box
        IQ_group = m.VGroup(I_IQ_box, I_IQ_text_up, I_IQ_text_down).rotate(30 * m.DEGREES).scale(0.4)

        # middle point of coords_I and coords_I_Q
        middle_I_IQ = (coords_I + coords_IQ) / 2
        IQ_group.move_to(middle_I_IQ)

        # I - IS - box
        I_IS_box = m.Polygon(*position_list, color=color_I, fill_color=self.background_color, fill_opacity=1, stroke_width=2)

        I_IS_text_up = self.term_text("Data", color=self.font_color).scale(box_text_scale).move_to(
            [0, box_text_y_shift, 0])
        I_IS_text_down = self.term_text("Intelligence", color=self.font_color).scale(box_text_scale).move_to(
            [0, -box_text_y_shift, 0])

        I_IS_box.move_to(m.ORIGIN)

        # group text box
        IS_group = m.VGroup(I_IS_box, I_IS_text_up, I_IS_text_down).rotate(-30 * m.DEGREES).scale(0.4)

        # middle point of coords_I and coords_I_S
        middle_I_IS = (coords_I + coords_IS) / 2
        IS_group.move_to(middle_I_IS)

        # Q - IQ - box
        Q_IQ_box = m.Polygon(*position_list, color=color_Q, fill_color=self.background_color, fill_opacity=1, stroke_width=2)

        Q_IQ_text_up = self.term_text("Sustainable", color=self.font_color).scale(box_text_scale).move_to(
            [0, box_text_y_shift, 0])
        Q_IQ_text_down = self.term_text("Organisations", color=self.font_color).scale(box_text_scale).move_to(
            [0, -box_text_y_shift, 0])

        Q_IQ_box.move_to(m.ORIGIN)

        # group text box
        QI_group = m.VGroup(Q_IQ_box, Q_IQ_text_up, Q_IQ_text_down).rotate(90 * m.DEGREES).scale(0.4)

        # middle point of coords_Q and coords_I_Q
        middle_Q_IQ = (coords_Q + coords_IQ) / 2
        QI_group.move_to(middle_Q_IQ)

        # Q - QS - box
        Q_QS_box = m.Polygon(*position_list, color=color_Q, fill_color=self.background_color, fill_opacity=1, stroke_width=2)

        Q_QS_text_up = self.term_text("Quality", color=self.font_color).scale(box_text_scale).move_to(
            [0, box_text_y_shift, 0])
        Q_QS_text_down = self.term_text("Intelligence", color=self.font_color).scale(box_text_scale).move_to(
            [0, -box_text_y_shift, 0])

        Q_QS_box.move_to(m.ORIGIN)

        # group text box
        QS_group = m.VGroup(Q_QS_box, Q_QS_text_up, Q_QS_text_down).rotate(-30 * m.DEGREES).scale(0.4)

        # middle point of coords_Q and coords_Q_S
        middle_Q_QS = (coords_Q + coords_QS) / 2

        QS_group.move_to(middle_Q_QS)

        # S - IS - box
        S_IS_box = m.Polygon(*position_list, color=color_S, fill_color=self.background_color, fill_opacity=1, stroke_width=2)

        S_IS_text_up = self.term_text("Intelligent", color=self.font_color).scale(box_text_scale).move_to(
            [0, box_text_y_shift, 0])
        S_IS_text_down = self.term_text("Metrology", color=self.font_color).scale(box_text_scale).move_to(
            [0, -box_text_y_shift, 0])

        S_IS_box.move_to(m.ORIGIN)

        # group text box
        SI_group = m.VGroup(S_IS_box, S_IS_text_up, S_IS_text_down).rotate(90 * m.DEGREES).scale(0.4)

        # middle point of coords_S and coords_I_S
        middle_S_IS = (coords_S + coords_IS) / 2
        SI_group.move_to(middle_S_IS)

        # S - QS - box
        S_QS_box = m.Polygon(*position_list, color=color_S, fill_color=self.background_color, fill_opacity=1, stroke_width=2)

        S_QS_text_up = self.term_text("Assembly", color=self.font_color).scale(box_text_scale).move_to(
            [0, box_text_y_shift, 0])
        S_QS_text_down = self.term_text("Automation", color=self.font_color).scale(box_text_scale).move_to(
            [0, -box_text_y_shift, 0])

        S_QS_box.move_to(m.ORIGIN)

        # group text box
        SQ_group = m.VGroup(S_QS_box, S_QS_text_up, S_QS_text_down).rotate(30 * m.DEGREES).scale(0.4)

        # middle point of coords_S and coords_Q_S
        middle_S_QS = (coords_S + coords_QS) / 2
        SQ_group.move_to(middle_S_QS)

        iqs_sub_groups = m.VGroup(
            IQ_group,
            IS_group,

            QI_group,
            QS_group,

            SI_group,
            SQ_group
        )

        # connection-circles
        con_circle_radius = 0.005
        con_circle_color = self.outline_color

        con_circles = []
        for coord in [
            np.array([0.01, 0.58, 0]),
            np.array([0.04, 0.42, 0]),
            np.array([0.18, 0.38, 0]),
            np.array([0.47, 0.38, 0]),
            np.array([-0.475, 0.23, 0]),
            np.array([-0.15, 0.171, 0]),
            np.array([-0.05, 0.127, 0]),
            np.array([0.05, 0.2, 0]),
            np.array([-0.19, 0.01, 0]),
            np.array([0.084, -0.05, 0]),
            np.array([0.387, -0.026, 0]),
            np.array([-0.365, -0.2, 0]),
            np.array([0.083, -0.213, 0]),
            np.array([0.18, -0.325, 0]),
            np.array([-0.15, -0.455, 0]),
        ]:
            con_circle = m.Circle(radius=con_circle_radius, stroke_color=con_circle_color, fill_opacity=1,
                                  fill_color=con_circle_color).move_to(coord)
            con_circles.append(con_circle)

        connection_circle_group = m.VGroup(*con_circles)

        # conncection
        con_line_stroke_width = 0.25

        # define hexagon to get coords for the connection lines
        poly_inner_hexagon = m.RegularPolygon(n=6, start_angle=0 * m.DEGREES, color=self.font_color,
                                              stroke_width=0.1).scale(0.75)
        # self.add(poly_inner_hexagon)
        # I - IQ
        con_edges_circles = []
        I_IQ_anchor = poly_inner_hexagon.get_vertices()[2]

        for idx in [0, 1, 4, 7, 8]:
            con_line = m.Line(start=I_IQ_anchor, end=con_circles[idx], color=con_circle_color,
                              stroke_width=con_line_stroke_width)
            con_edges_circles.append(con_line)

        I_IS_anchor = poly_inner_hexagon.get_vertices()[1]

        for idx in [0, 2, 3, 5, 9]:
            con_line = m.Line(start=I_IS_anchor, end=con_circles[idx], color=con_circle_color,
                              stroke_width=con_line_stroke_width)
            con_edges_circles.append(con_line)

        S_IS_anchor = poly_inner_hexagon.get_vertices()[0]

        for idx in [3, 6, 7, 10, 13, ]:
            con_line = m.Line(start=S_IS_anchor, end=con_circles[idx], color=con_circle_color,
                              stroke_width=con_line_stroke_width)
            con_edges_circles.append(con_line)

        S_ST_anchor = poly_inner_hexagon.get_vertices()[-1]

        for idx in [1, 2, 10, 14, 12]:
            con_line = m.Line(start=S_ST_anchor, end=con_circles[idx], color=con_circle_color,
                              stroke_width=con_line_stroke_width)
            con_edges_circles.append(con_line)

        Q_QS_anchor = poly_inner_hexagon.get_vertices()[4]

        for idx in [-1, -2, -4, -6, -7]:
            con_line = m.Line(start=Q_QS_anchor, end=con_circles[idx], color=con_circle_color,
                              stroke_width=con_line_stroke_width)
            con_edges_circles.append(con_line)

        Q_IQ_anchor = poly_inner_hexagon.get_vertices()[3]

        for idx in [4, 5, 6, 11, 12]:
            con_line = m.Line(start=Q_IQ_anchor, end=con_circles[idx], color=con_circle_color,
                              stroke_width=con_line_stroke_width)
            con_edges_circles.append(con_line)

        connection_edges_group = m.VGroup(*con_edges_circles)

        intelligence_text = self.term_text("Intelligence", color=self.font_color).scale(0.5).move_to(np.array([0.0, 0.1, 0]))
        in_text = self.term_text("in", color=self.font_color).scale(0.45).move_to(np.array([0.0, 0.0, 0]))
        quality_sensing_text = self.term_text("Quality Sensing", color=self.font_color).scale(0.5).move_to(
            np.array([0, -0.1, 0]))

        # change color of the first character
        intelligence_text[0].set_color(color_I)
        #quality_sensing_text[0].set_color(color_Q)
        #quality_sensing_text[7].set_color(color_S)
        #intelligence_text[0].weight = 30
        #quality_sensing_text[0].weight = 300
        #quality_sensing_text[7].weight = 3000

        iqs_text_group = m.VGroup(intelligence_text, in_text, quality_sensing_text)

        return m.VGroup(
            # poly_2,
            geo_group,
            text_group,
            connection_circle_group,
            connection_edges_group,
            iqs_sub_groups,
            iqs_text_group
        ).scale(2)
