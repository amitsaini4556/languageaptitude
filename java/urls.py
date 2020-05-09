from django.urls import path
from . import views
urlpatterns = [

    path('javaquiz', views.javaquiz , name='javaquiz'),
 ]
