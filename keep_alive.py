from flask import Flask
from threading import Thread

print('Server Starting...')

app = Flask('')
# Routes


@app.route('/')
def home():
    return "One ping at a time..."


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start
