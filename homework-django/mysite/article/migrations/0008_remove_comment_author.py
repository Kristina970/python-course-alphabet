# Generated by Django 2.2.2 on 2019-07-09 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20190708_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]
