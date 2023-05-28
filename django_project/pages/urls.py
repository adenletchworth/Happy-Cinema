from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    # Add more URL patterns for the pages app here
]