# type: ignore
from p52 import map  # it comes from utils.p52


def subdivide(start, end, n):
    return [map(i, 0, n - 1, start, end) for i in range(n)]


def widthRange(buffer=0):
    return (-width / 2 + buffer, width / 2 - buffer)


def heightRange(buffer=0):
    return (-height / 2 + buffer, height / 2 - buffer)


def randomPoint(buffer=0):
    return random(*widthRange(buffer)), random(*heightRange(buffer))


# TODO: capire come funziona per le rotation
def getRealCoord(x, y):
    matrix = drawingContext.getTransform()

    rotation = atan2(matrix.b, matrix.a)
    scale_x = sqrt(matrix.a**2 + matrix.c**2)
    scale_y = sqrt(matrix.b**2 + matrix.d**2)
    realX, realY = matrix.e / scale_x, matrix.f / scale_y

    return x - realX, y - realY
