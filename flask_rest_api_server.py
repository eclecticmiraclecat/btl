from flask import Flask, Response, request
from pprint import pprint
import time
import algebra

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
    try:
        radius = float(request.args.get('radius', '0.0'))
    except ValueError as e:
        return e.args[0]
    area = algebra.area_circle(radius)
    if 'text/html' in request.headers.get('Accept', '*/*'):
        return f'<p> The area is <em> {area} </em> </p>', 200, {'Content-Type': 'text/html'}
    return dict(radius=radius, area=area, service=request.path)

if __name__ == '__main__':
    app.run(debug=True)