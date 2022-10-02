import os
import smtplib
import Config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailHandler:
    def __init__(self, group, title, subject, message):
        """
        Default Constructor for EmailHandler
        :param group: Group name of customers
        :param title: Email title
        :param subject: Email subject
        :param message: Email message
        """
        self.customers = []
        self.group = group
        self.title = title
        self.subject = subject
        self.message = message

    def loadCustomers(self):
        """
        Loads all the customers to send the email to
        :return: boolean result of the emails being loaded
        """
        path = Config.EMAIL_GROUP_PATH[self.group]

        try:
            print("Path:", path)
            file = open(path, "r")
            for email in file:
                email = email.strip()
                self.customers.append(email)
            file.close()
            return True
        except FileNotFoundError:
            print("FILE NOT FOUND!")
        return False

    def sendEmail(self):
        """
        Sends the emails to the customers
        :return: boolean result of email being sent
        """
        has_loaded = self.loadCustomers()
        if not has_loaded:
            return False

        with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            user_email = Config.USER_EMAIL
            user_password = Config.USER_PASSWORD

            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Today's Menu: "
            msg['From'] = user_email

            # text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"

            # Open a file: file
            file = open('../Email/template.html', mode='r')

            # read all lines at once
            html = file.read()

            # close the file
            file.close()
            # part1 = MIMEText(text, 'plain')
            part2 = MIMEText(html, 'html')

            # msg.attach(part1)
            msg.attach(part2)

            print("*********************", user_email, user_password)
            smtp.login(user_email, user_password)

            for email in self.customers:
                smtp.sendmail(user_email, email, msg.as_string())

            smtp.close()

            return True
