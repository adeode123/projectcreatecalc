from flask import Flask, render_template, flash
from content_management import Content

TOPIC_DICT = Content()

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("base.html")


@app.route('/dashboard/')
def dashboard():

    flash("flash test!!!")

    return render_template("dashboard.html", TOPIC_DICT=TOPIC_DICT)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run()
