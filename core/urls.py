from . import views
from django.urls import path



urlpatterns=[
    path('',views.home,name="home"),
    path('index/',views.home,name="home"),
    path('singup/',views.signup,name="signup"),
    path('login/',views.user_login,name="login"),
    path('add-to-cart/',views.add_to_cart,name="add-to-cart"),
    path('delete-item/<int:item_id>/', views.delete_item, name='delete-item'),
    path('checkout/',views.checkout,name="checkout"),
    path('cart/',views.cart,name='cart')
    
]