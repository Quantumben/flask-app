from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

# Function to get the exchange rate
def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find the exchange rate in the HTML content
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])  # Remove the last 4 characters and convert to float
    return rate

# Initialize the Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return '<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>'

# API route to get currency exchange rate
@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
    rate = get_currency(in_cur, out_cur)
    result_dictionary = {
        'input_currency': in_cur,
        'output_currency': out_cur,
        'rate': rate
    }
    return jsonify(result_dictionary)

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0')
