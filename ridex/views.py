from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from ridex.models import Payment
from datetime import datetime
from ridex.models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username = username, password = pass1)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Wrong Credentials entered")
    return render(request, 'register.html')
    # return HttpResponse("Home")

def signin(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2 :
            messages.error(request, "Passwords entered are not same!!")
        elif password1 == password2 :
            my_user = User.objects.create_user(uname,email,password1)
            my_user.save()
            return redirect("register")
    return render(request, 'signin.html')
    # return HttpResponse("Home")

def LogoutPage(request):
    logout(request)
    return redirect('register')

# def info(request):
#     if request.method == "POST":
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')
#         number = request.POST.get('number')
#         address = request.POST.get('address')
#         info = Info(fname = fname, lname = lname, number = number, address = address, date = datetime.today())
#         info.save()
#     return render(request, 'info.html')

def payment(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        name = request.POST.get('name')
        ccnumber = request.POST.get('ccnumber')
        expirymonth = request.POST.get('expirymonth')
        expiryyear = request.POST.get('expiryyear')
        cvv = request.POST.get('cvv')
        payment = Payment(fullname = fullname, email = email, address = address, city = city, state = state, zipcode = zipcode, name = name, ccnumber = ccnumber,
                          expirymonth = expirymonth, expiryyear = expiryyear, cvv = cvv)
        payment.save()
    return render(request, 'payment.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mail = request.POST.get('mail')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(fname = fname, lname = lname, mail = mail, phone = phone, message = message)
        contact.save()
    return render(request, 'contact.html')