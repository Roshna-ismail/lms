# Generated by Django 4.0.3 on 2022-10-22 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcourseenrollment',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]