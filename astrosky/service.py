from datetime import datetime

from .coordinates import equatorial_to_horizontal
from .formatting import decimal_to_sexagesimal
from .time import gmst, julian_date, lst


def calculate_alt_az(
    ra_h: float,
    dec_deg: float,
    lat_deg: float,
    lon_deg: float,
    dt: datetime,
) -> tuple[tuple[int, int, float], tuple[int, int, float]]:
    jd = julian_date(dt)
    gmst_deg = gmst(jd)
    lst_deg = lst(gmst_deg, lon_deg)

    alt_deg, az_deg = equatorial_to_horizontal(ra_h, dec_deg, lat_deg, lst_deg)

    alt_dms, az_dms = decimal_to_sexagesimal(alt_deg), decimal_to_sexagesimal(az_deg)

    return alt_dms, az_dms
