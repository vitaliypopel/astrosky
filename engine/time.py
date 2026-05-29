from datetime import datetime

from .constants import J2000, JD_UNIX_EPOCH
from .utils import wrap360


def julian_date(dt: datetime) -> float:
    timestamp = dt.timestamp()

    jd = timestamp / 86400.0 + JD_UNIX_EPOCH

    return jd


def gmst(jd: float) -> float:
    T = (jd - J2000) / 36525.0

    gmst_deg = (
        280.46061837
        + 360.98564736629 * (jd - J2000)
        + 0.000387933 * T**2
        - T**3 / 38710000.0
    )

    return wrap360(gmst_deg)


def lst(gmst_deg: float, lon_deg: float) -> float:
    lst_deg = gmst_deg + lon_deg

    return wrap360(lst_deg)
