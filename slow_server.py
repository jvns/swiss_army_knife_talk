from flask import Flask, g
import time

app = Flask(__name__)

@app.route('/')
def slow():
    time.sleep(2)
    return "Hi!"

app.run()
