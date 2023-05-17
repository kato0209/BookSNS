# Generated by Django 3.2.7 on 2022-07-24 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SNS_App', '0037_auto_20220516_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='finished_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='finished_book', to='SNS_App.bookdata'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='reserved_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reserved_book', to='SNS_App.bookdata'),
        ),
        migrations.AlterField(
            model_name='connection',
            name='followed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followed', to=settings.AUTH_USER_MODEL),
        ),
    ]