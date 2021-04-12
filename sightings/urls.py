from django.urls import path
from . import views
app_name = 'sightings'

urlpatterns=[
        path('sightings/',views.index),
        path('sightings/add/',views.add,name='add'),
        path('sightings/stats/', views.stats, name='stats'),
        path('sightings/<str:Unique_Squirrel_ID>/',views.update,name='update'),
]
