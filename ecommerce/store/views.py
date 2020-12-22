from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
import json
from .models import Product, Customer, Order, OrderItem, View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import time
from django.contrib import messages
from .forms import *
import datetime
# Create your views here.

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request,'store/store.html', context)
    
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        messages.error(request, 'You need to login')
        return redirect('/login')
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        messages.error(request, 'You need to login')
        return redirect('/login')
        
    
    context = {
        'cartItems': cartItems,
        'items': items,
        'order': order,
    }
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('productId:', productId)
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

def view(request, name_id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    product = Product.objects.get(id=name_id)
    views = View.objects.filter(product=product)
    context = {
        'views': views,
        "cartItems": cartItems
    }
    return render(request, 'store/views.html', context)

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(user=user)
            messages.success(request, 'Registration Successful')
            return redirect('/login')
    else:
        form = CreateUserForm()

    return render(request,'store/register.html',{'form': form})

def contact(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    if request.method == 'POST':
        form = Contact(request.POST, files=request.FILES)
        if form.is_valid():
            print('message')
            user = form.save()
            obj = form.instance
            messages.success(request, 'Details Submitted')
            return redirect('/contact-us')
    else:
        form = Contact()
    return render(request, 'store/contact.html', {'form': form, 'cartItems': cartItems})
    

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()
        if order.shipping == True:
            Shipping.objects.get_or_create(
                customer = customer,
                order=order,
                address = data['shipping']['address'],
                zipcode = data['shipping']['zipcode'],
                country = data['shipping']['country'],
                state = data['shipping']['state'],
                )
    else:
        print('user is not logged in')
    print('Data:', request.body)
    return JsonResponse('Payment Complete!', safe=False)
