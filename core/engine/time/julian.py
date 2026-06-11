from datetime import datetime

from engine.time.constants import JD_UNIX_EPOCH


def julian_date(dt: datetime) -> float:
    return dt.timestamp() / 86400.0 + JD_UNIX_EPOCH
