# from multiprocessing.connection import wait
# from flask import Flask
from flask import Flask, render_template, redirect, url_for, request
# import webbrowser


# app = Flask(__name__)

# dummy_data = ["Pizza", "Chinese", "Halal", "Indian", "White People"]
# content = ""


# @app.route("/")
# def home():
#     return render_template("../Website/src/index.html")


# @app.route("/login")
# def login():
#     return render_template("login.html")


# from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("/index2.html")
    # return "<h1>Hello World!</h1>"


if __name__ == '__main__':
    app.run()
