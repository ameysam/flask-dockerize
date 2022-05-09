from flask import Flask
from redis import Redis

app = Flask(__name__)

@app.route('/')
def say_hello():
    r = Redis(host='myredis', port=6379, db=0)
    name = r.get("name").decode()
    return f'Hello {name.title()}\n'

if __name__ == "__main__":
    app.run("0.0.0.0",  80)