from django.conf.urls import url

from tasks import views

urlpatterns = [
    url(r'^customers/$', views.customerList),
    url(r'^customers/(?P<pk>[0-9]+)/$', views.customerDetails),
]
