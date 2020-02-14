# import necessary libraries
from flask import Flask, render_template
import pandas as pd
from pandas import DataFrame, read_csv;

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def page():
    return render_template("max_temperature.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def page():
    return render_template("humidity.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def index():
    return render_template("cloudiness.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def index():
    return render_template("wind_speed.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def index():
    return render_template("comparison.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def index():
    return render_template("data.html")

if __name__ == "__main__":
    app.run(debug=True)