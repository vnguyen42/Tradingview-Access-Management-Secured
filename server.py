from flask import Flask, request
from tradingview import tradingview
import json
import os
from functools import wraps

app = Flask('')

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = None
        # Try to get the API key from the header
        if 'X-API-KEY' in request.headers:
            api_key = request.headers['X-API-KEY']
        else:
            # Alternatively, get it from query params
            api_key = request.args.get('api_key')

        if not api_key or api_key != os.environ.get('API_KEY'):
            return json.dumps({'message': 'Unauthorized'}), 401, {
                'Content-Type': 'application/json; charset=utf-8'
            }
        return f(*args, **kwargs)
    return decorated

@app.route('/validate/<username>', methods=['GET'])
@require_api_key
def validate(username):
    try:
        print(username)
        tv = tradingview()
        response = tv.validate_username(username)
        return json.dumps(response), 200, {
            'Content-Type': 'application/json; charset=utf-8'
        }
    except Exception as e:
        print("[X] Exception Occurred: ", e)
        failureResponse = {'errorMessage': 'Unknown Exception Occurred'}
        return json.dumps(failureResponse), 500, {
            'Content-Type': 'application/json; charset=utf-8'
        }

@app.route('/access/<username>', methods=['GET', 'POST', 'DELETE'])
@require_api_key
def access(username):
    try:
        jsonPayload = request.json
        pine_ids = jsonPayload.get('pine_ids')
        print(jsonPayload)
        print(pine_ids)
        tv = tradingview()
        accessList = []
        for pine_id in pine_ids:
            access = tv.get_access_details(username, pine_id)
            accessList.append(access)

        if request.method == 'POST':
            duration = jsonPayload.get('duration')
            dNumber = int(duration[:-1])
            dType = duration[-1:]
            for access in accessList:
                tv.add_access(access, dType, dNumber)

        if request.method == 'DELETE':
            for access in accessList:
                tv.remove_access(access)
        return json.dumps(accessList), 200, {
            'Content-Type': 'application/json; charset=utf-8'
        }

    except Exception as e:
        print("[X] Exception Occurred: ", e)
        failureResponse = {'errorMessage': 'Unknown Exception Occurred'}
        return json.dumps(failureResponse), 500, {
            'Content-Type': 'application/json; charset=utf-8'
        }

@app.route('/')
def main():
    return 'Your bot is alive!'

def start_server():
    app.run(host='0.0.0.0', port=3000)
