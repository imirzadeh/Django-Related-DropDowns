from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from map import views as mapviews
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path('admin/', admin.site.urls, name="admin"),
    url(r'^index/', mapviews.index),
    url(r'^getdetails/', mapviews.getdetails),
]
