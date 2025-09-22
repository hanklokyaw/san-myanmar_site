from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import os
import logging
from datetime import datetime

# Flask setup
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "fallback-secret")
Bootstrap(app)

# Configure logging
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/visitors.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

# Contact form class
class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send Message")

# Visitor logging
@app.before_request
def log_visitors():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    user_agent = request.user_agent.string
    path = request.path
    logging.info(f"Visitor IP: {ip}, Path: {path}, Agent: {user_agent}")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f"✅ Thank you {form.name.data}, we received your message!", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
