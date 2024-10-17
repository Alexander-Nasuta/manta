# QR Codes




```{eval-rst}
.. manim:: MyQrCodeScene
    :save_last_frame:

    
    import manim as m

    from manta.components.qr_code_utils import QrCodeUtils
    from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
    from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


    class MyQrCodeScene(QrCodeUtils, MinimalSlideTemplate):
        subtitle_color = CatppuccinMochaTheme.yellow
        title_seperator_color = CatppuccinMochaTheme.magenta

        def construct(self):

            qr_code_without_icon = self.qr_code("https://fishshell.com")
            qr_code_with_icon = self.qr_code(
                payload="https://fishshell.com",
                icon='terminal',
                icon_size=6
            )

            qr_code_group = m.VGroup(
                qr_code_without_icon,
                qr_code_with_icon).arrange(m.RIGHT, buff=self.med_large_buff)

            self.play(
                self.set_title_row(
                title="QR Code",
                ),
                m.FadeIn(qr_code_group)
            )


    if __name__ == '__main__':
        MyQrCodeScene.render_video_medium()

```

```{eval-rst}
.. manim:: MySecondQrCodeScene

    
    import manim as m

    from manta.components.qr_code_utils import QrCodeUtils
    from manta.color_theme.catppucin.catppuccin_mocha import CatppuccinMochaTheme
    from manta.slide_templates.minimal.minimal_slide_template import MinimalSlideTemplate


    class MySecondQrCodeScene(QrCodeUtils, MinimalSlideTemplate):
        subtitle_color = CatppuccinMochaTheme.yellow
        title_seperator_color = CatppuccinMochaTheme.magenta

        def construct(self):

            neovim_qr_code = self.qr_code("https://neovim.io/", icon='Neovim')

            self.play(
                self.set_title_row(
                    title="QR Code",
                    seperator=": ",
                    subtitle="Neovim",
                ),
                m.FadeIn(neovim_qr_code)
            )
            self.wait(0.75)

            rust_qr_code = self.qr_code("https://www.rust-lang.org/", icon="language-rust", data_shape='circles')

            self.play(
                self.change_subtitle(subtitle="Rust"),
                m.ReplacementTransform(neovim_qr_code, rust_qr_code),
            )
            self.wait(0.75)

            python_qr_code = self.qr_code("https://www.python.org/",
                                           icon="language-python",
                                           data_shape='circles',
                                           corner_color=self.blue,
                                           icon_color=self.yellow,
                                           icon_size=4,  # make the icon 5 qr code pixels wide
                                          )

            self.play(
                self.change_subtitle(subtitle="Python"),
                m.ReplacementTransform(rust_qr_code, python_qr_code),
            )
            self.wait(0.75)

            # obligatory javascript joke
            js_qr_code = self.qr_code("https://www.javascript.com/",
                                      icon="poo",
                                      data_shape='circles',
                                      corner_color=self.magenta,
                                      white_color=self.yellow,
                                      icon_color=self.black,
                                      )

            self.play(
                self.change_subtitle(subtitle="JavaScript"),
                m.ReplacementTransform(python_qr_code, js_qr_code),
            )
            self.wait(0.75)


            # NOTE: the color 'mauve' and 'lavender' are specific to the catppuccin theme
            # follow the link to learn more about the colors catppuccin theme provides :)
            github_catppuccin_qr_code = self.qr_code("https://github.com/catppuccin/catppuccin",
                                                     icon='cat',
                                                     icon_color=self.mauve,
                                                     data_shape='circles',
                                                     white_color=self.lavender,
                                                     corner_color=self.mauve,
                                                     )

            self.play(
                self.change_subtitle(subtitle="Catppuccin on Github"),
                m.ReplacementTransform(js_qr_code, github_catppuccin_qr_code),
            )
            self.wait(0.75)
            
            self.fade_out_scene()



    if __name__ == '__main__':
        MySecondQrCodeScene.render_video_medium()
```