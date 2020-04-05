from flask import Flask
from flask_cors import CORS, cross_origin
from requests import get

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@cross_origin()
def proxy(path):
  return get('https://www.xeno-canto.org/api/2/recordings?query=' + path).content

if __name__ == '__main__':
  app.run()
