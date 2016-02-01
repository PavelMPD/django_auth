from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^auth$', views.auth_check),
    url(r'^logout$', views.logout),
    url(r'^loggedin$', views.loggedin),
    url(r'^invalid$', views.invalid_login),
    url(r'^add$', views.add),
]
