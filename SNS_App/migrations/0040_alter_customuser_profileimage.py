# Generated by Django 3.2.7 on 2023-09-10 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SNS_App', '0039_auto_20220724_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='ProfileImage',
            field=models.ImageField(default='media/default_img', upload_to=''),
        ),
    ]
