from flask import Flask, request, redirect
from settings import *
import asyncio
import requests
import json
from checker import Checker

app = Flask(__name__)

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

app.run(host=host, port=port)