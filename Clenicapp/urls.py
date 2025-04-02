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
    path('reply-contact/<int:contact_id>/', views.reply_contact, name='reply_contact'),
    path('edit_injury/<int:injury_id>/', views.edit_injury, name='edit_injury'),
    path('delete_injury/<int:injury_id>/', views.delete_injury, name='delete_injury'),
    # reservation
    path('reservation/', views.reservation, name='reservation'),
    path('user_reservations/', views.user_reservations, name='user_reservations'),
    path('reservation_details/<str:reservation_id>/', views.reservation_details, name='reservation_details'),
    path('cancel_reservation/<str:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
    path('edit_reservation/<str:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('accept_reservation/<str:reservation_id>/', views.accept_reservation, name='accept_reservation'),
    path('reject_reservation/<str:reservation_id>/', views.reject_reservation, name='reject_reservation'),
    path('confirm_reservation/<str:reservation_id>/', views.confirm_reservation, name='confirm_reservation'),
    path('no_show_reservation/<str:reservation_id>/', views.no_show_reservation, name='no_show_reservation'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
