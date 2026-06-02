from django.core.management.base import BaseCommand

from catalog.services.import_hyg import import_hyg


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        import_hyg()
        self.stdout.write(self.style.SUCCESS('HYG Database successfully imported'))
