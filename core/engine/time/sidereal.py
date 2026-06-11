from engine.math.angles import wrap360
from engine.time.constants import J2000


def gmst(jd: float) -> float:
    T = (jd - J2000) / 36525.0

    return wrap360(
        280.46061837
        + 360.98564736629 * (jd - J2000)
        + 0.000387933 * T**2
        - T**3 / 38710000.0
    )


def lst(gmst_deg: float, lon_deg: float) -> float:
    return wrap360(gmst_deg + lon_deg)
