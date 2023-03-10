# Generated by Django 3.2 on 2023-03-09 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role_app', '0004_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Doctor', 'doctor'), ('Paient', 'paient')], default='patient', max_length=20, verbose_name='Role'),
        ),
    ]
