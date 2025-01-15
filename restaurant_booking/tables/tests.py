from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from tables.models import Table

# Create your tests here.

class TableTests(APITestCase):
    def setUp(self):
        # Superuser ke config
        self.admin_user = User.objects.create_superuser(
            username='consultadd', password='consultadd', email='')
        self.token = Token.objects.create(user=self.admin_user)
        self.table_data = {
        'name': 'Table 1',
        'capacity': 4,
        'is-available': True
        }

    def test_view_all_tables(self):
        # Authenticate admin by token
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Dummy table
        Table.objects.create(**self.table_data)

        response = self.client.get('/admin/tables/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 

    def test_add_new_table(self):

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Send POST request to add a new table
        response = self.client.post('/admin/tables/', self.table_data, format='json')

        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Table 1')

    def test_update_table(self):
       
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create table to update
        table = Table.objects.create(**self.table_data)
        updated_data = {
            'name': 'Updated Table',
            'seats': 6,
            'status': 'Reserved'
        }

        response = self.client.put(f'/admin/tables/{table.id}/', updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Table')

    def test_delete_table(self):
        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create a table to delete
        table = Table.objects.create(**self.table_data)

        response = self.client.delete(f'/admin/tables/{table.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthorized_access(self):
        
        response = self.client.get('/admin/tables/')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)