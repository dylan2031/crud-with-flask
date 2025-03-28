from flask import Flask, render_template
from data import Posts

app = Flask(__name__)

Posts = Posts()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts = Posts)

@app.route('/post/<string:id>/')
def post(id):
    return render_template('post.html', id = id)

if __name__ == '__main__':
    app.run(debug=True)