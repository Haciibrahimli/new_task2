from django.shortcuts import render
from my_app.models import *
from my_app.forms import ContactForm

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



def login_view(request):
    context = {

    }
    return render(request,'login.html',context)

def products_view(request):

    obj = Products.objects.all()
    mycard = request.GET.get('mycard')
    if mycard is not None:
       obj = obj.filter(card_title__icontains = mycard)

    context = {
        'obj':obj
    }
    return render(request,'products.html',context)


