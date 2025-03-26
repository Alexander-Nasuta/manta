import math
import numpy as np

import graph_jsp_env.disjunctive_graph_jsp_env
import manim as m
import theme_elements as TE
import theme_colors as TC
import theme_silde as TS
from color_theme.rwth.rwth_theme import RwthTheme


def gantt_chart(env: graph_jsp_env.disjunctive_graph_jsp_env.DisjunctiveGraphJspEnv, width: float | None = None,
                height: float | None = None, **kwargs) -> m.VGroup:
    return gantt_chart_without_ticks(
        width=2.0 * 16.0 / 9 if width is None else width,
        height=2.0 if height is None else height,
        data=env.network_as_dataframe().to_dict(orient='records'),
        n_machines=env.n_machines,
        n_jobs=env.n_jobs,
        **kwargs
    )


def gantt_chart_without_ticks(width: float, height: float, data: list[dict], x_range: float = None, y_range=None,
                              color_map: dict[str, m.ManimColor] = None, c_map="coolwarm", resource_naming="Machine",
                              n_machines: int = None, n_jobs: int = None) -> m.VGroup:
    """
    colormasp.
    'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r',
    'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Grays', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1',
    'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy',
    'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia',
    'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg',
    'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth',
    'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_grey', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg',
    'gist_yarg_r', 'gist_yerg', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'grey', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma',
    'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring',
    'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r',
    'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r'

    [
        {'Task': 'Job 0', 'Start': 5, 'Finish': 16, 'Resource': 'Machine 0'},
        {'Task': 'Job 0', 'Start': 28, 'Finish': 31, 'Resource': 'Machine 1'},
        {'Task': 'Job 0', 'Start': 31, 'Finish': 34, 'Resource': 'Machine 2'},
        {'Task': 'Job 0', 'Start': 34, 'Finish': 46, 'Resource': 'Machine 3'},
        {'Task': 'Job 1', 'Start': 0, 'Finish': 5, 'Resource': 'Machine 0'},
        {'Task': 'Job 1', 'Start': 5, 'Finish': 21, 'Resource': 'Machine 2'},
        {'Task': 'Job 1', 'Start': 21, 'Finish': 28, 'Resource': 'Machine 1'},
        {'Task': 'Job 1', 'Start': 28, 'Finish': 32, 'Resource': 'Machine 3'}
    ]
    """
    if n_jobs is None:
        n_jobs = 0

    # calc y_range, if not given
    if y_range is None:
        # calc number of Jobs
        jobs = len(set([d["Task"] for d in data]))
        jobs = max(jobs, n_jobs)
        y_range = jobs + 2  # padding of 1 on top and bottom

    # calc x_range, if not given
    if x_range is None:
        if len(data):
            x_range = max(*[d["Finish"] for d in data], 0) + 1
        else:
            x_range = 1

    # calc colormap if not given
    if color_map is None:
        import matplotlib  # version <3.9
        import numpy as np
        c_map = matplotlib.colormaps.get_cmap(c_map)  # select the desired cmap
        arr = np.linspace(0, 1, n_machines)  # create a list with numbers from 0 to 1 with n items
        machine_colors = {m_id: c_map(val) for m_id, val in enumerate(arr)}
        colors = {f"{resource_naming} {m_id}": (r, g, b) for m_id, (r, g, b, a) in machine_colors.items()}

        # map rgb tuples to hex strings
        def rgb_to_hex(rgb):
            return '#{:02X}{:02X}{:02X}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

        color_map = {k: rgb_to_hex(v) for k, v in colors.items()}

    axes = m.Axes(
        x_range=[0, x_range, 1],
        y_range=[0, y_range, 1],
        x_length=width,
        y_length=height,
        y_axis_config={"tick_size": 0},
        x_axis_config={"tick_size": 0},
        axis_config={"include_numbers": False, "tip_width": 0.125, "tip_height": 0.25,
                     "color": RwthTheme.rwth_schwarz_75},
    )

    if not len(data):
        return axes

    # add color key to data dicts
    for d in data:
        d["color"] = color_map[d["Resource"]]

    # add y coordinate to data dicts
    for d in data:
        job_string = d["Task"]
        job_id = int(job_string.split(" ")[1])
        d["y"] = job_id + 1.5

    tasks = []
    for d in data:
        task = m.Rectangle(
            width=d["Finish"] - d["Start"],
            height=1,
            fill_color=d["color"],
            fill_opacity=1,
            stroke_width=1,
            stroke_color=TC.GREY_OUTLINE,
        )

        # sclae task form normal coordinates to axes coordinates
        x_scale = axes.get_x_unit_size()
        y_scale = axes.get_y_unit_size()

        # scale in x direction
        task.stretch(x_scale, 0)
        # scale in y direction
        task.stretch(y_scale, 1)

        task.move_to(axes.c2p(d["Start"] + (d["Finish"] - d["Start"]) / 2, d["y"]))
        tasks.append(task)

    return m.VGroup(*tasks, axes)


