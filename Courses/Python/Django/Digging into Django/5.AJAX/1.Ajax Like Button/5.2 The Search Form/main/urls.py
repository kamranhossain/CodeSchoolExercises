from django.conf.urls import url
from django.conf import settings
from django.views import static
from . import views

urlpatterns = [
    # Other URLs not displayed.

    url(r'^search/$', views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static.serve,
           {'document_root': settings.MEDIA_ROOT,}),
    ]
