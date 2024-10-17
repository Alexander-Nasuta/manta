<p align="center">
  <img src="https://raw.githubusercontent.com/Alexander-Nasuta/manta/main/resources/logos/logo.png" alt="Alt text" style="max-height: 200px;">
</p>

# Manta

A Framework for building Presentation Slides and themed Videos with Manim. 

- Github: [Manta](https://github.com/Alexander-Nasuta/manta)
- Pypi: [Manta](https://pypi.org/project/manta-manim-theme/)
- Documentation: [Manta Docs](https://alexander-nasuta.github.io/manta/)

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

For the default Manta Theme, the following Nerd Fonts are required to be installed on your system:
- [IosevkaTermSlab](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/IosevkaTermSlab.zip)
- [Symbols Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/NerdFontsSymbolsOnly.zip)

You can find the installation instructions for the Nerd Fonts [here](https://www.nerdfonts.com/)

First install manta via pip:
```shell
pip install manta-manim-theme
```
Then update manim to the latest version:
```shell
pip install -U manim
```
you might see the following error:

```
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
manim-editor 0.3.8 requires manim<0.14.0,>=0.13.1, but you have manim 0.18.1 which is incompatible.
```

Manta uses [Manim-Editor](https://docs.editor.manim.community/en/stable/) for creating slides.
Unfortunately the Manim-Editor dependency is a bit dated and states that it is only compatible with Manim version up to
0.13.1. However, Manta is actually required to use a more recent version of Manim (the initial manta package was developed with the manim version 0.18.1).


## Documentation

The documentation for Manta can be found [here](https://alexander-nasuta.github.io/manta/).

Here are also other resources that might be helpful:
- [Manim Documentation](https://docs.manim.community/en/stable/)
- [Manim-Editor Documentation](https://docs.editor.manim.community/en/stable/)
- [Manim-Community Discord](https://discord.gg/mMRrZQg)

## Contributing

If you want to contribute to Manta, you can do so by creating a pull request. 
If you add new features, please make sure to add minimal test and a example for them in the docs.
Currently there is no automated testing for Manta, I am also unsure if there is a feasible way to test the output of the slides.

## State of the Project

I am using Manta myself to create slides for my presentations, that need to be especially fancy. This will not change in the near future. 
I assume that I will continue to develop Manta and add new features to it till at least the end of 2027.

## Roadmap
- [ ] Add automated testing with tox and pytest
- [ ] Fix Manim-Editor version compatibility

## Contact

If you have any questions or feedback, feel free to contact me via [email](mailto:alexander.nasuta@wzl-iqs.rwth-aachen.de)

## Dev

# build
`poetry build`
# upload on PyPi
`twine check dist/**`
`twine upload dist/**`

# docs
`sphinx-autobuild docs/source/ docs/build/html/`