def rollout_line(color: m.ManimColor = TC.BLUE, range=4) -> m.Mobject:
    ax = m.Axes(x_range=[0, range * m.PI], y_range=[-1, 1], x_length=range, y_length=1)
    swiggly_line = ax.plot(lambda x: np.sin(x), color=color, x_range=[0, range * m.PI])

    swiggly_line.rotate(-90 * m.DEGREES, about_point=swiggly_line.get_start()).scale(0.25)
    return swiggly_line


def simple_neural_network(input_layer_dim: int = 4,
                          hidden_layer_dim=4,
                          hidden_layer_n=2,
                          output_layer_dim=2,
                          neuron_circle_kwargs=None,
                          arrow_kwargs=None,
                          layer_horizontal_spacing: float = 1.0,
                          layer_vertical_spacing: float = 0.35) -> m.VGroup:
    if neuron_circle_kwargs is None:
        neuron_circle_kwargs = {}
    if arrow_kwargs is None:
        arrow_kwargs = {}

    default_neuron_circle_kwargs = {
        "radius": 0.1,
        "stroke_width": 2,
        "fill_color": TC.GREY_DARK,
        "stroke_color": TC.DEFAULT_FONT,
        "fill_opacity": 0.0
    }
    merged_circle_kwargs = {**default_neuron_circle_kwargs, **neuron_circle_kwargs}

    default_connection_arrow_kwargs = {
        "stroke_width": 3 * 0.5,
        "buff": merged_circle_kwargs["radius"],
        "color": TC.DARK_FONT
    }

    layers = []

    # input layer
    input_layer = m.VGroup()
    input_layer_center = m.ORIGIN
    input_layer_top_coord = input_layer_center + m.UP * (input_layer_dim - 1) * layer_vertical_spacing / 2
    for i in range(input_layer_dim):
        neuron = m.Circle(**merged_circle_kwargs)
        neuron.move_to(input_layer_top_coord)
        neuron.shift(i * m.DOWN * layer_vertical_spacing)
        input_layer.add(neuron)

    layers.append(input_layer)

    # hidden layers

    for idx_h_layer in range(hidden_layer_n):
        hidden_layer = m.VGroup()
        hidden_layer_center = m.ORIGIN + m.RIGHT * layer_horizontal_spacing * len(layers)
        hidden_layer_top_coord = hidden_layer_center + m.UP * (hidden_layer_dim - 1) * layer_vertical_spacing / 2
        for i in range(hidden_layer_dim):
            neuron = m.Circle(**merged_circle_kwargs)
            neuron.move_to(hidden_layer_top_coord)
            neuron.shift(i * m.DOWN * layer_vertical_spacing)
            hidden_layer.add(neuron)
        layers.append(hidden_layer)

    # output layer
    output_layer = m.VGroup()
    output_layer_center = m.ORIGIN + m.RIGHT * layer_horizontal_spacing * len(layers)
    output_layer_top_coord = output_layer_center + m.UP * (output_layer_dim - 1) * layer_vertical_spacing / 2

    for i in range(output_layer_dim):
        neuron = m.Circle(**merged_circle_kwargs)
        neuron.move_to(output_layer_top_coord)
        neuron.shift(i * m.DOWN * layer_vertical_spacing)
        output_layer.add(neuron)
    layers.append(output_layer)

    arrow_layers = []

    # connect layers
    for prev_layer, next_layer in zip(layers[:], layers[1:]):
        arrow_layer = m.VGroup()
        for prev_neuron in prev_layer:
            for next_neuron in next_layer:
                arrow = m.Line(prev_neuron.get_center(), next_neuron.get_center(), **default_connection_arrow_kwargs)
                arrow_layer.add(arrow)
        arrow_layers.append(arrow_layer)

    return m.VGroup(
        m.VGroup(*arrow_layers),
        m.VGroup(*layers),
    )


