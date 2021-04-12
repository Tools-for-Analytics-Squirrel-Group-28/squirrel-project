from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import pandas as pd


class Command(BaseCommand):
    help = 'import squirrel data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help="csv file")

    def handle(self, path, **options):
        data1 = pd.read_csv(path)
        data = data1.drop_duplicates(subset='Unique Squirrel ID', keep='last', inplace=False)
        for i in range(len(data)):
            date = str(data.iloc[i]['Date'])
            _, created = Squirrel.objects.get_or_create(
                Latitude=data.iloc[i]['X'],
                Longitude=data.iloc[i]['Y'],
                Unique_Squirrel_ID=data.iloc[i]['Unique Squirrel ID'],
                Shift=data.iloc[i]['Shift'],
                Date=date[4:8] + '-' + date[0:2] + '-' + date[2:4],
                Age=data.iloc[i]['Age'],
                Primary_Fur_Color=data.iloc[i]['Primary Fur Color'],
                Location=data.iloc[i]['Location'],
                Specific_Location=data.iloc[i]['Specific Location'],
                Running=True if str(data.iloc[i]['Running']).lower() == 'true' else False,
                Chasing=True if str(data.iloc[i]['Chasing']).lower() == 'true' else False,
                Climbing=True if str(data.iloc[i]['Climbing']).lower() == 'true' else False,
                Eating=True if str(data.iloc[i]['Eating']).lower() == 'true' else False,
                Foraging=True if str(data.iloc[i]['Foraging']).lower() == 'true' else False,
                Other_Activities=data.iloc[i]['Other Activities'],
                Kuks=True if str(data.iloc[i]['Kuks']).lower() == 'true' else False,
                Quaas=True if str(data.iloc[i]['Quaas']).lower() == 'true' else False,
                Moans=True if str(data.iloc[i]['Moans']).lower() == 'true' else False,
                Tail_Flags=True if str(data.iloc[i]['Tail flags']).lower() == 'true' else False,
                Tail_Twitches=True if str(data.iloc[i]['Tail twitches']).lower() == 'true' else False,
                Approaches=True if str(data.iloc[i]['Approaches']).lower() == 'true' else False,
                Indifferent=True if str(data.iloc[i]['Indifferent']).lower() == 'true' else False,
                Runs_From=True if str(data.iloc[i]['Runs from']).lower() == 'true' else False, )

