from bottle import *

@route('/')
def welcome():
    return 'Hello'

if __name__ == '__main__':

    run(host='localhost', port=8080)