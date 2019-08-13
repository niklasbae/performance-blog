from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    name = request.args.get("name", "World")
    return f'<h1>Hello, <b>{escape(name)}!</b></h1>'

@app.route('/about')
def about():
    return f'<h1>This is the about page!</b></h1>'


if __name__ == '__main__':
    app.run(debug=True)