# Generated by Django 4.0.4 on 2022-06-08 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0007_remove_file_month_remove_file_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
