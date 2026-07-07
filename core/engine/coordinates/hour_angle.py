from engine.math import wrap180


def hour_angle(ra_h: float, lst_deg: float) -> float:
    return wrap180(lst_deg - ra_h * 15.0)
