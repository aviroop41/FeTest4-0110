from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import Attendance, LeaveBalance, RecentActivity, LeaveRequest, Employee, EmployeeProfile
from .services.report_service import ReportService
from .services.notification_service import fetch_notifications, mark_notification_as_read
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_roles(request):
    # logic to fetch roles goes here
    roles = []  # Replace with logic to fetch roles from the database
    return JsonResponse(roles, safe=False)

@api_view(['POST'])
def create_role(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Logic to create a new role goes here
        return JsonResponse({'status': 'Role created successfully'}, status=201)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@api_view(['PUT'])
def update_role_permissions(request, role_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        # Logic to update role permissions goes here
        return JsonResponse({'status': 'Permissions updated successfully'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@api_view(['DELETE'])
def delete_role(request, role_id):
    if request.method == 'DELETE':
        # Logic to delete the role goes here
        return JsonResponse({'status': 'Role deleted successfully'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

# Existing functions... (No changes to this part)

def get_notifications(request, employee_id):
    notifications = fetch_notifications(employee_id)
    return JsonResponse(list(notifications.values()), safe=False)


def mark_notification_read(request, employee_id, notification_id):
    if request.method == 'POST':
        success = mark_notification_as_read(notification_id)
        if success:
            return JsonResponse({'status': 'Notification marked as read'})
        return JsonResponse({'error': 'Notification not found'}, status=404)

# Existing functions continue... (Unchanged)
