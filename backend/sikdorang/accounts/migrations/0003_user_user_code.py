# Generated by Django 2.2.7 on 2020-09-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userphonecheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_code',
            field=models.IntegerField(default=0),
        ),
    ]
