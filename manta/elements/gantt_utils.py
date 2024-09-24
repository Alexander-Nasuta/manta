import itertools
from typing import Sequence

import manim as m
from manim import config

from elements.axes_utils import AxesUtils
from manta.logger import log


class GanttUtils(AxesUtils):

    def gantt_chart_without_ticks(self, width: float, height: float, data: list[dict], x_range: float = None,
                                  y_range=None,
                                  color_map: dict[str, m.ManimColor] = None, c_map="coolwarm",
                                  resource_naming="Machine",
                                  n_machines: int = None, n_jobs: int = None) -> m.VGroup:
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
            if color_map is None:
                # create a colormap
                from matplotlib.colors import LinearSegmentedColormap
                colors = [
                    self.blue,
                    self.green,
                    self.yellow,
                    self.red,
                ]
                c_map = LinearSegmentedColormap.from_list("custom_cmap", colors, N=256)
            else:
                c_map = matplotlib.colormaps.get_cmap(c_map)  # select the desired cmap
            arr = np.linspace(0, 1, n_machines)  # create a list with numbers from 0 to 1 with n items
            machine_colors = {m_id: c_map(val) for m_id, val in enumerate(arr)}
            colors = {f"{resource_naming} {m_id}": (r, g, b) for m_id, (r, g, b, a) in machine_colors.items()}


            # map rgb tuples to hex strings
            def rgb_to_hex(rgb):
                return '#{:02X}{:02X}{:02X}'.format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

            color_map = {k: rgb_to_hex(v) for k, v in colors.items()}

        axes = self.term_axes_minimal(
            x_range=[0, x_range, 1],
            y_range=[0, y_range, 1],
            x_length=width,
            y_length=height,
            axis_config={"include_numbers": False, "tip_width": 0.125, "tip_height": 0.25},
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
                stroke_color=self.outline_color,
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