def simple_neural_network_forward_animation(nn: m.VGroup, color: m.ManimColor = TC.PINK,
                                            run_time=1.5) -> m.AnimationGroup:
    animations = []
    total_runtime = run_time
    layer_runtime = total_runtime / len(nn[1])

    for layer_idx, (layer_connection, layer), in enumerate(zip(nn[0], nn[1])):
        layer_animation = m.AnimationGroup(
            m.ShowPassingFlash(layer_connection.copy().set_color(color), time_width=0.5),
            m.Indicate(layer, color=color, scale_factor=1.0),
            run_time=layer_runtime
        )
        animations.append(layer_animation)

    animations.append(
        m.Indicate(nn[1][-1], color=color, scale_factor=1.0, run_time=layer_runtime)
    )

    nn_animation = m.AnimationGroup(
        *animations,
        lag_ratio=layer_runtime
    )

    return nn_animation


def two_headed_network(
        shared_network_kwargs: dict = None,
        shared_network_color: m.ManimColor = TC.BLUE,
        top_head_network_kwargs: dict = None,
        top_head_network_color: m.ManimColor = TC.GREEN,
        bottom_networks_kwargs: dict = None,
        bottom_networks_color: m.ManimColor = TC.ORANGE_DARK,
        connection_arrow_kwargs: dict = None,
        layer_vertical_spacing=0.35,
        layer_horizontal_spacing=1.0,
) -> m.VGroup:
    if bottom_networks_kwargs is None:
        bottom_networks_kwargs = {}
    if top_head_network_kwargs is None:
        top_head_network_kwargs = {}
    if shared_network_kwargs is None:
        shared_network_kwargs = {}
    if connection_arrow_kwargs is None:
        connection_arrow_kwargs = {}

    default_shared_network_kwargs = {
        "input_layer_dim": 8,
        "hidden_layer_dim": 7,
        "hidden_layer_n": 1,
        "output_layer_dim": 7,
        "neuron_circle_kwargs": {
            "radius": 0.1,
            "stroke_width": 2,
            "fill_color": TC.GREY_DARK,
            "stroke_color": shared_network_color,
            "fill_opacity": 0.0
        },
        "arrow_kwargs": None,
        "layer_horizontal_spacing": layer_horizontal_spacing,
        "layer_vertical_spacing": layer_vertical_spacing
    }
    default_top_head_network_kwargs = {
        "input_layer_dim": 3,
        "hidden_layer_dim": 3,
        "hidden_layer_n": 1,
        "output_layer_dim": 1,
        "neuron_circle_kwargs": {
            "radius": 0.1,
            "stroke_width": 2,
            "fill_color": TC.GREY_DARK,
            "stroke_color": top_head_network_color,
            "fill_opacity": 0.0
        },
        "arrow_kwargs": None,
        "layer_horizontal_spacing": layer_horizontal_spacing,
        "layer_vertical_spacing": layer_vertical_spacing
    }
    default_bottom_head_network_kwargs = {
        "input_layer_dim": 3,
        "hidden_layer_dim": 3,
        "hidden_layer_n": 1,
        "output_layer_dim": 2,
        "neuron_circle_kwargs": {
            "radius": 0.1,
            "stroke_width": 2,
            "fill_color": TC.GREY_DARK,
            "stroke_color": bottom_networks_color,
            "fill_opacity": 0.0
        },
        "arrow_kwargs": None,
        "layer_horizontal_spacing": layer_horizontal_spacing,
        "layer_vertical_spacing": layer_vertical_spacing
    }

    merged_shared_network_kwargs = {**default_shared_network_kwargs, **shared_network_kwargs}
    merged_top_head_network_kwargs = {**default_top_head_network_kwargs, **top_head_network_kwargs}
    merged_bottom_head_network_kwargs = {**default_bottom_head_network_kwargs, **bottom_networks_kwargs}

    top_nn = simple_neural_network(**merged_top_head_network_kwargs)
    bottom_nn = simple_neural_network(**merged_bottom_head_network_kwargs)

    bottom_nn.next_to(top_nn, m.DOWN, buff=layer_vertical_spacing)

    head_networks = m.VGroup(top_nn, bottom_nn)

    shared_nn = simple_neural_network(**merged_shared_network_kwargs)
    shared_nn.next_to(head_networks, m.LEFT, buff=layer_horizontal_spacing)

    _, shared_nn_layers = shared_nn
    _, top_nn_layers = top_nn
    _, bottom_nn_layers = bottom_nn

    input_layer = shared_nn_layers[0]
    output_layer_top = top_nn_layers[-1]
    output_layer_bottom = bottom_nn_layers[-1]

    output_layer = m.VGroup(output_layer_top, output_layer_bottom)

    default_connection_arrow_kwargs = {
        "stroke_width": 3 * 0.5,
        "buff": 0.1,
        "color": TC.DARK_FONT
    }

    merged_connection_arrow_kwargs = {**default_connection_arrow_kwargs, **connection_arrow_kwargs}

    connection_arrows = m.VGroup()
    # connect last layer of shared network with first layer of top head network
    for shared_neuron in shared_nn_layers[-1]:
        for top_neuron in top_nn_layers[0]:
            arrow = m.Line(shared_neuron.get_center(), top_neuron.get_center(), **merged_connection_arrow_kwargs)
            connection_arrows.add(arrow)
    # connect ast layer of shared network with first layer of bottom head network
    for shared_neuron in shared_nn_layers[-1]:
        for bottom_neuron in bottom_nn_layers[0]:
            arrow = m.Line(shared_neuron.get_center(), bottom_neuron.get_center(), **merged_connection_arrow_kwargs)
            connection_arrows.add(arrow)

    return m.VGroup(input_layer, output_layer, connection_arrows, shared_nn, top_nn, bottom_nn).move_to(
        m.ORIGIN
    )


