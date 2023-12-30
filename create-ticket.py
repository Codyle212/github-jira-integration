import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import json

# load environmental variables from .env file
load_dotenv()

url = f"https://{os.environ.get("ATLASSIAN_DOMAIN")}/rest/api/3/issue"
api_token = os.environ.get("API_TOKEN")
auth = HTTPBasicAuth(os.environ.get("EMAIL"), api_token)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first Jira Ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10007"
    },
    "project": {
      "key": "GIC"
    },
    "summary": "First Jira Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))