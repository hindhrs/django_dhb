import json
import random
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from products.models import Product,Category
from django.http import JsonResponse
from .models import Cart,CartItem
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .utils import *
def home(request):
    username = get_user(request).username if get_user(request) else None
    cart=get_user_cart(request)
    cartItems=cart.get_items()
    cartItemsCount=cart.get_items_count()
    cartProductCount=cart.get_products_count()    
    
    products= list(Product.objects.all())
    random.shuffle(products)
    categories=Category.objects.all()
    mustHave=[Product.objects.filter(category=cat.name)[:5]for cat in categories]
    
    context = {
        'products': products,
        'categories':categories,
        'mustHave':mustHave,
        'username':username,
        'cart':cart,
        'cartItems':cartItems,
        'itemsCount':cartItemsCount,
        'productsCount':cartProductCount
    }
    return render(request, 'index.html', context)

def add_to_cart(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        product_id = data.get('productId')
       
        size = data.get('size')
        quantity = data.get('quantity')
        product=Product.objects.get(id=product_id)
        


        cart=None
        cart=Cart.objects.get(user=None)
        currentUser=request.user
        if currentUser and currentUser.is_authenticated:
            cart = Cart.objects.get(user=currentUser)

        
        itemsCount=cart.get_items_count()
        productsCount=cart.get_products_count()
            
        
        
        cart_item = CartItem.objects.filter(cart=cart, product=product, size=size).first()
        if cart_item:
            
            # update quantity
            cart_item.quantity += quantity
            cart_item.save()
            return JsonResponse({
                'message': f'{product.name} size {size} quantity updated in cart',
                'productsCount':productsCount,
                'total_price':cart.total_price(),
                'item': {
                    'id': cart_item.id,
                    'quantity': cart_item.quantity,
                    'total_price': cart_item.total_price()
                },
                'product': {
                    'id': cart_item.product.id,
                    'name': cart_item.product.name,
                    'img_path':cart_item.product.img_path()
                    # Add other fields as needed
                }
            })        
        else:
            # new CartItem
            cart_item = CartItem.objects.create(cart=cart, product=product, size=size, quantity=quantity)
            return JsonResponse({
                'message': f'{product.name} size {size} added to cart successfully',
                'productsCount':productsCount,
                'total_price':cart.total_price(),
                'item': {
                    'id': cart_item.id,
                    'quantity': cart_item.quantity,
                    'size':size,
                    'total_price': cart_item.total_price()
                },
                'product': {
                    'id': cart_item.product.id,
                    'name': cart_item.product.name,
                    'img_path':cart_item.product.img_path()
                    # Add other fields as needed
                }
            })
    return JsonResponse({'error': 'Invalid request method'})
# Create your views here.
def delete_item(request, item_id):
    if request.method == 'POST':
        try:
            item = CartItem.objects.get(id=item_id)
            item.delete()
            total_price=item.cart.total_price()
            productsCount=item.cart.get_products_count()
            return JsonResponse({'success': True,'total_price':total_price,'productsCount':productsCount})
        except CartItem.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Item does not exist'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')  # Redirect to the sign-up page

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('signup')  # Redirect to the sign-up page

        # Check if the email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered')
            return redirect('signup')  # Redirect to the sign-up page

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        Cart.objects.create(user=user)
        # user = authenticate(username=username, password=password)
        # login(request, user)

        
        return redirect('login')  

    return render(request, 'sign_up.html') 
def user_login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if not user:
            messages.error(request, 'username or password incorrect')
            return redirect('login') 
        login(request, user)
        return redirect("home")

    return render(request,'login.html')
def checkout(request):
    cart=get_user_cart(request)
    cartItems=cart.get_items()
    cartItemsCount=cart.get_items_count()
    cartProductCount=cart.get_products_count()
    tax=(cart.total_price()*1)/100
    grandTotal=cart.total_price()+tax
    context={
        'cart':cart,
        'cartItems':cartItems,
        'itemsCount':cartItemsCount,
        'productsCount':cartProductCount,
        'grandTotal':cart,
        'tax':tax,
        'grandTotal':grandTotal
}


    return render(request,"checkout.html",context)


def cart(request):
    cart=get_user_cart(request)
    cartItems=cart.get_items()
    cartItemsCount=cart.get_items_count()
    cartProductCount=cart.get_products_count()
    tax=(cart.total_price()*1)/100
    grandTotal=cart.total_price()+tax

    context={
        'cart':cart,
        'cartItems':cartItems,
        'itemsCount':cartItemsCount,
        'productsCount':cartProductCount,
        'grandTotal':cart,
        'tax':tax,
        'grandTotal':grandTotal
    }
    return render(request,"cart.html",context)