from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Cart(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='gift_items')

    def __str__(self):
        return self.name
print(Cart.objects.all())

class CartUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Userlog(models.Model):
    username=models.CharField(max_length=10)    
    password=models.CharField(max_length=15)

class Adminlog(models.Model) :  
    username=models.CharField(max_length=10)    
    password=models.CharField(max_length=15)

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='gift_items')
    category=models.CharField(max_length=255)

    def _str_(self):
        return self.name

class Order(models.Model):
    # Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User who made the order
    cart = models.JSONField()  # Store the cart items as a JSON object
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total price of the order
    payment_method = models.CharField(max_length=100)  # e.g., 'Credit Card', 'PayPal', etc.
    payment_status = models.CharField(max_length=50, default='Pending')  # e.g., 'Pending', 'Paid', 'Failed'
    timestamp = models.DateTimeField(default=timezone.now)  # Date and time the order was placed
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

    class Meta:
        ordering = ['-timestamp']  # Order by most recent by default
