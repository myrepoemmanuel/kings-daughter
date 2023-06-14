import email
from email import message
from itertools import product
from unicodedata import name
from django.shortcuts import render
from django.db.models import Q
from .models import *
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth.models import User
from .utils import cookieCart, cartData, productDet, guestOrder
#import requests
#from request.auth import HTTPBasicAuth


# Create your views here.
def index(request):
    
    context = {}
    return render(request, 'store/index.html', context)
    

def about(request):
    
    
    context = { 'title':'about',}
    return render(request, 'store/about.html', context)


def contact(request):
   
    context = {'title':'contactus',}
    return render(request, 'store/contacts.html', context)


def nike(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Featuredproduct.objects.all()
    
    context = {'products':products, 'cartItems':cartItems,'title':'nike',}
    return render(request, 'store/nike.html', context)

def adidas(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Featuredproduct.objects.all()
    
    context = {'products':products, 'cartItems':cartItems,'title':'adidas',}
    return render(request, 'store/adidas.html', context)

def balenciaga(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Featuredproduct.objects.all()
    
    context = {'products':products, 'cartItems':cartItems,'title':'balenciaga',}
    return render(request, 'store/balenciaga.html', context)


def dior(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Featuredproduct.objects.all()
    
    context = {'products':products, 'cartItems':cartItems,'title':'dior',}
    
  
    return render(request, 'store/dior.html', context)



def search(request):

    products = Featuredproduct.objects.all()
    query = request.GET.get("query")
    products_search = ""

    if query:
        products_search = products.filter(Q(name__icontains=query) | Q(description__icontains=query) )

    
    context = {
        'products_search': products_search,
        }
    return render(request, 'store/searches.html', context)

def store(request):
    
    data = cartData(request)
    cartItems = data['cartItems']
        
    products = Featuredproduct.objects.all()
    product_db = productDet(request,products)

    query = request.GET.get("query")

    products_search = ""

    if query:
        products_search = products.filter(Q(name__icontains=query) | Q(description__icontains=query) )

    
    context = {
        'products':products,
        "each_product_db":product_db['each_product_db'],
        'search_db':product_db['search_db'], 
        'cartItems':cartItems,
        'title':'store',
        'products_search': products_search,
        }
    return render(request, 'store/store2.html', context)

def cart(request):
    
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems,'title':'cart',}
    return render(request, 'store/cart.html', context)

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems,'title':'checkout',}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('action:', action)
    print('product:', productId)
    
    
    user = request.user.username
    customer = Customer.objects.get(user=user)
    product = Featuredproduct.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    
    
    return JsonResponse('item added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    
    if request.user.is_authenticated:
        #customer = request.user.customer
        user = request.user.username
        customer = Customer.objects.get(user=user)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        
        
        

    else:
        customer, order = guestOrder(request,data)
        

    total = float(data['shipping']['total'])
    order.transaction_id = transaction_id
    
    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    ShippingAddress.objects.create(
    customer=customer,
    order=order,
    address=data['shipping']['address'],
    phone=data['shipping']['phone'],
    state=data['shipping']['address'],
    zipcode=data['shipping']['postalcode'],
    mpesacode=data['userPayData']['payphone'],
    
    )


    return JsonResponse('payment complete', safe=False)


def processContact(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    

    Contact.objects.create(
    name=data['contactInfo']['name'],
    email=data['contactInfo']['email'],
    message=data['contactInfo']['message'],
    subject=data['contactInfo']['subject'],
    
    )


    return JsonResponse('contact sent', safe=False)




