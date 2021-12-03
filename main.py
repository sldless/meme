from threading import Thread
import requests
from meme import gen 

from flask import Flask, render_template,redirect
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
  results = gen()
                            
  context = {
    'subreddit': results[2],
    'img': results[4],
    'author': results[6].get('author'),
    'title': results[3],
    'hex': requests.get('https://www.colr.org/json/color/random').json().get('colors')[0].get('hex')
  }
  return render_template('index.html', **context)

@app.errorhandler(404)
def page_not_found(e):

  return redirect('https://meme.sldless.repl.co'), 404


if __name__ == "__main__":
    server = Thread(target=app.run(host="0.0.0.0", port=8080, debug=True))
    server.start()
