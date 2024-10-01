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