def two_headed_neural_network_forward_animation(two_headed_nn: m.VGroup, color: m.ManimColor = TC.PINK,
                                                run_time_per_layer: float = 0.5):
    input_layer, output_layer, connection_arrows, shared_nn, top_nn, bottom_nn = two_headed_nn

    n_layer_shared = len(shared_nn[1])
    n_layer_top = len(top_nn[1])
    n_layer_bottom = len(bottom_nn[1])

    animations = []

    shared_layer_run_time = run_time_per_layer * n_layer_shared
    top_layer_run_time = run_time_per_layer * n_layer_top
    bottom_layer_run_time = run_time_per_layer * n_layer_bottom

    # shared network
    shared_animation = simple_neural_network_forward_animation(
        shared_nn, color=color, run_time=shared_layer_run_time
    )
    animations.append(shared_animation)

    # animation between shared and top, bottom head networks
    # animate only lines, since the heads are already animated
    shared_to_heads_animation = m.ShowPassingFlash(
        connection_arrows.copy().set_color(color),
        time_width=1,
        run_time=run_time_per_layer
    )
    animations.append(shared_to_heads_animation)

    head_animations = m.AnimationGroup(
        simple_neural_network_forward_animation(top_nn, color=color, run_time=top_layer_run_time),
        simple_neural_network_forward_animation(bottom_nn, color=color, run_time=bottom_layer_run_time),
    )
    animations.append(head_animations)

    resulting_animation = m.AnimationGroup(
        *animations,
        lag_ratio=run_time_per_layer
    )

    return resulting_animation


def go_board(board: list[list[str | float]] = None,
             board_size: tuple[int, int] = (19, 19),
             black_str='B',
             white_str='W',
             blank_strs: list[str] = None,
             width: float = None,
             height: float = None,
             line_spacing: float = 0.125,
             line_kwargs=None,
             cricle_kwargs=None,
             white_color=TC.DEFAULT_FONT,
             black_color=TC.BLUE,
             numeric_value_color=TC.GREEN_LIGHT,
             invalid_position_color=TC.PINK,
             show_numeric_values: bool = False,
             show_stones: bool = True,
             indicate_invalid_positions: bool = False,
             dot_coords: list[tuple[float, float]] = None,
             default_dot_kwargs=None,
             line_color=TC.GREY_ICON,
             board_buff=TE.buff_small) -> m.VGroup:
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

    board_rectangle = TE.rounded_rectangle(width=width, height=height)

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
        'stroke_color': TC.GREY_OUTLINE,
    }

    black_circle_kwargs = {
        **merged_circle_kwargs,
        'fill_color': black_color,
        'stroke_color': TC.GREY_OUTLINE,
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
                    stroke_color=TC.GREY_OUTLINE,
                    stroke_width=0.0
                )
                numeric_stone.move_to(np.array(
                    [v_line.get_center()[0], h_line.get_center()[1], 0]
                ))
                if show_numeric_values:
                    numeric_stone_text = TE.console_math_text(f"{elem:.1f}").scale_to_fit_width(
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
                    stroke_color=TC.GREY_OUTLINE,
                    stroke_width=0.0
                )
                invalid_pos_stone.move_to(stone.get_center())
                invalid_positions.add(invalid_pos_stone)

    return m.VGroup(board_rectangle, grid, dots, invalid_positions, valid_positions, stones)


