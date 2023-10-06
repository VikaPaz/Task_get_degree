"""Main module."""
from math import pi


def get_degree(rdu: float, time: float, accl: float, vel: float = 0) -> float:
    """Get a degree from spacing traveled by the point.

    Args:
        rdu: float - radius
        time: float - time
        accl: float - acceleration
        vel: float - velocity

    Returns:
        float - degree of rotation
    """
    half_degree_circle = 180
    arc = vel * time + (accl * time ** 2) / 2
    alpha = arc / (pi * rdu / half_degree_circle)
    return round(alpha, 2)
