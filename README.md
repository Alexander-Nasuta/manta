
## Usage

Manim is an extremely versatile package. The following is an example `Scene` you can construct:

```python
from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
```

In order to view the output of this scene, save the code in a file called `example.py`. Then, run the following in a terminal window:

```sh
manim -p -ql example.py SquareToCircle
```

## Documentation

Documentation is in progress at [ReadTheDocs](https://docs.manim.community/).
