from django.conf.urls import url
from django.conf import settings
from django.views import static
from . import views

urlpatterns = [
    # ...
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static.serve,
           {'document_root': settings.MEDIA_ROOT,}),
    ]
