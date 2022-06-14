from django.urls import path, include
from .views import *
urlpatterns = [
    path('search/', SearchView.as_view(), name='search'),
    path('', HomePageView.as_view(), name='homepage'),
]
