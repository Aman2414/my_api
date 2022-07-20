import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

clientId = "83f51efbb5bf4ca79a3e2fc9594681ae"
clientSecret = "fbdfc66ea23a4d94893b2eb4147d6bc6"
code = ''
baseURl = 'http://127.0.0.1:5000'


# authorize function will return login page if user is not login, so we have to load html code in web view and when user logins it will redirect to saveToken Function and function will save the Token
@app.route('/authorize', methods=['GET', 'POST'])
def authorize():
    # authorizeUrl = f"https://accounts.spotify.com/authorize?response_type=code&client_id={clientId}&redirect_uri={baseURl + '/saveToken'} "
    authorizeUrl = f"https://accounts.spotify.com/authorize?response_type=code&client_id={clientId}&redirect_uri=https://accounts.spotify.com/status"


@app.route('/saveToken', methods=['GET', 'POST'])
def saveToken():
    args = request.args
    print(f"Args in saveToken Passed {args}")
    global code
    code = args['code']
    print(args.to_dict())
    return 'Login Successful means we got the token now call getToken to get the Token'


@app.route('/getToken', methods=['GET', 'POST'])
def getToken():
    return {'code': code}


if __name__ == "__main__":
    app.run(host='0.0.0.0')
