from django.contrib import admin

from .models import Clinec_site, Clinic_about_us, Contact


# Register your models here.

admin.site.register(Clinec_site)
admin.site.register(Clinic_about_us)
admin.site.register(Contact)
