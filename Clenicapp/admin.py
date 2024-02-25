from django.contrib import admin

from .models import Clinec_site, Clinic_about_us, Users

from .models import Clinec_site, Clinic_about_us, Add_user


# Register your models here.

admin.site.register(Clinec_site)
admin.site.register(Clinic_about_us)
admin.site.register(Users)
admin.site.register(Add_user)

