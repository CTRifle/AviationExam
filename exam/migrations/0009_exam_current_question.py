# Generated by Django 2.1 on 2018-11-13 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0008_auto_20181113_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='current_question',
            field=models.IntegerField(default=1, max_length=3),
            preserve_default=False,
        ),
    ]