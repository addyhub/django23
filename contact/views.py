from django.core.checks import messages
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
# Create your views here.
def contact(request):
    if request.method == 'POST':
       name = request.POST['name']
       phone = request.POST['phone'] 
       email = request.POST['email'] 
       message = request.POST['message'] 
       
       user = Contact(name=name,phone=phone,email=email,message=message)
       user.save()
       messages.info(request,'Submitted')
       
       return redirect('contact')
    
        
        
    else:
        return render(request,'contact.html')