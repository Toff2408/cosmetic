# Generated by Django 4.1.2 on 2022-11-01 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0004_shipping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='street',
        ),
        migrations.AddField(
            model_name='shipping',
            name='billing_address',
            field=models.CharField(default='a', max_length=50),
        ),
        migrations.AddField(
            model_name='shipping',
            name='delivery_address',
            field=models.CharField(default='a', max_length=50),
        ),
        migrations.AddField(
            model_name='shipping',
            name='email',
            field=models.EmailField(default='A', max_length=50),
        ),
        migrations.AddField(
            model_name='shipping',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='shipping',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
