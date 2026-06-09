def deg_to_dms(deg: float) -> tuple[int, int, float]:
    sign = -1 if deg < 0 else 1
    deg = abs(deg)

    d = int(deg)
    m = int((deg - d) * 60)
    s = round((deg - d - m / 60) * 3600, 1)

    return sign * d, m, s


def deg_to_hms(deg_hours: float) -> tuple[int, int, float]:
    return deg_to_dms(deg_hours / 15)


def dms_to_deg(d: int, m: int, s: float) -> float:
    sign = -1 if d < 0 else 1
    d = abs(d)

    return sign * (d + m / 60 + s / 3600)


def hms_to_deg(h: int, m: int, s: float) -> float:
    return dms_to_deg(h, m, s) * 15
