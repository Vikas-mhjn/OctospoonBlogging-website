from flask import Flask, render_template
import requests
app = Flask(__name__)

posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()


@app.route('/')
def home():
   return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/post.html")
def show_post():
    return render_template("post.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)