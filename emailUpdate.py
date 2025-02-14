import smtplib
from email.message import EmailMessage
from dotenv import dotenv_values

# Load credentials from .env file
config = dotenv_values(".env")

GMAIL_USERNAME = config.get('GMAIL_USERNAME')
GMAIL_PW = config.get('GMAIL_SMTP_PW')
RECIPIENT_EMAIL = config.get('RECIPIENT_EMAIL')


def sendEmailSMTP(message):
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(GMAIL_USERNAME, GMAIL_PW)
        smtpObj.send_message(message)
        smtpObj.quit()
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def constructMessage():
    msg = EmailMessage()
    msg['Subject'] = "Valorant Logo Test"
    msg['From'] = GMAIL_USERNAME
    msg['To'] = RECIPIENT_EMAIL
    
    # Explicitly set message type to multipart/related
    msg.set_content("This is a test email with an inline image.", subtype="plain")

    # HTML content referring to Content-ID
    html_content = """
    <html>
    <body>
        <p>THIS IS A TEST</p>
        <img src="cid:image1">
    </body>
    </html>
    """

    msg.add_alternative(html_content, subtype='html')

    # Read and attach image with Content-ID for inline embedding
    with open("newLogo.png", 'rb') as img:
        msg.get_payload()[1].add_related(img.read(), maintype="image", subtype="png", cid="image1")

    return msg


# Construct and send email
email_msg = constructMessage()
sendEmailSMTP(email_msg)
