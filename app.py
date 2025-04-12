from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Configure based on environment (staging or production)
app.config['ENV'] = os.getenv('FLASK_ENV', 'development')  # Default to 'development' if not set

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    message = request.form['message']
    return f"Thank you, {name}! Your message: {message} has been received."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

