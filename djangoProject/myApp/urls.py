from django.urls import path
from . import views
urlpatterns = [
    path('abc/', views.view1, name= "asbac" )
]
