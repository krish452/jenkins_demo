# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    message = request.form['message']
    return f"Thank you, {name}! Your message: {message} has been received."

if __name__ == '__main__':
    app.run(debug=True)
