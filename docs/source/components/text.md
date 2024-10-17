# Text


```{eval-rst}
.. manim:: MyTermTextExamplesScene
    :save_last_frame:

    import manim as m

    from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


    class MyTermTextExamplesScene(MinimalSlideTemplate):

        def construct(self):

            self.play(
                self.set_title_row(
                    title="Text Utils",
                    seperator=": ",
                    subtitle="term_text"
                )
            )

            my_text= self.term_text("Hello World!", font_size=36)

            self.play(
                m.FadeIn(my_text),
            )


    if __name__ == '__main__':
        MyTermTextExamplesScene.render_video_medium()
```

```{eval-rst}
.. manim:: MyTermMathTextExampleScene
    :save_last_frame:

    import manim as m
    
    from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate
    
    
    class MyTermMathTextExampleScene(MinimalSlideTemplate):
    
        def construct(self):
    
            self.play(
                self.set_title_row(
                    title="Text Utils",
                    seperator=": ",
                    subtitle="term_math_text"
                )
            )
    
            cubic_polynomial = self.term_math_text("ax^3 + bx^2 + cx + d")
            cubic_polynomial.scale(2.5)
    
            self.play(
                m.FadeIn(cubic_polynomial ),
            )
    
    
    
    if __name__ == '__main__':
        MyTermMathTextExampleScene.render_video_medium()


```


```{eval-rst}
.. manim:: MyMonospaceExampleScene
    :save_last_frame:

    
    import manim as m
    
    from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate
    
    mono_sketch ="""
                Client                             Server                 
                   ■                                  ■                 
                   │      Establish TCP Connection      │                 
    ┌ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ─ ─ 
                SYN├───────────────────────────────────>░SYN             │
    │              │                                    ░ACK              
                ACK│<───────────────────────────────────░                │
    └ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ─ ─ 
                   │                                    │                 
                   │                                    │                 
                   │         SSL/TLS Handshake          │                 
    ┌ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ─ ─ 
        ClientHello░───────────────────────────────────>░                │
    │              ░                                    ░Server Hello     
        Certificate░<───────────────────────────────────░Certificate     │
    │  verification░                                    ░                 
                   ░                                    ░                │
    │     ClientKey░<──────────────────────────────────>░ServerFinished   
           Exchange│                                    │                │
    └ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ─ ─ 
                   │                                    │                 
                   │     Encrypted Application Data     │                 
    ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ─ ─ 
              HTTP │<──────────────────────────────────>│HTTP            │
    │          GET │                                    │Response         
     ─ ─ ─ ─ ─ ─ ─ ┼ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘
                   │                                    │                 
                   ■                                  ■                 
    """
    
    class MyMonospaceExampleScene(MinimalSlideTemplate):
    
        def construct(self):
    
            mono_space_mobject = self.term_paragraph(
                mono_sketch,
            ).scale_to_fit_height(6)
    
            self.play(
                self.set_title_row(
                    title="Text Utils",
                    seperator=": ",
                    subtitle="term_paragraph"
                ),
                m.FadeIn(mono_space_mobject),
            )
    
    
    if __name__ == '__main__':
        MyMonospaceExampleScene.render_video_medium()

```

```{eval-rst}
.. manim:: MyTextLineExamplesScene
    

    import manim as m
    
    from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate
    
    
    class MyTextLineExamplesScene(MinimalSlideTemplate):
    
        def construct(self):
            self.play(
                self.set_title_row(
                    title="Text Utils",
                    seperator=": ",
                    subtitle="text_line"
                )
            )
    
            segment1, segment2, segment3 = self.text_line("Hello", ", ", "World!", font_size=36)
    
            self.play(
                m.FadeIn(segment1),
                m.FadeIn(segment2),
                m.FadeIn(segment3),
            )
    
            segment1.generate_target()
            segment1.target.set_color(self.magenta)
            segment1.target.to_edge(m.LEFT, buff=self.med_large_buff)
    
            segment2.generate_target()
            segment2.target.set_color(self.green)
            segment2.target.to_edge(m.DOWN, buff=self.med_large_buff)
    
            segment3.generate_target()
            segment3.target.set_color(self.cyan)
            segment3.target.to_edge(m.RIGHT, buff=self.med_large_buff)
    
            self.play(
                m.MoveToTarget(segment1),
                m.MoveToTarget(segment2),
                m.MoveToTarget(segment3),
            )
    
            circle1 = self.math_circle(math_text=r"s_1", color=self.magenta)
            circle2 = self.math_circle(math_text=r"s_2", color=self.green)
            circle3 = self.math_circle(math_text=r"s_3", color=self.cyan)
    
            circle_group = (m.VGroup(circle1, circle2, circle3)
                            .arrange(m.RIGHT, buff=self.med_large_buff)
                            .move_to(m.ORIGIN))
    
            self.play(
                m.ReplacementTransform(segment1, circle1),
                m.ReplacementTransform(segment2, circle2),
                m.ReplacementTransform(segment3, circle3),
            )
            
            self.wait(2)
    
    
    if __name__ == '__main__':
        MyTextLineExamplesScene.render_video_medium()


```

```{eval-rst}
.. manim:: MyTermTextMultilineExampleScene
    :save_last_frame:

    import manim as m
    
    from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate
    
    
    class MyTermTextMultilineExampleScene(MinimalSlideTemplate):
    
        def construct(self):
    
    
            my_text = self.term_text("Hello \n World!", font_size=self.font_size_huge, font_color=self.yellow)
    
            wine_text = """Wine is not 
            an emulator"""
    
            wine_text = self.term_text(wine_text, font_size=self.font_size_huge, color=self.magenta)
    
            text_group = m.VGroup(my_text, wine_text).arrange(m.RIGHT, buff=self.med_large_buff)
            text_group.move_to(m.ORIGIN)
    
    
            self.play(
                self.set_title_row(
                    title="Text Utils",
                    seperator=": ",
                    subtitle="term_text (multiline)",
                    subtitle_kwargs={
                        "t2c": {"(multiline)": self.magenta}
                    }
                ),
                m.FadeIn(text_group),
            )
    
    
    
    
    
    
    if __name__ == '__main__':
        MyTermTextMultilineExampleScene.render_video_medium()

```

```{eval-rst} 
.. manim:: MyBulletpointExampleScene
    :save_last_frame:
    

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

```

```{eval-rst}
.. manim:: MyTitleBulletpointsExampleScene
    :save_last_frame:


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

```
