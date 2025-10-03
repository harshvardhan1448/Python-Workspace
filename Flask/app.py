from flask import Flask, render_template


###WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Flask Application!"

@app.route("/index")
def Index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)