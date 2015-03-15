import sys
import requests

response = requests.get("http://localhost:5000")
print response.content
