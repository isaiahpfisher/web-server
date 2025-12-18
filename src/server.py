import socket
import threading
from src.request import Request
from src.response import Response
from src.router import Router
from exceptions.empty_request import EmptyRequestException
from exceptions.not_found import NotFoundException
from exceptions.forbidden import ForbiddenException

class WebServer:
    def __init__(self, host='localhost', port=3000):
        self.host = host
        self.port = port
        self.app = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.app.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        self.app.bind((self.host, self.port))
        self.app.listen()
        print(f"Listening on http://{self.host}:{self.port}...")
        
        while True:
            connection, address = self.app.accept()
            thread = threading.Thread(target=self.handle_client, args=(connection, address))
            thread.start()

    def handle_client(self, connection, address):
        with connection:
            try:
                request = Request(connection)
                body, mime_type = Router.resolve(request.path)
                response = Response(request, 200, {"Content-Type": mime_type}, body)
                response.send()
                
            except EmptyRequestException:
                print(f"Ignored empty request from {address}")
            except (NotFoundException, ForbiddenException) as e:
                body = f"<h1>{e.message}</h1>"
                Response(request, e.code, {"Content-Type": "text/html"}, body.encode()).send()
            except Exception as e:
                print(f"Internal Server Error: {e}")