import argparse
import time
from datetime import datetime, timezone

from .service import calculate_alt_az


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument('--ra', type=float, required=True)
    parser.add_argument('--dec', type=float, required=True)

    parser.add_argument('--lat', type=float, required=True)
    parser.add_argument('--lon', type=float, required=True)

    parser.add_argument('--interval', type=float, default=1.0)

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    while True:
        dt = datetime.now(timezone.utc)

        alt, az = calculate_alt_az(
            ra_h=args.ra,
            dec_deg=args.dec,
            lat_deg=args.lat,
            lon_deg=args.lon,
            dt=dt,
        )

        print(
            f'alt:\t{alt[0]}°\t{alt[1]}\'\t{alt[2]}"\n'
            f'az:\t{az[0]}°\t{az[1]}\'\t{az[2]}"\n'
        )

        time.sleep(args.interval)


if __name__ == '__main__':
    main()
