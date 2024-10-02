from django.http import JsonResponse
from .models import Employee


def get_organization_directory(request):
    employees = Employee.objects.all()
    return JsonResponse(list(employees.values()), safe=False)


def get_organization_structure(request):
    # Assuming each employee has a manager field representing the hierarchical structure
    employees = Employee.objects.select_related('manager')
    structure = []
    for employee in employees:
        structure.append({
            'id': employee.id,
            'name': employee.name,
            'manager_id': employee.manager.id if employee.manager else None
        })
    return JsonResponse(structure, safe=False)