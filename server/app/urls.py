from django.urls import path
from . import views

urlpatterns = []

urlpatterns += [
    path('api/employee/<int:employee_id>/attendance-details', views.get_attendance),
    path('api/employee/<int:employee_id>/leave-balance', views.get_leave_balance),
    path('api/employee/<int:employee_id>/recent-activities', views.get_recent_activities),
    path('api/employee/<int:employee_id>/request-leave', views.request_leave),
]