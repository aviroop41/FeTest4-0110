from django.test import TestCase
from .models import Employee, Attendance, LeaveBalance, RecentActivity, LeaveRequest, TeamAttendance, TeamLeaveRequest, OrganizationDirectory, OrganizationStructure, EmployeeProfile, AttendanceReport, Notification

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

class LeaveRequestModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(employee_id='EMP001', name='John Doe')
        self.leave_request = LeaveRequest.objects.create(employee=self.employee, start_date='2023-01-01', end_date='2023-01-05', reason='Vacation', status='Pending')

    def test_leave_request_creation(self):
        self.assertEqual(self.leave_request.reason, 'Vacation')
        self.assertEqual(self.leave_request.status, 'Pending')
        self.assertEqual(self.leave_request.employee, self.employee)

    def test_leave_request_date_validation(self):
        with self.assertRaises(Exception):
            LeaveRequest.objects.create(employee=self.employee, start_date='2023-01-10', end_date='2023-01-05', reason='Invalid Dates')

    def test_leave_request_employee_relation(self):
        self.assertEqual(self.leave_request.employee.employee_id, 'EMP001')

class TeamAttendanceModelTest(TestCase):
    def setUp(self):
        self.manager = Employee.objects.create(employee_id='EMP002', name='Jane Smith')
        self.employee = Employee.objects.create(employee_id='EMP001', name='John Doe')
        self.attendance = Attendance.objects.create(employee=self.employee, date='2023-01-01', status='Present')
        self.team_attendance = TeamAttendance.objects.create(manager=self.manager)
        self.team_attendance.attendance_records.add(self.attendance)

    def test_team_attendance_creation(self):
        self.assertIn(self.attendance, self.team_attendance.attendance_records.all())
        self.assertEqual(self.team_attendance.manager.name, 'Jane Smith')

class TeamLeaveRequestModelTest(TestCase):
    def setUp(self):
        self.manager = Employee.objects.create(employee_id='EMP002', name='Jane Smith')
        self.employee = Employee.objects.create(employee_id='EMP001', name='John Doe')
        self.leave_request = LeaveRequest.objects.create(employee=self.employee, start_date='2023-01-01', end_date='2023-01-05', reason='Vacation', status='Pending')
        self.team_leave_request = TeamLeaveRequest.objects.create(manager=self.manager, leave_request=self.leave_request)

    def test_team_leave_request_creation(self):
        self.assertEqual(self.team_leave_request.manager.name, 'Jane Smith')
        self.assertEqual(self.team_leave_request.leave_request.reason, 'Vacation')

class OrganizationDirectoryModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(employee_id='EMP001', name='John Doe')
        self.organization_directory = OrganizationDirectory.objects.create(employee=self.employee, position='Developer', department='Engineering')

    def test_organization_directory_creation(self):
        self.assertEqual(self.organization_directory.position, 'Developer')
        self.assertEqual(self.organization_directory.department, 'Engineering')
        self.assertEqual(self.organization_directory.employee.employee_id, 'EMP001')

class OrganizationStructureModelTest(TestCase):
    def setUp(self):
        self.manager = Employee.objects.create(employee_id='EMP002', name='Jane Smith')
        self.employee = Employee.objects.create(employee_id='EMP001', name='John Doe')
        self.organization_structure = OrganizationStructure.objects.create(employee=self.employee, manager=self.manager)

    def test_organization_structure_creation(self):
        self.assertEqual(self.organization_structure.employee.employee_id, 'EMP001')
        self.assertEqual(self.organization_structure.manager.employee_id, 'EMP002')

class EmployeeProfileModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(employee_id='EMP001', name='John Doe')
        self.employee_profile = EmployeeProfile.objects.create(employee=self.employee, address='123 Main St', phone_number='1234567890', email='john.doe@example.com', position='Developer')

    def test_employee_profile_creation(self):
        self.assertEqual(self.employee_profile.address, '123 Main St')
        self.assertEqual(self.employee_profile.phone_number, '1234567890')
        self.assertEqual(self.employee_profile.email, 'john.doe@example.com')
        self.assertEqual(self.employee_profile.position, 'Developer')

    def test_employee_profile_employee_relation(self):
        self.assertEqual(self.employee_profile.employee.employee_id, 'EMP001')

    def test_employee_profile_blank_fields(self):
        profile = EmployeeProfile.objects.create(employee=self.employee)
        self.assertIsNone(profile.address)
        self.assertIsNone(profile.phone_number)
        self.assertIsNone(profile.email)
        self.assertIsNone(profile.position)

class AttendanceReportModelTest(TestCase):
    def setUp(self):
        self.manager = Employee.objects.create(employee_id='EMP003', name='Alice Brown')
        self.attendance_report = AttendanceReport.objects.create(manager=self.manager, start_date='2023-01-01', end_date='2023-01-31', report_data={'EMP001': 'Present', 'EMP002': 'Absent'})

    def test_attendance_report_creation(self):
        self.assertEqual(self.attendance_report.manager.employee_id, 'EMP003')
        self.assertEqual(self.attendance_report.report_data, {'EMP001': 'Present', 'EMP002': 'Absent'})

    def test_attendance_report_date_range(self):
        self.assertEqual(self.attendance_report.start_date, '2023-01-01')
        self.assertEqual(self.attendance_report.end_date, '2023-01-31')

class NotificationModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(employee_id='EMP001', name='John Doe')
        self.notification = Notification.objects.create(employee=self.employee, message='Test Notification')

    def test_notification_creation(self):
        self.assertEqual(self.notification.message, 'Test Notification')
        self.assertEqual(self.notification.employee, self.employee)
        self.assertFalse(self.notification.is_read)
        self.assertIsNotNone(self.notification.created_at)

    def test_notification_employee_relation(self):
        self.assertEqual(self.notification.employee.employee_id, 'EMP001')

    def test_notification_read_status(self):
        self.notification.is_read = True
        self.notification.save()
        self.assertTrue(Notification.objects.get(id=self.notification.id).is_read)