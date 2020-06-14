from flask import Flask, render_template
import gunicorn
import test
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/api/resources/exchange', methods=['GET'])  
def api_all_exchangeRate():
    return test.get_exchangeRate();