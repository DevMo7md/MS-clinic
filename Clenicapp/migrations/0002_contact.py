# Generated by Django 4.2.5 on 2024-04-18 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clenicapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNum', models.CharField(max_length=12)),
                ('message', models.TextField()),
            ],
        ),
    ]
