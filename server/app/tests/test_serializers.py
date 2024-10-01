from django.test import TestCase
from rest_framework.exceptions import ValidationError
from app.models import Attendance, LeaveBalance, Activity
from app.serializers import AttendanceSerializer, LeaveBalanceSerializer, RecentActivitiesSerializer

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