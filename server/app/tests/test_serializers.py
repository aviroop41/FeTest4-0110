from django.test import TestCase
from rest_framework.exceptions import ValidationError
from app.models import Attendance, LeaveBalance, Activity, Leave, Employee, Notification
from app.serializers import AttendanceSerializer, LeaveBalanceSerializer, RecentActivitiesSerializer, LeaveRequestSerializer, AttendanceDetailSerializer, TeamAttendanceSerializer, TeamLeaveRequestSerializer, EmployeeSerializer, OrganizationDirectorySerializer, OrganizationStructureSerializer, EmployeeProfileSerializer, AttendanceReportSerializer, NotificationSerializer
class AttendanceSerializerTest(TestCase):
    def test_valid_serialization(self):
        attendance_data = {'user': 1, 'status': 'present', 'date': '2023-10-01'}
        serializer = AttendanceSerializer(data=attendance_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['status'], 'present')
    def test_invalid_serialization(self):
        attendance_data = {'user': 1, 'status': '', 'date': '2023-10-01'}
        serializer = AttendanceSerializer(data=attendance_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('status', serializer.errors)
class LeaveBalanceSerializerTest(TestCase):
    def test_valid_serialization(self):
        leave_balance_data = {'user': 1, 'annual_leave': 10, 'sick_leave': 5}
        serializer = LeaveBalanceSerializer(data=leave_balance_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['annual_leave'], 10)
    def test_invalid_serialization(self):
        leave_balance_data = {'user': 1, 'annual_leave': -1, 'sick_leave': 5}
        serializer = LeaveBalanceSerializer(data=leave_balance_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('annual_leave', serializer.errors)
class RecentActivitiesSerializerTest(TestCase):
    def test_valid_serialization(self):
        activity_data = {'user': 1, 'activity_type': 'login', 'timestamp': '2023-10-01T12:00:00Z'}
        serializer = RecentActivitiesSerializer(data=activity_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['activity_type'], 'login')
    def test_invalid_serialization(self):
        activity_data = {'user': 1, 'activity_type': '', 'timestamp': '2023-10-01T12:00:00Z'}
        serializer = RecentActivitiesSerializer(data=activity_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('activity_type', serializer.errors)
class LeaveRequestSerializerTest(TestCase):
    def test_valid_serialization(self):
        leave_request_data = {'employee': 1, 'start_date': '2023-10-01', 'end_date': '2023-10-10', 'reason': 'vacation'}
        serializer = LeaveRequestSerializer(data=leave_request_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['reason'], 'vacation')
    def test_invalid_serialization(self):
        leave_request_data = {'employee': 1, 'start_date': '', 'end_date': '2023-10-10', 'reason': 'vacation'}
        serializer = LeaveRequestSerializer(data=leave_request_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('start_date', serializer.errors)
class AttendanceDetailSerializerTest(TestCase):
    def test_valid_serialization(self):
        attendance_detail_data = {'employee': 1, 'date': '2023-10-01', 'status': 'present'}
        serializer = AttendanceDetailSerializer(data=attendance_detail_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['status'], 'present')
    def test_invalid_serialization(self):
        attendance_detail_data = {'employee': 1, 'date': '', 'status': 'present'}
        serializer = AttendanceDetailSerializer(data=attendance_detail_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('date', serializer.errors)
class TeamAttendanceSerializerTest(TestCase):
    def test_valid_serialization(self):
        team_attendance_data = {'employee': 1, 'date': '2023-10-01', 'status': 'present'}
        serializer = TeamAttendanceSerializer(data=team_attendance_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['status'], 'present')
    def test_invalid_serialization(self):
        team_attendance_data = {'employee': 1, 'date': '', 'status': 'present'}
        serializer = TeamAttendanceSerializer(data=team_attendance_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('date', serializer.errors)
class TeamLeaveRequestSerializerTest(TestCase):
    def test_valid_serialization(self):
        team_leave_request_data = {'employee': 1, 'start_date': '2023-10-01', 'end_date': '2023-10-10', 'reason': 'vacation', 'status': 'pending'}
        serializer = TeamLeaveRequestSerializer(data=team_leave_request_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['reason'], 'vacation')
    def test_invalid_serialization(self):
        team_leave_request_data = {'employee': 1, 'start_date': '2023-10-01', 'end_date': '', 'reason': 'vacation', 'status': 'pending'}
        serializer = TeamLeaveRequestSerializer(data=team_leave_request_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('end_date', serializer.errors)
class EmployeeSerializerTest(TestCase):
    def test_valid_serialization(self):
        employee_data = {'employee_id': 1, 'name': 'John Doe'}
        serializer = EmployeeSerializer(data=employee_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'], 'John Doe')
    def test_invalid_serialization(self):
        employee_data = {'employee_id': '', 'name': 'John Doe'}
        serializer = EmployeeSerializer(data=employee_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('employee_id', serializer.errors)
class OrganizationDirectorySerializerTest(TestCase):
    def test_valid_serialization(self):
        organization_data = {'employee_id': 1, 'name': 'John Doe', 'department': 'Engineering', 'position': 'Software Engineer'}
        serializer = OrganizationDirectorySerializer(data=organization_data)
        self.assertTrue(serializer.is_valid())
    def test_invalid_serialization(self):
        organization_data = {'employee_id': 1, 'name': ''}
        serializer = OrganizationDirectorySerializer(data=organization_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)
class OrganizationStructureSerializerTest(TestCase):
    def test_valid_serialization(self):
        structure_data = {'employee_id': 1, 'name': 'John Doe'}
        serializer = OrganizationStructureSerializer(data=structure_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'], 'John Doe')
    def test_invalid_serialization(self):
        structure_data = {'employee_id': '', 'name': 'John Doe'}
        serializer = OrganizationStructureSerializer(data=structure_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('employee_id', serializer.errors)
class EmployeeProfileSerializerTest(TestCase):
    def test_valid_serialization(self):
        employee_profile_data = {'employee_id': 1, 'name': 'John Doe'}
        serializer = EmployeeProfileSerializer(data=employee_profile_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'], 'John Doe')
    def test_invalid_serialization(self):
        employee_profile_data = {'employee_id': '', 'name': 'John Doe'}
        serializer = EmployeeProfileSerializer(data=employee_profile_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('employee_id', serializer.errors)
class AttendanceReportSerializerTest(TestCase):
    def test_valid_serialization(self):
        attendance_report_data = {'employee': 1, 'date': '2023-10-01', 'status': 'present'}
        serializer = AttendanceReportSerializer(data=attendance_report_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['status'], 'present')
    def test_invalid_serialization(self):
        attendance_report_data = {'employee': 1, 'date': '', 'status': 'present'}
        serializer = AttendanceReportSerializer(data=attendance_report_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('date', serializer.errors)
class NotificationSerializerTest(TestCase):
    def test_valid_serialization(self):
        notification_data = {'employee': 1, 'message': 'Test message', 'is_read': False}
        serializer = NotificationSerializer(data=notification_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['message'], 'Test message')
    def test_invalid_serialization(self):
        notification_data = {'employee': 1, 'message': '', 'is_read': False}
        serializer = NotificationSerializer(data=notification_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('message', serializer.errors)