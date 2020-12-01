from flask import Flask, request, redirect
from settings import *
import asyncio
import requests
import json

app = Flask(__name__)
currentRepos = []

@app.route('/')
def home():
    return ""

@app.route("/api/v1/getrepositories")
def get_repos():
    if('auth_token' in request.headers):
        for token in api_keys:
            if(request.headers['auth_token'] == token):
                return json.dumps(currentRepos)
    else:
        return ""

async def GetGithubRepo():
    req = requests.get(f"https://api.github.com/users/{github_username}/repos").json() 
    print(req[0])
    asyncio.sleep(120)
    currentRepos.clear()

app.run(host=host, port=port)