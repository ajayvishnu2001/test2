from flask import Flask
from pycaret.regression import *


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index23():
    return "hello"

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
