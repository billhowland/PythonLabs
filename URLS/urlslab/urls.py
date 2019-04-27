from django.urls import path
from . import views

urlpatterns = [
    path('', views.url_shortener, name='url_shortener'),
]
