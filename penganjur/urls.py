from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home_penganjur'),  #akan pegi pada site home penganjur
    
]