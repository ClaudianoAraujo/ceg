from django.urls import path
from .views import create, home, store

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('store/', store, name='store'),
]
