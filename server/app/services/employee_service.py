from django.shortcuts import render

# Create your models here.

import requests
from .models import Attendance, Leave, Activity

class EmployeeService:
    @staticmethod
    def get_attendance(employee_id):
        return Attendance.objects.filter(employee_id=employee_id)

    @staticmethod
    def get_leave_balance(employee_id):
        return Leave.objects.get(employee_id=employee_id)

    @staticmethod
    def get_recent_activities(employee_id):
        return Activity.objects.filter(employee_id=employee_id).order_by('-date')[:10]