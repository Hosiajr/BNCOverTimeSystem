from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "hosia12345"

@app.route("/home")
def index():
    return render_template("index.html") 
