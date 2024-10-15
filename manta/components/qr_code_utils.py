

import manim as m
import segno
import numpy as np
from components.rectangle_utils import RectangleUtils


class QrCodeUtils(RectangleUtils):

    def qr_code(self, payload: str, corner_size=7,
                icon: str | int | None = None,
                icon_color:str = None,
                icon_size: float = 10,  # in qr pixel
                icon_margin_size: float = 0.1,  # in qr pixel
                white_color: str = None,
                corner_color: str = None,
                data_shape: str = 'rectangles',
                rectangles_kwargs: dict = None,
                circle_kwargs: dict = None,
                error_correction='H',
                segno_kwargs: dict = None,
                ** kwargs, ) -> m.VGroup:
        if icon_color is None:
            icon_color = self.white
        if white_color is None:
            white_color = self.white
        if corner_color is None:
            corner_color = white_color
        if data_shape not in ['circles', 'rectangles']:
            raise ValueError(f"Invalid data_shape: {data_shape}. valid values are 'circles' and 'rectangles'")
        if rectangles_kwargs is None:
            rectangles_kwargs = {}
        if circle_kwargs is None:
            circle_kwargs = {}
        if segno_kwargs is None:
            segno_kwargs = {}


        # Create a QR code with the given data
        qr = segno.make(payload, error=error_correction, **segno_kwargs)

        # Get the dimensions of the QR code
        matrix = qr.matrix
        size = len(matrix)


        # Define the positions of the corner elements
        corner_positions = set()
        for i in range(corner_size):
            for j in range(corner_size):
                corner_positions.add((i, j))
                corner_positions.add((i, size - 1 - j))
                corner_positions.add((size - 1 - i, j))

        # Create a VGroup to hold all the elements
        qr_data_group = m.VGroup()
        qr_corner_group = m.VGroup()

        # Draw a rectangle or circle for each module of the QR code, except for the corner elements
        for y, row in enumerate(matrix):
            for x, is_white_qr_pixel in enumerate(row):
                current_elem = None

                if data_shape == 'rectangles' and is_white_qr_pixel:
                    default_rect_kwargs = {
                        'width': 1,
                        'height': 1,
                        'fill_opacity': 1,
                        'color': white_color,
                        'stroke_width': 0.5,
                    }
                    rect_kwargs = {**default_rect_kwargs, **rectangles_kwargs}

                    rect = m.Rectangle(
                        **rect_kwargs
                    )
                    rect.move_to(m.DOWN*y + m.RIGHT*x)
                    current_elem = rect

                elif data_shape == 'circles' and is_white_qr_pixel:
                    default_circle_kwargs = {
                        'radius': 0.5,
                        'fill_opacity': 1,
                        'color': white_color,
                        'stroke_width': 0.5,
                    }
                    circle_kwargs = {**default_circle_kwargs, **circle_kwargs}
                    circle = m.Circle(
                        **circle_kwargs
                    )
                    circle.move_to(m.DOWN*y + m.RIGHT*x)
                    current_elem = circle

                # override current_elem if it is a corner element
                if is_white_qr_pixel and (x, y) in corner_positions:
                    default_corner_kwargs = {
                        'width': 1,
                        'height': 1,
                        'fill_opacity': 1,
                        'color': corner_color,
                        'stroke_width': 0.5,
                    }
                    corner_kwargs = {**default_corner_kwargs, **rectangles_kwargs}
                    rect = m.Rectangle(
                        **corner_kwargs
                    )
                    rect.move_to(m.DOWN*y + m.RIGHT*x)
                    current_elem = rect

                    qr_corner_group.add(current_elem)
                    continue

                if current_elem is not None:
                    qr_data_group.add(current_elem)


        qr_code_group = m.VGroup(qr_corner_group, qr_data_group)
        qr_code_group.move_to(m.ORIGIN)

        if icon is not None:
            # add icon to the center
            center_icon = self.symbol(icon)
            center_icon.set_color(icon_color)
            # scale icon to fit the qr center mask

            # if width is larger than height, then scale by using scale_to_fit_width
            # else scale by using scale_to_fit_height
            if center_icon.width > center_icon.height:
                center_icon.scale_to_fit_width(icon_size - 2 * icon_margin_size)
            else:
                center_icon.scale_to_fit_height(icon_size - 2 * icon_margin_size)


            center_icon_bounding_box = m.Rectangle(width=icon_size, height=icon_size, fill_opacity=0, stroke_width=0)
            # filter out all the qr pixels that are inside the icon bounding box
            for qr_pixel in qr_data_group:
                pixel_x, pixel_y, _ = qr_pixel.get_center()

                box_min_x = center_icon_bounding_box.get_left()[0]
                box_max_x = center_icon_bounding_box.get_right()[0]

                box_min_y = center_icon_bounding_box.get_bottom()[1]
                box_max_y = center_icon_bounding_box.get_top()[1]

                if box_min_x <= pixel_x <= box_max_x and box_min_y <= pixel_y <= box_max_y:
                    qr_data_group.remove(qr_pixel)

            qr_code_group.add(center_icon)

        return qr_code_group.scale_to_fit_width(2)

