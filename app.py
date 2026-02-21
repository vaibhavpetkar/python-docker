# writting basic flask app code where we retrun "Hello World" when we visit on port 5000

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'
if __name__ == '__main__':
    app.run(debug=True, port=5000)
    