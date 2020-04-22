# Generated by Django 3.0 on 2020-04-22 16:34

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_auto_20200422_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=phone_field.models.PhoneField(max_length=31, null=True),
        ),
    ]
