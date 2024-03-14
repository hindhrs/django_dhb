from .models import Product,Category
from django.shortcuts import render
from core.models import Cart,CartItem
from core.utils import *
import random

def product(request,product_id):
    username = request.user.username if request.user.is_authenticated else None
    product= Product.objects.get(id=product_id)
    discount_price=product.price-(20*product.price/100)
    saved=product.price-discount_price
    product_may_like=list(Product.objects.all()[:9])
    random.shuffle(product_may_like)
    context = {
        'product': product,
        'discount_price':discount_price,
        'saved':saved,
        'may_like_lst':product_may_like,
        'username':username
        
    }
    return render(request, 'product.html', context)
def category(request,category_id):
    cart=get_user_cart(request)
    cartItems=cart.get_items()
    cartItemsCount=cart.get_items_count()
    cartProductCount=cart.get_products_count() 
    
    returnedCategory=Category.objects.get(id=category_id)
    products= Product.objects.filter(category=returnedCategory.name)



    context={
        'products':products,
        'category':returnedCategory,
        'cart':cart,
        'cartItems':cartItems,
        'itemsCount':cartItemsCount,
        'productsCount':cartProductCount,
    }
    return render(request,"category.html",context)



    

