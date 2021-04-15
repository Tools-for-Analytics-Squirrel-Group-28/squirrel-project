from django.urls import path
from . import views
app_name = 'sightings'

urlpatterns=[
        path('sightings/',views.index, name='index'),
        path('sightings/add/',views.add,name='add'),
        path('map/',views.mapping,name='mapping'),
        path('sightings/stats/', views.stats, name='stats'),
        path('', views.home, name='home'),
        path('sightings/<str:Unique_Squirrel_ID>/',views.update,name='update'),
]
