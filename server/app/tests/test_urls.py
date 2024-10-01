from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch

class UrlsTestCase(TestCase):
    def test_get_attendance_data(self):
        url = reverse('get_attendance_data', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_leave_balance(self):
        url = reverse('get_leave_balance', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_recent_activities(self):
        url = reverse('get_recent_activities', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    @patch('app.views.get_attendance_data')
    def test_get_attendance_data_invalid_employee_id(self, mock_get):
        mock_get.side_effect = Exception('Invalid Employee ID')
        url = reverse('get_attendance_data', args=[-1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)

    @patch('app.views.get_leave_balance')
    def test_get_leave_balance_invalid_employee_id(self, mock_get):
        mock_get.side_effect = Exception('Invalid Employee ID')
        url = reverse('get_leave_balance', args=[-1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)

    @patch('app.views.get_recent_activities')
    def test_get_recent_activities_invalid_employee_id(self, mock_get):
        mock_get.side_effect = Exception('Invalid Employee ID')
        url = reverse('get_recent_activities', args=[-1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)

    def test_get_attendance_data_nonexistent_employee(self):
        url = reverse('get_attendance_data', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_get_leave_balance_nonexistent_employee(self):
        url = reverse('get_leave_balance', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_get_recent_activities_nonexistent_employee(self):
        url = reverse('get_recent_activities', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    @patch('app.views.request_leave')
    def test_request_leave_invalid_employee_id(self, mock_request):
        mock_request.side_effect = Exception('Invalid Employee ID')
        url = reverse('request_leave', args=[-1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)

    @patch('app.views.request_leave')
    def test_request_leave_nonexistent_employee(self, mock_request):
        mock_request.side_effect = Exception('Invalid Employee ID')
        url = reverse('request_leave', args=[9999])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 404)
    
    def test_get_team_attendance(self):
        url = reverse('get_team_attendance', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_team_leave_requests(self):
        url = reverse('get_team_leave_requests', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_approve_leave_request(self):
        url = reverse('approve_leave_request', args=[1, 1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_deny_leave_request(self):
        url = reverse('deny_leave_request', args=[1, 1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    @patch('app.views.get_team_attendance')
    def test_get_team_attendance_invalid_manager_id(self, mock_get):
        mock_get.side_effect = Exception('Invalid Manager ID')
        url = reverse('get_team_attendance', args=[-1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)

    @patch('app.views.get_team_leave_requests')
    def test_get_team_leave_requests_invalid_manager_id(self, mock_get):
        mock_get.side_effect = Exception('Invalid Manager ID')
        url = reverse('get_team_leave_requests', args=[-1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)

    @patch('app.views.approve_leave_request')
    def test_approve_leave_request_invalid(self, mock_approve):
        mock_approve.side_effect = Exception('Invalid Leave Request')
        url = reverse('approve_leave_request', args=[1, -1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)

    @patch('app.views.deny_leave_request')
    def test_deny_leave_request_invalid(self, mock_deny):
        mock_deny.side_effect = Exception('Invalid Leave Request')
        url = reverse('deny_leave_request', args=[1, -1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)
    
    def test_get_organization_directory(self):
        url = reverse('get_organization_directory')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_organization_structure(self):
        url = reverse('get_organization_structure')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    @patch('app.views.get_organization_directory')
    def test_get_organization_directory_error(self, mock_get):
        mock_get.side_effect = Exception('Error occurred')
        url = reverse('get_organization_directory')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 500)

    @patch('app.views.get_organization_structure')
    def test_get_organization_structure_error(self, mock_get):
        mock_get.side_effect = Exception('Error occurred')
        url = reverse('get_organization_structure')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 500)