from django.shortcuts import render, get_list_or_404, redirect
from .models import *
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
def register(request):
    form = CreateUserForm() # Initialize an empty registration form
    if request.method == "POST": 
        form = CreateUserForm(request.POST) # Get the data from the submitted registration form
        if form.is_valid():
            form.save() # Save the new user to the database
            return redirect("login") # Redirect the user to the login page after successful registration
        else:
            messages.error(request, "Registration form is not valid. Please try again and verify your informations ")

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
                return redirect("main_page") # Redirect the user to the home page after successful login
            else:
                messages.error(request, "please fill the form correctly")
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
    context = {'aboutList': aboutList,}
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
        contact_email_toclinic(femail, fnamee, fphone, fcomment)
        messages.success(request, "Email sent successfully")
        return redirect("connect")
    
    return render(request, 'connect_us.html')


def details(request, pk):
    try:
        injury = Clinec_site.objects.get(pk=pk)
    except Clinec_site.DoesNotExist:
        return redirect('main_page')
    context = {'injury': injury}
    return render(request, 'details.html', context)


def knee_pain(request):
    return render(request, 'knee_pain.html')


def fakry(request):
    return render(request, 'fakry.html')


def PG_injuries(request):
    return render(request, 'PG_injuries.html')

# dashboard
def dashboard(request):
    if not (request.user.is_authenticated and request.user.is_staff):
        messages.error(request, "This page not allowed for you please login with your admin account")
        return redirect('login')
    contacts = Contact.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        details = request.POST.get('details')
        photos = request.FILES.getlist('images')
        # التحقق من صحة البيانات المدخلة
        if not name:
            messages.error(request, "حقل الاسم مطلوب.")
            return redirect('dashboard')
        if not details:
            messages.error(request, "حقل التفاصيل مطلوب.")
            return redirect('dashboard')
        if not photos:
            messages.error(request, "يجب رفع صورة واحدة على الأقل.")
            return redirect('dashboard')
        
        injury = Clinec_site.objects.create(healName=name, details=details, injuryImg=photos[0])
        for photo in photos[1:]:
            Injury_Photos.objects.create(injury=injury, photo=photo)
        messages.success(request, "Injury added successfully")
        return redirect('dashboard')
    return render(request, 'dashboard.html', {'contacts':contacts})

# contact email to clinic
def contact_email_toclinic(email_sender, sender_name, sender_phone, email_body):
    html_content = render_to_string('contact_email_toclinic.html', {'email_sender': email_sender, 'sender_name': sender_name, 'sender_phone': sender_phone, 'email_body': email_body})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        'Contact Email to Clinic',# subject
        text_content,   # body
        email_sender, # from email
        [settings.EMAIL_HOST_USER] # to email
    )
    email.attach_alternative(html_content, 'text/html')
    email.send()

def reply_contact(request, contact_id):
    if request.method == 'POST':
        contact = Contact.objects.get(id=contact_id)
        reply_message = request.POST.get('reply_message')
        
        contact_email_toclinic(
            settings.EMAIL_HOST_USER, 
            'MS-Clinic', 
            'MS-clinic(phone number)',
            f'تم ارد على رسالتك "{contact.message}" \n الرد : {reply_message}'
            )
        
        messages.success(request, 'تم إرسال الرد بنجاح')
        return redirect('dashboard')