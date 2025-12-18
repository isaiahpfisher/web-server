import unittest
from mocks.socket import MockSocket
from src.response import Response
from mocks.socket import MockSocket

class MockRequest:
    def __init__(self):
        self.version = "HTTP/1.1"
        self.connection = MockSocket()

class RequestResponse(unittest.TestCase):
    def test_send_html(self):
       request = MockRequest()
       body = "<h1>Test</h1>"
       response = Response(request, 200, {"Content-Type": "text/html"}, body)
       
       response.send()
       sent_data = request.connection.response_data
       
       self.assertIsInstance(sent_data, bytes)
       self.assertIn(b"HTTP/1.1 200 OK", sent_data)
       
       self.assertIn(b"\r\n\r\n", sent_data)
       self.assertIn(b"<h1>Test</h1>", sent_data)
       
       expected_len = str(len(body)).encode()
       self.assertIn(b"Content-Length: " + expected_len, sent_data)
       
    def test_404_response(self):
       request = MockRequest()
       body = "<h1>Test</h1>"
       response = Response(request, 404, {"Content-Type": "text/html"}, body)
       
       response.send()
       sent_data = request.connection.response_data
       
       self.assertIn(b"HTTP/1.1 404 Not Found", sent_data)
       
    def test_500_response(self):
       request = MockRequest()
       body = "<h1>Test</h1>"
       response = Response(request, 500, {"Content-Type": "text/html"}, body)
       
       response.send()
       sent_data = request.connection.response_data
       
       self.assertIn(b"HTTP/1.1 500 Internal Server Error", sent_data)
            
if __name__ == '__main__':
    unittest.main()