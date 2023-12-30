# Github + Jira Integration with flask

## Create Virtual Enviroment and install dependencies

run `python -m venv venv`
use `venv\Scripts\Activate.ps` for Windows or `source venv/bin/activate` for mac/linux
use `pip install -r requirements.txt` to install all dependencies

## Configure Jira API

- generate api in account management -> security ->API, and added the generated API Key to ENV file
  ![Generate API Key](./generate-jira-api-key.png)
- use email associated with Jira Account and the Domain for Jira Software in ENV file
