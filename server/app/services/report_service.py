class ReportService:
    @staticmethod
    def generate_attendance_report(manager_id, start_date, end_date):
        from app.models import Attendance
        from django.db.models import Q
        attendance_records = Attendance.objects.filter(
            Q(employee__manager_id=manager_id) & 
            Q(date__range=[start_date, end_date])
        )
        return attendance_records

    @staticmethod
    def get_attendance_report(manager_id, start_date, end_date):
        records = ReportService.generate_attendance_report(manager_id, start_date, end_date)
        return list(records.values())