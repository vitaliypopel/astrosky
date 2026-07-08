from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class CelestialObject:
    ra: float
    dec: float
