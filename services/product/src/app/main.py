from flask import Flask

app = Flask(__name__)

@app.route('/api/health')
def health_check():
    return {
        'name': 'Product',
        'description': 'Product microservice for Multi-Vendor E-Commerce Platform app',
        'version': '1.0.0',
    }
