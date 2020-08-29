from flask import Flask, request, jsonify
from blacklist_checker import is_blacklisted
from clickbait_model import predictor
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello():
    return 'API for chrome extension'


@app.route('/check-post', methods=['POST'])
def check_post():

    is_dodgy = False
    warning_msg = ''

    title_warning = ''
    title_is_dodgy = False

    title = request.json['title']
    link = request.json['link']
    # print(predictor(title))

    if link:
        if is_blacklisted(link):
            print('Blacklisted:', link)
            warning_msg = 'This source is known for producing fake news'
            is_dodgy = True
        '''
        if link is parsed - scrape the link
        '''
        pass
    
    if predictor(pd.Series(title)) == 1:
        print('Clickbait:', title)
        title_warning = 'Evidence supports this being a clickbait title'
        title_is_dodgy = True

    return jsonify(
        is_dodgy=is_dodgy,
        warning_msg=warning_msg
    )


# run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
