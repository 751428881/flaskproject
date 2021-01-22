"""
author:YZW
date:2021/1/22
time:9:50
reversion:1.0
file_name:dome2
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "欢迎来到flask页面"


@app.route("/<int:pk>")
def detail(pk):
    return f"欢迎来到flask页面{pk}"


if __name__ == '__main__':
    app.run(host="192.168.11.9", port="2323", debug=True)

