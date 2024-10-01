from django.contrib.auth.models import User
from rest_framework import serializers

# Create your serializers here.

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class LeaveBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveBalance
        fields = '__all__'

class RecentActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'