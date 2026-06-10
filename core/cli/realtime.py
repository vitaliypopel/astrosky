import argparse
import time
from datetime import datetime, timezone

from core.engine import calculate_altaz
from core.engine.formatting.sexagesimal import deg_to_dms, deg_to_hms


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

    ra_h = args.ra
    dec_deg = args.dec
    lat_deg = args.lat
    lon_deg = args.lon

    ra_hms = deg_to_dms(ra_h)
    dec_dms = deg_to_dms(dec_deg)

    while True:
        dt = datetime.now(timezone.utc)

        result = calculate_altaz(
            ra_h,
            dec_deg,
            lat_deg,
            lon_deg,
            dt,
        )

        ha_hms = deg_to_hms(result['ha'])
        alt_dms = deg_to_dms(result['alt'])
        az_dms = deg_to_dms(result['az'])

        print(
            f'ra:\t{ra_hms[0]}h\t{ra_hms[1]}m\t{ra_hms[2]}s\n'
            f'dec:\t{dec_dms[0]}°\t{dec_dms[1]}\'\t{dec_dms[2]}"\n'
            f'lat:\t{lat_deg}\n'
            f'lon:\t{lon_deg}\n'
            f'dt:\t{dt}\n'
            f'jd:\t{result["jd"]}\n'
            f'gmst:\t{result["gmst"]}\n'
            f'lst:\t{result["lst"]}\n'
            f'ha:\t{ha_hms[0]}h\t{ha_hms[1]}m\t{ha_hms[2]}s\n'
            f'alt:\t{alt_dms[0]}°\t{alt_dms[1]}\'\t{alt_dms[2]}"\n'
            f'az:\t{az_dms[0]}°\t{az_dms[1]}\'\t{az_dms[2]}"\n'
        )

        time.sleep(args.interval)


if __name__ == '__main__':
    main()
