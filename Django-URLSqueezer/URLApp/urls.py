from django.urls import path
from . import views

urlpatterns = [
    path('', views.urls_list, name='urls_list'),
    path('', views.show_url, name='show_url'),
    path('', views.url_input, name='url_input'),
]
