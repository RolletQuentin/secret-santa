import smtplib
import ssl
from dotenv import load_dotenv
import os

load_dotenv()


def sendEmail(to_email, message):
    smtp_client = os.getenv("SMTP_CLIENT")
    smtp_port = os.getenv("SMTP_PORT")
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_client, smtp_port, context=context) as server:
        server.login(email,
                     password)

        server.sendmail(email,
                        to_email, message)

        print(f'OK. Email sent to ${to_email}')


if __name__ == "__main__":
    sendEmail("rolletquen@gmail.com", "This is a test.")
