from datetime import datetime


def julian_date(dt: datetime) -> float:
    JD_UNIX_EPOCH = 2440587.5

    return dt.timestamp() / 86400.0 + JD_UNIX_EPOCH
