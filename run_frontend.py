
import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "frontend"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Frontend Server running at http://localhost:{PORT}")
            print("Press Ctrl+C to stop")
            httpd.serve_forever()
    except OSError as e:
        print(f"Error starting server: {e}")
        print("Maybe port 8000 is occupied? Try closing other python processes.")
