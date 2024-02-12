from django.shortcuts import render
from .models import Clinec_site, Clinic_about_us


# Create your views here.

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


def connect(request):
    return render(request, 'connect_us.html')


def details(request):
    cardInfo = Clinec_site.objects.all()
    cards_list = []
    for i in cardInfo:
        cards_list.append({"i": i})
    name = Clinec_site.healName
    context = {"cards_list": cards_list,
               "name": name,
               }
    return render(request, 'details.html', context)


