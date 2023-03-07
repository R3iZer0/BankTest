# Generated by Django 4.1.7 on 2023-03-06 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestBank', '0004_client_adress_client_city_client_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='adress',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='number',
            field=models.FloatField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='state',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='zip_code',
            field=models.CharField(default=' ', max_length=10),
        ),
    ]
