# Generated by Django 2.1.5 on 2019-02-26 11:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20190226_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
