from django.shortcuts import render

# Create your views here.
def index(request):
    template_name = 'main/index.html'
    return render(request,template_name)

def productDetails(request):
    template_name = 'main/product-details.html'
    return render(request,template_name)

def shop(request):
    template_name = 'main/shop.html'
    return render(request,template_name)

def cart(request):
    template_name = 'main/cart.html'
    return render(request,template_name)

def checkout(request):
    template_name = 'main/checkout.html'
    return render(request,template_name)

