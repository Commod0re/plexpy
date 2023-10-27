import unittest
from src.plexsdk.models.GetButlerTasksResponse import GetButlerTasksResponse


class TestGetButlerTasksResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_butler_tasks_response(self):
        # Create GetButlerTasksResponse class instance
        test_model = GetButlerTasksResponse(ButlerTasks={"accusantium": 1})
        self.assertEqual(test_model.ButlerTasks, {"accusantium": 1})


if __name__ == "__main__":
    unittest.main()
