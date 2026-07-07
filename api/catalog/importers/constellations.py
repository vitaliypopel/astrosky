import csv

from django.conf import settings
from django.db import transaction

from catalog.models import Constellation

CONSTELLATIONS_PATH = settings.CONSTELLATIONS_PATH


def import_constellations() -> None:
    constellations = []

    with open(CONSTELLATIONS_PATH, encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            constellations.append(
                Constellation(
                    name=row['name'],
                    code=row['iau'],
                    ra=row['ra'],
                    dec=row['dec'],
                    area=row['area_square_degrees'],
                    area_pct=row['area_sphere_percentage'],
                    season=row['season'],
                    eq=row['zone_equatorial'],
                    ecl=row['zone_ecliptic'],
                    mw=row['zone_milky_way'],
                    quad=row['quadrant'],
                    origin=row['origin_name'],
                )
            )

        with transaction.atomic():
            Constellation.objects.bulk_create(
                constellations,
                batch_size=2000,
                ignore_conflicts=True,
            )
