from dataclasses import dataclass

from engine.models.object import StellarObject


@dataclass(slots=True, frozen=True)
class StellarPosition:
    obj: StellarObject

    ha: float
    alt: float
    az: float
