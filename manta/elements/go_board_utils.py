import manim as m
import numpy as np

from elements.rectangle_utils import RectangleUtils


class GoBoardUtils(RectangleUtils):

    def go_board(self, board: list[list[str | float]] = None,
                 board_size: tuple[int, int] = (19, 19),
                 black_str='B',
                 white_str='W',
                 blank_strs: list[str] = None,
                 width: float = None,
                 height: float = None,
                 line_spacing: float = 0.125,
                 line_kwargs=None,
                 cricle_kwargs=None,
                 white_color=None,
                 black_color=None,
                 numeric_value_color=None,
                 invalid_position_color=None,
                 show_numeric_values: bool = False,
                 show_stones: bool = True,
                 indicate_invalid_positions: bool = False,
                 dot_coords: list[tuple[float, float]] = None,
                 default_dot_kwargs=None,
                 line_color=None,
                 board_buff=None) -> m.VGroup:
        if board_buff is None:
            board_buff = self.small_buff
        if line_color is None:
            line_color = self.outline_color
        if invalid_position_color is None:
            invalid_position_color = self.red
        if numeric_value_color is None:
            numeric_value_color = self.green
        if black_color is None:
            black_color = self.black
        if white_color is None:
            white_color = self.white

        if default_dot_kwargs is None:
            default_dot_kwargs = {}
        if blank_strs is None:
            blank_strs = [' ', '', None]

        if board is None:
            # set board to empty 9x9 board
            _n_rows, _n_cols = board_size
            board = [[blank_strs[0] for _ in range(_n_cols)] for _ in range(_n_rows)]

        if line_kwargs is None:
            line_kwargs = {}

        if cricle_kwargs is None:
            cricle_kwargs = {}

        # check if all board rows have the same length
        assert len(set([len(row) for row in board])) == 1, "All rows must have the same length"
        # check if all board entries are valid
        for row_idx, row in enumerate(board):
            for col_idx, elem in enumerate(row):
                if isinstance(elem, float):
                    assert 0.0 <= elem <= 1.0, f"[numeric] Invalid board entry: '{elem}' (row: {row_idx}, col: {col_idx})"
                    continue
                assert elem in [black_str, white_str, *blank_strs], \
                    f"Invalid board entry: '{elem}' (row: {row_idx}, col: {col_idx})"

        _len_rows = len(board)
        _len_cols = len(board[0])
        board_size = (_len_rows, _len_cols)

        if dot_coords is None:
            if board_size == (9, 9):
                dot_coords = [(2, 2), (2, 6), (6, 2), (6, 6), (4, 4), ]
            elif board_size == (13, 13):
                dot_coords = [(3, 3), (3, 9), (9, 3), (9, 9), (6, 6), ]
            elif board_size == (19, 19):
                dot_coords = [(3, 3), (3, 9), (3, 15), (9, 3), (9, 9), (9, 15), (15, 3), (15, 9), (15, 15), ]

        if width is None and height is None:
            width = line_spacing * _len_cols + 2 * board_buff
            height = line_spacing * _len_rows + 2 * board_buff

        if width is None and height is not None:
            width = height

        if width is not None and height is None:
            height = width

        _line_h_spacing = (width - 2 * board_buff) / (_len_cols - 1)
        _line_v_spacing = (height - 2 * board_buff) / (_len_rows - 1)
        line_spacing = min(_line_h_spacing, _line_v_spacing)

        board_rectangle = self.rounded_rectangle(width=width, height=height)

        default_line_kwargs = {
            "stroke_width": 1.0,
            "stroke_color": line_color
        }
        merged_line_kwargs = {**default_line_kwargs, **line_kwargs}
        # create grid
        grid = m.VGroup(
            m.VGroup(),  # horizontal lines
            m.VGroup(),  # vertical lines
        )
        horizontal_lines, vertical_lines = grid

        # horizontal lines
        for i in range(_len_rows):
            h_line = m.Line(
                start=board_rectangle.get_left() + board_buff * m.RIGHT,
                end=board_rectangle.get_right() + board_buff * m.LEFT,
                **merged_line_kwargs
            )
            h_line.shift(i * _line_v_spacing * m.DOWN)
            horizontal_lines.add(h_line)

        # vertical lines
        for i in range(_len_cols):
            v_line = m.Line(
                start=board_rectangle.get_bottom() + board_buff * m.UP,
                end=board_rectangle.get_top() + board_buff * m.DOWN,
                **merged_line_kwargs
            )
            # align vertical lines with horizontal lines
            v_line.move_to(horizontal_lines[0], aligned_edge=m.UL)
            v_line.shift(i * _line_h_spacing * m.RIGHT)
            vertical_lines.add(v_line)

        # position grid in the center of the board rectangle
        grid.move_to(board_rectangle.get_center())

        # board dots (indexed 0)
        default_dot_kwargs = {
            "radius": line_spacing * 0.2,
            "fill_color": line_color,
            "fill_opacity": 1.0,
            "stroke_width": 0.0
        }
        merged_dot_kwargs = {**default_dot_kwargs, **default_dot_kwargs}

        # add dots to grid
        dots = m.VGroup()
        for row, col in dot_coords:
            dots.add(m.Circle(**merged_dot_kwargs).move_to(np.array(
                [vertical_lines[col].get_center()[0], horizontal_lines[row].get_center()[1], 0]
            )))

        # create stones
        circle_default_kwargs = {
            'radius': line_spacing / 2.0 * 0.8,
            'stroke_width': 1.0,
            'fill_opacity': 1.0,
        }
        merged_circle_kwargs = {**circle_default_kwargs, **cricle_kwargs}

        white_circle_kwargs = {
            **merged_circle_kwargs,
            'fill_color': white_color,
            'stroke_color': self.outline_color,
        }

        black_circle_kwargs = {
            **merged_circle_kwargs,
            'fill_color': black_color,
            'stroke_color': self.outline_color,
        }

        stones = m.VGroup()

        valid_positions = m.VGroup()
        invalid_positions = m.VGroup()

        for h_line, row in zip(horizontal_lines, board):
            for v_line, elem in zip(vertical_lines, row):
                if elem == white_str:
                    stone = m.Circle(**white_circle_kwargs)
                elif elem == black_str:
                    stone = m.Circle(**black_circle_kwargs)
                elif isinstance(elem, float):
                    numeric_stone = m.RoundedRectangle(
                        corner_radius=line_spacing * 0.0,
                        height=line_spacing * 0.9,
                        width=line_spacing * 0.9,
                        fill_color=numeric_value_color,
                        fill_opacity=0.3 + elem * 0.7,
                        stroke_color=self.outline_color,
                        stroke_width=0.0
                    )
                    numeric_stone.move_to(np.array(
                        [v_line.get_center()[0], h_line.get_center()[1], 0]
                    ))
                    if show_numeric_values:
                        numeric_stone_text = self.term_math_text(f"{elem:.1f}").scale_to_fit_width(
                            numeric_stone.width * 0.9)
                        numeric_stone_text.move_to(numeric_stone.get_center())
                        numeric_stone = m.VGroup(numeric_stone, numeric_stone_text)
                    valid_positions.add(numeric_stone)
                    continue
                else:
                    continue
                stone.move_to(np.array(
                    [v_line.get_center()[0], h_line.get_center()[1], 0]
                ))
                if not show_stones:
                    stone.set_opacity(0.0)

                stones.add(stone)

                if indicate_invalid_positions:
                    invalid_pos_stone = m.RoundedRectangle(
                        corner_radius=line_spacing * 0.0,
                        height=line_spacing * 0.9,
                        width=line_spacing * 0.9,
                        fill_color=invalid_position_color,
                        fill_opacity=0.9,
                        stroke_color=self.outline_color,
                        stroke_width=0.0
                    )
                    invalid_pos_stone.move_to(stone.get_center())
                    invalid_positions.add(invalid_pos_stone)

        return m.VGroup(board_rectangle, grid, dots, invalid_positions, valid_positions, stones)

    def go_board_9x9_prefilled(self, **kwargs) -> m.VGroup:
        board = [
            [" ", " ", " ", "W", " ", " ", " ", " ", " "],
            [" ", " ", " ", "W", "B", " ", " ", " ", " "],
            [" ", " ", " ", "W", "B", " ", " ", " ", " "],
            [" ", " ", " ", " ", "W", " ", "W", " ", " "],
            [" ", " ", " ", " ", " ", " ", "B", "W", " "],
            [" ", "B", "B", "W", "W", "W", "B", " ", " "],
            [" ", " ", "B", "W", " ", "B", " ", " ", " "],
            [" ", " ", " ", " ", " ", "B", " ", " ", " "],
            [" ", " ", " ", " ", " ", "B", " ", " ", " "],
        ]
        return self.go_board(board=board, **kwargs)

    def go_board_9x9_masked(self, **kwargs) -> m.VGroup:
        board = [
            [.02, .05, .05, "W", .10, .10, .10, .05, .02],
            [.05, .10, .10, "W", "B", .40, .30, .05, .05],
            [.10, .20, .15, "W", "B", .80, .35, .20, .10],
            [.15, .30, .20, .70, "W", .90, "W", .20, .10],
            [.50, .70, .90, .90, 1.0, .95, "B", "W", .10],
            [.30, "B", "B", "W", "W", "W", "B", .10, .10],
            [.20, .30, "B", "W", .50, "B", .10, .10, .10],
            [.05, .20, .60, .55, .50, "B", .10, .10, .10],
            [.05, .10, .10, .20, .30, "B", .10, .10, .10],
        ]
        return self.go_board(
            board=board,
            indicate_invalid_positions=False,
            show_stones=True,
            numeric_value_color=self.yellow,
            **kwargs)

    def go_board_9x9_p_values(self, **kwargs) -> m.VGroup:
        board = [
            [.02, .05, .05, .15, .10, .10, .10, .05, .02],
            [.05, .10, .10, .40, .50, .40, .30, .05, .05],
            [.10, .20, .15, .50, .70, .80, .35, .20, .10],
            [.15, .30, .20, .70, .80, .90, .50, .20, .10],
            [.50, .70, .90, .90, 1.0, .95, .60, .30, .10],
            [.30, .75, .88, .87, .85, .75, .70, .10, .10],
            [.20, .30, .75, .80, .50, .40, .10, .10, .10],
            [.05, .20, .60, .55, .50, .40, .10, .10, .10],
            [.05, .10, .10, .20, .30, .35, .10, .10, .10],
        ]
        return self.go_board(
            board=board,
            indicate_invalid_positions=False,
            show_stones=True,
            numeric_value_color=self.yellow,
            **kwargs)

    def go_board_9x9_action_mask(self, board: list[list[str | float]] = None, **kwargs) -> m.VGroup:
        board = [
            [.02, .05, .05, "W", .10, .10, .10, .05, .02],
            [.05, .10, .10, "W", "B", .40, .30, .05, .05],
            [.10, .20, .15, "W", "B", .80, .35, .20, .10],
            [.15, .30, .20, .70, "W", .90, "W", .20, .10],
            [.50, .70, .90, .90, 1.0, .95, "B", "W", .10],
            [.30, "B", "B", "W", "W", "W", "B", .10, .10],
            [.20, .30, "B", "W", .50, "B", .10, .10, .10],
            [.05, .20, .60, .55, .50, "B", .10, .10, .10],
            [.05, .10, .10, .20, .30, "B", .10, .10, .10],
        ] if board is None else board

        board_rectangle, grid, dots, invalid_positions, valid_positions, stones = self.go_board(
            board=board,
            indicate_invalid_positions=True,
            show_stones=False,
            **kwargs)

        return m.VGroup(board_rectangle, grid, dots, invalid_positions.set_opacity(0.9),
                        valid_positions.set_opacity(0.9))

    def go_board_13x13_prefilled(self, **kwargs) -> m.VGroup:
        board = [
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", "B", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", "B", "W", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", "B", " ", "W", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", "B", "W", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", "B", "W", " ", " ", " ", " "],
            [" ", " ", "W", "W", "B", "W", "W", "W", " ", "B", " ", " ", " "],
            [" ", " ", "W", " ", "B", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", "B", " ", " ", " ", " ", " ", "B", " ", " "],
            [" ", " ", " ", " ", "W", "B", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", "W", "B", "B", " ", "B", " ", " ", " ", " "],
            [" ", " ", "W", " ", " ", "B", "W", "W", "W", "B", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", "B", " ", " ", "W", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        ]
        return self.go_board(board=board, **kwargs)

    def go_board_19x19_prefilled(self, **kwargs) -> m.VGroup:
        board = [
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", "B", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "B", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "B", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "B", " ", "B", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "B", " ", "W", " ", " ", " ", " ", " ", " "],
            [" ", " ", "W", " ", "B", " ", "B", " ", " ", "W", "W", " ", " ", " ", " ", "W", "W", " ", " "],
            [" ", " ", " ", "W", "W", "B", " ", " ", " ", "B", "B", "W", "W", "W", "B", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", "B", "W", "B", "B", "W", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        ]
        return self.go_board(board=board, **kwargs)
