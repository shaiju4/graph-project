# Generated by Django 4.0.4 on 2022-06-08 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0006_alter_file_month_alter_file_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='month',
        ),
        migrations.RemoveField(
            model_name='file',
            name='year',
        ),
    ]