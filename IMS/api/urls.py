from django.urls import path
from . import views



urlpatterns = [
    path('', views.getRoutes),
    path('products/', views.getProducts),
    path('products/<str:pk>/', views.getProduct),
    path('users/', views.getUsers),
    path('users/<str:pk>/', views.getUser),
    path('profiles/', views.getProfiles),
    path('profiles/<str:pk>/', views.getProfile),
    path('purchases/', views.getPurchases),
    path('purchases/<str:pk>/', views.getPurchase),
    
    path('add_products/', views.postProduct),
]