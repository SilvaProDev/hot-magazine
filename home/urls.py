
from django.urls import path, include

from . import views
urlpatterns = [

    path('', views.index, name="home"),
    path('world', views.world, name="world"),
    path('travel', views.travel, name="travel"),
    path('tech', views.tech, name="tech"),
    path('fashion', views.fashion, name="fashion"),
    path('video', views.video, name="video"),
    path('sport', views.sport, name="sport"),
    path('food_healt', views.food_healt, name="food_healt"),
    path('autor_list', views.autor_list, name="autor_list"),
]
