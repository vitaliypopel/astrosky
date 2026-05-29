import math

from .utils import deg2rad, rad2deg, wrap180, wrap360


def equatorial_to_horizontal(
    ra_h: float,
    dec_deg: float,
    lat_deg: float,
    lst_deg: float,
) -> tuple[float, float]:
    ra_deg = ra_h * 15.0

    H = wrap180(lst_deg - ra_deg)

    ha = deg2rad(H)
    dec = deg2rad(dec_deg)
    lat = deg2rad(lat_deg)

    sin_alt = math.sin(dec) * math.sin(lat) + math.cos(dec) * math.cos(lat) * math.cos(
        ha
    )

    alt = math.asin(sin_alt)

    sin_az = -math.sin(ha) * math.cos(dec)
    cos_az = (math.sin(dec) - math.sin(alt) * math.sin(lat)) / (
        math.cos(alt) * math.cos(lat)
    )

    az = math.atan2(sin_az, cos_az)

    alt_deg, az_deg = rad2deg(alt), wrap360(rad2deg(az))

    return alt_deg, az_deg
