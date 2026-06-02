from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Dockerized Flask App!'

@app.route('/about')
def about():
    return 'Hello! This is the about page!'

@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
