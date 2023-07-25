from django.urls import path
from . import views


urlpatterns = [
    path('show_product/<int:pk>', views.show_product, name='show_product'),
]