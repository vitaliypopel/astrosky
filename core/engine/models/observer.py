from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Observer:
    lat: float
    lon: float
