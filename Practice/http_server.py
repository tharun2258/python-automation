import psutil
import json
from http.server import BaseHTTPRequestHandler ,HTTPServer


class MetricsHandler(BaseHTTPRequestHandler):
    

    def do_GET(self):
        metrics = {
            "cpu_usage" : psutil.cpu_percent(),
            "mem_usage" : psutil.virtual_memory()._asdict(),
            "disk_usage" : psutil.disk_usage('/')._asdict(),

        }

        self.send_response(200)
        self.send_header('content-Type', 'application/json')
        self.end_headers()

        self.wfile.write(json.dumps(metrics).encode())


 # Function to run the HTTP server
def run_server():
     server_address = ('', 8000)  # Listen on all interfaces (localhost) and port 8000
     httpd = HTTPServer(server_address, MetricsHandler)  # Create the HTTP server
     print("Server running on port 8000...")
     httpd.serve_forever()  # Start the server to handle requests

    # Run the server when the script is executed
if __name__ == "__main__":
   run_server()
