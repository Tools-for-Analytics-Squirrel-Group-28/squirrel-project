from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import pandas as pd

class Command(BaseCommand):
    help = 'import squirrel data from csv file'
    def add_arguments(self, parser):
        parser.add_argument('path',type=str,help="csv file")
    def handle(self, path,**options):
        data1 = pd.read_csv(path)  
        data = data1.drop_duplicates(subset='Unique Squirrel ID', keep='last', inplace=False)        
        for i in range(len(data)):
            date = str(data.iloc[i]['Date'])
            _, created = Squirrel.objects.get_or_create(
                Latitude = data.iloc[i]['Y'],
                Longitude= data.iloc[i]['X'],
                Unique_Squirrel_ID = data.iloc[i]['Unique Squirrel ID'],
                Shift = data.iloc[i]['Shift'],
                Date = date[4:8]+'-'+ date[0:2]+'-'+ date[2:4],
                Age = data.iloc[i]['Age'],
                Primary_Fur_Color=data.iloc[i]['Primary Fur Color'],
                Location = data.iloc[i]['Location'],
                Specific_Location = data.iloc[i]['Specific Location'],
                Running = True if data.iloc[i]['Running']=='TRUE' else False,
                Chasing = True if data.iloc[i]['Chasing']=='TRUE' else False,
                Climbing = True if data.iloc[i]['Climbing']=='TRUE' else False,
                Eating = True if data.iloc[i]['Eating']=='TRUE' else False,
                Foraging = True if data.iloc[i]['Foraging']=='TRUE' else False,
                Other_Activities = data.iloc[i]['Other Activities'],
                Kuks = True if data.iloc[i]['Kuks']=='TRUE' else False,
                Quaas = True if data.iloc[i]['Quaas']=='TRUE' else False,
                Moans = True if data.iloc[i]['Moans']=='TRUE' else False,
                Tail_Flags = True if data.iloc[i]['Tail flags']=='TRUE' else False,
                Tail_Twitches = True if data.iloc[i]['Tail twitches']=='TRUE' else False,
                Approaches = True if data.iloc[i]['Approaches']=='TRUE' else False,
                Indifferent = True if data.iloc[i]['Indifferent']=='TRUE' else False,
                Runs_From = True if data.iloc[i]['Runs from']=='TRUE' else False,)
