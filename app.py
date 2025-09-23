from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import os
import sqlite3
from datetime import datetime

# Flask setup
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "fallback-secret")
Bootstrap(app)

# Contact form class
class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send Message")

# --- Step 3: Database logging ---
def log_to_db(ip, path, agent):
    conn = sqlite3.connect("logs/visitors.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS visitors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ip TEXT,
                    path TEXT,
                    agent TEXT,
                    timestamp TEXT
                )""")
    c.execute("INSERT INTO visitors (ip, path, agent, timestamp) VALUES (?, ?, ?, ?)",
              (ip, path, agent, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

@app.before_request
def log_visitors():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    user_agent = request.user_agent.string
    path = request.path
    log_to_db(ip, path, user_agent)

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
    if not os.path.exists("logs"):
        os.makedirs("logs")
    app.run(debug=True)
