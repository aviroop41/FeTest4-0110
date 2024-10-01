from django.utils import timezone
from .models import Attendance, Employee
import requests

# New function to link employee's calendar

def link_calendar(employee_id, calendar_token):
    try:
        employee = Employee.objects.get(id=employee_id)
        # Logic to save the calendar token with the employee record
        employee.calendar_token = calendar_token
        employee.save()
        return {'status': 'Calendar linked successfully.'}
    except Employee.DoesNotExist:
        return {'error': 'Employee not found.'}

# New function to fetch calendar events

def fetch_calendar_events(employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
        # Logic to retrieve events from the external calendar API
        # This is a mockup of the request; adapt it as needed for the specific calendar API
        headers = {'Authorization': f'Bearer {employee.calendar_token}'}
        response = requests.get('https://api.calendar.com/v1/events', headers=headers)
        events = response.json()

        attendance_records = []
        for event in events:
            if event['start']['dateTime'] 
            and timezone.make_aware(datetime.fromisoformat(event['start']['dateTime'])).date() == timezone.now().date():
                # Log attendance based on events
                attendance_records.append(Attendance(employee=employee, date=event['start']['dateTime'], status='Present'))

        Attendance.objects.bulk_create(attendance_records)
        return {'status': 'Attendance logged successfully from calendar events.'}
    except Employee.DoesNotExist:
        return {'error': 'Employee not found.'}
    except Exception as e:
        return {'error': str(e)}