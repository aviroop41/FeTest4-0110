from django.urls import path
from . import views

urlpatterns = []

urlpatterns += [
    path('api/employee/<int:employee_id>/attendance-details', views.get_attendance),
    path('api/employee/<int:employee_id>/leave-balance', views.get_leave_balance),
    path('api/employee/<int:employee_id>/recent-activities', views.get_recent_activities),
    path('api/employee/<int:employee_id>/request-leave', views.request_leave),
    path('api/manager/<int:manager_id>/team-attendance', views.get_team_attendance),
    path('api/manager/<int:manager_id>/team-leave-requests', views.get_team_leave_requests),
    path('api/manager/<int:manager_id>/leave-requests/<int:request_id>/approve', views.approve_leave_request),
    path('api/manager/<int:manager_id>/leave-requests/<int:request_id>/deny', views.deny_leave_request),
]