from flask import Flask, escape, request, render_template, url_for


app = Flask(__name__)

posts = [
    {
        'author': 'Niklas Bae Pedersen',
        'title' : 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 13, 2019'
    },
    {
        'author': 'Caroline Kavli',
        'title' : 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 13, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)