from math import pi


def get_degree(r: float, t: float, a: float, v: float = 0) -> float:
    s = v * t + a * t ** 2 / 2
    alpha = s / (pi * r * 180)
    return round(alpha, 2)

print(get_degree(1, 2, 2))