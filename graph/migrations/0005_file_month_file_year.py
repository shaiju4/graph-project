# Generated by Django 4.0.4 on 2022-06-06 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0004_file_table_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='month',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]