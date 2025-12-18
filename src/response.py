class Response:
    def __init__(self, request, status_code, headers, body):
        self.request = request
        self.status_code = status_code
        self.headers = headers
        self.body = body
        
    
    def send(self):
       self.request.connection.sendall(self._build().encode()) 
        
    def _build(self):
        response = []
        response.append(f"{self.request.version} {self.status_code} {self._get_status()}")
        for key, value in self.headers.items():
            response.append(f"{key}: {value}")
        response.append("")
        response.append(self.body)
        
        return "\r\n".join(response)
    
    def _get_status(self):
        if self.status_code == 200:
            return "OK"
        elif self.status_code == 404:
            return "Not Found"
        else:
            return "Internal Server Error"