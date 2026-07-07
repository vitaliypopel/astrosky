import math

from engine.math import deg2rad


def horizontal_kernel(
    ha_deg: float,
    dec_deg: float,
    lat_deg: float,
) -> tuple[float, float, float]:
    ha = deg2rad(ha_deg)
    dec = deg2rad(dec_deg)
    lat = deg2rad(lat_deg)

    sin_ha = math.sin(ha)
    cos_ha = math.cos(ha)
    sin_dec = math.sin(dec)
    cos_dec = math.cos(dec)
    sin_lat = math.sin(lat)
    cos_lat = math.cos(lat)

    sin_alt = sin_dec * sin_lat + cos_dec * cos_lat * cos_ha
    alt = math.asin(sin_alt)

    sin_az = -sin_ha * cos_dec
    cos_az = (sin_dec - math.asin(alt) * sin_lat) / (math.cos(alt) * cos_lat)

    return alt, sin_az, cos_az
