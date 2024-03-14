from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>/', views.product, name='product'),
    path('category/<int:category_id>/',views.category,name='category'),
]