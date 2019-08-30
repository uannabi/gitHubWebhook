from flask import json
from flask import request
from flask import Flask

app =Flask(__name__)



@app.route('/')
def root():
    return 'Just a github webhook'

if __name__ == '__main__':
    app.run(debug=True)



