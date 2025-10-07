from flask import Flask, render_template,request


###WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Flask Application!"

@app.route("/index")
def Index():
    return render_template("index.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    return render_template("form.html")
@app.route("/Submit", methods=["GET", "POST"])
def Submit():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    return render_template("form.html")
       

if __name__ == "__main__":
    app.run(debug = True)