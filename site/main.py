from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__)

@app.route("/")
def test():
    return 