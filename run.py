'''Entry point script of the flask. Contains flask app and endpoints.'''
from flask import Flask
from flask import request
from flask import render_template
import requests

from helpers import parser

# create flask app
app = Flask(__name__)

@app.route('/')
def index():
    ''' Render entry point template. '''
    return render_template("index.html")

@app.route('/gists', methods= ['POST'])
def get_gists():
    ''' Get the github public gists of given username. '''
    username = request.form['username']
    headers = {'Accept': 'application/vnd.github.v3+json'}
    url_endpoint = 'https://api.github.com/users/'+username+'/gists'
    # call github api to fetch gists
    response = requests.get(url_endpoint, headers=headers)
    # check api response status
    if response.status_code != 200:
        raise Exception('Server error: Cannot fetch all gists: {}'.format(response.status_code))
    # parse response json
    parsed_response = parser(response.json())
    return render_template("index.html", available_gists=parsed_response)

if __name__ == "__main__":
    app.run(debug=True)
