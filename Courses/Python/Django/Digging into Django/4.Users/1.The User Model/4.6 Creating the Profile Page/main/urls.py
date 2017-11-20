from django.conf.urls import url
from django.conf import settings
from django.views import static
from . import views

urlpatterns = [
    # Other views not displayed.
    url(r'^$', views.home, name = 'home'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static.serve,
           {'document_root': settings.MEDIA_ROOT,}),
    ]
