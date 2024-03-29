from flask import Flask, render_template
from flask_cors import CORS, cross_origin
#import gunicorn
import test
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')


@app.route('/api/resources/exchange', methods=['GET'])
def api_all_exchangeRate():
    return test.get_exchangeRate()


@app.route('/api/resources/test', methods=['GET'])
def api_all():
    return test.get_data_from_EPSList()


@app.route('/api/resources/test/<string:stock_name_id>', methods=['GET'])
def api_single_data(stock_name_id):
    return test.get_single_data_from_website(stock_name_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
