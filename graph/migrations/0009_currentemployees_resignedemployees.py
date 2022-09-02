# Generated by Django 4.0.4 on 2022-06-11 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0008_file_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currentemployees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_Code', models.IntegerField()),
                ('Emp_Name', models.CharField(max_length=200)),
                ('Joining_Date', models.DateField()),
                ('Division', models.CharField(max_length=200)),
                ('Rel_Exp_Till_Date_in_Yrs', models.IntegerField()),
                ('Designation', models.CharField(max_length=200)),
                ('Date_of_Birth', models.DateField()),
                ('Project_Function', models.CharField(max_length=200)),
                ('QA_Dev_DB', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=10)),
                ('Source', models.CharField(max_length=200)),
                ('Full_Time_Contractual', models.CharField(max_length=200)),
                ('Manager_Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Resignedemployees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_Code', models.IntegerField()),
                ('Emp_Name', models.CharField(max_length=200)),
                ('Joining_Date', models.DateField()),
                ('Division', models.CharField(max_length=200)),
                ('Rel_Exp_Till_Date_in_Yrs', models.IntegerField()),
                ('Designation', models.CharField(max_length=200)),
                ('Date_of_Birth', models.DateField()),
                ('Project_Function', models.CharField(max_length=200)),
                ('QA_Dev_DB', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=10)),
                ('Source', models.CharField(max_length=200)),
                ('Full_Time_Contractual', models.CharField(max_length=200)),
                ('Manager_Name', models.CharField(max_length=200)),
            ],
        ),
    ]
