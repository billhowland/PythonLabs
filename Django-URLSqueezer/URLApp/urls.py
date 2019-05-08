from django.urls import path
from . import views

urlpatterns = [
    path('<short_url>', views.show_url, name='show_url'),
    path('', views.urls_base, name='urls_base'),


]
