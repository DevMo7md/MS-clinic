from django.shortcuts import render, get_list_or_404, redirect
from .models import Clinec_site, Clinic_about_us, Contact
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def register(request):
    form = CreateUserForm() # Initialize an empty registration form
    if request.method == "POST": 
        form = CreateUserForm(request.POST) # Get the data from the submitted registration form
        if form.is_valid():
            form.save() # Save the new user to the database
            return redirect("login") # Redirect the user to the login page after successful registration
        else:
            messages.error(request, "Registration form is not valid. Please try again and verify your infornations ")

    context = {
        'registerform': form, # Pass the registration form to the template context
    }

    return render(request, 'register.html', context=context)

def login(request):

    form = LoginForm() # Initialize an empty login form
    if request.method == 'POST':

        form = LoginForm(request, data=request.POST) # Get the data from the submitted login form

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password) # Authenticate the user
            if user is not None:
                auth.login(request, user) # Log the user in
                messages.success(request, "User logged in successfully!")
                return redirect("connect") # Redirect the user to the home page after successful login
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()                
            

    context = {
        'loginForm': form, # Pass the login form to the template context
    }

    return render(request, 'login.html' , context=context)  




def main_page(request):
    cardInfo = Clinec_site.objects.all()
    cards_list = []
    for i in cardInfo:
        cards_list.append({"i": i})
    name = request.GET.get('name') or ''
    context = {"cards_list": cards_list,
               'name': name}
    return render(request, 'home.html', context)


def about_us(request):
    about = Clinic_about_us.objects.all()
    aboutList = []
    for a in about:
        aboutList.append({'a': a})
    name = request.GET.get('name') or ''
    context = {'aboutList': aboutList,
               'name': name}
    return render(request, 'about_us.html', context)

def logout(request):
    auth.logout(request) # Log out the user
    return redirect("/")  

@login_required(login_url='login')
def connect(request):
    if request.method == "POST" :
        fnamee = request.POST.get('name')
        femail = request.POST.get('email')
        fphone = request.POST.get('telephone')
        fcomment = request.POST.get('comment')
        query = Contact(name=fnamee, email=femail, phoneNum=fphone, message=fcomment)
        
        query.save()
        return redirect("connect")
    
    return render(request, 'connect_us.html')


def details(request):
    detailInfo = Clinec_site.objects.all()
    details_list = []
    for i in detailInfo:
        details_list.append({"i": i})
    name = Clinec_site.healName
    context = {"details_list": details_list,
               "name": name,
               }
    return render(request, 'details.html', context)


def knee_pain(request):
    return render(request, 'knee_pain.html')


def fakry(request):
    return render(request, 'fakry.html')


def PG_injuries(request):
    return render(request, 'PG_injuries.html')