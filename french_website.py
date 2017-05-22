from flask import Flask, g, request, make_response
import time

app = Flask(__name__)

@app.route('/')
def index():
    language = request.headers.get('Accept-Language', '')
    if 'en' in language:
        body = "Hello, Devops Montreal! =D =D so fun"
    else:
        body= u"Bonsoir, Devops Montr\xe9al!"
    resp = u"""
    <html>
    <body>
    <h1>{body}</h1>
    </body>
    </html>
    """.format(body=body)
    return make_response(resp)

app.run(port=4000)
