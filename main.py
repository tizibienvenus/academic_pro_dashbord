from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class SPARequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path != '/' and not os.path.exists(self.translate_path(self.path)):
            self.path = '/index.html'
        return super().do_GET()

if __name__ == '__main__':
    PORT = 8000
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, SPARequestHandler)
    print(f"Serving on port {PORT}")
    httpd.serve_forever()

