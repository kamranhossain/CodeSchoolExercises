from django.conf.urls import url
from django.conf import settings
from django.views import static
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^([0-9]+)/$', views.detail, name = 'detail'),
    url(r'^post_location/$', views.post_location, name = 'post_location'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^register/$', views.register, name='register'),

]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static.serve,
           {'document_root': settings.MEDIA_ROOT,}),
    ]
