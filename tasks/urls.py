from django.conf.urls import url

from tasks import views

urlpatterns = [
    # shows a list of all the customers
    url(r'^customers/$', views.customerList),

   # shows the tasks associated with an individual customer
    url(r'^customers/(?P<pk>[0-9]+)/$', views.customerDetails),

    #shows a list of all the tasks in the database
    url(r'^tasks/$', views.taskList),

    #shows the details of the individual tasks
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.taskSpecifics),

    #shows the joining record of the peeps
    url(r'^joiningRecord/$', views.joiningList),

    url(r'^customers/(?P<pk>[0-9]+)/lastTask/$', views.customerFinalTask),

]
