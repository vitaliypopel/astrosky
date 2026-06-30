import csv

from django.conf import settings
from django.db import transaction

from catalog.models import Catalog, Constellation, Star

HYG_PATH = settings.HYG_PATH


def import_hyg() -> None:
    catalog, _ = Catalog.objects.get_or_create(
        code='hyg',
        defaults={
            'name': 'HYG Database',
            'description': 'HYG Database (v4.2) is subset of the star data in three major catalogs: '
            'the Hipparcos Catalog, the Yale Bright Start Catalog (5th Edition) '
            'and the Gliese Catalog of Nearbly Stars (3rd Edition).',
        },
    )

    constellations = {}

    stars = []

    with open(HYG_PATH, encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            constellation = constellations.get(row['con'])

            if constellation is None:
                constellation = Constellation.objects.filter(code=row['con']).first()

                if constellation is not None:
                    constellations[row['con']] = constellation

            stars.append(
                Star(
                    catalog=catalog,
                    source_id=int(row['id']),
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
