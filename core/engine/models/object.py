from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class StellarObject:
    ra: float
    dec: float
