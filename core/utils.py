from .models import Cart

def get_user_cart(request):
    user=request.user
    if user.is_authenticated:
        return Cart.objects.get_or_create(user=user)[0] #this is because the this function returns a tuple of two values first is the cart object and second is a boolean
    return Cart.objects.get_or_create(user=None) [0]

def get_user(request):
    return request.user if request.user.is_authenticated else None