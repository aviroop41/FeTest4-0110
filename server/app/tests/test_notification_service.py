from django.test import TestCase
from .models import Notification
from django.contrib.auth.models import User

class NotificationServiceTest(TestCase):
    def setUp(self):
        self.employee = User.objects.create(username='testuser')
        self.notification_message = 'This is a test notification.'
        self.notification = Notification.objects.create(employee=self.employee, message=self.notification_message)

    def test_create_notification(self):
        self.assertEqual(Notification.objects.count(), 1)
        self.assertEqual(self.notification.message, self.notification_message)

    def test_fetch_notifications(self):
        notifications = fetch_notifications(self.employee.id)
        self.assertEqual(notifications.count(), 1)
        self.assertEqual(notifications.first().message, self.notification_message)

    def test_mark_notification_as_read(self):
        result = mark_notification_as_read(self.notification.id)
        self.notification.refresh_from_db()
        self.assertTrue(result)
        self.assertTrue(self.notification.is_read)

    def test_mark_non_existent_notification_as_read(self):
        result = mark_notification_as_read(999)
        self.assertFalse(result)

    def test_create_notification_without_message(self):
        with self.assertRaises(ValueError):
            create_notification(self.employee, '')

    def test_fetch_notifications_for_non_existent_employee(self):
        notifications = fetch_notifications(999)
        self.assertEqual(notifications.count(), 0)
