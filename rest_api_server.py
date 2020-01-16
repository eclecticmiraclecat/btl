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
# handle 500 error when query wrong type, http://localhost:8080/area/circle?radius=xyz
@route('/area/circle')
def circle_area_service():
    pprint(dict(request.query))
    response.set_cookie('last-visit', time.ctime())
    try:
        radius = float(request.query.get('radius', '0.0'))
    except ValueError as e:
        return e.args[0]
    area = algebra.area_circle(radius)
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return f'<p> The area is <em> {area} </em> </p>'
    return dict(radius=radius, area=area, service=request.path)


if __name__ == '__main__':

    run(host='localhost', port=8080, reloader=True)