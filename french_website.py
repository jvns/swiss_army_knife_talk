from flask import Flask, g, request, make_response
import time

app = Flask(__name__)

@app.route('/')
def index():
    language = request.headers.get('Accept-Language', '')
    if 'en' in language:
        body = "Hello, welcome to PyCon! =D =D so fun"
    else:
        body= u"Bonjour, bienvenue \xe0 PyCon!"
    resp = u"""
    <html>
    <body>
    <h1>{body}</h1>
    </body>
    </html>
    """.format(body=body)
    return make_response(resp)

app.run()
