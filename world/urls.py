from django.conf.urls import patterns, include, url

from django.contrib import admin
from map import views as mapviews
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'world.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^index/', mapviews.index),
                       url(r'^getdetails/', mapviews.getdetails),
                       )
