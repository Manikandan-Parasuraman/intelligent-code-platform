import urllib.request
import json

url = "http://localhost:8000/generate"
data = {
    "question": "Add a root health check endpoint to repo/resume-backend/main.py that returns status OK."
}
headers = {
    "x-api-key": "secure-key",
    "Content-Type": "application/json"
}

req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers)
try:
    with urllib.request.urlopen(req, timeout=300) as response:
        print(response.read().decode())
except Exception as e:
    print("Error: ",e)
