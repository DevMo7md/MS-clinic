from django.db import models

# Create your models here

class Clinec_site(models.Model):
    healName = models.CharField(max_length=50, help_text='اسم الاصابه')
    injuryImg = models.ImageField(upload_to='Clenic site/Clenic/', verbose_name='Injury photo', null=True, blank=True)
    healinfo = models.TextField(help_text='معلومات عنها و طريقه الوقايه منها و طرق علاجها')
    details = models.TextField(default='', help_text='تفاصيل عن طرق علاجها بالمركز')

    def __str__(self) -> str:
        return self.healName


class Clinic_about_us(models.Model):
    head = models.CharField(max_length=500, help_text='رأس الموضوع')
    body = models.TextField(max_length=500000, help_text='الموضوع')

    def __str__(self) -> str:
        return self.head


class Contact(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField()
    phoneNum = models.CharField(max_length=12)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} Send {self.message}"