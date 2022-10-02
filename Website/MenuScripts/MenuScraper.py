import Config
from EmailHandler import EmailHandler
import sys


def run(group=Config.GROUP_DEVELOPERS):
    handler = EmailHandler(group, "Title", "Subject", "Message")

    if handler.sendEmail():
        print("Email sent!")
    else:
        print("Email not sent!")


if __name__ == '__main__':
    run()
