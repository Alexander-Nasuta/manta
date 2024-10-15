from manta.slide_templates.rwth.rwth_slide_template import RwthSlideTemplate


class MyRwthSlide(RwthSlideTemplate):
    subtitle_color = RwthSlideTemplate.rwth_blau_75

    def construct(self):
        self.play(
            self.set_title_row(
                title="RWTH Aachen",
                seperator=": ",
                subtitle="Rheinisch-Westfälische Technische Hochschule Aachen"
            ),
            self.add_logos(),
            self.add_seperator_lines(),
        )


if __name__ == '__main__':
    MyRwthSlide.show_last_frame()