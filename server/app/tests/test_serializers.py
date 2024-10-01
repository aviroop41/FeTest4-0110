from django.test import TestCase
from rest_framework.exceptions import ValidationError
from app.models import Attendance, LeaveBalance, Activity, Leave
from app.serializers import AttendanceSerializer, LeaveBalanceSerializer, RecentActivitiesSerializer, LeaveRequestSerializer, AttendanceDetailSerializer

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