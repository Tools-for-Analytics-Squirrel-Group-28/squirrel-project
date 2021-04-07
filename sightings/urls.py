from django.urls import path
from . import views
app_name = 'sightings'

urlpatterns=[
        path('',views.index),
        path('add/',views.add,name='add'),
        path('<str:Unique_Squirrel_ID>/',views.update,name='update'),
]
