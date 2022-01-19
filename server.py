from flask import Flask, redirect, request
from json import dumps
from urllib.parse import urlencode

app = Flask(__name__)
app.debug = True

steam_openid_url = 'https://steamcommunity.com/openid/login'

@app.route("/")
def hello():
    return '<a href="http://localhost:5000/auth">Login with steam</a>'

@app.route("/auth")
def auth_with_steam():

  params = {
    'openid.ns': "http://specs.openid.net/auth/2.0",
    'openid.identity': "http://specs.openid.net/auth/2.0/identifier_select",
    'openid.claimed_id': "http://specs.openid.net/auth/2.0/identifier_select",
    'openid.mode': 'checkid_setup',
    'openid.return_to': 'http://127.0.0.1:5000/authorize',
    'openid.realm': 'http://127.0.0.1:5000'
  }

  query_string = urlencode(params)
  auth_url = steam_openid_url + "?" + query_string
  print(auth_url)
  return redirect(auth_url)

@app.route("/authorize")
def authorize():
  print(request.args)
  return dumps(request.args) + '<br><br><a href="http://localhost:5000/auth">Login with steam</a>'

if __name__ == "__main__":
    app.run()
