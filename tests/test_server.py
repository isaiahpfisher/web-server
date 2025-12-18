import unittest
from src.server import WebServer
from mocks.socket import MockSocket

class TestServer(unittest.TestCase):
    def test_handle_client_serves_file(self):
        server = WebServer()
        self.addCleanup(server.app.close)
        
        raw_request = (
            b"GET /about HTTP/1.1\r\n"
            b"Host: localhost:3000\r\n\r\n"
        )
        mock_connection = MockSocket(raw_request)
        
        server.handle_client(mock_connection, ("127.0.0.1", 12345))
        
        self.assertIn(b"HTTP/1.1 200 OK", mock_connection.response_data)
        self.assertIn(b"<h1>About</h1>", mock_connection.response_data)

    def test_handle_client_handles_404(self):
        server = WebServer()
        self.addCleanup(server.app.close)
        
        raw_request = b"GET /fake-page HTTP/1.1\r\nHost: localhost\r\n\r\n"
        mock_connection = MockSocket(raw_request)
        
        server.handle_client(mock_connection, ("127.0.0.1", 12345))
        
        self.assertIn(b"404 Not Found", mock_connection.response_data)

if __name__ == '__main__':
    unittest.main()