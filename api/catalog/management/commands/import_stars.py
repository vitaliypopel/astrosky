from django.core.management.base import BaseCommand

from catalog.importers import import_stars


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        import_stars()
        self.stdout.write(self.style.SUCCESS('Stars successfully imported'))
