from twilio.rest import Client
from flight_data import FlightData
import smtplib
import os
import requests
from pprint import pprint

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/36a8b23504f2db994cf6c3c9ec104cde/flightDeals/users"
SHEETY_HEADERS = {
            "Authorization": f"Bearer {os.environ['TOKEN']}"
        }




class NotificationManager:

    def send_sms(self, message):
        client = Client(TWILIO_SID, TWILIO_TOKEN)

        message = client.messages \
            .create(
            body=message,
            from_='+14199633924',
            to='+523317603281'
        )

        print(message.status)

    def send_emails(self, message):
        from_email = "janf.tst@gmail.com"
        from_password = "T3$71n9U$3r"
        response = requests.get(SHEETY_USERS_ENDPOINT, headers=SHEETY_HEADERS)
        users = response.json()["users"]
        pprint(users)
        for user in users:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=from_email, password=from_password)
                connection.sendmail(
                    from_addr=from_email,
                    to_addrs=user["email"],
                    msg=f"Subject:{message.encode('utf-8').strip()}!\n\nlink"
                )

