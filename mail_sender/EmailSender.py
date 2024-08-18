import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(
    sender_email: str,
    sender_password: str,
    receiver_email: str,
) -> bool:
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = sender_email
    smtp_password = sender_password
    recipient_email = receiver_email

    subject = "Confirmation of Complaint Receipt"
    body = """
    Dear [Recipient's Name],

    Thank you for your recent communication. This email is to confirm that we have received your complaint regarding [specific issue or subject of the complaint].

    We appreciate you bringing this matter to our attention. Our team will thoroughly review the details provided and take appropriate action. We are committed to addressing genuine issues with accuracy and ensuring they are resolved with the appropriate level of urgency and severity.

    If you have any further information to add or questions regarding the complaint, please feel free to reply to this email.

    Thank you for your patience and understanding.

    Best regards,

    [Your Full Name]
    [Your Position]
    [Your Contact Information]
    [Company/Organization Name]
    """

    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, recipient_email, msg.as_string())
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
