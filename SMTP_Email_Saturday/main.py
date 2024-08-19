import smtplib
import datetime as dt
import random
import os

day_of_the_week = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}


def send_email():
    my_email = "andy.vargas.noesi@gmail.com"
    app_password = os.getenv("GMAIL_SECRET")

    with open("quotes.txt", mode="r") as quotes:
        quotes_lines = quotes.readlines()
        pick_quote = random.choice(quotes_lines)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject: Happy Monday\n\n "
                f"{pick_quote}"
        )


now = dt.datetime.now()

if now.weekday() == day_of_the_week["saturday"]:
    send_email()
