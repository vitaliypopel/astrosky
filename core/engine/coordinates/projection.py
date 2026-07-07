import math

from engine.math import rad2deg, wrap360


def project_horizontal(alt: float, sin_az: float, cos_az: float) -> tuple[float, float]:
    az = math.atan2(sin_az, cos_az)

    return rad2deg(alt), wrap360(rad2deg(az))
