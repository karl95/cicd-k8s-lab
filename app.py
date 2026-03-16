from flask import Flask, jsonify       # Flask veebiraamistik, jsonify teeb dict -> JSON
from datetime import datetime          # Ajatempli jaoks

app = Flask(__name__)                  # Loob Flask rakenduse

@app.route('/')                        # Pealeht: GET /
def home()
    return jsonify({
        'message': 'CI/CD + K8s Demo API',
        'version': '1.0.0',           # Versioon - testid kontrollivad seda!
        'timestamp': str(datetime.now())
    })

@app.route('/health')                  # Health check: GET /health
def health():                          # K8s ja CI pipeline kasutavad seda
    return jsonify({'status': 'healthy'}), 200  # 200 = OK

@app.route('/products')                # Toodete nimekiri: GET /products
def products():
    return jsonify([
        {'id': 1, 'name': 'Laptop', 'price': 999},
        {'id': 2, 'name': 'Phone', 'price': 599}   # Seda hinda muudame hiljem testiks
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # 0.0.0.0 = kuulab kõigil IP'del (vajalik Docker'is)
