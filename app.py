from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>'

@app.route('/ben')
def ben():
    return '<h1>QuantumBen was here</h1>'

if __name__ == '__main__':
    app.run()
