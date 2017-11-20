from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Location
from .forms import LocationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse

def home(request):
    locations = Location.objects.all()
    form = LocationForm()
    return render(request, 'home.html', {'locations': locations, 'form':form})

def detail(request, location_id):
    location = Location.objects.get(id=location_id)
    return render(request, 'detail.html', {'location': location})

def post_location(request):
    form = LocationForm(request.POST, request.FILES)
    if form.is_valid():
        location = form.save(commit=False)
        location.user = request.user
        location.save()
    return HttpResponseRedirect('/')

def profile(request, username):
    user = User.objects.get(username=username)
    locations = Location.objects.filter(user=user)
    print('locations', locations)
    return render(request, 'profile.html',
                  {'username': username,
                   'locations': locations})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                # the password verified for the user
                if user.is_active:
                    print("User is valid, active and authenticated")
                    login(request, user)
                    return HttpResponseRedirect('/')
                    #return Index(request)
                else:
                    print("The password is valid, but the account has been disabled!")
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def search(request):
    search_val = request.GET.get('search', None)

    if (search_val != None):
        results = []
        locations = Location.objects.filter(name__icontains=search_val)
        for location in locations:
            json = {}
            json['name'] = location.name
            results.append(json)
        return JsonResponse({'results':results})
    else:
        return render(request, 'search.html')
