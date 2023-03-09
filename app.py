from flask import Flask, send_from_directory as send
from flask_cors import CORS
from data import *

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return indexPage

@app.route('/<path:path>')
def getFile(path):
    rPath='./'+path
    idx=rPath.rfind('/')
    return send(rPath[:idx+1],rPath[idx+1:])

@app.route('/favicon.ico')
def icon():
    return ''

# for i in range(size):
#     app.add_url_rule(files[i][1:],'func'+str(i),lambda i=i:contents[i])

if __name__=='__main__':
    app.run()