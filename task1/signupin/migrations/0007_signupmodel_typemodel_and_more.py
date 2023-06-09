# Generated by Django 4.2 on 2023-04-20 00:58

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('signupin', '0006_registerationmodel_delete_registermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpModel',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ProfilePic', models.ImageField(upload_to='profilepic/')),
                ('ConfirmPassword', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.CharField(choices=[('Patient', 'PATIENT'), ('Doctor', 'DOCTOR')], default='Patient', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='registerationmodel',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='UserTypeModel',
        ),
        migrations.DeleteModel(
            name='RegisterationModel',
        ),
    ]
