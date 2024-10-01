from django.urls import path

urlpatterns = []

urlpatterns += [
    path('api/employee/<int:employee_id>/attendance', views.get_attendance_data),
    path('api/employee/<int:employee_id>/leave-balance', views.get_leave_balance),
    path('api/employee/<int:employee_id>/recent-activities', views.get_recent_activities),
]