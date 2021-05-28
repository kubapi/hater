from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('ranking/', views.ranking, name='ranking'),
    path('architect/', views.architect, name='architect'),
]