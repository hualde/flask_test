from flask import Flask, url_for, render_template, request, redirect


app = Flask(__name__)


posts = [3,4,5]

@app.route("/")
def index():
    page = request.args.get('page', 1)
    list = request.args.get('list', 20)
    return render_template("index.html", page=page, list=list)


@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)

