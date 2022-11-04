from flask import render_template
from .fake_data import posts
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Miquel"}
    return render_template("index.html", title="Home", user=user, posts=posts)
