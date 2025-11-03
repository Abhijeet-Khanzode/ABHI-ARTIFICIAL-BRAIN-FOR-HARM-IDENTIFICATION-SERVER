
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER_EMAIL = "abhi.s.khanzode@gmail.com"
SENDER_PASSWORD = "ahlx zipv mbzi qmzb" 

def send_thank_you_email(to_email, user_name, reported_url):
    try:
        subject = "Thank you for your feedback – ABHI Team"
        body = f"""
        Hi {user_name},

        Thank you for submitting your feedback about the website:

        🔗 {reported_url}

        Our team will review the site and get back to you shortly.
        In the meantime, please stay alert and avoid sharing sensitive information.

        — ABHI Shield Team 🛡️
        """

        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)

        print("📧 Email sent successfully to", to_email)
        return True

    except Exception as e:
        print("❌ Email sending failed:", e)
        return False
    

    
def send_review_email(name, recipient_email, url, status):
    subject = f"🔒 ABHI Shield - Site Review Result: {status}"
    
    if status == "SAFE":
        message = f"""
Hi {name},

✅ Thank you for submitting your feedback regarding this website:
🔗 {url}

After review by both our security model and human authority, we confirm this site is safe.

However, please remain cautious and avoid sharing any sensitive information unnecessarily.

— ABHI Shield Team 🛡️
"""
    else:
        message = f"""
Hi {name},

⚠️ Thank you for submitting your feedback regarding this website:
🔗 {url}

After review by our system and human experts, we’ve flagged this site as potentially a PHISHING attempt.

Please do not enter your sensitive information and avoid visiting this site.

— ABHI Shield Team 🛡️
"""

    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)

        print(f"📧 Email sent successfully to {recipient_email}")

    except Exception as e:
        print("❌ Email sending failed:", str(e))
