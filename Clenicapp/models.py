from django.db import models


# Create your models here

class Clinec_site(models.Model):
    healName = models.CharField(max_length=50, help_text='اسم الاصابه')
    injuryImg = models.ImageField(upload_to='Clenic site/Clenic/', verbose_name='Injury photo', null=True, blank=True)
    healinfo = models.CharField(max_length=100000, help_text='معلومات عنها و طريقه الوقايه منها و طرق علاجها')
    details = models.CharField(max_length=1000000, default='', help_text='تفاصيل عن طرق علاجها بالمركز')


class Clinic_about_us(models.Model):
    head = models.CharField(max_length=500, help_text='رأس الموضوع')
    body = models.CharField(max_length=500000, help_text='الموضوع')



