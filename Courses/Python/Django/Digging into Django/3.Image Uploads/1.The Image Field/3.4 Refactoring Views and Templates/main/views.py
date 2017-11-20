from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Location
from .forms import LocationForm

def home(request):
    locations = Location.objects.all()
    form = LocationForm()
    return render(request, 'home.html', {'locations': locations, 'form': form})

def detail(request, location_id):
    location = Location.objects.get(id=location_id)
    return render(request, 'detail.html', {'location': location})

def post_location(request):
    form = LocationForm(request.POST, request.FILES)
    if form.is_valid():
        form.save(commit=True)
    return HttpResponseRedirect('/')
