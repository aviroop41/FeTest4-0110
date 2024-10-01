from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch, MagicMock
from .models import Attendance, Leave, Activity, LeaveRequest

class AttendanceViewsTests(TestCase):

    @patch('app.models.Attendance.objects.filter')
    def test_get_attendance_success(self, mock_filter):
        mock_filter.return_value = MagicMock()
        mock_filter.return_value.values.return_value = [{'date': '2023-10-01', 'employee_id': 1}]
        response = self.client.get(reverse('get_attendance', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{'date': '2023-10-01', 'employee_id': 1}])

    @patch('app.models.Attendance.objects.filter')
    def test_get_attendance_empty(self, mock_filter):
        mock_filter.return_value = MagicMock()
        mock_filter.return_value.values.return_value = []
        response = self.client.get(reverse('get_attendance', args=[2]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

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
        self.assertEqual(response.json(), [{'activity': 'Meeting', 'date': '2023-10-01'}])

    @patch('app.models.Activity.objects.filter')
    def test_get_recent_activities_no_data(self, mock_filter):
        mock_filter.return_value.order_by.return_value[:5] = MagicMock()
        mock_filter.return_value.order_by.return_value[:5].values.return_value = []
        response = self.client.get(reverse('get_recent_activities', args=[2]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    @patch('app.models.Leave.objects.filter')
    def test_request_leave_success(self, mock_filter):
        mock_filter.return_value.first.return_value = None
        data = {'leave_type': 'sick', 'start_date': '2023-10-10', 'end_date': '2023-10-15'}
        response = self.client.post(reverse('request_leave', args=[1]), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'status': 'Leave request submitted'})

    @patch('app.models.Leave.objects.filter')
    def test_request_leave_invalid_method(self, mock_filter):
        response = self.client.get(reverse('request_leave', args=[1]))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'Invalid request method'})

    @patch('app.models.Leave.objects.filter')
    def test_request_leave_missing_fields(self, mock_filter):
        data = {'leave_type': 'sick'}  
        response = self.client.post(reverse('request_leave', args=[1]), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    @patch('app.models.Attendance.objects.filter')
    def test_get_team_attendance_success(self, mock_filter):
        mock_filter.return_value = MagicMock()
        mock_filter.return_value.values.return_value = [{'date': '2023-10-01', 'employee_id': 1}]
        response = self.client.get(reverse('get_team_attendance', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{'date': '2023-10-01', 'employee_id': 1}])

    @patch('app.models.Attendance.objects.filter')
    def test_get_team_attendance_empty(self, mock_filter):
        mock_filter.return_value = MagicMock()
        mock_filter.return_value.values.return_value = []
        response = self.client.get(reverse('get_team_attendance', args=[2]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    @patch('app.models.LeaveRequest.objects.filter')
    def test_get_team_leave_requests_success(self, mock_filter):
        mock_filter.return_value = MagicMock()
        mock_filter.return_value.values.return_value = [{'id': 1, 'employee_id': 1}]
        response = self.client.get(reverse('get_team_leave_requests', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{'id': 1, 'employee_id': 1}])

    @patch('app.models.LeaveRequest.objects.filter')
    def test_get_team_leave_requests_empty(self, mock_filter):
        mock_filter.return_value = MagicMock()
        mock_filter.return_value.values.return_value = []
        response = self.client.get(reverse('get_team_leave_requests', args=[2]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    @patch('app.models.LeaveRequest.objects.get')
    def test_approve_leave_request_success(self, mock_get):
        mock_leave_request = MagicMock()
        mock_leave_request.status = 'Pending'
        mock_get.return_value = mock_leave_request
        response = self.client.post(reverse('approve_leave_request', args=[1, 1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'Leave request approved'})

    @patch('app.models.LeaveRequest.objects.get')
    def test_approve_leave_request_not_found(self, mock_get):
        mock_get.side_effect = LeaveRequest.DoesNotExist
        response = self.client.post(reverse('approve_leave_request', args=[1, 999]))
        self.assertEqual(response.status_code, 404)

    @patch('app.models.LeaveRequest.objects.get')
    def test_deny_leave_request_success(self, mock_get):
        mock_leave_request = MagicMock()
        mock_get.return_value = mock_leave_request
        response = self.client.post(reverse('deny_leave_request', args=[1, 1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'Leave request denied'})

    @patch('app.models.LeaveRequest.objects.get')
    def test_deny_leave_request_not_found(self, mock_get):
        mock_get.side_effect = LeaveRequest.DoesNotExist
        response = self.client.post(reverse('deny_leave_request', args=[1, 999]))
        self.assertEqual(response.status_code, 404)