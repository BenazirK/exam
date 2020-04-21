from flask import Flask , render_template, request

app= Flask(__name__)

@app.route("/")
def index():
    f = open("urls.txt", "r", encoding="utf-8")
    images = []
    for row in f:
        url = row.split()[0] 
        description = row[len(url):] 
        images.append([description, url])
    f.close()
    return render_template("index.html",images=images )


@app.route("/add")
def add():

    return render_template("add.html")

@app.route("/reciever" , methods=["POST"])
def reciever():
    description = request.form.get("description")
    url = request.form.get("url")    
    f = open("urls.txt", "a+", encoding="utf-8")
    f.write(url + " " + description + "\n")
    f.close()
    return render_template("add.html") 