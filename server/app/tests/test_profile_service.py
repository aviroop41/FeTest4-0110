from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from .models import Employee


class EmployeeProfileServiceTests(TestCase):

    @patch('app.models.Employee')
    def test_update_employee_profile_success(self, mock_employee):
        mock_instance = mock_employee.return_value
        mock_instance.employee_id = 1

        response = update_employee_profile(1, {'name': 'John Doe'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'Profile updated successfully'})

    @patch('app.models.Employee')
    def test_update_employee_profile_employee_not_found(self, mock_employee):
        mock_employee.side_effect = Employee.DoesNotExist

        response = update_employee_profile(1, {'name': 'Jane Doe'})

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'error': 'Employee not found'})

    @patch('app.models.Employee')
    def test_update_employee_profile_general_error(self, mock_employee):
        mock_instance = mock_employee.return_value
        mock_instance.employee_id = 1
        mock_instance.save.side_effect = Exception('Database error')

        response = update_employee_profile(1, {'name': 'John Doe'})

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'Database error'})

    @patch('app.models.Employee')
    def test_get_employee_profile_success(self, mock_employee):
        mock_instance = mock_employee.return_value
        mock_instance.employee_id = 1
        mock_instance.name = 'John Doe'

        response = get_employee_profile(1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'employee_id': 1, 'name': 'John Doe'})

    @patch('app.models.Employee')
    def test_get_employee_profile_employee_not_found(self, mock_employee):
        mock_employee.side_effect = Employee.DoesNotExist

        response = get_employee_profile(1)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'error': 'Employee not found'})

    @patch('app.models.Employee')
    def test_get_employee_profile_general_error(self, mock_employee):
        mock_employee.side_effect = Exception('Database error')

        response = get_employee_profile(1)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {'error': 'Database error'})