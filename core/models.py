from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def get_items(self):
        return CartItem.objects.filter(cart=self)
    

    def get_items_count(self):
        return len(self.get_items())
    

    def get_products_count(self):
        cpt=0
        for cardItem in self.get_items():
            cpt+=cardItem.quantity
        return cpt
    
    def total_price(self):
        sum=0
        items=self.get_items()
        for item in items:
            sum+=item.total_price()
        return sum
    

    def __str__(self):

        username=self.user.username if self.user else 'shared_cart'
        return f'cart for user : {username}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=50, blank=True)
    
    def total_price(self):
        sum=0
        item = CartItem.objects.filter(product=self.product,cart=self.cart,size=self.size).first()
        if item:
            sum+=item.product.price*item.quantity
        return sum
            
        
    def __str__(self):
        return f"{self.quantity} x {self.product.name} ({self.size})"
    
  
# Create your models here.
