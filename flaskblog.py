from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'<h1>Hello, <b>{escape(name)}!</b></h1>'