from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns('',
    url(r'^index.html$', 'shop.views.home'),
    url(r'^shop.html$', 'shop.views.shop'),
    url(r'^contact-us.html$', 'shop.views.contact'),
    url(r'^checkout.html$', 'shop.views.checkout'),
    url(r'^login.html$', 'shop.views.login'),
    url(r'^cart.html$', 'shop.views.cart'),
    url(r'^product-details.html$', 'shop.views.product'),
    
    

)
urlpatterns += staticfiles_urlpatterns()