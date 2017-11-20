from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Location
from .forms import LocationForm

def home(request):
    locations = Location.objects.all()
    return render(request, 'home.html', {'locations': locations})

def detail(request, location_id):
    location = Location.objects.get(id=location_id)
    return render(request, 'detail.html', {'location': location})

def post_location(request):
    form = LocationForm(request.POST)
    if form.is_valid():
        location = Location(name = form.cleaned_data['name'],
                            num_restaurants = form.cleaned_data['num_restaurants'],
                            predators = form.cleaned_data['predators'],
                            img_url = form.cleaned_data['img_url'])
        location.save()
    
    return HttpResponseRedirect('/')
