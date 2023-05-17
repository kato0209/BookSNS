# Generated by Django 3.2.7 on 2021-12-09 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SNS_App', '0008_alter_tweetmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SNS_App.comment'),
        ),
        migrations.AlterField(
            model_name='like',
            name='tweet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SNS_App.tweetmodel'),
        ),
    ]