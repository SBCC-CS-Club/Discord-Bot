#!/bin/env python3
import smtplib, ssl
from email.message import EmailMessage
from settings import GOOGLE_APP_PASSWORD


def send_verification_email(to: str, key: str):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    password = GOOGLE_APP_PASSWORD
    message = EmailMessage()
    message["From"] = "jrayvazian@pipeline.sbcc.edu"
    message["To"] = to
    message["Subject"] = "Please verify your email!"
    message.set_content(
        f"Thanks for joining the Offical CS Club Discord server! Please send the following code to "
        f"the bot to verify your email:\n"
        f"{key}\n"
        f"https://linktr.ee/sbcccsclub\n"
        f"Note: This is an automated message replies may not be seen."
    )
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login("jrayvazian@pipeline.sbcc.edu", password)
        server.send_message(message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