def go_board_9x9_prefilled(**kwargs) -> m.VGroup:
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
    return go_board(board=board, **kwargs)


def go_board_9x9_masked(**kwargs) -> m.VGroup:
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
    return go_board(
        board=board,
        indicate_invalid_positions=False,
        show_stones=True,
        numeric_value_color=TC.ORANGE_LIGHT,
        **kwargs)


def go_board_9x9_p_values(**kwargs) -> m.VGroup:
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
    return go_board(
        board=board,
        indicate_invalid_positions=False,
        show_stones=True,
        numeric_value_color=TC.ORANGE_LIGHT,
        **kwargs)


def go_board_9x9_action_mask(board: list[list[str | float]] = None, **kwargs) -> m.VGroup:
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

    board_rectangle, grid, dots, invalid_positions, valid_positions, stones = go_board(
        board=board,
        indicate_invalid_positions=True,
        show_stones=False,
        **kwargs)

    return m.VGroup(board_rectangle, grid, dots, invalid_positions.set_opacity(0.9), valid_positions.set_opacity(0.9))


def go_board_13x13_prefilled(**kwargs) -> m.VGroup:
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
    return go_board(board=board, **kwargs)


def go_board_19x19_prefilled(**kwargs) -> m.VGroup:
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
    return go_board(board=board, **kwargs)



