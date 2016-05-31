# Minimal Flask Implementation using Steam OpenID

Setup using a python `virtualenv`:

```bash
$ virtualenv venv
$ source venv/bin/activate
$ python server.py
```

## Authenticating

Open [http://localhost:5000](http://localhost:5000) and click on the "Login with Steam" link. You will be redirected back to [http://localhost:5000/authorize](http://localhost:5000) after authenticating with your Steam account. The response parameters received from the Steam authentication provider will be displayed.
