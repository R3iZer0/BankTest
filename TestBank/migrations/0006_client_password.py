# Generated by Django 4.1.7 on 2023-03-06 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestBank', '0005_alter_client_active_alter_client_adress_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='password',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]