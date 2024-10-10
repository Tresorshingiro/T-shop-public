from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import models


def Home(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'Home.html', context)

def aproduct(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'aproduct.html', {'product': product})
def bproduct(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'bproduct.html',{'product': product})

def cproduct(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'cproduct.html',{'product':product})
def dproduct(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request, 'dproduct.html',{'product':product})
def eproduct(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request, 'eproduct.html',{'product':product})
def fproduct(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request, 'fproduct.html',{'product':product})
def gproduct(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request, 'gproduct.html',{'product':product})
def hproduct(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request, 'hproduct.html',{'product':product})
def iproduct(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request, 'iproduct.html',{'product':product})
def Login(request):
    return render(request, 'login.html')
def shoe1(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request, 'shoe1.html',{'product':product})
def shoe2(request,product_id):
    product=get_object_or_404(Product,pk=product-id)
    return render(request, 'shoe2.html',{'product':product})
def shoe3(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request, 'shoe3.html',{'product':product})
def shoe4(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request, 'shoe4.html',{'product':product})
def shoe5(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request, 'shoe5.html',{'product':product})
def shoe6(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request, 'shoe6.html',{'product':product})
def shoe7(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request, 'shoe7.html',{'product':product})
def shoe8(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request, 'shoe8.html',{'product':product})
def shoe9(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request, 'shoe9.html',{'product':product})
def cart(request, product_id=None):
    if product_id is not None:
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            pass
    else:
        cart_items = CartItem.objects.all()  
        total_price = sum(item.product.price for item in cart_items)
        total_items = cart_items.count()
    
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'total_items': total_items})

def product_list(request):
    products = products.objects.filter(is_available=True)
    return render(request, 'products/product_list.html', {'products': products})
# Create similar functions for other templates...

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to the home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def protected_view(request):
    return render(request, 'protected_template.html')


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user who owns the cart item
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to the product in the cart
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity