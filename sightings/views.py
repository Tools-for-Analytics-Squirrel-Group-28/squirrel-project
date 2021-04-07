from django.shortcuts import render
from .models import Squirrel
from django.shortcuts import get_object_or_404, redirect
from .forms import SquirrelForm


def index(request):
   squirrels= Squirrel.objects.all()
   context = {'squirrels':squirrels,}
   return render(request, 'sightings/index.html', context)

def update(request,Unique_Squirrel_ID):
   squirrel_update=get_object_or_404( Squirrel, Unique_Squirrel_ID=Unique_Squirrel_ID)

   if request.method == 'POST':
       form = SquirrelForm(request.POST, instance=squirrel_update)
       if form.is_valid():
           form.save()
           return redirect("/sightings/")
   else:
       form = SquirrelForm(instance = squirrel_update)

   context = {'form':form,}

   return render(request, 'sightings/update.html', context)

def add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")
    else:
        form = SquirrelForm()

    context={'form':form,}

    return render(request, 'sightings/add.html', context)
# Create your views here.    
