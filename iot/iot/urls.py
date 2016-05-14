from django.conf.urls import url
from django.contrib import admin
from power import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^/power/$', views.power_main, name='power'),
    url(r'^/power/(?P<device_id>\d+)/enabler/$', views.enabler, name='enabler')
]
