from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('persons/', views.persons, name='persons'),
    path('persons/<slug:slug>/', views.person_detail, name='person_detail'),
]