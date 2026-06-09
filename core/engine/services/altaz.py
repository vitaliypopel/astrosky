from datetime import datetime

from core.engine.coordinates import (
    equatorial_to_horizontal_from_ha,
    hour_angle,
)
from core.engine.time.julian import julian_date
from core.engine.time.sidereal import gmst, lst


def calculate_altaz(
    ra_h: float,
    dec_deg: float,
    lat_deg: float,
    lon_deg: float,
    dt: datetime,
) -> dict[str, float]:
    jd = julian_date(dt)
    gmst_deg = gmst(jd)
    lst_deg = lst(gmst_deg, lon_deg)

    ha_deg = hour_angle(ra_h, lst_deg)
    alt_deg, az_deg = equatorial_to_horizontal_from_ha(ha_deg, dec_deg, lat_deg)

    return {
        'jd': jd,
        'gmst': gmst_deg,
        'lst': lst_deg,
        'ha': ha_deg,
        'alt': alt_deg,
        'az': az_deg,
    }
