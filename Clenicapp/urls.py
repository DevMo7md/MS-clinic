from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('about_us/', views.about_us, name='about_us'),
    path('connect_us/', views.connect, name='connect'),
    path('details/<int:pk>/', views.details, name='details'),
    path('knee_pain/', views.knee_pain, name='knee_pain'),
    path('alfakry/', views.fakry, name='fakry'),
    path('Playground_injuries/', views.PG_injuries, name='PG_injuries'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
