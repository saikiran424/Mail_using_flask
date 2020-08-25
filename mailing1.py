from flask import Flask
from flask_mail import Mail, Message

import os

app = Flask(__name__)
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_PORT": 465,
    "MAIL_USERNAME": 'l.saikiran4597@gmail.com',
    "MAIL_PASSWORD": 'Alt@2331'
}

app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
    with app.app_context():
        msg = Message(sender=app.config.get("MAIL_USERNAME"),
                      recipients=["saikiranlingampally4397@gmail.com"])
        msg.subject = "Testing_1"
        msg.body = "This is first mail"

        mail.send(msg)
