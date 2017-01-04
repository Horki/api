import os
from flask import Flask
from flask_mail import Message, Mail
from api.app import rq
from api.config import configure_app


@rq.job
def send_mail(user):
    app = Flask(__name__)
    with app.app_context():
        configure_app(app)
        mail = Mail(app)
        hostname = os.environ.get("HOSTNAME")
        msg = Message(
            'Register your account',
            sender='ivanzvonimirhorvat@gmail.com',
            recipients=[user.email]
        )
        url = "http://%s/auth/active/%s" % (hostname, user.token)
        # raw email
        msg.body = "Please confirm token %s" % url
        # html email
        msg.html = "Please confirm token <a href='%s'>here</a>" % url
        mail.send(msg)
