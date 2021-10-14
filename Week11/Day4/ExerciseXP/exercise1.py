from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

current_time = datetime.datetime.now()
greeting = ' '


@app.route("/")
def greeting():
    return render_template("greeting.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
