# encoding: utf-8
import os
from time import sleep

import requests
from twilio.rest import TwilioRestClient

latest = requests.get("http://lo01.pl/staszic/zastepstwa/api.php?method=zastepstwa").json()
twilio_client = TwilioRestClient(account=os.getenv("TWILIO_ACCOUNT"), token=os.getenv("TWILIO_TOKEN"))

while True:
    sleep(3 * 60)
    fresh = requests.get("http://lo01.pl/staszic/zastepstwa/api.php?method=zastepstwa").json()
    if fresh != latest:
        message = twilio_client.messages.create(messaging_service_sid=os.getenv("TWILIO_SID"),
                                                body="Pojawiły się nowe zastępstwa: http://za.staszi.cf",
                                                to="+48503988250")
    latest = fresh
