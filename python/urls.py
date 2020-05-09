from django.urls import path
from . import views
urlpatterns = [

    path('pythonquiz', views.pythonquiz , name='pythonquiz'),
 ]
