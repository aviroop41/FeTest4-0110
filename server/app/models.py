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

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='Pending')

class TeamAttendance(models.Model):
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance_records = models.ManyToManyField(Attendance)

class TeamLeaveRequest(models.Model):
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_request = models.ForeignKey(LeaveRequest, on_delete=models.CASCADE)

class OrganizationDirectory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

class OrganizationStructure(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='subordinates')
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='managers')

# New Model for employee profile updates
class EmployeeProfile(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)

class AttendanceReport(models.Model):
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    report_data = models.JSONField()  # Store structured data for attendance

class Notification(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    permissions = models.JSONField(default=list)  # Store permissions as a JSON list

class EmployeeRole(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)