def igs_hexagon() -> m.VGroup:
    poly_2 = m.RegularPolygon(n=6, start_angle=30 * m.DEGREES, color=TC.DEFAULT_FONT)
    # self.add(poly_2)

    # circles at the corners
    color_small_circle = TC.CHART_TEAL_LIGHT
    color_I = TC.CHART_TEAL
    color_Q = TC.GREEN
    color_S = TC.BLUE

    radius_big_circle = 0.075
    big_circle_text_scale = 0.2
    big_circle_label_scale = 0.125

    radius_small_circle = 0.045

    edge_stroke_width = 1.5

    # I-Bereich
    coords_I = poly_2.get_vertices()[1]
    circle_up = m.Circle(radius=radius_big_circle, color=color_I, fill_opacity=1).move_to(coords_I)
    circle_up_text = TE.text("I", color=TC.DEFAULT_FONT).scale(big_circle_text_scale).move_to(coords_I)
    circle_up.move_to(coords_I)
    circle_up_group = m.VGroup(circle_up, circle_up_text)

    I_text_line1 = TE.text("Information", color=TC.DEFAULT_FONT).scale(big_circle_label_scale)
    # change color of the first character
    I_text_line1[0].set_color(color_I)
    # make first character bold
    I_text_line1[0].weight = "bold"

    I_text_line2 = TE.text("Management", color=TC.DEFAULT_FONT).scale(big_circle_label_scale)

    I_text_line1.move_to(m.ORIGIN)
    I_text_line2.move_to(np.array([0, -0.1, 0]))

    I_text_group = m.VGroup(I_text_line1, I_text_line2)
    I_text_group.move_to(coords_I + np.array([0, 0.25, 0]))

    # Q-Bereich
    coords_Q = poly_2.get_vertices()[3]
    circle_left_down = m.Circle(radius=radius_big_circle, color=color_Q, fill_opacity=1).move_to(coords_Q)
    circle_left_down_text = TE.text("Q", color=TC.DEFAULT_FONT).scale(big_circle_text_scale).move_to(coords_Q)
    circle_left_down.move_to(coords_Q)
    circle_left_down_group = m.VGroup(circle_left_down, circle_left_down_text)

    Q_text_line1 = TE.text("Sustainable", color=TC.DEFAULT_FONT).scale(big_circle_label_scale)
    # change color of the first character
    Q_text_line2 = TE.text("Quality", color=TC.DEFAULT_FONT).scale(big_circle_label_scale)
    Q_text_line2[0].set_color(color_Q)

    Q_text_line1.move_to(m.ORIGIN)
    Q_text_line2.move_to(m.ORIGIN + np.array([0, -0.1, 0]))

    Q_text_group = m.VGroup(Q_text_line1, Q_text_line2)
    Q_text_group.move_to(coords_I + np.array([0.0, 0.35, 0]))

    Q_text_group.rotate(120 * m.DEGREES, about_point=m.ORIGIN).rotate(-120 * m.DEGREES)

    # S-Bereich
    coords_S = poly_2.get_vertices()[5]
    circle_down_right = m.Circle(radius=radius_big_circle, color=color_S, fill_opacity=1).move_to(coords_S)
    circle_down_right_text = TE.text("S", color=TC.DEFAULT_FONT).scale(big_circle_text_scale).move_to(coords_S)
    circle_down_right.move_to(coords_S)
    circle_down_right_group = m.VGroup(circle_down_right, circle_down_right_text)

    S_text_line1 = TE.text("Sensing &", color=TC.DEFAULT_FONT).scale(big_circle_label_scale)
    # change color of the first character
    S_text_line1[0].set_color(color_S)
    S_text_line2 = TE.text("Robotics", color=TC.DEFAULT_FONT).scale(big_circle_label_scale)

    S_text_line1.move_to(m.ORIGIN)
    S_text_line2.move_to(m.ORIGIN + np.array([0, -0.1, 0]))

    S_text_group = m.VGroup(S_text_line1, S_text_line2)
    S_text_group.move_to(coords_I + np.array([0.0, 0.35, 0]))
    S_text_group.rotate(-120 * m.DEGREES, about_point=m.ORIGIN).rotate(120 * m.DEGREES)


    text_group = m.VGroup(I_text_group, Q_text_group, S_text_group)

    # small circles

    # I - S - connection
    coords_IS = poly_2.get_vertices()[0]
    circle_right_up = m.Circle(radius=radius_small_circle, color=color_I, fill_opacity=1, stroke_color=TC.BLUE,
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
    box_text_scale = 0.25

    position_list = [
        [width, height, 0],  # middle right
        [width + width_shift_corners, 0, 0],  # bottom right
        [width, -height, 0],  # bottom left
        [-width, -height, 0],  # top left
        [-width - width_shift_corners, 0, 0],  # middle
        [-width, height, 0],  # top right
    ]

    # I - IQ - box

    I_IQ_box = m.Polygon(*position_list, color=color_I, fill_color=TC.GREY_DARK, fill_opacity=1, stroke_width=2)

    I_IQ_text_up = TE.text("Socio-Technical", color=TC.DEFAULT_FONT).scale(box_text_scale).move_to(
        [0, box_text_y_shift, 0])
    I_IQ_text_down = TE.text("Systems", color=TC.DEFAULT_FONT).scale(box_text_scale).move_to(
        [0, -box_text_y_shift, 0])

    I_IQ_box.move_to(m.ORIGIN)

    # group text box
    IQ_group = m.VGroup(I_IQ_box, I_IQ_text_up, I_IQ_text_down).rotate(30 * m.DEGREES).scale(0.4)

    # middle point of coords_I and coords_I_Q
    middle_I_IQ = (coords_I + coords_IQ) / 2
    IQ_group.move_to(middle_I_IQ)

    # I - IS - box
    I_IS_box = m.Polygon(*position_list, color=color_I, fill_color=TC.GREY_DARK, fill_opacity=1, stroke_width=2)

    I_IS_text_up = TE.text("Data", color=TC.DEFAULT_FONT).scale(box_text_scale).move_to(
        [0, box_text_y_shift, 0])
    I_IS_text_down = TE.text("Intelligence", color=TC.DEFAULT_FONT).scale(box_text_scale).move_to(
        [0, -box_text_y_shift, 0])

    I_IS_box.move_to(m.ORIGIN)

    # group text box
    IS_group = m.VGroup(I_IS_box, I_IS_text_up, I_IS_text_down).rotate(-30 * m.DEGREES).scale(0.4)

    # middle point of coords_I and coords_I_S
    middle_I_IS = (coords_I + coords_IS) / 2
    IS_group.move_to(middle_I_IS)

    # Q - IQ - box
    Q_IQ_box = m.Polygon(*position_list, color=color_Q, fill_color=TC.GREY_DARK, fill_opacity=1, stroke_width=2)

    Q_IQ_text_up = TE.text("Sustainable", color=TC.DEFAULT_FONT).scale(box_text_scale).move_to(
        [0, box_text_y_shift, 0])
    Q_IQ_text_down = TE.text("Organisations", color=TC.DEFAULT_FONT).scale(box_text_scale).move_to(
        [0, -box_text_y_shift, 0])

    Q_IQ_box.move_to(m.ORIGIN)

    # group text box
    QI_group = m.VGroup(Q_IQ_box, Q_IQ_text_up, Q_IQ_text_down).rotate(90 * m.DEGREES).scale(0.4)

    # middle point of coords_Q and coords_I_Q
    middle_Q_IQ = (coords_Q + coords_IQ) / 2
    QI_group.move_to(middle_Q_IQ)

    # Q - QS - box
    Q_QS_box = m.Polygon(*position_list, color=color_Q, fill_color=TC.GREY_DARK, fill_opacity=1, stroke_width=2)

    Q_QS_text_up = TE.text("Quality", color=TC.DEFAULT_FONT).scale(box_text_scale).move_to(
        [0, box_text_y_shift, 0])
    Q_QS_text_down = TE.text("Intelligence", color=TC.DEFAULT_FONT).scale(box_text_scale).move_to(
        [0, -box_text_y_shift, 0])

    Q_QS_box.move_to(m.ORIGIN)

    # group text box
    QS_group = m.VGroup(Q_QS_box, Q_QS_text_up, Q_QS_text_down).rotate(-30 * m.DEGREES).scale(0.4)

    # middle point of coords_Q and coords_Q_S
    middle_Q_QS = (coords_Q + coords_QS) / 2

    QS_group.move_to(middle_Q_QS)

    # S - IS - box
    S_IS_box = m.Polygon(*position_list, color=color_S, fill_color=TC.GREY_DARK, fill_opacity=1, stroke_width=2)

    S_IS_text_up = TE.text("Intelligent", color=TC.DEFAULT_FONT).scale(box_text_scale).move_to(
        [0, box_text_y_shift, 0])
    S_IS_text_down = TE.text("Metrology", color=TC.DEFAULT_FONT).scale(box_text_scale).move_to(
        [0, -box_text_y_shift, 0])

    S_IS_box.move_to(m.ORIGIN)

    # group text box
    SI_group = m.VGroup(S_IS_box, S_IS_text_up, S_IS_text_down).rotate(90 * m.DEGREES).scale(0.4)

    # middle point of coords_S and coords_I_S
    middle_S_IS = (coords_S + coords_IS) / 2
    SI_group.move_to(middle_S_IS)

    # S - QS - box
    S_QS_box = m.Polygon(*position_list, color=color_S, fill_color=TC.GREY_DARK, fill_opacity=1, stroke_width=2)

    S_QS_text_up = TE.text("Assembly", color=TC.DEFAULT_FONT).scale(box_text_scale).move_to(
        [0, box_text_y_shift, 0])
    S_QS_text_down = TE.text("Automation", color=TC.DEFAULT_FONT).scale(box_text_scale).move_to(
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
    con_circle_color = TC.GREY_OUTLINE

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
    poly_inner_hexagon = m.RegularPolygon(n=6, start_angle=0 * m.DEGREES, color=TC.DEFAULT_FONT,
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

    intelligence_text = TE.text("Intelligence", color=TC.DEFAULT_FONT).scale(0.175).move_to(np.array([0.0, 0.1, 0]))
    in_text = TE.text("in", color=TC.DEFAULT_FONT).scale(0.1).move_to(np.array([0.0, 0.0, 0]))
    quality_sensing_text = TE.text("Quality Sensing", color=TC.DEFAULT_FONT).scale(0.175).move_to(
        np.array([0, -0.1, 0]))

    # change color of the first character
    intelligence_text[0].set_color(color_I)
    quality_sensing_text[0].set_color(color_Q)
    quality_sensing_text[7].set_color(color_S)
    intelligence_text[0].weight = 30
    quality_sensing_text[0].weight = 300
    quality_sensing_text[7].weight = 3000

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
