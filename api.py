import re

import requests
from flask import Flask, jsonify
from requests_html import HTMLSession

app = Flask(__name__)

@app.route('/getTimeMostRead', methods=['GET'])
def get_timesnews():
    URL = "https://time.com/"
    try:
        session = HTMLSession()
        response = session.get(URL)

    except requests.exceptions.RequestException as e:
        print(e)

    tmp = []
    for i in response.html.find('li[class="most-popular-feed__item"]'):
        tmp.append({'title' :i.text, 'link': i.absolute_links})

    for i in tmp:
        i['title'] = re.sub(r'\s+', ' ', i['title'])
        i['title'] = i['title'].strip()
        i['title'] = i['title'].replace('’', "'")
        i['title'] = i['title'].replace('“', '"')
        i['title'] = i['title'][2:]
        i['link'] = list(i['link'])[1]


    return jsonify({'news': tmp})


if __name__ == '__main__':
    app.run(debug=True)
