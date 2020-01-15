from bottle import *
from pprint import pprint

@route('/')
def welcome():
    pprint(dict(request.headers))
    response.content_type = 'text/plain'
    return 'Hello'

if __name__ == '__main__':

    run(host='localhost', port=8080)