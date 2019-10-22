import json

from django.test import TestCase
from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APIClient

class TestLoginView(TestCase):

    fixtures = ['myapp/fixtures/dumpdata.json']

    def login(self):
        client = Client()
        login_path = '/o/token/'
        login_data = {
            'username': 'dilipen',
            'password': '123456',
            'grant_type': 'password',
            'client_id': 'VOWDKbkTSoO1VvmzkzdlVknzEygii7Ch7XMTKtMW'
        }
        init_response = client.post(login_path, login_data)
        token_data = init_response.content
        byte_json = token_data.decode('utf8').replace("'", '"')
        json_data = json.loads(byte_json)
        # print(json_data)
        access_token = json_data.get('access_token')
        return access_token

    def test_create_corporate(self):
        access_token = self.login()
        client = Client()
        if access_token is not None:
            headers = {'HTTP_AUTHORIZATION': 'Bearer ' + access_token}
            path = '/companies'
            data = {
                "name": "Chennai Dell",
            }
            response = client.post(path, data, **headers)
            process_data = response.content.decode('utf8').replace("'", '"')
            # print(process_data)
            json_data = json.loads(process_data)
            corporate_id = json_data.get("id")
            self.assertEquals(response.status_code, 201)
            return corporate_id
