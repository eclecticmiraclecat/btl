from flask import Flask, Response, request
from pprint import pprint
import time

app = Flask(__name__)

@app.route('/')
def welcome():
    pprint(dict(request.headers))
    if 'text/html' in request.headers.get('Accept', '*/*'):
        return '<h1> Howdy! </h1>', 200, {'Content-Type': 'text/html'}
    return 'Hello', 200, {'Content-Type': 'text/plain'}
    #return Response('Hello', mimetype='text/plain')
    
@app.route('/now')
def time_service():
    return time.ctime(), 200, {'Content-Type': 'text/plain'}

@app.route('/upper/<word>')
def upper_case_service(word):
    return word.upper(), 200, {'Content-Type': 'text/plain'}

# query is passed through ?, http://localhost:8080/area/circle?radius=10
@app.route('/area/circle')
def circle_area_service():
    pprint(dict(request.args))
    return 'Test'

if __name__ == '__main__':
    app.run(debug=True)