from dataclasses import dataclass

from engine.models.context import ObservationContext
from engine.models.position import CelestialObjectPosition


@dataclass(slots=True, frozen=True)
class Observation:
    context: ObservationContext
    positions: list[CelestialObjectPosition]
