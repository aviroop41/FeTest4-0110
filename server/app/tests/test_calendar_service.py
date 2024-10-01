import unittest
from unittest.mock import patch, MagicMock
from app.services import link_calendar, fetch_calendar_events
from app.models import Employee, Attendance

class TestCalendarService(unittest.TestCase):

    @patch('app.models.Employee.objects.get')
    def test_link_calendar_success(self, mock_get):
        mock_employee = MagicMock()
        mock_employee.id = 1
        mock_employee.calendar_token = None
        mock_get.return_value = mock_employee

        response = link_calendar(1, 'test_token')
        self.assertEqual(response, {'status': 'Calendar linked successfully.'})
        mock_employee.save.assert_called_once()

    @patch('app.models.Employee.objects.get')
    def test_link_calendar_employee_not_found(self, mock_get):
        mock_get.side_effect = Employee.DoesNotExist

        response = link_calendar(99, 'test_token')
        self.assertEqual(response, {'error': 'Employee not found.'})

    @patch('app.models.Employee.objects.get')
    @patch('requests.get')
    def test_fetch_calendar_events_success(self, mock_requests_get, mock_get):
        mock_employee = MagicMock()
        mock_employee.id = 1
        mock_employee.calendar_token = 'test_token'
        mock_get.return_value = mock_employee

        mock_events = [{'start': {'dateTime': '2023-10-01T10:00:00'}}]
        mock_requests_get.return_value.json.return_value = mock_events

        with patch('app.models.Attendance.objects.bulk_create') as mock_bulk_create:
            response = fetch_calendar_events(1)
            self.assertEqual(response, {'status': 'Attendance logged successfully from calendar events.'})
            mock_bulk_create.assert_called_once()

    @patch('app.models.Employee.objects.get')
    @patch('requests.get')
    def test_fetch_calendar_events_employee_not_found(self, mock_requests_get, mock_get):
        mock_get.side_effect = Employee.DoesNotExist

        response = fetch_calendar_events(99)
        self.assertEqual(response, {'error': 'Employee not found.'})

    @patch('app.models.Employee.objects.get')
    @patch('requests.get')
    def test_fetch_calendar_events_general_exception(self, mock_requests_get, mock_get):
        mock_employee = MagicMock()
        mock_employee.id = 1
        mock_employee.calendar_token = 'test_token'
        mock_get.return_value = mock_employee

        mock_requests_get.side_effect = Exception('API error')

        response = fetch_calendar_events(1)
        self.assertEqual(response, {'error': 'API error'})

if __name__ == '__main__':
    unittest.main()