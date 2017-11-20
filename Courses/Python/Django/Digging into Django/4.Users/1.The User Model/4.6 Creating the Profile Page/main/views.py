from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Location
# ...
from django.contrib.auth.models import User

# Other views not displayed.

def home(request):
    locations = Location.objects.all()
    # ...
    return render(request, 'home.html', {'locations': locations})

def profile(request, username):
    user = User.objects.get(username=username)
    locations = Location.objects.filter(user=user)
    print('locations', locations)
    return render(request, 'profile.html',
                  {'username': username,
                   'locations': locations})
