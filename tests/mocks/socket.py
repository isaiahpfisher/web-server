class MockSocket:
    def __init__(self, request_data=None):
        self.request_data = request_data
        
    def recv(self, size):
        return self.request_data
    
    def sendall(self, response_data):
        self.response_data = response_data
    
    def close(self):
        pass