from django.shortcuts import redirect, render
from my_app.models import *
from my_app.forms import ContactForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def contact_view(request):

    form = ContactForm()
    
    text = Contact.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
           
    context = {

              'form':form,  
              'text':text, 

    }
    
    return render(request,'contact.html',context)


def products_view(request):

    obj = Products.objects.all()
    mycard = request.GET.get('mycard')
    if mycard is not None:
       obj = obj.filter(card_title__icontains = mycard)

    paginator = Paginator(obj, 1)
    page = request.GET.get('page', 1)
    p = paginator.get_page(page)

    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)

    context = {
        'obj':obj,
        'p':p
    }
    return render(request,'products.html',context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("my_app:products")
        
    context = {}

    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("my_app:products")