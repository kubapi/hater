from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kontakt/', views.contact, name='contact'),
    path('o-projekcie/', views.about, name='about'),
    path('ranking/', views.ranking, name='ranking'),
    path('architekt/', views.architect, name='architect'),
]