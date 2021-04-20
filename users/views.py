from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserForm, AddressForm
from .models import *


# Create your views here.
def home(request):
    return render(request, "users/home.html")

def register(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
	form = UserForm
	return render (request, "users/register.html", {"register_form":form})

def login_req(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/users/shop/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, "users/login.html", context={"login_form":form})

def shop(request):
    products = Product.objects.all()
    return render(request, 'users/shop.html', {'products':products})

def cart(request):
    try:
        order = Order.objects.get(user=request.user, ordered=False)
        items= order.orderedproducts_set.all()
    except:
        order = []
        items = []
   
    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'users/cart.html', context)
    
def checkout(request):
    if request.method =="POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            street_address = form.cleaned_data.get('street_address')
            apartment_address = form.cleaned_data.get('apartment_address')
            country = form.cleaned_data.get('country')
            zip = form.cleaned_data.get('zip')
            address = Address(
                    user=request.user,
                    street_address=street_address,
                    apartment_address=apartment_address,
                    country=country,
                    zip=zip
                )
            address.save()
        order = Order.objects.get(user=request.user, ordered=False)
        order.ordered = True
        order.save()
        return redirect("order_review")
    else:    

        order = Order.objects.get(user=request.user, ordered=False)
        items= order.orderedproducts_set.all()
        form = AddressForm()
        context = {
            'items': items,
            'order': order,
            'form':form
        }
        return render(request, 'users/checkout.html', context)

def logout_req(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/users/shop")

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, ordered=False)
    ordered_product, created = OrderedProducts.objects.get_or_create(
        order=order,
        product=product
    )
    ordered_product.quantity = (ordered_product.quantity +1)
    ordered_product.save()
    return redirect("/users/shop/")
         
def order_review(request):
    items_list = []
    orders = Order.objects.filter(user=request.user, ordered=True)
    for order in orders:
        items= order.orderedproducts_set.all()
        items_list.append(items)
    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'users/order_review.html', context)