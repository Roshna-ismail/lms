# Generated by Django 4.0.3 on 2022-10-23 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_chapter_enrollstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='enrollStatus',
        ),
    ]