from http.server import BaseHTTPRequestHandler
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split('?')[0]
        
        if path == '/api/python/deploy':
            response = {
                "status": "success",
                "message": "Python app deployment API",
                "versions": ["3.8", "3.9", "3.10"],
                "frameworks": ["Django", "Flask", "FastAPI"]
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
        elif path == '/api/python/websites':
            # Simulate getting websites list
            websites = [
                {"id": 1, "name": "My Django App", "url": "django-app.vercel.app", "status": "active"},
                {"id": 2, "name": "Flask API", "url": "flask-api.vercel.app", "status": "active"}
            ]
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"websites": websites}).encode())
            
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'''
                <html>
                <head><title>Python Hosting</title></head>
                <body>
                    <h1>Python Hosting API</h1>
                    <p>Endpoints:</p>
                    <ul>
                        <li><a href="/api/python/deploy">/api/python/deploy</a></li>
                        <li><a href="/api/python/websites">/api/python/websites</a></li>
                    </ul>
                </body>
                </html>
            ''')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        
        # Handle website deployment
        if self.path == '/api/python/deploy':
            website_name = data.get('name', 'Untitled')
            python_version = data.get('version', '3.9')
            
            response = {
                "status": "success",
                "message": f"Python website '{website_name}' deployed successfully!",
                "url": f"https://{website_name}-python.vercel.app",
                "version": python_version,
                "deployment_id": os.urandom(8).hex()
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
