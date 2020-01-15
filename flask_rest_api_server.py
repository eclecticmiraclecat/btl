from flask import Flask, Response, request
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def welcome():
    pprint(dict(request.headers))
    return 'Hello', 200, {'Content-Type': 'text/plain'}
    #return Response('Hello', mimetype='text/plain')
    

if __name__ == '__main__':
    app.run(debug=True)