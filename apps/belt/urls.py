from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^login$',views.login),
    url(r'^create$',views.create),
    url(r'^logout$',views.logout),
    url(r'^create_quote$',views.create_quote),
    url(r'^user/(?P<number>\d+)$',views.user),
    url(r'^add/(?P<number>\d+)$',views.add),
    url(r'^remove/(?P<number>\d+)$',views.remove),









]
