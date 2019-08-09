from django.urls import path

from . import views

urlpatterns = [
    path('', views.allitems, name='allitems'),

]
