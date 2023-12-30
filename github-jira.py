from flask import Flask
import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import json
#get environmental variables
load_dotenv()

url = f"https://{os.environ.get("ATLASSIAN_DOMAIN")}/rest/api/3/issue"
api_token = os.environ.get("API_TOKEN")
auth = HTTPBasicAuth(os.environ.get("EMAIL"), api_token)

#Create a flask app instance
app = Flask(__name__)
port = 5000 

@app.route("/createJIRA", methods=['POST'])
def create_jira():
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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)