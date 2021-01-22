"""
author:YZW
date:2021/1/22
time:10:22
reversion:1.0
file_name:dome3
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    name = "yzw"
    age = "18"
    return render_template('index.html', **locals())


if __name__ == "__main__":
    app.run(debug=True)




