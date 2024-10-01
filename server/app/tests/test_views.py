from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch, MagicMock
from .models import Attendance, Leave, Activity

class AttendanceViewsTests(TestCase):

    @patch('app.models.Attendance.objects.filter')
    def test_get_attendance_success(self, mock_filter):
        mock_filter.return_value = MagicMock()
        mock_filter.return_value.values.return_value = [{'date': '2023-10-01', 'employee_id': 1}]
        response = self.client.get(reverse('get_attendance', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'attendance': [{'date': '2023-10-01', 'employee_id': 1}]})

    @patch('app.models.Attendance.objects.filter')
    def test_get_attendance_empty(self, mock_filter):
        mock_filter.return_value = MagicMock()
        mock_filter.return_value.values.return_value = []
        response = self.client.get(reverse('get_attendance', args=[2]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'attendance': []})

    @patch('app.models.Leave.objects.filter')
    def test_get_leave_balance_success(self, mock_filter):
        mock_leave = MagicMock()
        mock_leave.balance = 10
        mock_filter.return_value.first.return_value = mock_leave
        response = self.client.get(reverse('get_leave_balance', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'leave_balance': 10})

    @patch('app.models.Leave.objects.filter')
    def test_get_leave_balance_no_data(self, mock_filter):
        mock_filter.return_value.first.return_value = None
        response = self.client.get(reverse('get_leave_balance', args=[2]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'leave_balance': 0})

    @patch('app.models.Activity.objects.filter')
    def test_get_recent_activities_success(self, mock_filter):
        mock_filter.return_value.order_by.return_value[:5] = MagicMock()
        mock_filter.return_value.order_by.return_value[:5].values.return_value = [{'activity': 'Meeting', 'date': '2023-10-01'}]
        response = self.client.get(reverse('get_recent_activities', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'recent_activities': [{'activity': 'Meeting', 'date': '2023-10-01'}]})

    @patch('app.models.Activity.objects.filter')
    def test_get_recent_activities_no_data(self, mock_filter):
        mock_filter.return_value.order_by.return_value[:5] = MagicMock()
        mock_filter.return_value.order_by.return_value[:5].values.return_value = []
        response = self.client.get(reverse('get_recent_activities', args=[2]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'recent_activities': []})