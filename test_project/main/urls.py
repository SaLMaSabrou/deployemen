from django.urls import path

from . import views

urlpatterns =[
    path("main/",views.index,name="index"),
    path("",views.view1,name="view1"),
]