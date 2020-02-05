from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def signup(request):
    if request.user.is_active == True and request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        print(request.POST)
        username  = request.POST['username']
        password  = request.POST['password']
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        aadhar = request.POST["aadhar"]
        user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name)
        user.set_password(password)
        user.save()
        user = authenticate(username = username, password = password)
        login(request, user)
        if request.POST["iswhat"] == "voter":
            profile = Userprofile()
            profile.user = user 
            profile.aadhar_number = aadhar
            profile.save()
            return redirect('/dashboard')
        else :
            return redirect('/auth/profile/')
        return redirect('/')
    return render(request, 'authentication/signup.djt', None)

def signin(request):
    if request.user.is_authenticated and request.user.is_active == True :
        return redirect('/dashboard')
    if request.method == 'POST':
        user_name = request.POST['username']
        try:
            user = User._default_manager.get(username__iexact = user_name.lower())
            username = user.username
        except:
            try:
                user = User.objects.filter(email = user_name).last()
                username = user.username
            except:
                return render(request, 'authentication/signin.djt', {'error' : 'User-Name/Password Invalid'})
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user == None :
            return render(request, 'authentication/signin.djt', {'error' : 'User-Name/Password Invalid'})
        elif user.is_active == False :
            login(request, user)
            return redirect('/dashboard')
        else : 
            login(request, user)
            return redirect('/dashboard')
    return render(request, 'authentication/signin.djt', None)

def signout(request):
    logout(request)
    return redirect('/dashboard')

def party_register(request):
    if request.method == "POST":
        profile = CandidateProfile()
        pname = request.POST["pname"]
        pshort = request.POST["pshort"]
        if request.FILES.get('symbol') :
            profile.party_symbol = request.FILES.get('symbol')
        profile.party_name = pname
        profile.party_short = pshort
        profile.user = request.user
        profile.save()
        return redirect('/candidatepanel')
    return render(request, 'authentication/profile.djt')
        

