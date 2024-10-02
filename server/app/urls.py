from django.urls import path
from . import views

urlpatterns = []

urlpatterns += [
    path('api/employee/<int:employee_id>/attendance-details', views.get_attendance),
    path('api/employee/<int:employee_id>/leave-balance', views.get_leave_balance),
    path('api/employee/<int:employee_id>/recent-activities', views.get_recent_activities),
    path('api/employee/<int:employee_id>/request-leave', views.request_leave),
    path('api/employee/<int:employee_id>/notifications', views.get_notifications),
    path('api/employee/<int:employee_id>/notifications/<int:notification_id>/read', views.mark_notification_read),
    path('api/employee/<int:employee_id>/calendar/link', views.link_employee_calendar),
    path('api/employee/<int:employee_id>/calendar/events', views.get_calendar_events),
    path('api/manager/<int:manager_id>/team-attendance', views.get_team_attendance),
    path('api/manager/<int:manager_id>/team-leave-requests', views.get_team_leave_requests),
    path('api/manager/<int:manager_id>/leave-requests/<int:request_id>/approve', views.approve_leave_request),
    path('api/manager/<int:manager_id>/leave-requests/<int:request_id>/deny', views.deny_leave_request),
    path('api/organization/directory', views.get_organization_directory),
    path('api/organization/structure', views.get_organization_structure),
    path('api/employee/<int:employee_id>/profile', views.get_employee_profile),
    path('api/employee/<int:employee_id>/profile/update', views.update_employee_profile),
    path('api/manager/<int:manager_id>/attendance-reports', views.generate_attendance_report),
    path('api/hr/roles', views.get_roles),
    path('api/hr/roles/create', views.create_role),
    path('api/hr/roles/<int:role_id>/update', views.update_role_permissions),
    path('api/hr/roles/<int:role_id>/delete', views.delete_role),
]