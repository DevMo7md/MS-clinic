from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here

class Clinec_site(models.Model):
    healName = models.CharField(max_length=50, help_text='اسم الاصابه')
    injuryImg = models.ImageField(upload_to='Clenic site/Clenic/', verbose_name='Injury photo', null=True, blank=True)
    healinfo = models.TextField(help_text='معلومات عنها و طريقه الوقايه منها و طرق علاجها')
    details = models.TextField(default='', help_text='تفاصيل عن طرق علاجها بالمركز')

    def __str__(self) -> str:
        return self.healName

class Injury_Photos(models.Model):
    injury = models.ForeignKey(Clinec_site, on_delete=models.CASCADE, related_name='injury_photos')
    photo = models.ImageField(upload_to='Injury_Photos/', verbose_name='Injury photo')
    def __str__(self):
        return f'photo of {self.injury.healName}'



class Clinic_about_us(models.Model):
    head = models.CharField(max_length=500, help_text='رأس الموضوع')
    body = models.TextField(help_text='الموضوع')

    def __str__(self) -> str:
        return self.head


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNum = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name} Send {self.message}"
    
class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    name = models.CharField(max_length=50)
    phoneNum = models.CharField(max_length=15)
    age = models.IntegerField()
    date = models.DateField(null=True, blank=True)
    SERVICE_CHOICES = [
        ('physical_therapy', 'علاج طبيعي'),
        ('massage', 'مساج'),
        ('rehabilitation', 'إعادة تأهيل'),
        ('consultation', 'استشارة'),
    ]

    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    time = models.TimeField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
        ('no_show', 'No Show'),
    ]

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} reservated in {self.date}"

