from flask import Flask, render_template

app = Flask("Website")

@app.route("/")
def home():
    return render_template("tutorial.html")

@app.route("/Store/")
def store():
    return render_template("store.html")

@app.route("/About/")
def about():
    return render_template("about.html")

@app.route("/Contact/")
def contact():
    return render_template("contact.html")

app.run(debug=True)