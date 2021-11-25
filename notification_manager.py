from twilio.rest import Client
from flight_data import FlightData
import os

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")


class NotificationManager:

    def send_SMS(self, message):
        client = Client(TWILIO_SID, TWILIO_TOKEN)

        message = client.messages \
            .create(
            body=message,
            from_='+14199633924',
            to='+523317603281'
        )

        print(message.status)
