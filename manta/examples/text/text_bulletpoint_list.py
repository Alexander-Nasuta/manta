import manim as m

from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


class MyBulletpointExampleScene(MinimalSlideTemplate):

    def construct(self):

        my_bullet_point_list1= self.bullet_point_list(
            bulletpoints=[
                "Bullet Point 1",
                "Bullet Point 2",
                "Bullet Point 3",
            ],
        )

        my_bullet_point_list2 = self.bullet_point_list(
            bulletpoints=[
                "Bullet Point 1",
                "Bullet Point 2",
                "Bullet Point 3",
            ],
            bullet_icon='hamburger',
            bullet_icon_color=self.blue
        )

        list_group = m.VGroup(my_bullet_point_list1, my_bullet_point_list2)
        list_group.arrange(m.RIGHT, buff=self.med_large_buff)

        self.play(
            self.set_title_row(
                title="Text Utils",
                seperator=": ",
                subtitle="bullet_point_list"
            ),
            m.FadeIn(list_group),
        )



if __name__ == '__main__':
    MyBulletpointExampleScene.render_video_medium()
