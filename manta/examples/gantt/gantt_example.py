import manim as m

from color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from elements.gantt_utils import GanttUtils
from slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyGanttExampleScene(GanttUtils, MinimalSlideTemplate):
    subtitle_color = CatppuccinMochaTheme.yellow
    title_seperator_color = CatppuccinMochaTheme.magenta

    def construct(self):
        self.play(
            self.set_title_row(
                title="GanttUtils",
                seperator=": ",
                subtitle="gantt_chart_without_ticks",
            ),
        )

        gantt_data = [
            {'Task': 'Job 0', 'Start': 5, 'Finish': 16, 'Resource': 'Machine 0'},
            {'Task': 'Job 0', 'Start': 28, 'Finish': 31, 'Resource': 'Machine 1'},
            {'Task': 'Job 0', 'Start': 31, 'Finish': 34, 'Resource': 'Machine 2'},
            {'Task': 'Job 0', 'Start': 34, 'Finish': 46, 'Resource': 'Machine 3'},
            {'Task': 'Job 1', 'Start': 0, 'Finish': 5, 'Resource': 'Machine 0'},
            {'Task': 'Job 1', 'Start': 5, 'Finish': 21, 'Resource': 'Machine 2'},
            {'Task': 'Job 1', 'Start': 21, 'Finish': 28, 'Resource': 'Machine 1'},
            {'Task': 'Job 1', 'Start': 28, 'Finish': 32, 'Resource': 'Machine 3'}
        ]

        gantt_char = self.gantt_chart_without_ticks(
            width=4, height=2, data=gantt_data, n_machines=4, resource_naming="Machine"
        )

        gantt_data2 = [{'Task': 'Order 0', 'Start': 0, 'Finish': 27, 'Resource': 'Line 1'},
         {'Task': 'Order 1', 'Start': 16, 'Finish': 36, 'Resource': 'Line 0'},
         {'Task': 'Order 2', 'Start': 26, 'Finish': 41, 'Resource': 'Line 2'},
         {'Task': 'Order 3', 'Start': 36, 'Finish': 56, 'Resource': 'Line 0'},
         {'Task': 'Order 4', 'Start': 0, 'Finish': 10, 'Resource': 'Line 0'},
         {'Task': 'Order 5', 'Start': 37, 'Finish': 47, 'Resource': 'Line 1'},
         {'Task': 'Order 6', 'Start': 10, 'Finish': 16, 'Resource': 'Line 0'},
         {'Task': 'Order 7', 'Start': 8, 'Finish': 13, 'Resource': 'Line 2'},
         {'Task': 'Order 8', 'Start': 0, 'Finish': 8, 'Resource': 'Line 2'},
         {'Task': 'Order 9', 'Start': 13, 'Finish': 26, 'Resource': 'Line 2'},
         {'Task': 'Order 10', 'Start': 27, 'Finish': 37, 'Resource': 'Line 1'},
         {'Task': 'Order 11', 'Start': 64, 'Finish': 71, 'Resource': 'Line 0'},
         {'Task': 'Order 12', 'Start': 73, 'Finish': 78, 'Resource': 'Line 1'},
         {'Task': 'Order 13', 'Start': 73, 'Finish': 79, 'Resource': 'Line 0'},
         {'Task': 'Order 14', 'Start': 76, 'Finish': 80, 'Resource': 'Line 2'},
         {'Task': 'Order 15', 'Start': 68, 'Finish': 72, 'Resource': 'Line 2'},
         {'Task': 'Order 16', 'Start': 67, 'Finish': 73, 'Resource': 'Line 1'},
         {'Task': 'Order 17', 'Start': 52, 'Finish': 68, 'Resource': 'Line 2'},
         {'Task': 'Order 18', 'Start': 55, 'Finish': 59, 'Resource': 'Line 1'},
         {'Task': 'Order 19', 'Start': 60, 'Finish': 64, 'Resource': 'Line 0'},
         {'Task': 'Order 20', 'Start': 56, 'Finish': 60, 'Resource': 'Line 0'},
         {'Task': 'Order 21', 'Start': 45, 'Finish': 52, 'Resource': 'Line 2'},
         {'Task': 'Order 22', 'Start': 59, 'Finish': 67, 'Resource': 'Line 1'},
         {'Task': 'Order 23', 'Start': 47, 'Finish': 55, 'Resource': 'Line 1'},
         {'Task': 'Order 24', 'Start': 41, 'Finish': 45, 'Resource': 'Line 2'},
         {'Task': 'Order 25', 'Start': 72, 'Finish': 76, 'Resource': 'Line 2'}]

        self.play(
            m.Transform(
                gantt_char,
                self.gantt_chart_without_ticks(
                    width=4,
                    height=2,
                    data=gantt_data2,
                    n_machines=3,
                    resource_naming="Line"
                )
            ),
        )


if __name__ == '__main__':
    MyGanttExampleScene.render_video_medium()
