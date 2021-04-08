from django.urls import path
from . import views
app_name = 'sightings'

urlpatterns=[
        path('sightings/',views.index),
        path('sightings/add/',views.add,name='add'),
        path('map/',views.mapping,name='mapping'),
        path('sightings/<str:Unique_Squirrel_ID>/',views.update,name='update'),
]
