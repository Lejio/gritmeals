# from multiprocessing.connection import wait
import email
from random import randint
from flask import Flask
from flask import Flask, render_template, redirect, url_for, request
# from Website.MenuScripts.EmailHandler import EmailHandler
# from meals_db import entry as e
# from MenuScripts import EmailHandler, Config
import smtplib
from MenuScripts import Config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import sqlite3
import random


global count
app = Flask(__name__)


@app.route("/")
def run_app():
    return render_template("/index.html")
    # return "<h1>Hello World!</h1>"


@app.route("/test", methods=['POST'])
def test1():
    output = request.get_json()
    result = json.loads(output)

    # Eh = EmailHandler(None, "You have subscribed!",
    #                   "test", "Test tes", result['email'])
    print(result['email'])
    send_email(result['email'])
    return result


def send_email(result):
    with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        print("test")
        user_email = Config.USER_EMAIL
        user_password = Config.USER_PASSWORD

        smtp.login(user_email, user_password)
        print("test")
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "You have Subscribed! "
        msg['From'] = user_email
        msg['To'] = result

        text = "You have been subscribed to the UMBC dining bot!"
        print("test")
        part1 = MIMEText(text, "plain")

        msg.attach(part1)

        # print(result["email"])
        smtp.sendmail(user_email, result, msg.as_string())

        print("test")
        smtp.close()

        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        count = random.randint(1, 100000)
        r = cursor.execute(
            'INSERT INTO subs VALUES (' + str(count)+', "'+result+'")')

        print(r)
        conn.commit()
        conn.close()


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000)
