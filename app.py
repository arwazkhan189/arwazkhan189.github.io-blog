from flask import Flask, render_template, make_response
import requests
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def blogHome():
    url = "https://dev.to/api/articles?username=arwazkhan189"
    req = requests.get(url)
    data = json.loads(req.content)
    return render_template('index.html',data=data)

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('404.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

if __name__ == "__main__":
    app.run()