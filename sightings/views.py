from django.shortcuts import render
from .models import Squirrel
from django.shortcuts import get_object_or_404, redirect
from .forms import SquirrelForm
from django.http import JsonResponse

def home(request):
    return render(request, 'sightings/home.html', {})


def index(request):
    squirrels = Squirrel.objects.all()
    context = {'squirrels': squirrels, }
    return render(request, 'sightings/index.html', context)


def update(request, Unique_Squirrel_ID):
    squirrel_update = get_object_or_404(Squirrel, Unique_Squirrel_ID=Unique_Squirrel_ID)

    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel_update)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")
    else:
        form = SquirrelForm(instance=squirrel_update)

    context = {'form': form, }

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

def mapping(request):
    squirrels = Squirrel.objects.all()[0:100]
    context = {'squirrels':squirrels,}
    return render(request, 'sightings/mapping.html', context)
# Create your views here.   

def stats(request):

    squirrels = Squirrel.objects.all()
    total_count = squirrels.count()
    
    # adult rate
    juvenile_count = squirrels.filter(Age='Juvenile').count()
    adult_count = squirrels.filter(Age='Adult').count()
    if adult_count + juvenile_count !=0:
        adult_rate = adult_count / (adult_count + juvenile_count)
        adult_rate = "{:.2%}".format(adult_rate)
    else:
        adult_rate=0

    # friendliness
    approaches_count = squirrels.filter(Approaches=True).count()
    indifferent_count = squirrels.filter(Indifferent=True).count()
    runs_from_count = squirrels.filter(Runs_From=True).count()
    if approaches_count + indifferent_count + runs_from_count !=0:
        friendliness = approaches_count / (approaches_count + indifferent_count + runs_from_count)
        friendliness = "{:.2%}".format(friendliness)
    else:
        friendliness=0


    # runs from prediction based on tail motions
    predict_runs_from_true = squirrels.filter(Tail_Flags=True, Runs_From=True).count()  # confusing rivals or predators
    predict_runs_from_false = squirrels.filter(Tail_Flags=True, Runs_From=False).count()
    if predict_runs_from_true + predict_runs_from_false !=0:
        predict_runs_from_acc = predict_runs_from_true / (predict_runs_from_true + predict_runs_from_false)
        predict_runs_from_acc = "{:.2%}".format(predict_runs_from_acc)
    else:
        predict_runs_from_acc = 0

    # approaches prediction based on tail motions
    predict_approaches_true = squirrels.filter(Tail_Twitches=True, Approaches=True).count()  # communicate interest, curiosity
    predict_approaches_false = squirrels.filter(Tail_Twitches=True, Approaches=False).count()
    if predict_approaches_true + predict_approaches_false != 0:
        predict_approaches_acc = predict_approaches_true / (predict_approaches_true + predict_approaches_false)
        predict_approaches_acc = "{:.2%}".format(predict_approaches_acc)
    else:
        predict_approaches_acc = 0

    # vocal communication
    kuks_count = squirrels.filter(Kuks=True).count()
    quaas_count = squirrels.filter(Quaas=True).count()
    moans_count = squirrels.filter(Moans=True).count()
    if kuks_count + quaas_count + moans_count != 0:
        kuks_rate = kuks_count / (kuks_count + quaas_count + moans_count)
        kuks_rate = "{:.2%}".format(kuks_rate)
        quaas_rate = quaas_count / (kuks_count + quaas_count + moans_count)
        quaas_rate = "{:.2%}".format(quaas_rate)
        moans_rate = moans_count / (kuks_count + quaas_count + moans_count)
        moans_rate = "{:.2%}".format(moans_rate)
    else:
        kuks_rate = 0
        quaas_rate = 0
        moans_rate = 0

    context = {
        'total_count': total_count,
        'adult_rate': adult_rate,
        'friendliness': friendliness,
        'predict_runs_from_acc': predict_runs_from_acc,
        'predict_approaches_acc': predict_approaches_acc,
        # 'vocal communication': {'Kuks':kuks_rate, 'Quaas':quaas_rate, 'Moans':moans_rate},
        'Kuks': kuks_rate,
        'Quaas': quaas_rate,
        'Moans': moans_rate,
    }

    return render(request, 'sightings/stats.html', context)
