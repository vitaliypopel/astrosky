from engine.coordinates.hour_angle import hour_angle
from engine.coordinates.kernel import horizontal_kernel
from engine.coordinates.projection import project_horizontal


def equatorial_to_horizontal(
    ra_h: float,
    dec_deg: float,
    lat_deg: float,
    lst_deg: float,
) -> tuple[float, float]:
    ha_deg = hour_angle(ra_h, lst_deg)

    alt, sin_az, cos_az = horizontal_kernel(ha_deg, dec_deg, lat_deg)

    return project_horizontal(alt, sin_az, cos_az)


def equatorial_to_horizontal_from_ha(
    ha_deg: float,
    dec_deg: float,
    lat_deg: float,
) -> tuple[float, float]:
    alt, sin_az, cos_az = horizontal_kernel(ha_deg, dec_deg, lat_deg)

    return project_horizontal(alt, sin_az, cos_az)
