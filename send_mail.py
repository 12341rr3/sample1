from flask import Flask, request, render_template
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# ✅ Your Gmail credentials
GMAIL_USER = "shreyrj2205@gmail.com"
GMAIL_APP_PASSWORD = "juqt sdem gaan axab"

# ✅ Static destination email (your inbox)
TO_EMAIL = "coding220405@gmail.com"  # Or same as GMAIL_USER

@app.route('/')
def contact_form():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        name = request.form['name']
        user_email = request.form['email']
        message = request.form['message']

        subject = f"New message from {name}"
        full_message = f"""
        You received a new message from your website contact form:

        Name: {name}
        Email: {user_email}

        Message:
        {message}
        """

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = GMAIL_USER
        msg['To'] = TO_EMAIL
        msg.set_content(full_message)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            smtp.send_message(msg)

        return "✅ Message sent successfully to admin!"
    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
