# Generated by Django 5.0.6 on 2024-09-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_back_alter_user_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='back',
            field=models.ImageField(blank=True, null=True, upload_to='users/back/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='users/icon/%Y/%m/%d'),
        ),
    ]
