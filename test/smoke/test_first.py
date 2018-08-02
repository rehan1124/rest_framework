import unittest, pytest, requests
from lib.resources.resources import *
from lib.parameters.parameters import *


class TestRest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("****Test is started****\n")

    @classmethod
    def tearDownClass(cls):
        print("\n****Test is over****")

    @pytest.mark.first
    def test_get_user(self):

        self.get_user_resp = requests.request('GET', api_url + get_single_user)

        assert self.get_user_resp.status_code == 200
        self.assertTrue(b"Janet" in self.get_user_resp.content)
        self.assertTrue(b"Weaver" in self.get_user_resp.content)

    @pytest.mark.second
    def test_user_not_found(self):

        self.user_not_found = requests.request('GET', api_url + get_user_not_found)

        assert self.user_not_found.status_code == 404

    @pytest.mark.third
    def test_single_resource(self):

        self.single_resource = requests.request('GET', api_url + get_single_resource)

        assert self.single_resource.status_code == 200
        self.assertTrue(b"fuchsia rose" in self.single_resource.content)

    @pytest.mark.fourth
    def test_create_user(self):

        self.create_user_response = requests.request('POST', api_url + post_create_user, data=create_user)

        assert self.create_user_response.status_code == 201
        self.assertTrue(b"morpheus" in self.create_user_response.content)
        self.assertTrue(b"leader" in self.create_user_response.content)

    @pytest.mark.fifth
    def test_update_user(self):

        self.update_user_response = requests.request('PUT', api_url + put_update_user, data=update_user)

        assert self.update_user_response.status_code == 200
        self.assertTrue(b"morpheus" in self.update_user_response.content)
        self.assertTrue(b"zion resident" in self.update_user_response.content)

    @pytest.mark.last
    def test_delete_user(self):

        self.delete_user_response = requests.request('DELETE', api_url + delete_user)

        assert self.delete_user_response.status_code == 204
