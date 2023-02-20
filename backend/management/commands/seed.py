from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('database', nargs='?', type=str)

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['database'])
        self.stdout.write('done.')


def run_seed(self, database):
    pass
