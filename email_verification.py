from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import secrets

app = Flask(__name__)

# Configuration for Flask-Mail and Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'engen.inyang@gmail.com'
app.config['MAIL_PASSWORD'] = 'YourGmailPassword'

mail = Mail(app)

# Simulate a database to store verification codes
verification_codes = {}

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Simulate user registration
        username = request.form['username']
        email = request.form['email']

        # Generate a random verification code
        verification_code = secrets.token_hex(4)  # Generate a 4-byte hex token

        # Store the verification code (you would typically store this in a database)
        verification_codes[email] = verification_code

        # Send the verification email
        send_verification_email(email, verification_code)

        flash('A verification email has been sent. Please check your inbox.')

        return redirect(url_for('login'))

    return render_template('register.html')

def send_verification_email(to_email, verification_code):
    subject = 'Account Verification'
    sender_email = app.config['MAIL_USERNAME']
    recipient_email = to_email

    message_body = f'Your verification code is: {verification_code}'

    msg = Message(subject=subject, sender=sender_email, recipients=[recipient_email])
    msg.body = message_body

    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)
