
from django.urls import path

from . import views
urlpatterns = [

    path('', views.index, name="home"),
    # Inscription
    path('signup', views.signup, name="signup"),
    # Connexion
    path('log_in', views.login_in, name="log_in"),
    # Deconnexion
    path('log-out', views.login_out, name="log-out"),
    # Page de recherche 
    path('search', views.search, name="search"),
    # Page de contact
    path('contact', views.contact_us, name="contact"),

    # Page de contact
    path('my-account', views.my_account, name="my-account"),






    path('world', views.world, name="world"),
    path('travel', views.travel, name="travel"),
    path('tech', views.tech, name="tech"),
    path('fashion', views.fashion, name="fashion"),
    path('video', views.video, name="video"),
    path('sport', views.sport, name="sport"),
    path('food_healt', views.food_healt, name="food_healt"),
    path('autor_list', views.autor_list, name="autor_list"),

    path('single_post', views.single_post, name="single_post"),
    



]
