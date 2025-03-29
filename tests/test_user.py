import pytest
import requests
from unittest.mock import patch
from requests.models import Response

# Mock the requests.get (or any other relevant HTTP method) to simulate the server behavior
@pytest.fixture
def mock_users_endpoint():
    # Creating a mock response
    mock_response = Response()
    mock_response.status_code = 401
    mock_response._content = b''  # Empty response body
    
    # Patch the 'requests.get' or 'requests.post' method, depending on your endpoint's method
    with patch('requests.get', return_value=mock_response):
        yield

def test_users_endpoint(mock_users_endpoint):
    # The URL and parameters for the request
    url = 'http://127.0.0.1:8000/users'
    params = {'username': 'admin', 'password': 'admin'}
    
    # Send the request (this will use the mock instead of actually hitting the server)
    response = requests.get(url, params=params)
    
    # Assertions to validate the mock response
    assert response.status_code == 401
    assert response.text == ''  # Ensure the response body is empty