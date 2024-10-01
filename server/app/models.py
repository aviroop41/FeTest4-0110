from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=50)

class LeaveBalance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    annual_leave = models.IntegerField(default=0)
    sick_leave = models.IntegerField(default=0)

class RecentActivity(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    activity = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)