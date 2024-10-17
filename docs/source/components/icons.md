# Icons

```{eval-rst}
.. manim:: MyIconExamplesScene
    :save_last_frame:
    
        
    import manim as m
    
    from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate
    
    
    class MyIconExamplesScene(MinimalSlideTemplate):
    
        def construct(self):
    
            hamburger_icon = self.symbol("hamburger")
            coffee_icon = self.symbol(0xEC15)
    
            icon_group = m.VGroup(hamburger_icon, coffee_icon)
            icon_group.arrange(m.RIGHT, buff=self.med_large_buff)
            icon_group.move_to(m.ORIGIN)
    
            self.play(
                self.set_title_row(
                    title="NerdfontIconUtils",
                    seperator=": ",
                    subtitle="symbol"
                ),
                m.FadeIn(icon_group),
            )
    
    
    
    if __name__ == '__main__':
        MyIconExamplesScene.render_video_medium()


```


```{eval-rst}
.. manim:: MySmallIconGalleryExampleScene
    :save_last_frame:
    
            
    import manim as m
    
    from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate
    
    
    class MySmallIconGalleryExampleScene(MinimalSlideTemplate):
    
        def construct(self):
    
            self.play(
                self.set_title_row(
                    title="NerdfontIconUtils",
                    seperator=": ",
                    subtitle="some example icons",
                )
            )
    
            no_rows = 6
            no_cols = 5
            item_per_page = no_rows * no_cols
    
            from manta.components.nerdfont_icons import SYMBOLS_UNICODE
    
            icon_key_list = list(SYMBOLS_UNICODE.keys())
    
            def icon_group(idx):
                icon_name = icon_key_list[idx]
                icon_unicode = SYMBOLS_UNICODE[icon_name]
    
                m_symbol = self.symbol(icon_unicode)
                m_name = self.term_text(icon_name, font_size=self.font_size_script)
                m_unicode = self.term_text(
                    f"0x{icon_unicode:04X}",
                    font_size=self.font_size_script,
                    font_color=self.blue
                )
    
                m_name.move_to(m.DOWN * 0.35 )
                m_unicode.move_to(m.DOWN * 0.6)
    
                return m.VGroup(m_symbol, m_name, m_unicode)
    
            offset = 7331
            table_content = [
                [
                    icon_group(idx=i*no_cols+j+offset) for j in range(no_cols)
                ] for i in range(no_rows)
            ]
            table = m.MobjectTable(
                table_content,
                v_buff=0.1,
                h_buff=0.1,
                # don't show v adn h lines
                line_config={"stroke_width": 0},
            )
    
            self.play(
                m.FadeIn(table),
            )
    
    
    
    if __name__ == '__main__':
        MySmallIconGalleryExampleScene.render_video_medium()

```