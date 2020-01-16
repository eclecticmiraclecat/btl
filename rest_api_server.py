from bottle import *
from pprint import pprint
import time
import algebra

@route('/')
def welcome():
    pprint(dict(request.headers))
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return '<h1> Howdy! </h1>'
    response.content_type = 'text/plain'
    return 'Hello'

@route('/now')
def time_service():
    response.content_type = 'text/plain'
    return time.ctime()

@route('/upper/<word>')
def upper_case_service(word):
    response.content_type = 'text/plain'
    return word.upper()

# query is passed through ?, http://localhost:8080/area/circle?radius=10
@route('/area/circle')
def circle_area_service():
    pprint(dict(request.query))
    return 'Test'

if __name__ == '__main__':

    run(host='localhost', port=8080)