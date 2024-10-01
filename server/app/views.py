from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import Attendance, LeaveBalance, RecentActivity, LeaveRequest, Employee
from .services.report_service import ReportService
from .services.notification_service import fetch_notifications, mark_notification_as_read
from datetime import datetime


def get_notifications(request, employee_id):
    notifications = fetch_notifications(employee_id)
    return JsonResponse(list(notifications.values()), safe=False)


def mark_notification_read(request, employee_id, notification_id):
    if request.method == 'POST':
        success = mark_notification_as_read(notification_id)
        if success:
            return JsonResponse({'status': 'Notification marked as read'})
        return JsonResponse({'error': 'Notification not found'}, status=404)

# Existing functions... (No changes to this part)

def get_attendance(request, employee_id):
    attendance_data = Attendance.objects.filter(employee_id=employee_id)
    return JsonResponse(list(attendance_data.values()), safe=False)


def get_leave_balance(request, employee_id):
    leave_balance = LeaveBalance.objects.filter(employee_id=employee_id).first()
    return JsonResponse({'leave_balance': leave_balance.balance})


def get_recent_activities(request, employee_id):
    recent_activities = RecentActivity.objects.filter(employee_id=employee_id).order_by('-timestamp')[:5]
    return JsonResponse(list(recent_activities.values()), safe=False)


def request_leave(request, employee_id):
    if request.method == 'POST':
        # Assume some logic to handle leave request
        return JsonResponse({'status': 'Leave request submitted'}), 201
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def get_team_attendance(request, manager_id):
    team_attendance = Attendance.objects.filter(employee__manager_id=manager_id)
    return JsonResponse(list(team_attendance.values()), safe=False)


def get_team_leave_requests(request, manager_id):
    team_leave_requests = LeaveRequest.objects.filter(employee__manager_id=manager_id)
    return JsonResponse(list(team_leave_requests.values()), safe=False)


def approve_leave_request(request, manager_id, request_id):
    leave_request = LeaveRequest.objects.get(id=request_id)
    leave_request.status = 'Approved'
    leave_request.save()
    return JsonResponse({'status': 'Leave request approved'})


def deny_leave_request(request, manager_id, request_id):
    leave_request = LeaveRequest.objects.get(id=request_id)
    leave_request.status = 'Denied'
    leave_request.save()
    return JsonResponse({'status': 'Leave request denied'})


def get_organization_directory(request):
    employees = Employee.objects.all()
    return JsonResponse(list(employees.values()), safe=False)


def get_organization_structure(request):
    employees = Employee.objects.all()
    structure = []
    for employee in employees:
        structure.append({'id': employee.id, 'name': employee.name, 'manager_id': employee.manager_id})
    return JsonResponse(structure, safe=False)


def get_employee_profile(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
        return JsonResponse({'employee_id': employee.employee_id, 'name': employee.name})
    except Employee.DoesNotExist:
        return JsonResponse({'error': 'Employee not found'}, status=404)


def update_employee_profile(request, employee_id):
    if request.method == 'PUT':
        try:
            employee = Employee.objects.get(id=employee_id)
            data = json.loads(request.body)
            employee.name = data.get('name', employee.name)
            employee.save()
            return JsonResponse({'status': 'Profile updated successfully'})
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def generate_attendance_report(request, manager_id):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        attendance_report = ReportService.get_attendance_report(manager_id, start_date, end_date)
        return JsonResponse(attendance_report, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)