import unittest
from unittest.mock import patch, MagicMock
from simulator import delete_pod

class TestSimulator(unittest.TestCase):
    @patch('simulator.client.CoreV1Api')
    @patch('simulator.config.load_kube_config')
    def test_delete_pod_success(self, mock_load_kube_config, mock_CoreV1Api):
        # Mock the delete_namespaced_pod method to always return True
        instance = mock_CoreV1Api.return_value
        instance.delete_namespaced_pod = MagicMock(return_value=True)

        # Call the delete_pod function with a test pod name and namespace
        result = delete_pod('test-pod', 'default')

        # Assert that the result is True, indicating the pod was "deleted" successfully
        self.assertTrue(result)
        
        # Ensure delete_namespaced_pod was called with correct parameters
        instance.delete_namespaced_pod.assert_called_with('test-pod', 'default', body=client.V1DeleteOptions())

    @patch('simulator.client.CoreV1Api')
    @patch('simulator.config.load_kube_config')
    def test_delete_pod_failure(self, mock_load_kube_config, mock_CoreV1Api):
        # Simulate an ApiException when trying to delete a pod
        instance = mock_CoreV1Api.return_value
        instance.delete_namespaced_pod = MagicMock(side_effect=client.exceptions.ApiException("Failed to delete pod"))

        # Call the delete_pod function with a test pod name and namespace
        result = delete_pod('test-pod', 'default')

        # Assert that the result is False, indicating the pod deletion failed
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
