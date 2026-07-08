from dataclasses import dataclass

from engine.models.object import CelestialObject


@dataclass(slots=True, frozen=True)
class CelestialObjectPosition:
    obj: CelestialObject

    ha: float
    alt: float
    az: float
