from flask import Flask
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    logging.info("/endpoint was reached")
    return "Hello World!"

@app.route("/status")
def status():
    logging.info("/status endpoint was reached")
    return "OK - healthy"

@app.route("/metrics")
def metrics():
    logging.info("/metrics endpoint was reached")
    return {"UserCount": 140, "UserCountActive": 23}

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
