#================================Dependencies==================================
#to send mesj
import smtplib, ssl
#to manipulate the email format
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

try:
    import credentials
except:
    print("Credentials.py not found")

print("Program was init")


# Send mail function
def send_emails(emails: list, subject: str = "automated-BOT-remainder", text_message: str="Bot ramainder message"):
    smtp_server = "smtp.gmail.com"
    sender_email = credentials.username
    password = credentials.password
    receiver_email = emails

    message = MIMEMultipart()
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email if type(receiver_email)==str else ",".join(receiver_email)

    msj = MIMEText(text_message, "plain")

    message.attach(msj)

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    with smtplib.SMTP_SSL(smtp_server, 465, context=context) as server:
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print('Email was send to ', receiver_email)


if __name__ == "__main__":
    emails_to_send = ["raul022107@gmail.com", "pichardoraul@gmail.com"]
    send_emails(emails_to_send)
