from datetime import datetime
from typing import Iterable

from engine.coordinates import equatorial_to_horizontal_from_ha, hour_angle
from engine.models import (
    CelestialObject,
    CelestialObjectPosition,
    Observation,
    ObservationContext,
    Observer,
)
from engine.time import gmst, julian_date, lst


def create_context(observer: Observer, dt: datetime) -> ObservationContext:
    jd = julian_date(dt)
    gmst_deg = gmst(jd)
    lst_deg = lst(gmst_deg, observer.lon)

    return ObservationContext(observer, dt, jd, gmst_deg, lst_deg)


def calculate_position(
    context: ObservationContext,
    obj: CelestialObject,
) -> CelestialObjectPosition:
    ha_deg = hour_angle(obj.ra, context.lst)
    alt_deg, az_deg = equatorial_to_horizontal_from_ha(
        ha_deg, obj.dec, context.observer.lat
    )

    return CelestialObjectPosition(obj, ha_deg, alt_deg, az_deg)


def calculate_positions(
    context: ObservationContext,
    objects: Iterable[CelestialObject],
) -> list[CelestialObjectPosition]:
    return [calculate_position(context, obj) for obj in objects]


def observe(observer: Observer, obj: CelestialObject, dt: datetime) -> Observation:
    context = create_context(observer, dt)
    position = calculate_position(context, obj)

    return Observation(context, [position])


def observe_many(
    observer: Observer,
    objects: Iterable[CelestialObject],
    dt: datetime,
) -> Observation:
    context = create_context(observer, dt)
    positions = calculate_positions(context, objects)

    return Observation(context, positions)
