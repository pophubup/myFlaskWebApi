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

@app.route('/api/resources/test', methods=['GET'])
def api_all():
    return test.get_data_from_EPSList();

@app.route('/api/resources/test/<string:stock_name_id>', methods=['GET'])
def api_single_data(stock_name_id):
    return test.get_single_data_from_website(stock_name_id);