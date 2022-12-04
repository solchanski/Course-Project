# Generated by Django 4.1.3 on 2022-12-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_tickets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='company',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='company',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='location',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='location',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='route',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='bus',
            name='seats',
            field=models.FloatField(max_length=5),
        ),
    ]