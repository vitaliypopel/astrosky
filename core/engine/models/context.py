from dataclasses import dataclass
from datetime import datetime

from engine.models.observer import Observer


@dataclass(slots=True, frozen=True)
class ObservationContext:
    observer: Observer
    dt: datetime

    jd: float
    gmst: float
    lst: float
