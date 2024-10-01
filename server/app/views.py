from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import Attendance, LeaveBalance, RecentActivity


def get_attendance(request, employee_id):
    attendance_data = Attendance.objects.filter(employee_id=employee_id)
    return JsonResponse(list(attendance_data.values()), safe=False)


def get_leave_balance(request, employee_id):
    leave_balance = LeaveBalance.objects.filter(employee_id=employee_id).first()
    return JsonResponse({'leave_balance': leave_balance.balance})


def get_recent_activities(request, employee_id):
    recent_activities = Activity.objects.filter(employee_id=employee_id).order_by('-date')[:5]
    return JsonResponse(list(recent_activities.values()), safe=False)


def request_leave(request, employee_id):
    if request.method == 'POST':
        # Assume some logic to handle leave request
        return JsonResponse({'status': 'Leave request submitted'}), 201
    return JsonResponse({'error': 'Invalid request method'}, status=400)
