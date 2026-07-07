from django.core.management.base import BaseCommand

from catalog.importers import import_constellations


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        import_constellations()
        self.stdout.write(self.style.SUCCESS('Constellations successfully imported'))
