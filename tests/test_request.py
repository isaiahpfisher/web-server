import unittest
from mocks.socket import MockSocket
from src.request import Request
from exceptions.empty_request import EmptyRequestException

class RequestTest(unittest.TestCase):
    def test_valid_get_request(self):
        raw_request = (
            b"GET /hello HTTP/1.1\r\n"
            b"Host: localhost:3000\r\n"
            b"User-Agent: TestRunner\r\n"
            b"\r\n"
        )
        
        connection = MockSocket(raw_request)
        request = Request(connection)
        
        self.assertEqual(request.method, "GET")
        self.assertEqual(request.path, "/hello")
        self.assertEqual(request.version, "HTTP/1.1")
        self.assertEqual(request.header("Host"), "localhost:3000")
        self.assertEqual(request.header("User-Agent"), "TestRunner")
    
    def test_valid_post_request(self):
        raw_request = (
            b"POST /hello HTTP/1.1\r\n"
            b"Host: localhost:3000\r\n"
            b"User-Agent: TestRunner\r\n"
            b"\r\n"
        )
        
        connection = MockSocket(raw_request)
        request = Request(connection)
        
        self.assertEqual(request.method, "POST")
        self.assertEqual(request.path, "/hello")
        self.assertEqual(request.version, "HTTP/1.1")
        self.assertEqual(request.header("Host"), "localhost:3000")
        self.assertEqual(request.header("User-Agent"), "TestRunner")
        
    def test_empty_request(self):
        raw_request = b""
        connection = MockSocket(raw_request)
        with self.assertRaises(EmptyRequestException) as context:
            Request(connection)
            
if __name__ == '__main__':
    unittest.main()