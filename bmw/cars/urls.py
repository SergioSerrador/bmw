from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.cars, name='cars'),
    path('persons/', views.persons, name='persons'),
    path('products/', views.product_list_view, name='list_products'),
    path('persons/<slug:slug>/', views.person_detail, name='person_detail'),    
]