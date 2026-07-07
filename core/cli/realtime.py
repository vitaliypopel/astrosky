import argparse
import time
from datetime import datetime, timedelta, timezone

from engine import observe
from engine.formatting import deg_to_dms, deg_to_hms
from engine.models import Observer, StellarObject


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--ra',
        type=float,
        required=True,
        help='Right Ascension in degrees, e.g. 3.141592',
    )
    parser.add_argument(
        '--dec',
        type=float,
        required=True,
        help='Declination in degrees, e.g. 3.141592',
    )

    parser.add_argument(
        '--lat',
        type=float,
        required=True,
        help='Latitude in degrees, e.g. 40.741895',
    )
    parser.add_argument(
        '--lon',
        type=float,
        required=True,
        help='Longitude in degrees, e.g. -73.989308',
    )

    parser.add_argument(
        '--dt',
        type=lambda dt_iso: datetime.fromisoformat(str(dt_iso)),
        help='ISO 8601 datetime, e.g. 2000-01-01T00:00:00+00:00',
    )

    parser.add_argument(
        '--interval',
        type=float,
        default=1.0,
        help='Real-time interval in seconds, e.g. 1, 5, 10',
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    observer = Observer(args.lat, args.lon)
    obj = StellarObject(args.ra, args.dec)

    ra_hms = deg_to_dms(obj.ra)
    dec_dms = deg_to_dms(obj.dec)

    dt = args.dt or datetime.now(timezone.utc)

    interval = args.interval

    while True:
        observation = observe(observer, obj, dt)

        ha_hms = deg_to_hms(observation.positions[0].ha)
        alt_dms = deg_to_dms(observation.positions[0].alt)
        az_dms = deg_to_dms(observation.positions[0].az)

        print(
            f'ra:\t{ra_hms[0]}h\t{ra_hms[1]}m\t{ra_hms[2]}s\n'
            f'dec:\t{dec_dms[0]}°\t{dec_dms[1]}\'\t{dec_dms[2]}"\n'
            f'lat:\t{observer.lat}\n'
            f'lon:\t{observer.lon}\n'
            f'dt:\t{dt}\n'
            f'jd:\t{observation.context.jd}\n'
            f'gmst:\t{observation.context.gmst}\n'
            f'lst:\t{observation.context.lst}\n'
            f'ha:\t{ha_hms[0]}h\t{ha_hms[1]}m\t{ha_hms[2]}s\n'
            f'alt:\t{alt_dms[0]}°\t{alt_dms[1]}\'\t{alt_dms[2]}"\n'
            f'az:\t{az_dms[0]}°\t{az_dms[1]}\'\t{az_dms[2]}"\n'
        )

        dt += timedelta(seconds=interval)
        time.sleep(interval)


if __name__ == '__main__':
    main()
