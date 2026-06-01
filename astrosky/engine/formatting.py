def decimal_to_sexagesimal(deg: float) -> tuple[int, int, float]:
    sign = -1 if deg < 0 else 1
    deg = abs(deg)

    d = int(deg)
    m_float = (deg - d) * 60
    m = int(m_float)
    s = round((m_float - m) * 60, 1)

    return sign * d, m, s


def sexagesimal_to_decimal(d: int, m: int, s: float) -> float:
    sign = -1 if d < 0 else 1

    d = abs(d)
    deg = sign * (d + m / 60 + s / 3600)

    return deg
