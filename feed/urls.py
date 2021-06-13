from django.urls import path

from . import views

app_name = 'feed'  

urlpatterns = [
    path('', views.index, name='index'),
    path('kontakt/', views.contact, name='contact'),
    path('o-projekcie/', views.about, name='about'),
    path('ranking/', views.ranking, name='ranking'),
    path('architekt/', views.architect, name='architect'),
    path("rejestracja/", views.register_view, name="register"),
    path("logowanie/", views.login_view, name="login"),
    path("wylogowywanie/", views.logout_view, name="logout"),
    path("aktywuj_karte/", views.activate_card, name="activate_card")
]