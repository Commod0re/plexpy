import unittest
import responses
from src.plexsdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.plexsdk.services.hubs import Hubs


class TestHubs_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_global_hubs(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/hubs", json={}, status=200)
        # call the method to test
        test_service = Hubs("testkey")
        response = test_service.get_global_hubs(8, 6)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_global_hubs_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/hubs", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Hubs("testkey")
            test_service.get_global_hubs(7, 6)
        responses.reset()

    @responses.activate
    def test_get_library_hubs(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/hubs/sections/6213953233", json={}, status=200
        )
        # call the method to test
        test_service = Hubs("testkey")
        response = test_service.get_library_hubs(6213953233, 3, 6)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_library_hubs_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/hubs/sections/1940252847", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Hubs("testkey")
            test_service.get_library_hubs()
        responses.reset(),

    @responses.activate
    def test_get_library_hubs_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://10.10.10.47:32400/hubs/sections/4767149535", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Hubs("testkey")
            test_service.get_library_hubs(4767149535, 6, 1)
        responses.reset()


if __name__ == "__main__":
    unittest.main()
