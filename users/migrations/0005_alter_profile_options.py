# Generated by Django 3.2.4 on 2022-12-22 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
    ]
