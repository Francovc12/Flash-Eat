from django.urls import path
from .views import DishListCreateView, DishDetailView

urlpatterns = [
    path('dishes/', DishListCreateView.as_view(), name='dish-list-create'),
    path('dishes/<int:pk>/', DishDetailView.as_view(), name='dish-detail'),
]
