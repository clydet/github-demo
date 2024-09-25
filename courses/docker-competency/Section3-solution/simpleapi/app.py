from flask import Flask, jsonify

class SimpleAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def home():
            return jsonify({"message": "Welcome to the Simple Flask API!"})

        @self.app.route('/hello/<name>')
        def hello(name):
            return jsonify({"message": f"Hello, {name}!"})

    def run(self):
        self.app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    api = SimpleAPI()
    api.run()
