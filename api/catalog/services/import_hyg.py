import csv

from django.conf import settings
from django.db import transaction

from catalog.models import Catalog, Star

HYG_PATH = settings.HYG_PATH


def import_hyg() -> None:
    catalog, _ = Catalog.objects.get_or_create(
        code='hyg',
        defaults={
            'name': 'HYG Database',
            'description': 'HYG Database (v4.2) is subset of the star data in three major catalogs: the Hipparcos Catalog, the Yale Bright Start Catalog (5th Edition) and the Gliese Catalog of Nearbly Stars (3rd Edition).',
        },
    )

    stars = []

    with open(HYG_PATH, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            stars.append(
                Star(
                    catalog=catalog,
                    source_id=int(row['id']),
                    hip=row.get('hip') or None,
                    hd=row.get('hd') or None,
                    hr=row.get('hr') or None,
                    gl=row.get('gl') or '',
                    bf=row.get('bf') or '',
                    name=row.get('proper') or '',
                    bayer=row.get('bayer') or '',
                    flam=row.get('flaw') or None,
                    con=row.get('con') or '',
                    ra=row['ra'],
                    dec=row['dec'],
                    dist=row.get('dist') or None,
                    mag=row['mag'],
                    absmag=row.get('absmag') or None,
                    spect=row.get('spect') or '',
                    ci=row.get('ci') or None,
                    pmra=row.get('pmra') or None,
                    pmdec=row.get('pmdec') or None,
                    rv=row.get('rv') or None,
                    lum=row.get('lum') or None,
                )
            )

    with transaction.atomic():
        Star.objects.bulk_create(
            stars,
            batch_size=2000,
            ignore_conflicts=True,
        )
