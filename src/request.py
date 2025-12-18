import socket
from exceptions.empty_request import EmptyRequestException

class Request:
    def __init__(self, connection: socket):
        self.connection = connection
        self.request = connection.recv(1024).decode()
        self._parse()
    
    def get_header(self, key):
        return self.headers.get(key.lower())
    
    def _parse(self):
        if not self.request:
            raise EmptyRequestException()
        
        lines = self.request.splitlines()
        method, path, version = lines[0].split()
        self.method = method
        self.path = path
        self.version = version
        
        self.headers = {}
        for line in lines[1:]:
            if line:
              key, value = line.split(":", 1)
              self.headers[key.lower()] = value.strip()