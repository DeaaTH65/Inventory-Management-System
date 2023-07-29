from django.urls import path
from . import views



urlpatterns = [
    path('', views.getRoutes),
    path('products/', views.getProducts),
    path('products/<str:pk>/', views.getProduct),
    path('profiles/', views.getProfiles),
    path('profiles/<str:pk>/', views.getProfile),
    path('purchases/', views.getPurchases),
    path('purchases/<str:pk>/', views.getPurchase),
]