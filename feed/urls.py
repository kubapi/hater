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
    path("akceptuj/", views.accept_choice, name="accept_choice"),
    path("odrzuc/", views.reject_choice, name="reject_choice"),
    path("tinder-demo/", views.tinder_demo, name="tinder_demo"),
]