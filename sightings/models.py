from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _
from django.forms import ModelForm


class Squirrel(models.Model):
    Latitude = models.FloatField(
        null=False,
        blank=False
    )

    Longitude = models.FloatField(
        null=False,
        blank=False

    )

    Unique_Squirrel_ID = models.CharField(
        help_text=_('Example:"37F-PM-1014-03"'),
        max_length=200,
        unique=True,
        null=False,
        blank=False,
        validators=[
            RegexValidator(
                regex=r'^\d{1,2}[A-Z]{1}-[A-Z]{2}-\d{4}-\d{2}$',
                message='Please enter in the format of: <Hectare ID>-<AM/PM>-<4-digit Date>-<Hectare Squirrel Number>.',
                code='invalid_ID'
            ),
        ]
    )

    PM = 'PM'
    AM = 'AM'
    SHIFT_CHOICES = [(PM, 'PM'), (AM, 'AM')]
    Shift = models.CharField(
        max_length=15,
        choices=SHIFT_CHOICES,
        null=False,
        blank=False
    )

    Date = models.DateField(
        help_text=_('date when the squirrel is found'),
        null=False,
        blank=False,
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    AGE_CHOICES = [(ADULT, _('Adult')), (JUVENILE, _('Juvenile'))]
    Age = models.CharField(
        max_length=15,
        help_text=_('the age of the squirrel'),
        choices=AGE_CHOICES,
        null=True,
        blank=True
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    COLOR_CHOICES = [(GRAY, _('Gray')), (CINNAMON, _('Cinnamon')), (BLACK, _('Black'))]
    Primary_Fur_Color = models.CharField(
        max_length=200,
        help_text=_('primary fur color'),
        choices=COLOR_CHOICES,
        null=True,
        blank=True
    )

    ABOVE_GROUND = 'Above Ground'
    GROUND_PLANE = 'Ground Plane'
    LOCATION_CHOICES = [(ABOVE_GROUND, _('Above Ground')), (GROUND_PLANE, _('Ground Plane'))]
    Location = models.CharField(
        max_length=15,
        help_text=_('the Location of the squirrel'),
        choices=LOCATION_CHOICES,
        null=True,
        blank=True
    )

    Specific_Location = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    Running = models.BooleanField(
        null=True,
        blank=True
    )

    Chasing = models.BooleanField(
        null=True,
        blank=True
    )

    Climbing = models.BooleanField(
        null=True,
        blank=True
    )
    Eating = models.BooleanField(
        null=True,
        blank=True
    )

    Foraging = models.BooleanField(
        null=True,
        blank=True
    )
    Other_Activities = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    Kuks = models.BooleanField(
        help_text=_('Squirrel was heard kukking.'),
        null=True,
        blank=True
    )

    Quaas = models.BooleanField(
        help_text=_('Squirrel was heard quaaing.'),
        null=True,
        blank=True
    )

    Moans = models.BooleanField(
        help_text=_('Squirrel was heard moaning.'),
        null=True,
        blank=True
    )
    Tail_Flags = models.BooleanField(
        help_text=_('Squirrel was seen flagging its tail.'),
        null=True,
        blank=True
    )
    Tail_Twitches = models.BooleanField(
        help_text=_('Squirrel was seen twitching its tail.'),
        null=True,
        blank=True
    )
    Approaches = models.BooleanField(
        help_text=_('Squirrel was seen approaching human.'),
        null=True,
        blank=True
    )
    Indifferent = models.BooleanField(
        help_text=_('Squirrel was indifferent to human presence.'),
        null=True,
        blank=True
    )
    Runs_From = models.BooleanField(
        help_text=_('Squirrel was seen running from humans, seeing them as a threat.'),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.Unique_Squirrel_ID

