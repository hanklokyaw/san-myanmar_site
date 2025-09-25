# Smart Housing Flask App

This is a Flask-based web application for **Smart Housing**, a modern housing solution company.  
The app includes a professional landing page, About page, Contact form with validation, and visitor logging.

---

## 🚀 Features
- **Home Page**: Hero section, About highlights, Video showcase, Call-to-action.  
- **About Page**: Mission, Expertise, and Vision sections.  
- **Contact Page**:  
  - Contact info with icons  
  - Google Maps embed  
  - Secure contact form with CSRF protection (Flask-WTF)  
  - Form validation (name, email, message)  
- **Visitor Logging**: Logs IP, path, user agent, timestamp into `logs/visitors.db` (SQLite).  
- **Responsive Design**: Built with Bootstrap 5 and Bootstrap Icons.  
- **Reusable Templates**: Uses a `base.html` layout with navbar, footer, and flash messages.

---

## 📂 Project Structure
```
smart-housing/
│── app.py                # Flask application
│── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│── static/
│   ├── logo_invert.png
│   ├── Smart Housing Industry.mp4
│   ├── favicon.ico
│── logs/
│   └── visitors.db       # Visitor logs (auto-created)
│── requirements.txt
│── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/your-username/smart-housing.git
cd smart-housing
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate    # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables
Create a `.env` file:
```
FLASK_SECRET_KEY=your-secret-key
```

### 5. Run the App
```bash
flask run
```
or
```bash
python app.py
```

Visit: [http://127.0.0.1:8022](http://127.0.0.1:8022)

---

## 📦 Requirements
Create `requirements.txt` with:
```
flask
flask-bootstrap
flask-wtf
wtforms
email-validator
```

---

## 📝 Logging
- Visitors are logged into `logs/visitors.db` automatically.
- Each request stores: `IP, Path, User Agent, Timestamp`.

To inspect logs:
```bash
sqlite3 logs/visitors.db "SELECT * FROM visitors ORDER BY timestamp DESC LIMIT 10;"
```

---

## 🔐 Security Notes
- Do not expose your `FLASK_SECRET_KEY`.  
- Run with Gunicorn or uWSGI behind Nginx in production.  
- Use HTTPS (Cloudflare tunnel or reverse proxy).

---

## 📄 License
MIT License © 2025 Smart Housing Inc.
