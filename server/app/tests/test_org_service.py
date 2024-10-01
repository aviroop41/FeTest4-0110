from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch, MagicMock
from .models import Employee

class OrgServiceTests(TestCase):
    @patch('app.models.Employee.objects.all')
    def test_get_organization_directory_success(self, mock_all):
        mock_all.return_value = [Employee(id=1, name='John Doe'), Employee(id=2, name='Jane Smith')]
        response = self.client.get(reverse('get_organization_directory'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    @patch('app.models.Employee.objects.all')
    def test_get_organization_directory_empty(self, mock_all):
        mock_all.return_value = []
        response = self.client.get(reverse('get_organization_directory'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    @patch('app.models.Employee.objects.select_related')
    def test_get_organization_structure_success(self, mock_select_related):
        employee1 = MagicMock(id=1, name='John Doe', manager=None)
        employee2 = MagicMock(id=2, name='Jane Smith', manager=None)
        mock_select_related.return_value = [employee1, employee2]
        response = self.client.get(reverse('get_organization_structure'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]['name'], 'John Doe')

    @patch('app.models.Employee.objects.select_related')
    def test_get_organization_structure_empty(self, mock_select_related):
        mock_select_related.return_value = []
        response = self.client.get(reverse('get_organization_structure'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    @patch('app.models.Employee.objects.select_related')
    def test_get_organization_structure_with_manager(self, mock_select_related):
        manager = MagicMock(id=3, name='Manager A')
        employee = MagicMock(id=1, name='Employee A', manager=manager)
        mock_select_related.return_value = [employee]
        response = self.client.get(reverse('get_organization_structure'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['manager_id'], 3)

    @patch('app.models.Employee.objects.all')
    def test_get_organization_directory_failure(self, mock_all):
        mock_all.side_effect = Exception('Database error')
        response = self.client.get(reverse('get_organization_directory'))
        self.assertEqual(response.status_code, 500)

    @patch('app.models.Employee.objects.select_related')
    def test_get_organization_structure_failure(self, mock_select_related):
        mock_select_related.side_effect = Exception('Database error')
        response = self.client.get(reverse('get_organization_structure'))
        self.assertEqual(response.status_code, 500)