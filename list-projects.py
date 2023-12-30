import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import json
# load environmental variables from .env file
load_dotenv()

url = f"https://{os.environ.get("ATLASSIAN_DOMAIN")}/rest/api/3/project"
api_token = os.environ.get("API_TOKEN")
auth = HTTPBasicAuth(os.environ.get("EMAIL"), api_token)

headers = {
	"Accept": "application/json"
}

response = requests.request(
   	"GET",
   	url,
   	headers=headers,
   	auth=auth
)

projects = json.loads(response.text)

for project in projects:
	print(project["name"])