"""
author:YZW
date:2021/1/23
time:11:43
reversion:1.0
file_name:user
"""

from flask import render_template, request, session, redirect, url_for, Blueprint, flash

userbp = Blueprint("user", __name__)


users = [
    {
        "email": "751428881@qq.com",
        "password": "123456"
    }
]


@userbp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", **locals())
    elif request.method == "POST":
        user = None
        email = request.form.get("email")
        password = request.form.get("password")
        for u in users:
            if u["email"] == email and u["password"] == password:
                session["user"] = email
                return redirect(url_for("main.index"))
        flash("用户名或密码错误！")
        return redirect(url_for("user.login"))


@userbp.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("main.index"))


@userbp.route("/regist", methods=["GET", "POST"])
def regist():
    if request.method == "GET":
        return render_template("regist.html", **locals())
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        for u in users:
            if u["email"] == email:
                flash("邮箱已注册")
                return redirect(url_for("user.regist"))
        if password != password2:
            flash("密码不一致")
            return redirect(url_for("user.regist"))

        users.append({
            "email": email,
            "password": password
        })
        return redirect(url_for('user.login'))

