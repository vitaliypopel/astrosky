import csv

from django.conf import settings
from django.db import transaction

from catalog.models import Constellation, Star

STARS_PATH = settings.STARS_PATH


def import_stars() -> None:
    constellations = {}

    stars = []

    with open(STARS_PATH, encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            constellation = constellations.get(row['con'])

            if constellation is None:
                constellation = Constellation.objects.filter(code=row['con']).first()

                if constellation is not None:
                    constellations[row['con']] = constellation

            stars.append(
                Star(
                    constellation=constellation,
                    hip=row['hip'] or None,
                    hd=row['hd'] or None,
                    hr=row['hr'] or None,
                    gl=row['gl'],
                    bf=row['bf'],
                    name=row['proper'],
                    bayer=row['bayer'],
                    flam=row['flam'] or None,
                    ra=row['ra'],
                    dec=row['dec'],
                    dist=row['dist'] or None,
                    mag=row['mag'],
                    absmag=row['absmag'] or None,
                    spect=row['spect'],
                    ci=row['ci'] or None,
                    pmra=row['pmra'] or None,
                    pmdec=row['pmdec'] or None,
                    rv=row['rv'] or None,
                    lum=row['lum'] or None,
                )
            )

    with transaction.atomic():
        Star.objects.bulk_create(
            stars,
            batch_size=2000,
            ignore_conflicts=True,
        )
