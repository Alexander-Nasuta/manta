import manim as m

from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyTitleBulletpointsExampleScene(MinimalSlideTemplate):

    def construct(self):

        titled_bulletpoints= self.titled_bulletpoints(
            titled_bulletpoints=[(
                "Title 1",
                [
                    "Bullet Point 1",
                    "Bullet Point 2",
                    "Bullet Point 3",
                ]
            ),
                (
                    "Title 2",
                    [
                        "Bullet Point 1",
                        "Bullet Point 2",
                        "Bullet Point 3",
                    ]
                )
            ],
        )
        titled_bulletpoints2 = self.titled_bulletpoints(
            titled_bulletpoints=[(
                "Title 1",
                [
                    "Bullet Point 1",
                    "Bullet Point 2",
                    "Bullet Point 3",
                ]
            ),
                (
                    "Title 2",
                    [
                        "Bullet Point 1",
                        "Bullet Point 2",
                        "Bullet Point 3",
                    ]
                )
            ],
            bullet_icon='hamburger',
            bullet_icon_color=self.blue
        )

        my_group = m.VGroup(titled_bulletpoints, titled_bulletpoints2)
        my_group.arrange(m.RIGHT, buff=self.med_large_buff)
        my_group.move_to(m.ORIGIN)

        self.play(
            self.set_title_row(
                title="Text Utils",
                seperator=": ",
                subtitle="titled_bulletpoints"
            ),
            m.FadeIn(my_group),
        )



if __name__ == '__main__':
    MyTitleBulletpointsExampleScene.render_video_medium()
