from flask import json
from flask import request
from flask import Flask

app =Flask(__name__)


#comment
@app.route('/')
def root():
    return 'Just a github webhook'

@app.route('/table', methods=['POST'])
def github_message():
    if request.headers['Content-Type'] == 'aplication/json':
        return json.dump(request.json)

if __name__ == '__main__':
    app.run(debug=True)



