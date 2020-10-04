# Generated by Django 2.2.7 on 2020-10-04 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ThemeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AchiveStore',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achievement.Themes')),
            ],
        ),
        migrations.CreateModel(
            name='AchieveUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('receipt', models.ImageField(upload_to='receipt/%Y/%m/%d', verbose_name='영수증사진')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
