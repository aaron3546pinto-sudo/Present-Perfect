from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import redirect
import json
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from Qpage.models import *
 
def index(request):
    return render(request, 'index.html')

def user_login(request):
    return render(request, 'userlogin.html')

def home(request):
    return render(request, 'home.html')

def admin_login(request):
    return render(request, 'adminlogin.html')

def my_cart(request):
    return render(request, 'mycart.html')

def checkout(request):
    return render(request,'checkout.html')

def user_registration(request):
    return render(request,'userregistration.html')

def categories(request):
    return render(request, 'categories.html')

def categories1(request):
    return render(request, "categories1.html")

# views.py

def add_to_cart(request, product_id):
    product = Item.objects.get(id=product_id)
    user = request.user  # Assuming the user is logged in

    # Get or create a cart for the user
    cart, created = Cart.objects.get_or_create(user=user)

    # Check if the product is already in the cart
    cart_item, item_created = Item.objects.get_or_create(cart=cart, product=product, defaults={'price': product.price, 'quantity': 1})

    if not item_created:
        # If the item already exists in the cart, increase the quantity
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')  # Redirect to the cart page


#  changes made in the views.py file 
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        # Extract username and password from request
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)

        # Check if authentication was successful
        
        if user is not None:
            # Return success response
            return JsonResponse({'status': 'success', 'message': 'User authenticated successfully!'}, status=200)
        else:
            # Return failure response
            return JsonResponse({'status': 'failure', 'message': 'Invalid credentials'}, status=401)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def admin_view(request):
    if request.method == 'POST':
        # Extract username and password from request
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        # Authenticate the user
        admin= authenticate(username=username, password=password)

        # Check if authentication was successful
        
        if Userlog is not None:
            # Return success response
            return JsonResponse({'status': 'success', 'message': 'User authenticated successfully!'}, status=200)
        else:
            # Return failure response
            return JsonResponse({'status': 'failure', 'message': 'Invalid credentials'}, status=401)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)





@csrf_exempt
@login_required  # Ensure the user is authenticated before processing the checkout
def process_checkout(request):
    if request.method == 'POST':
        try:
            # Get the data sent from the frontend (cart, payment method, etc.)
            data = json.loads(request.body)
            cart = data.get('cart', [])
            payment_method = data.get('paymentMethod', '')
            total_amount = data.get('totalAmount', 0)

            # Check if the cart is empty
            if not cart:
                return JsonResponse({'status': 'error', 'message': 'Your cart is empty!'}, status=400)

            # Save the order in the database (only if the user is authenticated)
            if request.user.is_authenticated:
                new_order = Order.objects.create(
                    user=request.user,
                    cart=json.dumps(cart),  # Save the cart as a JSON string
                    total_amount=total_amount,
                    payment_method=payment_method,
                    payment_status='Pending',  # Default payment status
                    created_at=timezone.now(),  # Explicitly set the created_at timestamp (optional)
                )

                # Return a success response with timestamps
                return JsonResponse({
                    'status': 'success',
                    'message': 'Order processed successfully!',
                    'order_id': new_order.id,
                    'created_at': new_order.created_at.strftime('%Y-%m-%d %H:%M:%S'),  # Format the timestamp
                }, status=200)
            else:
                # If user is not authenticated, return an error
                return JsonResponse({'status': 'error', 'message': 'User is not authenticated!'}, status=403)

        except Exception as e:
            # Handle any errors during the process
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    # If the request method is not POST, return an error
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


# views.py

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Disable CSRF for now, but ideally, handle CSRF properly in production
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                return JsonResponse({'status': 'fail', 'message': 'Username already taken'}, status=400)

            # Create the new user
            User.objects.create_user(username=username, email=email, password=password)
            return JsonResponse({'status': 'success', 'message': 'User registered successfully'}, status=200)

        except Exception as e:
            return JsonResponse({'status': 'fail', 'message': str(e)}, status=400)
    else:
        return JsonResponse({'status': 'fail', 'message': 'Invalid request method'}, status=405)


from django.shortcuts import render
from .models import Order
from django.contrib.auth.decorators import login_required

@login_required
def my_orders(request):
    # Query for the logged-in user's orders
    orders = Order.objects.filter(user=request.user).order_by('-timestamp')
    
    # Check if any orders exist
    if not orders.exists():
        return render(request, 'myorder.html', {'orders': None, 'message': 'You have no orders yet.'})
    
    # Render the orders to the template
    return render(request, 'myorder.html', {'orders': orders})

