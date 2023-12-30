from flask import Flask,request,jsonify
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

    event = json.loads(request.data)
    if event['comment']['body'] != '/jira':
        respone = jsonify({"message":"No JIRA ticket created based on this comment"})
        respone.status_code = 200
        return respone

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
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
    })

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    data = json.loads(response.text)
    data['message']='Created Jira ticket base on the current issue'
    response=jsonify(data)
    response.status_code = 201
    return response
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)