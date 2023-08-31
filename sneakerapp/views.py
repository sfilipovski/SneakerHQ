from django.shortcuts import render, redirect
from .forms import SneakerForm
from .models import Sneaker
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
import random

# Create your views here.


def index(request):
    sneakers = Sneaker.objects.all()
    context = {'sneakers': sneakers}
    return render(request, 'sneakerapp/index.html', context=context)


def details(request, sneaker_id):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['price'] = request.POST['price']
        request.session['color'] = request.POST['color']
        request.session['size'] = request.POST['size']
        return redirect('order')
    sneaker = Sneaker.objects.get(pk=sneaker_id)
    sizes = sneaker.size.split(',')
    in_stock = random.randint(1, 50)
    context = {'sneaker': sneaker, 'sizes': sizes, 'in_stock': in_stock}
    return render(request, 'sneakerapp/details.html', context)


def add(request):
    form = SneakerForm()
    context = {'form': form}
    return render(request, 'sneakerapp/add.html', context)


def order(request):
    if request.method == 'POST':
        quantity_int = request.POST['quantity']
        quantity = int(quantity_int)
        request.session['quantity'] = quantity
        return redirect('order_placed')
    name = request.session.get('name')
    price = request.session.get('price')
    color = request.session.get('color')
    size = request.session.get('size')
    context = {'name': name, 'price': price, 'color': color, 'size': size}
    return render(request, 'sneakerapp/order.html', context)


def order_placed(request):
    price = request.session['price']
    price = int(price)
    quantity = request.session['quantity']
    total = price * quantity
    context = {'total': total}
    return render(request, 'sneakerapp/order_placed.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    return render(request, 'sneakerapp/login.html')


def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'sneakerapp/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
