# Generated by Django 4.1.7 on 2023-03-13 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestBank', '0009_client_active_alter_client_user'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='client',
            table='testbank_client',
        ),
    ]
