from django.http import JsonResponse
from .models import Employee


def update_employee_profile(employee_id, new_data):
    try:
        employee = Employee.objects.get(employee_id=employee_id)
        if 'name' in new_data:
            employee.name = new_data['name']
        employee.save()
        return JsonResponse({'status': 'Profile updated successfully'}, status=200)
    except Employee.DoesNotExist:
        return JsonResponse({'error': 'Employee not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_employee_profile(employee_id):
    try:
        employee = Employee.objects.get(employee_id=employee_id)
        return JsonResponse({'employee_id': employee.employee_id, 'name': employee.name}, status=200)
    except Employee.DoesNotExist:
        return JsonResponse({'error': 'Employee not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)