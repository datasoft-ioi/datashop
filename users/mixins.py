from django.conf import settings
from twilio.rest import Client
import random


class MessageHandler:
    
    phone_number = None
    otp = None

    def __init__(self, phone_number, otp) -> None:
        self.phone_number = phone_number
        self.otp = otp


    def send_otp_to_phone(self):
        client = Client(settings.SID_ACCOUNT, settings.AUTH_TOKEN_TWLO)

        message = client.messages.create(
            body=f"Faollashtirishi uchun kodingiz: {self.otp}",
            from_="+16074146268",
            to=self.phone_number
        )

        print(message.sid)

