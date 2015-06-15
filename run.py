from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<username>')
def show_user_name(username):
	return 'User %s' % username

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug = True)