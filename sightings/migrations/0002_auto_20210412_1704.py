# Generated by Django 3.1.7 on 2021-04-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Age',
            field=models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('Unknown', 'Unknown')], help_text='the age of the squirrel', max_length=15),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Specific_Location',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
