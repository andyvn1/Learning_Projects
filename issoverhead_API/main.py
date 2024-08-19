import requests
import os
from datetime import datetime
import smtplib
import time

# Application send an email using smtplib if the  iss satellite is near me to go see it in the sky.

MY_LAT = 47.605480  # Your latitude
MY_LONG = -122.035561  # Your longitude
EMAIL = "andy.vargas.noesi@gmail.com"
PASSWORD = os.getenv("GMAIL_SECRET")

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour


def iss_overhead():
    if sunset <= time_now >= sunrise and MY_LAT - 5 <= iss_latitude >= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude >= MY_LONG:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject: ISS is overhead\n\n"
                    f"Look at the sky the satellite is over you today")
            connection.close()


while 0 == 0:
    time.sleep(60)
    iss_overhead()
