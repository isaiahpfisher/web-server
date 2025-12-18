import socket
from src.request import Request
from src.response import Response
from exceptions.empty_request import EmptyRequestException

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
        
        body = "<h1>Hello, World!</h1>"
        response = Response(request, 200, {"Content-Type": "text/html"}, body)
        response.send()
        
      except EmptyRequestException as e:
          print(e)
      
