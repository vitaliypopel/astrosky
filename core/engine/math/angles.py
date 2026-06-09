def wrap360(deg: float) -> float:
    return deg % 360.0


def wrap180(deg: float) -> float:
    return (deg + 180.0) % 360.0 - 180.0
