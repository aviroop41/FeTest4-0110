from django.test import TestCase
from app.models import Role
from app.services import RoleService
from unittest.mock import patch, MagicMock

class RoleServiceTestCase(TestCase):
    @patch('app.models.Role')
    def test_get_all_roles(self, mock_role):
        mock_role.objects.all.return_value.values.return_value = [{"id": 1, "name": "Admin", "permissions": []}]
        roles = RoleService.get_all_roles()
        self.assertEqual(len(roles), 1)
        self.assertEqual(roles[0]['name'], "Admin")

    @patch('app.models.Role')
    def test_create_role(self, mock_role):
        mock_role.objects.create.return_value.id = 1
        role_data = {"name": "User", "permissions": []}
        role_id = RoleService.create_role(role_data)
        self.assertEqual(role_id, 1)
        mock_role.objects.create.assert_called_once_with(**role_data)

    @patch('app.models.Role')
    def test_update_role_permissions(self, mock_role):
        mock_role.objects.get.return_value = MagicMock(id=1, permissions=[])  
        new_permissions = ["read", "write"]
        role_id = RoleService.update_role_permissions(1, new_permissions)
        self.assertEqual(role_id, 1)
        mock_role.objects.get.assert_called_once_with(id=1)
        mock_role.objects.get.return_value.save.assert_called_once()

    @patch('app.models.Role')
    def test_delete_role(self, mock_role):
        RoleService.delete_role(1)
        mock_role.objects.filter.assert_called_once_with(id=1)
        mock_role.objects.filter.return_value.delete.assert_called_once()

    @patch('app.models.Role')
    def test_get_role(self, mock_role):
        mock_role.objects.filter.return_value.values.return_value = [{"id": 1, "name": "User", "permissions": []}]
        role = RoleService.get_role(1)
        self.assertEqual(role['name'], "User")
        mock_role.objects.filter.assert_called_once_with(id=1)

    @patch('app.models.Role')
    def test_check_permission(self, mock_role):
        mock_role.objects.get.return_value = MagicMock(id=1, permissions=["read", "write"])
        has_permission = RoleService.check_permission(1, "read")
        self.assertTrue(has_permission)
        has_permission = RoleService.check_permission(1, "execute")
        self.assertFalse(has_permission)
        mock_role.objects.get.assert_called_once_with(id=1)