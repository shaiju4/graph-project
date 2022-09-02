from django.db import models

# Create your models here.
class File(models.Model):
    file_id=models.AutoField(primary_key=True)
    table_name=models.CharField(max_length=100,default='na')
    file=models.FileField(upload_to='documents')
    date=models.DateField(null=True)
    
class Currentemployees(models.Model):
    Emp_Code=models.IntegerField()
    Emp_Name=models.CharField(max_length=200)
    Joining_Date=models.DateField(any)
    Division=models.CharField(max_length=200)
    Rel_Exp_Till_Date_in_Yrs=models.IntegerField()
    Designation=models.CharField(max_length=200)
    Date_of_Birth=models.DateField()
    Project_or_Function=models.CharField(max_length=200)
    QA_Dev_DB=models.CharField(max_length=200)
    Gender=models.CharField(max_length=10)
    Source=models.CharField(max_length=200)
    Full_Time_or_Contractual=models.CharField(max_length=200)
    Manager_Name=models.CharField(max_length=200)
    def __str__(self):
        return self.Emp_Name



class Resignedemployees(models.Model):
    Emp_Code=models.IntegerField()
    Emp_Name=models.CharField(max_length=200)
    Joining_Date=models.DateField(any)
    Division=models.CharField(max_length=200)
    Rel_Exp_Till_Date_in_Yrs=models.IntegerField()
    Designation=models.CharField(max_length=200)
    Date_of_Birth=models.DateField()
    Project_or_Function=models.CharField(max_length=200)
    QA_Dev_DB=models.CharField(max_length=200)
    Gender=models.CharField(max_length=10)
    Source=models.CharField(max_length=200)
    Full_Time_or_Contractual=models.CharField(max_length=200)
    Manager_Name=models.CharField(max_length=200)




