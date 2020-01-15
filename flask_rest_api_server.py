from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello', 200, {'Content-Type': 'text/plain'}
    #return Response('Hello', mimetype='text/plain')
    

if __name__ == '__main__':
    app.run(debug=True)