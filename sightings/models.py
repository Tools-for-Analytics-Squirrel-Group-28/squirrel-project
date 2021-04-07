from django.db import models
from django.utils.translation import gettext as _
from django.forms import ModelForm

class Squirrel(models.Model):
    Latitude = models.FloatField(
            null=False,
            blank=False
    )

    Longitude= models.FloatField(
            null=False, 
            blank=False

    )

    Unique_Squirrel_ID = models.CharField(
            max_length=200,
            unique=True,
            null=False, 
            blank=False
    )

   # Hectare = models.CharField(
    #        max_length=200,
     #       unique=True,
      #      null=False,
   # )

    PM= 'PM'
    AM='AM'
    SHIFT_CHOICES=[(PM,'PM'),(AM,'AM')]
    Shift = models.CharField(
            max_length=15,
            choices=SHIFT_CHOICES,
    )

    Date = models.DateField(
            help_text=_('date when the squirre is found'),
    )

    ADULT= 'Adult'
    JUVENILE='Juvenile'
    AGE_CHOICES=[(ADULT,_('Adult')),(JUVENILE,_('Juvenile'))]
    Age = models.CharField(
            max_length=15,
            help_text=_('the age of the squirrel'),
            choices=AGE_CHOICES,
    )

    Primary_Fur_Color = models.CharField(
            max_length=200,
            null=False,
    )


    ABOVE_GROUND= 'Above Ground'
    GROUND_PLANE='Gound Plane'
    LOCATION_CHOICES=[(ABOVE_GROUND,_('Above Ground')),(GROUND_PLANE,_('Ground Plane'))]
    Location = models.CharField(
            max_length=15,
            help_text=_('the Location of the squirrel'),
            choices=LOCATION_CHOICES,
    )

    Specific_Location = models.TextField(
            blank=True,
    )


    Running=models.BooleanField(
            null=True, 
            blank=True
    )

    Chasing=models.BooleanField(
            null=True, 
            blank=True
    )

    Climbing=models.BooleanField(
            null=True, 
            blank=True
    )
    Eating=models.BooleanField(
            null=True, 
            blank=True
    )

    Foraging=models.BooleanField(
            null=True, 
            blank=True
    )
    Other_Activities=models.CharField(
            max_length=200, 
            null=True, 
            blank=True
    )
    Kuks=models.BooleanField(
            null=True, 
            blank=True
    )

    Quaas=models.BooleanField(
            null=True, 
            blank=True
    )

    Moans=models.BooleanField(
            null=True, 
            blank=True
    )
    Tail_Flags=models.BooleanField(
            null=True, 
            blank=True
    )
    Tail_Twitches=models.BooleanField(
            null=True, 
            blank=True
    )
    Approaches=models.BooleanField(
            null=True, 
            blank=True
    )
    Indifferent=models.BooleanField(
            null=True, 
            blank=True
    )
    Runs_From=models.BooleanField(
            null=True, 
            blank=True
    )
    
    def __str__(self):
        return self.Unique_Squirrel_ID

