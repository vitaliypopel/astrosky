import math
import time

from datetime import datetime, timezone

JD_UNIX_EPOCH = 2440587.5
J2000 = 2451545.0


def wrap360(deg: float) -> float:
    return deg % 360.0


def wrap180(deg: float) -> float:
    return (deg + 180.0) % 360.0 - 180.0


def deg2rad(deg: float) -> float:
    return math.radians(deg)


def rad2deg(rad: float) -> float:
    return math.degrees(rad)


def sexagesimal_to_decimal(d: int, m: int, s: float) -> float:
    sign = -1 if d < 0 else 1

    d = abs(d)
    deg = sign * (d + m / 60 + s / 3600)

    return deg


def decimal_to_sexagesimal(deg: float) -> tuple[int, int, float]:
    sign = -1 if deg < 0 else 1
    deg = abs(deg)

    d = int(deg)
    m_float = (deg - d) * 60
    m = int(m_float)
    s = round((m_float - m) * 60, 1)

    return sign * d, m, s


def julian_date(dt: datetime) -> float:
    timestamp = dt.timestamp()

    jd = timestamp / 86400.0 + JD_UNIX_EPOCH

    return jd


def gmst(jd: float) -> float:
    T = (jd - J2000) / 36525.0

    gmst_deg = (
        280.46061837 + 360.98564736629 * (jd - J2000) +
        0.000387933 * T**2 - T**3 / 38710000.0
    )

    return wrap360(gmst_deg)


def lst(gmst_deg: float, lon_deg: float) -> float:
    lst_deg = gmst_deg + lon_deg

    return wrap360(lst_deg)


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

    sin_alt = (
        math.sin(dec) * math.sin(lat) +
        math.cos(dec) * math.cos(lat) * math.cos(ha)
    )

    alt = math.asin(sin_alt)

    sin_az = -math.sin(ha) * math.cos(dec)
    cos_az = (
        math.sin(dec) - math.sin(alt) * math.sin(lat)
    ) / (math.cos(alt) * math.cos(lat))

    az = math.atan2(sin_az, cos_az)

    alt_deg, az_deg = rad2deg(alt), wrap360(rad2deg(az))

    return alt_deg, az_deg


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


def main():
    sirius_ra_h = 6.7525
    sirius_dec_deg = -16.7161

    lat_deg = 49.84
    lon_deg = 24.03

    while True:
        dt = datetime.now(timezone.utc)

        alt_dms, az_dms = calculate_alt_az(
            sirius_ra_h, sirius_dec_deg, lat_deg, lon_deg, dt,
        )

        print(
            f'alt: {alt_dms[0]}° {alt_dms[1]}\' {alt_dms[2]}\"\n'
            f'az: {az_dms[0]}° {az_dms[1]}\' {az_dms[2]}\"\n'
        )

        time.sleep(1)


if __name__ == '__main__':
    main()
