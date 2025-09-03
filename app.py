from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")  # for flash messages
Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        flash(f"Thank you {name}, we received your message!", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
