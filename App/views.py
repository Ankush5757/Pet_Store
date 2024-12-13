from django.shortcuts import render,redirect
from App.models import Pets, Cart, Payments , Delivery_details
from django.core.exceptions import ObjectDoesNotExist
from Accounts.models import Cust_register, Profile_Pic
from django.db.models import Q
import razorpay
import random

# Create your views here.

def index(request):
    return render(request, 'index.html')

def savetocart(request,id):
    user_id = request.session.get('id')
    user = Cust_register.objects.get(id=user_id)
    pet = Pets.objects.get(id=id)
    try:
        cart_check = Cart.objects.get(user=user,pet=pet)
        return redirect('/mycart/')
    except ObjectDoesNotExist:
        cart = Cart.objects.create(user=user,pet=pet)
        cart.save()
    return redirect('/mycart/')


def mycart(request):
    user_id = request.session.get('id')
    user = Cust_register.objects.get(id=user_id)
    carts = Cart.objects.filter(user=user)
    grand_total = sum(item.quantity * item.pet.price for item in carts)
    return render(request, 'mycart.html',{"carts":carts, "grand_total":grand_total})


def checkout(request):
    return render(request, 'checkout.html')

def orders(request):
    user_id = request.session.get('id')
    user = Cust_register.objects.get(id=user_id)
    orders = Delivery_details.objects.filter(user=user)
    return render(request, 'orders.html', {'orders':orders})

def pets(request):
    pets = Pets.objects.all().order_by('id')
    if request.method == "POST":
        max_price = request.POST['max_price']
        min_price = request.POST['min_price']
        max_age = request.POST['max_age']
        min_age = request.POST['min_age']
        breed = request.POST['breed']
        gender = request.POST['gender']
        name = request.POST['name']
        
        if name:
            pets = Pets.objects.filter(name=name)
        if min_price:
            pets = Pets.objects.filter(price__gte=min_price)
        if max_price:
            pets = Pets.objects.filter(price__lte=max_price)
        if breed:
            pets = Pets.objects.filter(breed=breed)
        if min_age:
            pets = Pets.objects.filter(age__gte=min_age)
        if max_age:
            pets = Pets.objects.filter(age__lte=max_age)
        if gender:
            pets = Pets.objects.filter(gender=gender)

        return render(request,'pets.html',{'pets':pets})
    return render(request, 'pets.html',{'pets':pets})



def profile(request):  
    user = request.session.get('id')  
    reads = Cust_register.objects.get(id=user)  
    
    try:  
        profile_pic = Profile_Pic.objects.get(user=reads)  
    except Profile_Pic.DoesNotExist:  
        profile_pic = None  # Set to None if no profile_pic exists  
    
    return render(request, 'profile.html', {'user': user, 'profile_pic': profile_pic, 'reads': reads})



def wishlist(request):
    return render(request, 'wishlist.html')


def remove_pet(request,id):
    delete_pet = Cart.objects.get(id=id)
    delete_pet.delete()
    return redirect('/mycart/')

def search(request):
    if request.method == "POST":
        search = request.POST['search']
        pets = Pets.objects.filter(Q(name__icontains=search) | Q(breed__icontains=search) | Q(gender__icontains=search) | Q(age__icontains=search)
    ) if search else []
        return render(request,'pets.html',{'pets':pets})
    
def update_quantity(request,id,action):
    cart_item = Cart.objects.get(id=id)

    if action == "plus":
        cart_item.quantity += 1
        cart_item.total_price = cart_item.pet.price * cart_item.quantity
    elif action == "minus" and cart_item.quantity > 0:
        cart_item.quantity -= 1
        cart_item.total_price = cart_item.pet.price * cart_item.quantity
    cart_item.save()
    user_id = request.session.get('id')
    user = Cust_register.objects.get(id=user_id)
    all_cart_of_a_user = Cart.objects.filter(user=user)
    for all_cart_of_a_user in all_cart_of_a_user:
        all_cart_of_a_user.grand_total += all_cart_of_a_user.total_price
    all_cart_of_a_user.save()
    return redirect('/mycart/')


def buyapet(request,id):
    pet = Cart.objects.get(id=id)

    return render(request,'checkout.html',{'pet':pet})


def buyallpets(request):
    user_id = request.session.get('id')
    user = Cust_register.objects.get(id=user_id)
    pets = Cart.objects.filter(user=user)
    grand_total = sum(item.quantity * item.pet.price for item in pets)
    return render(request,'checkouts.html',{'pets':pets,'grand_total':grand_total})

def payment(request,amount):
    client=razorpay.Client(auth=('rzp_test_FEPt1zurcD7mlA','ieJwbe6ly4aZ3O5n17tmc6Tz'))
    response_payment=client.order.create(dict(amount=int(amount)*100,currency="INR"))
    print('response_payment',response_payment)
    return redirect('/orders/')


def success(request,amount,id,payment_id,address,session):
    user=Cust_register.objects.get(id=session)
    pet=Cart.objects.get(id=id)
    subs=Payments.objects.create(user=user,amount=amount,pet=pet,payment_id=payment_id)
    subs.save()
    user_token = random.randint(1,1000)
    delivery_token = random.randint(1,1000)
    delivery_details = Delivery_details.objects.create(user=user,pet=pet,amount=amount,user_token=user_token,delivery_token=delivery_token,address=address,delivery_status='delivered')
    delivery_details.save()
    return redirect(f'/payment/{amount}/')



def expensive_pets(request):
    pets = Pets.objects.filter(price__gt=5000)
    return render(request, 'expensive_pets.html', {'pets': pets})

def home(request):
    all_pets = Pets.objects.all()  # Fetch all pets for the homepage
    expensive_pets = Pets.objects.filter(price__gt=5000)  # Fetch expensive pets
    return render(request, 'home.html', {'all_pets': all_pets, 'expensive_pets': expensive_pets})


    