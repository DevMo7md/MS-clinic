from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main page'),
    path('about_us/', views.about_us, name='about_us'),
    path('connect_us/', views.connect, name='connect'),
    path('details/', views.details, name='details'),

]
