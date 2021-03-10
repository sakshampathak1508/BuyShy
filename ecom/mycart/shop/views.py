from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .models import Product,Contact,Order
def index(request):
    product = Product.objects.all()
    params = {'product':product}
    return render(request,"shop/index.html",params)

def about(request):
    return render(request, "shop/about.html")

def tracker(request):
    return render(request, "shop/tracker.html")


def contact(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(c_name=name, c_email=email, c_phone=phone, c_desc=desc)
        contact.save()
        thank = True
        return render(request, "shop/contact.html",{'thank':thank})
    return render(request, "shop/contact.html")

def products(request,myid):
    prodview = Product.objects.filter(id=myid)
    params = {'prodview': prodview[0]}
    return render(request, "shop/products.html",params)

def checkout(request):
    if request.method =="POST":
        items_json = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount',0)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + \
            " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        pin_code = request.POST.get('pin_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, email=email,
                       address=address, city=city, state=state, pin_code=pin_code, phone=phone,amount=amount)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, "shop/checkout.html")


# Create your views here.
