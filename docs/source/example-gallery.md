# Example Gallery

This gallery contains a collection of code snippets together with their corresponding output, illustrating different 
functionalities all across the library.

```{tip}
This gallery is not the only place in our documentation where you can see explicit code and video examples: there are many more in our reference manual – see, for example, our documentation for the modules TODO and many more.

Check out our interactive Jupyter environment which allows running the examples online, without requiring a local installation.
```

```{eval-rst}
.. manim:: ExampleIntroSlide
    
    from manta.slide_templates.minimal.minimal_intro_slide import MinimalIntroSlide
    
    class ExampleIntroSlide(MinimalIntroSlide):

        title = "Manta "
        subtitle = "A Framework for creating Presentation Slides \n with Manim"

        def construct(self):
            self.play(
            
                self.fade_in_slide()
            )

```




