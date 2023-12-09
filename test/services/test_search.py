import unittest
import responses
from src.plexsdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.plexsdk.services.search import Search


class TestSearch_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_perform_search(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/hubs/search", json={}, status=200)
        # call the method to test
        test_service = Search("testkey")
        response = test_service.perform_search("minima", 1529679933, 4)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_perform_search_required_fields_missing(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/hubs/search", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Search("testkey")
            test_service.perform_search()
        responses.reset(),

    @responses.activate
    def test_perform_search_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/hubs/search", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Search("testkey")
            test_service.perform_search("ea", 9609551200, 8)
        responses.reset()

    @responses.activate
    def test_perform_voice_search(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/hubs/search/voice", json={}, status=200)
        # call the method to test
        test_service = Search("testkey")
        response = test_service.perform_voice_search("omnis", 3615660003, 4)
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_perform_voice_search_required_fields_missing(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/hubs/search/voice", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Search("testkey")
            test_service.perform_voice_search()
        responses.reset(),

    @responses.activate
    def test_perform_voice_search_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/hubs/search/voice", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Search("testkey")
            test_service.perform_voice_search("quia", 2836523631, 1)
        responses.reset()

    @responses.activate
    def test_get_search_results(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/search", json={}, status=200)
        # call the method to test
        test_service = Search("testkey")
        response = test_service.get_search_results("totam")
        self.assertEqual(response.data, {})
        responses.reset(),

    @responses.activate
    def test_get_search_results_required_fields_missing(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/search", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Search("testkey")
            test_service.get_search_results()
        responses.reset(),

    @responses.activate
    def test_get_search_results_error_on_non_200(self):
        # Mock the API response
        responses.get("http://10.10.10.47:32400/search", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Search("testkey")
            test_service.get_search_results("aperiam")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
