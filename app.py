import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST"])
def update():
    return "Well hello there!"

@app.route("/", methods=["PUT"])
def send():
    return "FEED ME SEYMOUR!!!"

@app.route("/", methods=["GET"])
def do():
    return "safary sucks"

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return "Page/File not found", 404


if __name__ == '__main__':
    app.run(debug=True)
