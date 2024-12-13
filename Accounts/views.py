from django.shortcuts import render, redirect
from Accounts.models import Cust_register,Profile_Pic
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password,check_password




# Create your views here.

def register_view(request):
    if request.method=="POST":
        name=request.POST['name']
        contact_number = request.POST['contact_number']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        pin_code = request.POST['pin_code']
        address = request.POST['address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if confirm_password == password:
            if Cust_register.objects.filter(email=email).exists():
                messages.info(request,'Email exists')
                return redirect('/Accounts/register/')
            elif Cust_register.objects.filter(contact_number=contact_number).exists():
                messages.info(request,'Number already Exists')
                return redirect('/Accounts/')
            else:
                password = make_password(password)
                customer = Cust_register.objects.create(name=name,email=email,state=state,city=city,address=address,contact_number=contact_number,pin_code=pin_code, password=password)
                customer.save()
                return redirect('/Accounts/login/')
        else:
            messages.info(request,'Password and confirm password does not match')
            return redirect('/Accounts/')
    return render(request, 'register.html', {'register':register_view})



def login_view(request):
    if request.method=="POST":
        mobile = request.POST['mobile']
        password = request.POST['password']
        
        try:
            customer = Cust_register.objects.get(contact_number=mobile)

            if customer.contact_number == int(mobile) and check_password(password,customer.password): # to unhash and check the password properly in the hashed
                request.session['id']=customer.id
                return redirect('/profile/')
            else:
                messages.info(request,'Invalid Credentials')
                return redirect('/Accounts/login')
            
        except ObjectDoesNotExist:
            messages.info(request,'Mobile does not exists')
            return redirect('/Accounts/login/')
        
    return render(request, 'login.html')



def logout_view(request):
    request.session.flush()
    return redirect('/Accounts/login/')


def remove_cart(request):
    cart = Cust_register.objects.get(id=id)
    cart.delete()
    return redirect('/mycart/')


def profile_pic(request,id):
    if request.method=="POST":
        profile_picture = request.FILES["profile_pic"]
        user_id = request.session.get('id')
        user = Cust_register.objects.get(id=user_id)

        try:
            user = Cust_register.objects.get(id=user_id)
            profile_pics, created = Profile_Pic.objects.get_or_create(user=user)
            profile_pics.image = profile_picture
            profile_pics.save()
            
        except Cust_register.DoesNotExist:
            return redirect('/profile/')
    return redirect('/profile/')


def delete_profile(request,id):
    image = Profile_Pic.objects.get(id=id)
    image.delete()
    return redirect('/profile/')


