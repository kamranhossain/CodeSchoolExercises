from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# ...
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Other views not displayed.

def search(request):
    return render(request, 'search.html')
