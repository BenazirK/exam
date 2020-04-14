from flask import Flask , render_template, request

app= Flask(__name__)

@app.route("/", methods=["GET" ,"POST"])
def gallery():
    return render_template("gallery.html")

@app.route("/add")
def add():
    return render_template("add.html")