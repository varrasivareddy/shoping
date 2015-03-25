from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    return render_to_response("index.html")

def login(request):
    return render_to_response("login.html")

def checkout(request):
    return render_to_response("checkout.html")


def cart(request):
    return render_to_response("cart.html")


def shop(request):
    return render_to_response("shop.html")


def contact(request):
    return render_to_response("contact-us.html")


def product(request):
    return render_to_response("product-details.html")
