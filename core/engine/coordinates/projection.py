import math

from engine.math.angles import wrap360
from engine.math.scalar import rad2deg


def project_horizontal(alt: float, sin_az: float, cos_az: float) -> tuple[float, float]:
    az = math.atan2(sin_az, cos_az)

    return rad2deg(alt), wrap360(rad2deg(az))
