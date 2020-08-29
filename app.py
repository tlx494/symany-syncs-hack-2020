from flask import Flask, request, jsonify
from blacklist_checker import Blacklister
import json
from clickbait_model import predictor
import pandas as pd
from flask_cors import CORS, cross_origin
import urllib.parse
import re

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

blacklister = Blacklister()


@app.route('/')
@cross_origin()
def hello():
    return 'API for chrome extension'


@app.route('/check-post', methods=['POST'])
@cross_origin()
def check_post():

    domain_is_dodgy = False
    warning_msg = ''

    title_is_dodgy = False
    title_warning = ''

    data = json.loads(request.data.decode('utf-8'))

    title = data['title']
    link = data['link']

    link = urllib.parse.unquote(link)
    link = re.sub('https:\/\/l\.facebook\.com\/l\.php\?u=', '', link)
    link = re.sub('\?fbclid.*', '', link)

    print('Checking Title:', title, '\nLink:', link)

    if link:
        if blacklister.is_blacklisted(link):
            print('Blacklisted:', link)
            warning_msg = 'This source is known for producing fake news'
            domain_is_dodgy = True

    if predictor(pd.Series(title)) == 1:
        print('Clickbait:', title)
        title_warning = 'This headline may be fake news or clickbait'
        title_is_dodgy = True

    return jsonify(
        domain_is_dodgy=domain_is_dodgy,
        warning_msg=warning_msg,
        title_warning=title_warning,
        title_is_dodgy=title_is_dodgy
    )


# run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'))
