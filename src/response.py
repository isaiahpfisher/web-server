class Response:
    def __init__(self, request, status_code, headers, body):
        self.request = request
        self.status_code = status_code
        self.headers = headers
        self.body = body
    
    def send(self):
        body_bytes = self.body.encode() if isinstance(self.body, str) else self.body
        header_lines = [f"{self.request.version} {self.status_code} {self._get_status()}"]
        
        for key, value in self.headers.items():
            header_lines.append(f"{key}: {value}")
        if "Content-Length" not in self.headers:
            header_lines.append(f"Content-Length: {len(body_bytes)}")
        
        header_lines.append("") 
        header_block = "\r\n".join(header_lines).encode()
        self.request.connection.sendall(header_block + b"\r\n" + body_bytes)

    def _get_status(self):
        STATUS_MAP = {
            200: "OK",
            404: "Not Found",
            500: "Internal Server Error",
        }
        return STATUS_MAP.get(self.status_code, "Unknown")