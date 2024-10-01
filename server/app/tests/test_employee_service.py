from django.test import TestCase
from unittest.mock import patch, MagicMock
from app.models import Attendance, Leave, Activity
from app.services import EmployeeService

class EmployeeServiceTest(TestCase):
    @patch('app.models.Attendance.objects.filter')
    def test_get_attendance_success(self, mock_filter):
        mock_filter.return_value = [MagicMock()]
        result = EmployeeService.get_attendance(employee_id=1)
        self.assertEqual(len(result), 1)

    @patch('app.models.Attendance.objects.filter')
    def test_get_attendance_no_records(self, mock_filter):
        mock_filter.return_value = []
        result = EmployeeService.get_attendance(employee_id=999)
        self.assertEqual(len(result), 0)

    @patch('app.models.Leave.objects.get')
    def test_get_leave_balance_success(self, mock_get):
        mock_get.return_value = MagicMock(balance=10)
        result = EmployeeService.get_leave_balance(employee_id=1)
        self.assertEqual(result.balance, 10)

    @patch('app.models.Leave.objects.get')
    def test_get_leave_balance_not_found(self, mock_get):
        mock_get.side_effect = Leave.DoesNotExist
        with self.assertRaises(Leave.DoesNotExist):
            EmployeeService.get_leave_balance(employee_id=999)

    @patch('app.models.Activity.objects.filter')
    def test_get_recent_activities_success(self, mock_filter):
        mock_filter.return_value.order_by.return_value[:10] = [MagicMock()]*5
        result = EmployeeService.get_recent_activities(employee_id=1)
        self.assertEqual(len(result), 5)

    @patch('app.models.Activity.objects.filter')
    def test_get_recent_activities_no_records(self, mock_filter):
        mock_filter.return_value.order_by.return_value[:10] = []
        result = EmployeeService.get_recent_activities(employee_id=999)
        self.assertEqual(len(result), 0)