import manim as m
import numpy as np

from color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
from elements.go_board_utils import GoBoardUtils
from slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyGoBoardExampleScene(GoBoardUtils, MinimalSlideTemplate):
    subtitle_color = CatppuccinMochaTheme.yellow
    title_seperator_color = CatppuccinMochaTheme.magenta

    def construct(self):
        self.play(
            self.set_title_row(
                title="GoBoardUtils",
                seperator=": ",
                subtitle="go_board",
            ),
        )

        board = [
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", "W", "B", "B", "W", "W", "B", "B", " "],
            [" ", "W", " ", "B", " ", "W", " ", "B", " "],
            [" ", "W", "B", "B", "W", "W", " ", "B", " "],
            [" ", "W", " ", "B", " ", "W", " ", "B", " "],
            [" ", "W", "B", "B", "W", "W", " ", "B", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        ]

        go_board = self.go_board(board=board)

        self.play(
            m.FadeIn(go_board),
        )
        self.wait(1.5)

        self.play(
            self.change_subtitle("go_board_9x9_prefilled"),
            m.Transform(go_board, self.go_board_9x9_prefilled())
        )
        self.wait(1.5)

        self.play(
            self.change_subtitle("go_board_9x9_masked"),
            m.Transform(go_board, self.go_board_9x9_masked())
        )
        self.wait(1.5)

        self.play(
            self.change_subtitle("go_board_9x9_p_values"),
            m.Transform(go_board, self.go_board_9x9_p_values())
        )
        self.wait(1.5)

        self.play(
            self.change_subtitle("go_board_9x9_action_mask"),
            m.Transform(go_board, self.go_board_9x9_action_mask())
        )
        self.wait(1.5)

        self.play(
            self.change_subtitle("go_board_13x13_prefilled"),
            m.Transform(go_board, self.go_board_13x13_prefilled())
        )
        self.wait(1.5)

        self.play(
            self.change_subtitle("go_board_19x19_prefilled"),
            m.Transform(go_board, self.go_board_19x19_prefilled())
        )
        self.wait(1.5)

        self.fade_out_scene()


if __name__ == '__main__':
    MyGoBoardExampleScene.render_video_medium()
