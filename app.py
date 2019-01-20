import time
import redis
import json
from flask import Flask
from json2html import *

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')


def colors():

     count = get_hit_count()

     input = json.loads(open('./colors.json').read())

     return json2html.convert(json = input) 


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
