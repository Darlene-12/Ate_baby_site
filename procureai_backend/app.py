from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from models import db, ContactMessage
from config import Config
from flask_cors import CORS
import smtplib

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
CORS(app)

# Initialize Flask-Mail
mail = Mail()
mail.init_app(app)

def error_response(message, status_code=400):
    return jsonify({
        "success": False,
        "error": message
    }), status_code


@app.route('/')
def home():
    return "ProcureAI Backend is running."

@app.route('/submit', methods=['POST'])
def submit_contact():
    try:
        data = request.form
        name = data.get('name')
        email = data.get('email')
        company = data.get('company', '')
        message = data.get('message')

        if not all([name, email, message]):
            return error_response("Name, email, and message are required.", 422)

        new_msg = ContactMessage(
            name=name,
            email=email,
            company=company,
            message=message
        )
        db.session.add(new_msg)
        db.session.commit()

        print("✅ Saved to DB")

        msg = Message(
            subject=f"New Contact from {name}",
            recipients=["stacyate018@gmail.com"],
            body=f"Name: {name}\nEmail: {email}\nCompany: {company}\nMessage:\n{message}"
        )
        mail.send(msg)
        print("✅ Email sent to stacyate018@gmail.com")

        return jsonify({"success": True, "message": "Message received and email sent."}), 200

    except Exception as e:
        print("❌ Flask error:", e)
        return error_response("Unexpected error occurred", 500)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
