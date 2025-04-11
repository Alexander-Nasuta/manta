<p align="center">
  <img src="https://raw.githubusercontent.com/Alexander-Nasuta/manta/main/resources/logos/logo.png" alt="Alt text" style="max-height: 200px;">
</p>

# Manta

A Framework for building Presentation Slides and themed Videos with Manim. 

- Gitlab: [Manta on Gitlab](https://git-ce.rwth-aachen.de/alexander.nasuta/manta)
- Github: [Manta on Github](https://github.com/Alexander-Nasuta/manta)
- Pypi: [Manta on PiPy](https://pypi.org/project/manta-manim-theme/)
- Documentation: [Manta on Read the Docs](https://manta.readthedocs.io/en/latest/)

## Description

Manta originated from the idea of creating presentation slides with Manim in an easy and time-efficient way.
PowerPoints has extensions and libraries such as [Efficient Elements](https://www.efficient-elements.com/de/) to get 
done presentations faster and more efficiently. Manta essentially tries to do the same for Manim.

Manta is a framework that provides a set of useful tools to create presentation slides with Manim.
It features the following components:
- **SlideTemplates**: Manta provides a set of predefined slide templates that can be used to create slides.
- **Theming**: Manta provides a set of predefined themes and the possibility to create custom themes. Predefined themes
  include [Catppuccin](https://github.com/catppuccin/catppuccin) and [Tokyo Night](https://github.com/folke/tokyonight.nvim).
- **Icons**: Manta provides a waste set of icons that can be used in the slides that you might know from using Nerdfonts.  
- **Editor**: Manim-Editor is a GUI for creating slides with Manim. Mantas slides are designed to be used with Manim-Editor.
- **Examples**: Manta provides a set of examples to get started with creating slides.


## Table of Contents

- [Quickstart](#quickstart)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [State of the Project](#state-of-the-project)
- [Roadmap](#roadmap)
- [Contact](#contact)


## Quickstart

First install manta via pip:
```shell
pip install manta-manim-theme
```

Here is a minimal example of how to use Manta:
```python
from manta.slide_templates.minimal.minimal_intro_slide import MinimalIntroSlide


class MyMinimalExampleSlide(MinimalIntroSlide): # make sure to inherit from one of the slide templates
    
    # have a look at the source code of MinimalIntroSlide for customization options (font size, colors, etc.)
    title = "Manta"
    subtitle = "A Framework for creating Presentation Slides \n with Manim and Python"

    def construct(self):
        self.play(
            self.fade_in_slide()
        )
        self.wait(2)

        self.fade_out_scene()


if __name__ == '__main__':
    # instead of using the command line to render the video (like in Manim)
    # you can use the following method to render the video
    # there is a variety of methods to render the videos 
    # in my opinion this more convenient than using the command line
    MyMinimalExampleSlide.show_last_frame()
```

A brief presentation showcasing Mantas Key-Features is available in its documentation in the **Usage** section.

## Documentation

The documentation for Manta can be found [here](https://alexander-nasuta.github.io/manta/).

Here are also other resources that might be helpful:
- [Manim Documentation](https://docs.manim.community/en/stable/)
- [Manim-Editor Documentation](https://docs.editor.manim.community/en/stable/)
- [Manim-Community Discord](https://discord.gg/mMRrZQg)


## State of the Project

I am using Manta myself to create slides for my presentations, that need to be especially fancy. 
This will not change in the near future. 
I assume that I will continue to develop Manta and add new features to it till at least the end of 2027.

## Contact

If you have any questions or feedback, feel free to contact me via [email](mailto:alexander.nasuta@wzl-iqs.rwth-aachen.de)

## Development


In order to publish the project to PyPi, the project needs to be built and then uploaded to PyPi.

To build the project, run the following command:
`poetry build`
It is considered good practice use the tool `twine` for checking the build and uploading the project to PyPi.
By default the build command creates a `dist` folder with the built project files.
To check all the files in the `dist` folder, run the following command:

```shell
twine check dist/**
```

If the check is successful, you can upload the project to PyPi with the following command:

```shell
twine upload dist/**
```

### Documentation

This project uses `sphinx` for generating the documentation.
It also uses a lot of sphinx extensions to make the documentation more readable and interactive.
For example the extension `myst-parser` is used to enable markdown support in the documentation (instead of the usual .rst-files).
It also uses the `sphinx-autobuild` extension to automatically rebuild the documentation when changes are made.
By running the following command, the documentation will be automatically built and served, when changes are made (make sure to run this command in the root directory of the project):

```shell
sphinx-autobuild ./docs/source/ ./docs/build/html/
```

This project features most of the extensions featured in this Tutorial: [Document Your Scientific Project With Markdown, Sphinx, and Read the Docs | PyData Global 2021](https://www.youtube.com/watch?v=qRSb299awB0).
