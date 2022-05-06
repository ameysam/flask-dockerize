from flask import Flask
from redis import Redis

app = Flask(__name__)

@app.route('/')
def say_hello():
    r = Redis(host='localhost', port=6379, db=0)
    name = r.get("name").decode()
    return f'Hello {name}\n'

if __name__ == "__main__":
    app.run("0.0.0.0",  5000)