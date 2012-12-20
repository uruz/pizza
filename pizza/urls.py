from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from .views import pizza_list, margo, create_order

urlpatterns = patterns('',
    url(r'^$', pizza_list, name='home'),
    url(r'^margo/$', margo),
    url(r'^order/$', create_order, name='Order'),
    # url(r'^pizza/', include('pizza.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
