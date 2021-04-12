from django.core.management import BaseCommand
from sightings.models import Squirrel
import csv


class Command(BaseCommand):
    help = 'export squirrel data into csv file'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help="csv file")

    def handle(self, path, **options):
        fields = Squirrel._meta.fields
        with open(path, 'w', newline='') as csv_file:
            writer_ = csv.writer(csv_file)
            for object in Squirrel.objects.all():
                rows = []
                for field in fields:
                    rows.append(getattr(object, field.name))
                writer_.writerow(rows)
