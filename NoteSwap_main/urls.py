
from django.urls import path
from . import views  # Import your views here

urlpatterns = [
    path('', views.index, name='index'),  # Example URL pattern
]

