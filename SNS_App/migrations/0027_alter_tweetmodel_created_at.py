# Generated by Django 3.2.7 on 2022-01-14 15:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SNS_App', '0026_remove_tweetmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetmodel',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
