# Generated by Django 2.1 on 2018-11-10 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('choiceA', models.CharField(max_length=100)),
                ('choiceB', models.CharField(max_length=100)),
                ('choiceC', models.CharField(max_length=100)),
                ('choiceD', models.CharField(max_length=100)),
                ('answer_text', models.CharField(max_length=100)),
                ('subject', models.CharField(choices=[('PSTAR', 'PSTAR'), ('PPL', 'Private Pilots License'), ('CPL', 'Commercial Pilots Licence'), ('IFR', 'Instrument Rating'), ('ATPL', 'Airline Pilots License')], default='', max_length=100)),
            ],
        ),
    ]
