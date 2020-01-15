from bottle import *
from pprint import pprint

@route('/')
def welcome():
    pprint(dict(request.headers))
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return '<h1> Howdy! </h1>'
    response.content_type = 'text/plain'
    return 'Hello'

if __name__ == '__main__':

    run(host='localhost', port=8080)