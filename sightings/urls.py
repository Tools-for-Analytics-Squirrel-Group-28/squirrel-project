from django.urls import path
from . import views
app_name = 'sightings'

urlpatterns=[
        path('sightings/',views.index),
        path('sightings/add/',views.add,name='add'),
<<<<<<< HEAD
        path('map/',views.mapping,name='mapping'),
=======
        path('sightings/stats/', views.stats, name='stats'),
>>>>>>> 895253159e20cf030ecdfd8673f8c09066299b6e
        path('sightings/<str:Unique_Squirrel_ID>/',views.update,name='update'),
]
