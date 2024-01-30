Write your p5js sketches with python and automatically launch them in a new window just by running your script.
* no html
* no javascript
* just python

Also included: autoreload on save!

# Installation
The package is not yet published, so you have to install it as a local package
download the repo, `cd` into it and then
`pip3 install .`


# Usage

open your favourite editor and create a new file `<script.py>` and save it wherever you want

```
from p52 import *

def setup():
    createCanvas(windowWidth, windowHeight)
    stroke(100, 100, 100, 100)
    noFill()


def draw():
    background(100)
    ellipse(mouseX, mouseY, 30, 30)
```

open a terminal, move to the folder where you saved the script and run it with `python3 <script.py>` or just use your editor "run" button if available.

A new window should popup with your sketch!

Bonus: try changing your code and saving, the changes should automatically be reflected in the sketch.

# How does it work?
This package is heavily inspired by the library pyp5js and leverages transcrypt to compile python to javascript.