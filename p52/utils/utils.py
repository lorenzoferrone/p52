# type: ignore
from p52 import map  # it comes from utils.p52


def subdivide(start, end, n):
    return [map(i, 0, n - 1, start, end) for i in range(n)]
