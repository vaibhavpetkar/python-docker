# writting basic flask app code where we retrun "Hello World" when we visit on port 5000

from flask import Flask, jsonify
from flask_cors import CORS



app = Flask(__name__)
CORS(app)  # This allows all origins to access the API

# create a route for the home page
@app.route('/')
def home():
    return jsonify({"message": "Hello World"})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)