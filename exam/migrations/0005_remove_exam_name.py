# Generated by Django 2.1 on 2018-11-10 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20181110_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='name',
        ),
    ]
