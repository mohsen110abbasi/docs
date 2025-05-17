from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
from urllib.parse import urlencode
from urllib.parse import urlparse

import json

class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        Kavenegar_API_KEY = "{API-KEY}"

        # مسیر URL را بررسی می‌کنیم
        parsed_path = urlparse(self.path).path
        # تعیین شماره تلفن بر اساس مسیر
        if parsed_path == '/critical':
            receptor = '09991111111'
        elif parsed_path == '/warning':
            receptor = '09999999999'
        else:
            receptor = '09999999999'   # پیش‌فرض

        # Handle POST requests
        # Set the response code and headers
        # Parse the POST request data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data_str = post_data.decode('utf-8')

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        try:
                data = json.loads(post_data_str)
                # Extract the 'key' and 'recipients' values from the JSON data
                for alert in data['alerts']:
                        alertname = alert.get("labels", {}).get("alertname")
                        description = alert.get("annotations", {}).get("description")
                        # print(f"Alert Name: {alertname}")
                        # print(f"Description: {description}")
                        message = f"Alert Name: {alertname} \n Description: {description}"
                        print(f"Message: {message}")
                        data = {'receptor': receptor, 'message': message}
                        response = requests.post(f"https://api.kavenegar.com/v1/{Kavenegar_API_KEY}/sms/send.json", data=data)

        except Exception as e:
                print("Error processing request:", e)

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8088):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
