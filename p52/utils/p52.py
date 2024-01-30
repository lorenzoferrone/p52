# type: ignore

# here I can define or import those names
# that are modified by the transcrypt compiler
# or that I want to be available inside the sketch without importing
# ie: pop, map, center, etc


# funziona perché js_pop è predefinito dentro transcrypt
def pop():
    window.js_pop()


def canvas():
    createCanvas(windowWidth, windowHeight)


def center():
    translate(windowWidth / 2, windowHeight / 2)


def map(t, a, b, x, y):
    return (t - a) / (b - a) * (y - x) + x
