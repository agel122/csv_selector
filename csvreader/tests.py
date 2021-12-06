from rest_framework.test import APITestCase
from rest_framework import status
from django.test.utils import override_settings
from .tasks import adding_task


class AddTestCase(APITestCase):
    @override_settings(CELERY_TASK_ALWAYS_EAGER=True, CELERY_TASK_EAGER_PROPOGATES=True)
    def testNoError(self):
        """Test that the ``adding_task`` task runs with no errors,
        and returns the correct result."""
        result = adding_task.delay(8, 8)

        assert result.successful() == True
        assert result.get() == 16

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True, CELERY_TASK_EAGER_PROPOGATES=True)
    def testAddData(self):
        data = {'filename': 'data.csv'}
        response = self.client.post('/api/start', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["filename"], "data.csv")
        self.assertEqual(response.data["status"], "in_work")

    # @override_settings(CELERY_TASK_ALWAYS_EAGER=True, CELERY_TASK_EAGER_PROPOGATES=True)
    def testCountInWork(self):
        data = {'filename': 'data.csv'}
        self.client.post('/api/start', data)
        response = self.client.get('/api/ongoing')
        self.assertEqual(response.json(), {"tasks in work": 1})

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True, CELERY_TASK_EAGER_PROPOGATES=True)
    def testFinalResult(self):
        data = {'filename': 'data.csv'}
        self.client.post('/api/start', data)
        response1 = self.client.get('/api/getresult?filename=data')
        response2 = self.client.get('/api/ongoing')
        self.assertEqual(response1.data["filename"], "data.csv")
        self.assertEqual(response1.data["status"], "done")
        self.assertEqual(response1.data["dataresult"], '89.2416354295115000')
        self.assertEqual(response2.json(), {"tasks in work": 0})











