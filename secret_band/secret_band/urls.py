from django.conf.urls import include, url
from django.contrib import admin
from secret_band_main import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'secret_band.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index')
]
