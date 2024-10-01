import unittest
from unittest.mock import patch, MagicMock
from app.models import Attendance
from app.services.report_service import ReportService

class TestReportService(unittest.TestCase):

    @patch('app.models.Attendance')
    def test_generate_attendance_report_success(self, mock_attendance):
        mock_attendance.objects.filter.return_value = [MagicMock(), MagicMock()]
        result = ReportService.generate_attendance_report(1, '2022-01-01', '2022-01-31')
        self.assertEqual(len(result), 2)
        mock_attendance.objects.filter.assert_called_once()

    @patch('app.models.Attendance')
    def test_generate_attendance_report_no_records(self, mock_attendance):
        mock_attendance.objects.filter.return_value = []
        result = ReportService.generate_attendance_report(1, '2022-01-01', '2022-01-31')
        self.assertEqual(len(result), 0)
        mock_attendance.objects.filter.assert_called_once()

    @patch('app.models.Attendance')
    def test_generate_attendance_report_invalid_dates(self, mock_attendance):
        with self.assertRaises(ValueError):
            ReportService.generate_attendance_report(1, None, '2022-01-31')

    @patch('app.models.Attendance')
    def test_get_attendance_report_success(self, mock_attendance):
        mock_attendance.objects.filter.return_value = [MagicMock(), MagicMock()]
        result = ReportService.get_attendance_report(1, '2022-01-01', '2022-01-31')
        self.assertEqual(len(result), 2)
        mock_attendance.objects.filter.assert_called_once()

    @patch('app.models.Attendance')
    def test_get_attendance_report_no_records(self, mock_attendance):
        mock_attendance.objects.filter.return_value = []
        result = ReportService.get_attendance_report(1, '2022-01-01', '2022-01-31')
        self.assertEqual(len(result), 0)
        mock_attendance.objects.filter.assert_called_once()

    @patch('app.models.Attendance')
    def test_get_attendance_report_invalid_dates(self, mock_attendance):
        with self.assertRaises(ValueError):
            ReportService.get_attendance_report(1, None, '2022-01-31')

if __name__ == '__main__':
    unittest.main()