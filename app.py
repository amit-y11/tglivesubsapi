from flask import Flask
from flask_cors import CORS
from scrapeweb import scrape
app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return 'Welcome to telegram live subcribers count api'

@app.route('/getsubs/<channel>')
def getsubs(channel):
    result=scrape(channel)
    return result

@app.route('/getsubs')
def subs_page():
    return "Enter name of the channel in the format /getsubs/channel-name"


if __name__=='__main__':
    app.run()
