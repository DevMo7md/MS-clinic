# Generated by Django 5.1.3 on 2025-04-01 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clenicapp', '0006_reservation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='service',
            field=models.CharField(choices=[('physical_therapy', 'علاج طبيعي'), ('massage', 'مساج'), ('rehabilitation', 'إعادة تأهيل'), ('consultation', 'استشارة')], max_length=50),
        ),
    ]
