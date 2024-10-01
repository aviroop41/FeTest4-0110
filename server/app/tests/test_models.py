from django.test import TestCase
from .models import Employee, Attendance, LeaveBalance, RecentActivity

class EmployeeModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(employee_id='EMP001', name='John Doe')

    def test_employee_creation(self):
        self.assertEqual(self.employee.employee_id, 'EMP001')
        self.assertEqual(self.employee.name, 'John Doe')
        self.assertIsNotNone(self.employee.id)

    def test_unique_employee_id(self):
        with self.assertRaises(Exception):
            Employee.objects.create(employee_id='EMP001', name='Jane Doe')

class AttendanceModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(employee_id='EMP001', name='John Doe')
        self.attendance = Attendance.objects.create(employee=self.employee, date='2023-01-01', status='Present')

    def test_attendance_creation(self):
        self.assertEqual(self.attendance.status, 'Present')
        self.assertEqual(self.attendance.employee, self.employee)

    def test_attendance_employee_relation(self):
        self.assertEqual(self.attendance.employee.employee_id, 'EMP001')

class LeaveBalanceModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(employee_id='EMP001', name='John Doe')
        self.leave_balance = LeaveBalance.objects.create(employee=self.employee, annual_leave=10, sick_leave=5)

    def test_leave_balance_creation(self):
        self.assertEqual(self.leave_balance.annual_leave, 10)
        self.assertEqual(self.leave_balance.sick_leave, 5)

    def test_leave_balance_employee_relation(self):
        self.assertEqual(self.leave_balance.employee.employee_id, 'EMP001')

class RecentActivityModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(employee_id='EMP001', name='John Doe')
        self.activity = RecentActivity.objects.create(employee=self.employee, activity='Logged in')

    def test_recent_activity_creation(self):
        self.assertEqual(self.activity.activity, 'Logged in')
        self.assertEqual(self.activity.employee, self.employee)
        self.assertIsNotNone(self.activity.timestamp)

    def test_recent_activity_employee_relation(self):
        self.assertEqual(self.activity.employee.employee_id, 'EMP001')