import math


def wrap360(deg: float) -> float:
    return deg % 360.0


def wrap180(deg: float) -> float:
    return (deg + 180.0) % 360.0 - 180.0


def deg2rad(deg: float) -> float:
    return math.radians(deg)


def rad2deg(rad: float) -> float:
    return math.degrees(rad)
