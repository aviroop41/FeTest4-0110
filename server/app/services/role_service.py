from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.JSONField()

class RoleService:
    @staticmethod
    def get_all_roles():
        return Role.objects.all().values()

    @staticmethod
    def create_role(role_data):
        role = Role.objects.create(**role_data)
        return role.id

    @staticmethod
    def update_role_permissions(role_id, permissions):
        role = Role.objects.get(id=role_id)
        role.permissions = permissions
        role.save()
        return role.id

    @staticmethod
    def delete_role(role_id):
        Role.objects.filter(id=role_id).delete()

    @staticmethod
    def get_role(role_id):
        return Role.objects.filter(id=role_id).values().first()

    @staticmethod
    def check_permission(role_id, permission):
        role = Role.objects.get(id=role_id)
        return permission in role.permissions