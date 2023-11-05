from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def main():
    return '<p>This page for keep alive bot!</p>'

def run_main():
    app.run()

def keep():
    print('Run module keep alive!')
    Thread(target=run_main).run()
