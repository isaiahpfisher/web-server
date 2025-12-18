import socket
from src.request import Request
from src.response import Response
from src.router import Router
from exceptions.empty_request import EmptyRequestException
from exceptions.not_found import NotFoundException
from exceptions.forbidden import ForbiddenException

# constants
HOST = 'localhost'
PORT = 3000

# one-time setup
app = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
app.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
app.bind((HOST, PORT))
app.listen()

print(f"Listening on http://{HOST}:{PORT}...")

# main loop
while True:
  connection, address = app.accept()

  with connection:
      try:
        request = Request(connection)
        body, mime_type = Router.resolve(request.path)
        response = Response(request, 200, {"Content-Type": mime_type}, body)
        response.send()
        
      except EmptyRequestException as e:
          print(f"Ignored empty request from {address}")
          continue
      except (NotFoundException, ForbiddenException) as e:
          body = f"<h1>{e.message}</h1>"
          Response(request, e.code, {"Content-Type": "text/html"}, body.encode()).send()