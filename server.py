import http.server
import socketserver
import time

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
  def handle_one_request(self) -> None:
    return super().handle_one_request()

Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()