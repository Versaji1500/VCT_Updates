import smtplib
from email.message import EmailMessage
from dotenv import dotenv_values
import http.client, urllib

# Load credentials from .env file
config = dotenv_values(".env")

GMAIL_USERNAME = config.get('GMAIL_USERNAME')
GMAIL_PW = config.get('GMAIL_SMTP_PW')
RECIPIENT_EMAIL = config.get('RECIPIENT_EMAIL')
APP_TOKEN = config.get("PUSHOVER_API_TOKEN")
USER_KEY = config.get("PUSHOVER_USER_KEY")

# SMTP server function to send an email with a specified message
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
        

# Construct email message to send with pushover
def constructMessage(subject, message):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = GMAIL_USERNAME
    msg['To'] = RECIPIENT_EMAIL
    


    # HTML content referring to Content-ID, using an f-string to insert the message
    html_content = f"""
    <html>
    <body>
        <p>{message}</p>
    </body>
    </html>
    """

    msg.add_alternative(html_content, subtype='html')

    return msg


# Function to send a push notification with Pushover API
def pushoverNotification(message, title="VCT Updates"):
    # HTTPS Connection object
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": APP_TOKEN,
        "user": USER_KEY,
        "message": message,
        "title": title,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

