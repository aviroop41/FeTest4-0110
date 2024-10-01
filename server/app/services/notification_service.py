from django.db import models

# New model for Notifications
class Notification(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.employee.name}: {self.message}'


def create_notification(employee, message):
    notification = Notification(employee=employee, message=message)
    notification.save()


def fetch_notifications(employee_id):
    return Notification.objects.filter(employee_id=employee_id).order_by('-timestamp')


def mark_notification_as_read(notification_id):
    try:
        notification = Notification.objects.get(id=notification_id)
        notification.is_read = True
        notification.save()
        return True
    except Notification.DoesNotExist:
        return False