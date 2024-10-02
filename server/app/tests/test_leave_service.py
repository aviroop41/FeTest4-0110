import unittest
from unittest.mock import patch, MagicMock

class LeaveServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.service = LeaveService()

    def test_leave_creation_success(self):
        data = {'employee_id': 1, 'leave_type': 'sick', 'start_date': '2023-10-01', 'end_date': '2023-10-03'}
        with patch('app.services.LeaveService.create_leave') as mock_create:
            mock_create.return_value = True
            response = self.service.create_leave(data)
            self.assertTrue(response)
            mock_create.assert_called_once_with(data)

    def test_leave_creation_missing_fields(self):
        data = {'employee_id': 1, 'leave_type': 'sick'}  # Missing start_date and end_date
        with self.assertRaises(ValueError):
            self.service.create_leave(data)

    def test_leave_status_success(self):
        with patch('app.services.LeaveService.get_leave_status') as mock_get:
            mock_get.return_value = 'approved'
            response = self.service.get_leave_status(1)
            self.assertEqual(response, 'approved')
            mock_get.assert_called_once_with(1)

    def test_leave_status_not_found(self):
        with patch('app.services.LeaveService.get_leave_status') as mock_get:
            mock_get.side_effect = LeaveNotFoundException
            with self.assertRaises(LeaveNotFoundException):
                self.service.get_leave_status(999)

    def test_leave_update_success(self):
        data = {'leave_id': 1, 'status': 'approved'}
        with patch('app.services.LeaveService.update_leave_status') as mock_update:
            mock_update.return_value = True
            response = self.service.update_leave_status(data)
            self.assertTrue(response)
            mock_update.assert_called_once_with(data)

    def test_leave_update_invalid_id(self):
        data = {'leave_id': 999, 'status': 'approved'}
        with patch('app.services.LeaveService.update_leave_status') as mock_update:
            mock_update.side_effect = LeaveNotFoundException
            with self.assertRaises(LeaveNotFoundException):
                self.service.update_leave_status(data)

if __name__ == '__main__':
    unittest.main()