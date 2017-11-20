from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Location
# ...
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Other views not displayed.

def detail(request, location_id):
    location = Location.objects.get(id=location_id)
    return render(request, 'detail.html', {'location': location})

def search(request):
    search_val = request.GET.get('search', None)

    if (search_val != None):
        results = []
        locations = Location.objects.filter(name__icontains=search_val)
        for location in locations:
            json = {}
            json['name'] = location.name
            json['link'] =  '/' + str(location.id) + '/'
            results.append(json)
        return JsonResponse({'results':results})
    else:
        return render(request, 'search.html')
