from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch, MagicMock
from .models import LeaveRequest, Attendance

class TeamServiceTests(TestCase):
    def setUp(self):
        self.manager_id = 1
        self.employee_ids = [1, 2]
        self.leave_request = LeaveRequest.objects.create(id=1, status='Pending', employee_id=1)
        self.attendance_record = Attendance.objects.create(employee_id=1)

    @patch('app.services.get_employee_ids_by_manager')
    def test_get_team_attendance(self, mock_get_employee_ids):
        mock_get_employee_ids.return_value = self.employee_ids
        attendance = get_team_attendance(self.manager_id)
        self.assertEqual(len(attendance), 1)
        self.assertEqual(attendance[0].employee_id, 1)

    @patch('app.services.get_employee_ids_by_manager')
    def test_get_team_leave_requests(self, mock_get_employee_ids):
        mock_get_employee_ids.return_value = self.employee_ids
        leave_requests = get_team_leave_requests(self.manager_id)
        self.assertEqual(len(leave_requests), 1)
        self.assertEqual(leave_requests[0].status, 'Pending')

    @patch('app.services.get_object_or_404')
    def test_approve_leave_request_success(self, mock_get_object_or_404):
        mock_get_object_or_404.return_value = self.leave_request
        response = approve_leave_request(self.manager_id, self.leave_request.id)
        self.assertEqual(response['status'], 'Leave request approved')
        self.leave_request.refresh_from_db()
        self.assertEqual(self.leave_request.status, 'Approved')

    @patch('app.services.get_object_or_404')
    def test_approve_leave_request_failure(self, mock_get_object_or_404):
        mock_get_object_or_404.return_value = LeaveRequest(id=2, status='Denied')
        response = approve_leave_request(self.manager_id, 2)
        self.assertEqual(response[0]['status'], 'Leave request cannot be approved')
        self.assertEqual(response[1], 400)

    @patch('app.services.get_object_or_404')
    def test_deny_leave_request_success(self, mock_get_object_or_404):
        mock_get_object_or_404.return_value = self.leave_request
        response = deny_leave_request(self.manager_id, self.leave_request.id)
        self.assertEqual(response['status'], 'Leave request denied')
        self.leave_request.refresh_from_db()
        self.assertEqual(self.leave_request.status, 'Denied')

    @patch('app.services.get_object_or_404')
    def test_deny_leave_request_failure(self, mock_get_object_or_404):
        mock_get_object_or_404.return_value = LeaveRequest(id=2, status='Approved')
        response = deny_leave_request(self.manager_id, 2)
        self.assertEqual(response[0]['status'], 'Leave request cannot be denied')
        self.assertEqual(response[1], 400)