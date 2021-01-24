from http.server import HTTPServer, SimpleHTTPRequestHandler

class LoggingHandler(SimpleHTTPRequestHandler):
  def do_GET(self):
    print(self.headers)
    super().do_GET()

print("Starting example server...")
server_object = HTTPServer(server_address=('', 8080), RequestHandlerClass=LoggingHandler)
server_object.serve_forever()
