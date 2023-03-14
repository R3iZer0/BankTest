# Generated by Django 3.1.8 on 2023-03-14 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TestBank', '0007_auto_20230311_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='active',
        ),
        migrations.RemoveField(
            model_name='client',
            name='adress',
        ),
        migrations.RemoveField(
            model_name='client',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
        migrations.RemoveField(
            model_name='client',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='client',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='number',
        ),
        migrations.RemoveField(
            model_name='client',
            name='password',
        ),
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='state',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='zip_code',
            field=models.CharField(max_length=10),
        ),
    ]
